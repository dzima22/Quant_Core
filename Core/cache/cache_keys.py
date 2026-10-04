import hashlib
import json


def build_cache_key(
    namespace: str,
    payload,
) -> str:

    if hasattr(payload, "model_dump"):
        payload = payload.model_dump(
            mode="json",
            by_alias=True,
        )

    raw = json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
    )

    digest = hashlib.sha256(raw.encode("utf-8")).hexdigest()

    return f"quant:v1:{namespace}:{digest}"
