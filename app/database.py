import redis
from app import settings
from typing import Union

redis_client = redis.Redis(
  host=settings.redis_host,
  port=settings.redis_port,
  password=settings.redis_password,
  decode_responses=True
)

def store_url(url: str, hash: str):
    redis_client.set(name=hash, value=url)

def get_url_by_hash(url_hash: str) -> Union[str, None]:
    return redis_client.get(url_hash)
