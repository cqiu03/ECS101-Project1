from encrypt import Encrypt
from decrypt import Decrypt

#Read in a txt file containing str and convert it to binary
Encrypt("Input_Text.txt")

#Read in a txt file containing the binary and convert it to str
Decrypt("binary_result.txt")
print("----------DONE------------")