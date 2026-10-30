FROM debian:bookworm-slim
RUN apt-get update && apt-get install -y --no-install-recommends python3 python3-flask python3-gunicorn python3-libvoikko libvoikko1 voikko-fi ca-certificates && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY api.py /app/api.py
ENV PORT=10000
CMD ["/usr/bin/gunicorn", "--bind", "0.0.0.0:10000", "--workers", "2", "--timeout", "90", "api:app"]
