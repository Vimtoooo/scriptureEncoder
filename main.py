
# TODO: Create a program that converts a script line into an ASCII code then convert it to the 'target_base' value to return the result, with the spaces applied.

import string

def encodeScripture(script_line: str, target_base: int) -> str:
    
    if not (script_line or target_base):
        
        return None
    
    result: str = ""

    ASCII_LIST = [ord(char) for char in script_line]

    if 2 <= target_base <= 9:
        
        for code in ASCII_LIST:
        
            conversion: str = ""

            while code != 0:

                remainder: int = code % target_base
                conversion += string.digits[remainder]
                code //= target_base
        
            reversed_conversion = conversion[::-1]
            result += reversed_conversion + " "
    
    elif 10 <= target_base <= 36:
        
        for code in ASCII_LIST:
        
            conversion: str = ""

            while code != 0:

                remainder = code % target_base

                if remainder <= 9:
                    conversion += string.digits[remainder]
                    
                else:
                    conversion += string.ascii_uppercase[remainder - 10]

                code //= target_base
        
            reversed_conversion = conversion[::-1]
            result += reversed_conversion + " "
    
    else:

        return None


    return result


