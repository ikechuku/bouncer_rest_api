import random
import string
def random_string_generator(size=8, chars=string.ascii_lowercase + string.digits+ string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))