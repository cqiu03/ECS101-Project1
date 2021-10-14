from encrypt import Encrypt
from decrypt import Decrypt

#Read in a txt file containing str and convert it to binary
encoder = Encrypt("Input_Text.txt")

#Read in a txt file containing binary and convert it to str
decoder = Decrypt("binary_result.txt")
print("----------DONE------------")