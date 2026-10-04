import json

from redis import Redis


class RedisCache:
    def __init__(self, redis_url: str):
        self.client = Redis.from_url(
            redis_url,
            decode_responses=True,
        )

    def get(self, key: str):
        value = self.client.get(key)

        if value is None:
            return None

        return json.loads(value)

    def set(
        self,
        key: str,
        value,
        ttl: int,
    ) -> None:

        self.client.set(
            key,
            json.dumps(value, ensure_ascii=False),
            ex=ttl,
        )

    def delete(self, key: str) -> None:
        self.client.delete(key)

    def ping(self) -> bool:
        return bool(self.client.ping())

    def close(self) -> None:
        self.client.close()
