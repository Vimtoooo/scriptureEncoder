
# TODO: Create a program that converts a script line into an ASCII code then convert it to the 'target_base' value to return the result, with the spaces applied.

import string

def encodeScripture(script_line: str, target_base: int) -> str:
    
    if not (script_line or target_base):
        return None
    
    result: str = ""

    ASCII_LIST = [ord(char) for char in script_line]
    ASCII_LENGTH = len(ASCII_LIST)

    for code in ASCII_LIST:
        
        res_int: int = code // target_base
        remainder: int = code % target_base
        result += string.digits[remainder] + " "

    


