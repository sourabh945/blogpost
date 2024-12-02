
from string import digits , ascii_lowercase , ascii_uppercase

valid_characters = digits + ascii_lowercase + ascii_uppercase + ' '

def validate_username(username:str) -> bool:
    for char in username:
        if char not in valid_characters:
            return False
    return True