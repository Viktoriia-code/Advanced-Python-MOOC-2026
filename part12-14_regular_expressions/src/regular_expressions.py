import re

def is_dotw(my_string: str):
    return bool(re.search("Mon|Tue|Wed|Thu|Fri|Sat|Sun", my_string))

def all_vowels(my_string: str):
    return bool(re.search("^[a|o|i|e|u]+$", my_string))

def time_of_day(my_string: str):
    return bool(re.search("(?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d", my_string))