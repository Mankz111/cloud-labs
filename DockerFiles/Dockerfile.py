FROM debian:stable-slim

COPY main.py main.py
COPY books/ books/

RUN <<EOF

pip install python

EOF



CMD ["python", "main.py"]