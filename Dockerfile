
FROM debian:bookworm-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3 \
    python3-flask \
    python3-libvoikko \
    libvoikko1 \
    voikko-fi \
    ca-certificates && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY api.py /app/api.py

ENV PORT=10000
ENV PYTHONUNBUFFERED=1

EXPOSE 10000

CMD ["python3", "-c", "import os; from api import app; app.run(host='0.0.0.0', port=int(os.environ.get('PORT', '10000')))"]
