docker run -it --rm \
  -v $(pwd)/app:/app \
  -w /app \
  python:3.11 \
  python main.py