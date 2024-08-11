import redis
from app import settings

redis_client = redis.Redis(
  host=settings.redis_host,
  port=settings.redis_port,
  password=settings.redis_password
)

def store_url(url: str, hash: str):
    redis_client.set(name=hash, value=url)
