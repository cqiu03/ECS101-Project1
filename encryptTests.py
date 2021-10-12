#Conversion Chart for the Char combinations

#1101100  , the , 00110 1010111 00010
#1101101  , and , 00001 01111 1010100
#1101110  , are , 00001 1011101 00010
#1101111  , for , 1010101 00100 1011101
#1110000  , not , 01111 00100 00110
#1110001  , but , 1000000 00101 00110
#1110010  , that , 00110 1010111 00001 00110
#1110011  , with , 1100010 00011 00110 1010111
#1110100  , have , 1010111 00001 1100011 00010
#1110101  , this , 00110 1010111 00011 00111
#1110110  , will , 1100010 00011 1011001 1011001
#1110111  , be , 1000000 00010
#1111000  , it , 00011 00110
#1111001  , to , 00110 00100
#1111010  , of , 00100 1010101
#1111011  , in , 00011 01111
#1111100  , is ,  00011 00111
#1111101  , as , 00001 00111
#1111110  , ing , 00011 01111 1010110
#1111111  , ed , 00010 1010100

AlltheChar = {"a":"00001", "e":"00010", "i":"00011", "o":"00100",
              "u":"00101", "t":"00110", "s":"00111", "W":"01000", "T":"01001",
              "I":"01010", "A":"01011", "H":"01100", "S":"01101", "B":"01110", "n":"01111", "b":"1000000",
              "C":"1010010", "D":"1000001", "E":"1000010", "F":"1000011", "G":"1000100", "J":"1000101",
              "K":"1000101", "L":"1000111", "M":"1001000", "N":"1001001", "O":"1001100", "P":"1001011", "Q":"1001100",
              "R":"1001101", "U":"1001110", "V":"1001111", "X":"1010000", "Y":"1010001", "Z":"1010010",
              "c":"1010011", "d":"1010100", "f":"1010101", "g":"1010110", "h":"1010111", "k":"1011000",
              "l":"1011001", "m":"1011010", "p":"1011011", "q":"1011100", "r":"1011101", "v":"1011110",
              "x":"1011111", "y":"1100000", "z":"1100001", "w":"1100010","j":"1101010", ".":"1100011",
              " ":"00000", "-":"1100101", ",":"1100100", "!":"1100110", "'":"1100111", "\n":"1101000", "and":"1101101"}
OtherVar = {}
def encrypt(word: str):
    encrypted = ""
    for i in word:
        encrypted += AlltheChar[i]
    if "00110101011100010" in encrypted:
        encrypted = encrypted.replace("00110101011100010","1101100")
    if "00001011111010100" in encrypted:
        encrypted = encrypted.replace("00001011111010100","1101101")
    if "00001101110100010" in encrypted:
        encrypted = encrypted.replace("00001101110100010","1101110")
    if "1010101001001011101" in encrypted:
        encrypted = encrypted.replace("1010101001001011101","1101111")
    if "011110010000110" in encrypted:
        encrypted = encrypted.replace("011110010000110","1110000")
    if "10000000010100110" in encrypted:
        encrypted = encrypted.replace("10000000010100110","1110001")
    if "0011010101110000100110" in encrypted:
        encrypted = encrypted.replace("0011010101110000100110","1110010")
    if "110001000011001101010111" in encrypted:
        encrypted = encrypted.replace("110001000011001101010111", "1110011")
    if "101011100001110001100010" in encrypted:
        encrypted = encrypted.replace("101011100001110001100010","1110100")
    if "0011010101110001100111" in encrypted:
        encrypted = encrypted.replace("0011010101110001100111", "1110101")
    if "11000100001110110011011001" in encrypted:
        encrypted = encrypted.replace("11000100001110110011011001", "1110110")
    if "100000000010" in encrypted:
        encrypted = encrypted.replace("100000000010","1110111")
    if "0001100110" in encrypted:
        encrypted = encrypted.replace("0001100110", "1111000")
    if "0011000100" in encrypted:
        encrypted = encrypted.replace("0011000100", "1111001")
    if "001001010101" in encrypted:
        encrypted = encrypted.replace("001001010101","1111010")
    if "0001101111" in encrypted:
        encrypted = encrypted.replace("0001101111","1111011")
    if "0001100111" in encrypted:
        encrypted = encrypted.replace("0001100111","1111100")
    if "0000100111" in encrypted:
        encrypted = encrypted.replace("0000100111","1111101")
    if "00011011111010110" in encrypted:
        encrypted = encrypted.replace("00011011111010110","1111110")
    if "000101010100" in encrypted:
        encrypted = encrypted.replace("000101010100","1111111")


    return str(len(word)) + "." + encrypted

print(encrypt("for tests"))
