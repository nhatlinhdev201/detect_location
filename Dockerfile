# Bắt đầu từ image Python
FROM python:3.9-slim

# Cài đặt các thư viện cần thiết
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy mã nguồn của bạn vào container
COPY ./src /app/src

# Expose port mà FastAPI sẽ chạy
EXPOSE 8088

# Cấu hình để chạy ứng dụng FastAPI
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8088"]
