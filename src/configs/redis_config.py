import os
from dotenv import load_dotenv
import redis

# Tải các biến môi trường từ tệp .env
load_dotenv()

# Redis Configuration
redis_password = os.getenv("REDIS_PASSWORD")
redis_host = os.getenv("REDIS_HOST")
redis_url = f"redis://:{redis_password}@redis:{redis_host}"

# Kết nối Redis
redis_client = redis.StrictRedis.from_url(redis_url, decode_responses=True)
