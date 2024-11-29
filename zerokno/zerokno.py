from base58 import b58encode
from hashlib import sha256


class ZeroKno:
    def __init__(self, app_secret: str = "", storage: str = None):
        self.path = storage
        self.secret = app_secret

    @staticmethod
    def algo(password: str, secret: str) -> str:
        try: return b58encode(sha256(password.encode()).digest()).decode()
        except Exception as e: raise Exception(e)
    
    def store(self, password: str, uid: str) -> bool:
        try:
            with open(self.path+uid, "w+") as f:
                f.write(self.algo(password, self.secret))
                return True
        except Exception as e:
            raise Exception(e)


    def validate(self, password: str, uid: str) -> bool:
        try:
            with open(self.path+uid, "r") as f:
                return self.algo(password, self.secret) == f.read()
        except FileNotFoundError:
            raise Exception("Key not found")
