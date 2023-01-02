import redis

redis_client: redis.Redis = redis.Redis(db=4)

def set(key: str, value: str) -> bool:
    try:
        redis_client.set(key, value)
        return True
    except redis.exceptions as e:
        print(e)
        return False

def get_value(key: str) -> str:
    try:
        return redis_client.get(key).decode("utf-8")
    except redis.xceptions as e:
        print(e)
        return None

