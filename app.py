import io
import os
import threading
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image, ImageOps
import numpy as np

app = FastAPI(title='WordVault OCR MVP', version='3.0.0')
origins = [s.strip() for s in os.getenv('ALLOWED_ORIGINS','https://word-vault-vey6.onrender.com').split(',') if s.strip()]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_methods=['GET','POST'], allow_headers=['*'])
_lock = threading.Lock()
_engine = None

def get_engine():
    global _engine
    with _lock:
        if _engine is None:
            from paddleocr import PaddleOCR
            _engine = PaddleOCR(lang='fi', ocr_version='PP-OCRv5', use_doc_orientation_classify=False, use_doc_unwarping=False, use_textline_orientation=False)
        return _engine

@app.get('/health')
def health():
    return {'status':'ok','model_loaded':_engine is not None,'version':'3.0.0'}

@app.post('/ocr')
async def ocr(image: UploadFile = File(...)):
    if image.content_type not in ('image/jpeg','image/png','image/webp'):
        raise HTTPException(415,'Only JPEG, PNG and WebP images are supported')
    payload = await image.read(8 * 1024 * 1024 + 1)
    if len(payload) > 8 * 1024 * 1024:
        raise HTTPException(413,'Image exceeds 8 MB')
    try:
        img = ImageOps.exif_transpose(Image.open(io.BytesIO(payload))).convert('RGB')
        if img.width * img.height > 16_000_000:
            raise HTTPException(413,'Image exceeds 16 megapixels')
        arr = np.asarray(img)
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(400,'Invalid image')
    try:
        # Run CPU-intensive OCR in a worker thread to avoid blocking the event loop.
        from starlette.concurrency import run_in_threadpool
        def infer():
            with _lock:
                # Initialize outside lock: get_engine() acquires it.
                return get_engine().predict(arr)
        # One model instance: serialized inference handled with separate lock below.
        engine = await run_in_threadpool(get_engine)
        def predict():
            with _inference_lock:
                return list(engine.predict(arr))
        result = await run_in_threadpool(predict)
        lines = []
        for item in result:
            data = item.json if hasattr(item,'json') else {}
            if isinstance(data,dict) and 'res' in data:
                data = data['res']
            texts = data.get('rec_texts',[]) if isinstance(data,dict) else []
            scores = data.get('rec_scores',[]) if isinstance(data,dict) else []
            boxes = data.get('rec_polys',[]) if isinstance(data,dict) else []
            for i,t in enumerate(texts):
                poly = boxes[i].tolist() if i < len(boxes) and hasattr(boxes[i],'tolist') else (boxes[i] if i < len(boxes) else None)
                lines.append({'text':str(t),'confidence':float(scores[i]) if i<len(scores) else None,'polygon':poly})
        return {'text':'\n'.join(line['text'] for line in lines),'lines':lines,'width':img.width,'height':img.height}
    except Exception as exc:
        raise HTTPException(503,'OCR unavailable: '+str(exc)[:250])

_inference_lock = threading.Lock()
