import string
import itertools

def password_generator(length):
    """Returns iterator that generates passwords from digits and lower-case letters"""
    return itertools.product(string.ascii_lowercase + string.digits, repeat=length)