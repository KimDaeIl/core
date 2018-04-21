# Created encryption.py by KimDaeil on 04/20/2018
import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES


class AESCipher(object):
    def __init__(self, key=None):
        self.bs = 32
        if key is None:
            from flask import current_app
            key = current_app.config.get("SECRET_KEY")

        if key is None:
            # TODO 2018. 04. 22. raise 500 exception if key is emtpy or None
            pass
        self.key = hashlib.sha256(key.encode()).digest()

    #
    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        print(base64.b64encode(iv).decode('utf-8'))
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw)).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _unpad(self, s):
        return s[:-ord(s[len(s) - 1:])]