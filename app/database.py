import redis
from app import settings

redis_client = redis.Redis(
  host=settings.redis_host,
  port=settings.redis_port,
  password=settings.redis_password
)

def store_url(url: str, hash: str):
    response = redis_client.set(name=hash, value=url)
    if response:
        print('stored')
    else:
        print('not stored')

def get_url(hash: str):
    redis_client.get(hash)
