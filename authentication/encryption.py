import base64
from django.conf import settings
from cryptography.fernet import Fernet

def test(data):
    print(data)
    
def encrpyt(data):
    fernet_key = Fernet(settings.ENCRYPT_KEY)
    encrypt_data = fernet_key.encrypt(data.encode('ascii'))
    return base64.urlsafe_b64encode(encrypt_data).decode("ascii")


def decrypt(data):
    fernet_key = Fernet(settings.ENCRYPT_KEY)
    encrpted_data = base64.urlsafe_b64decode(data)
    return fernet_key.decrypt(encrpted_data).decode("ascii")