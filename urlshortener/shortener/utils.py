import string
import random

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    short_code = ''.join(random.choices(characters, k=length))
    return short_code
