# Created security.py by KimDaeil on 04/26/2018

from base64 import b64encode, b64decode
from hashlib import sha3_256
from core.models.users import UserModel
from datetime import datetime
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
        self.key = sha3_256(key.encode()).digest()

    #
    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        print(b64encode(iv).decode('utf-8'))
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return b64encode(iv + cipher.encrypt(raw)).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    def decrypt(self, enc):
        enc = b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _unpad(self, s):
        return s[:-ord(s[len(s) - 1:])]


def make_hashed(data):
    if data:
        if not isinstance(data, str):
            data = str(data)

        data = data.encode()

        return b64encode(sha3_256(data).digest()).decode('utf-8')


def generate_password(user):
    if user and isinstance(user, UserModel):
        user.password = make_hashed("{}{}{}".format(user.password, user.salt, datetime.now()))
