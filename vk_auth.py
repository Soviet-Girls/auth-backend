import os
import hashlib

secret_key=os.getenv("VKAPP_SECRET_KEY")

def check(expire: int, mid: str, secret: str, sid: str, sig: str) -> bool:
    sign = f"expire={expire}mid={mid}secret={secret}sid={sid}{secret_key}"
    print(sign)
    sign = hashlib.md5(sign.encode()).hexdigest()
    print(sign)
    print(sig)
    if sig != sign:
        return False
    return True