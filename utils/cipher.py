import base64
import random
import hashlib

class SecretCipher:
    def __init__(self, key=None):
        self._key = key or hashlib.sha256(str(random.randint(1, 1000)).encode()).hexdigest()[:8]
    
    def encrypt(self, text):
        # Simple substitution cipher with random shift
        shift = sum(ord(c) for c in self._key) % 26
        return ''.join(chr((ord(c) + shift) % 256) for c in text)
    
    def decrypt(self, text):
        # Reverse the substitution
        shift = sum(ord(c) for c in self._key) % 26
        return ''.join(chr((ord(c) - shift) % 256) for c in text)
    
    @staticmethod
    def encode_base64(text):
        return base64.b64encode(text.encode()).decode()
    
    @staticmethod
    def decode_base64(encoded_text):
        try:
            return base64.b64decode(encoded_text).decode()
        except:
            return "Decoding failed. Are you sure this is the right message?"