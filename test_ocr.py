import argparse
import requests
p=argparse.ArgumentParser()
p.add_argument('image')
p.add_argument('--url',default='http://localhost:10000')
a=p.parse_args()
with open(a.image,'rb') as f:
    r=requests.post(a.url.rstrip('/')+'/ocr',files={'image':(a.image,f,'image/jpeg')},timeout=240)
print('HTTP',r.status_code)
print(r.text)
