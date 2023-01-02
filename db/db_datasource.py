import redis

redis_client: redis.Redis = redis.Redis(db=4)

def set_value(key: str, value: str) -> bool:
    try:
        redis_client.set(key, value)
        return True
    except Exception as e:
        print(e)
        return False

def get_value(nif: str) -> str:
    try:
        return redis_client.get(nif).decode("utf-8")
    except Exception as e:
        print(e)
        return None

