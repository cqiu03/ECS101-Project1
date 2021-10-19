class Encrypt:
    def __init__(self, filename):

        #read file
        self.file = open(filename,encoding="utf8")
        self.text = self.file.read()

        #list containing all the custom words that we feel are the most frequently used word
        self.CHAR_SP = ['and', 'the','are','for', 'not', 'but', 'that', 'with',
                        'have','this','will','be','it','to','of','in','is','as',
                        'ing', 'ed']
        #A dictionary containing the key pair values that convert a str into binary
        self.CHAR_CONVERSION = {"a":"00001", "e":"00010", "i":"00011", "o":"00100", "u":"00101",
        "t":"00110", "s":"00111", "W":"01000", "T":"01001", "I":"01010",
        "A":"01011", "H":"01100", "S":"01101", "B":"01110", "n":"01111",
        "C":"1000000", "D":"1000001", "E":"1000010", "F":"1000011",
        "G":"1000100", "J":"1000101", "K":"1000110", "L":"1000111",
        "M":"1001000", "N":"1001001", "O":"1001010", "P":"1001011",
        "Q":"1001100", "R":"1001101", "U":"1001110", "V":"1001111",
        "X":"1010000", "Y":"1010001", "Z":"1010010", "c":"1010011",
        "d":"1010100", "f":"1010101", "g":"1010110", "h":"1010111",
        "k":"1011000", "l":"1011001", "m":"1011010", "p":"1011011",
        "q":"1011100", "r":"1011101", "v":"1011110", "x":"1011111",
        "y":"1100000", "z":"1100001", "w":"1100010","j":"1101010",
        ".":"1100011", " ":"00000", "-":"1100101", 'b':'1101001','!':'1100110',
        '"':'1101011', '“':'1101011', '”':'1101011', ',': '1100100', "'": "1100111", "’": "1100111","\n":"1101000",
        'the': '1101100', 'and': '1101101', 'are': '1101110', 'for': '1101111',
        'not': '1110000','but': '1110001', 'that': '1110010', 'with': '1110011', 'have': '1110100',
        'this': '1110101','will': '1110110', 'be': '1110111', 'it': '1111000', 'to': '1111001', 'of': '1111010',
        'in': '1111011','is': '1111100', 'as': '1111101', 'ing': '1111110', 'ed':'1111111'}

        self.export()

    #encode the input according to the conversion table to binary
    def encrypt(self):
        encrypted = ""
        x = 0
        #check for custom words
        while x < len(self.text):
            char = self.text[x]
            if self.text[x:x+2] in self.CHAR_SP:
                char = self.text[x:x+2]
                x+=1
            if self.text[x:x+3] in self.CHAR_SP:
                char = self.text[x:x+3]
                x+=2
            if self.text[x:x+4] in self.CHAR_SP:
                char = self.text[x:x+4]
                x+=3

            encrypted += self.CHAR_CONVERSION[char]
            x+=1
        #add the length of the binary string with a period
        encrypted = (str)(len(encrypted)) + "." + encrypted
        return encrypted

    #write to a file
    def export(self):
        with open('binary_result.txt', 'w', newline='') as f:
            f.write(self.encrypt())
        f.close()
