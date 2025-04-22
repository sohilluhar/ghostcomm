from cryptography.fernet import Fernet
from django.conf import settings

fernet = Fernet(settings.FERNET_KEY)

def encrypt_message(text):
    return fernet.encrypt(text.encode()).decode()

def decrypt_message(encrypted_text):
    return fernet.decrypt(encrypted_text.encode()).decode()
    
# core/utils.py

import random
import string

def generate_random_username():
    names = ['Ghost', 'Phantom', 'Shadow', 'Wraith', 'Cipher', 'Nighthawk', 'Specter', 'Agent', 'Nova', 'Echo']
    number = ''.join(random.choices(string.digits, k=4))
    return random.choice(names) + number
