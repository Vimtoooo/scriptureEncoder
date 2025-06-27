
# IDEA: Usage examples of the program
import string
import main

# Test case 1:
script: str = "Amen"
base: int = 2
# print(encodeScripture(script_line=script, target_base=base)) # INFO: Returns "1000001 1101101 1100101 1101110"

# Test case 2:
script: str = "Jesus wept."
base: int = 8
# print(encodeScripture(script, base)) # INFO: Returns "112 145 163 165 163 40 167 145 160 164 56"

# Test case 3:
script: str = "For God so loved the world"
base: int = 16
# print(encodeScripture(script, base)) # INFO: Returns "46 6F 72 20 47 6F 64 20 73 6F 20 6C 6F 76 65 64 20 74 68 65 20 77 6F 72 6C 64"

# Test case 4:
script: str = "Peace be with you."
base: int = 36
# print(encodeStripture(script, base)) # INFO: Returns "28 2T 2P 2R 2T W 2Q 2T W 3B 2X 38 2W W 3D 33 39 1A"


# IDEA: Other tests

# digit: int = 2
# res = string.digits[digit]
# print(res)

res = ""
base: int = 2
ascii_list = [ord(char) for char in "Amen"]
for code in ascii_list:
    remainder = code % base
    res += string.digits[remainder] + " "
print(res)