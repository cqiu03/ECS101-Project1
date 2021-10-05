class Encrypt:
    #We need a function to somehow preprocess the text to include the things that we want
    #for example if "and" is a reoccuring world and its value is 1 we need to change all and into 1
    def encrypt(self):
        encrypted = ""
        for char in self.text:
            encrypted += self.CHAR_CONVERSION[char]
        encrypted = (str)(len(encrypted)) + "." + encrypted
        return encrypted

    def export(self):
        with open('binary_result.txt', 'w', newline='') as f:
            f.write(self.encrypt())
        f.close()

    def __init__(self, filename):
        self.file = open(filename)
        self.text = self.file.read()
        #Have a special dictionary that contains the special cases so make it easier
        #to iterate through it
        self.CHAR_CONVERSION = {"a":"00001", "e":"00010", "i":"00011", "o":"00100", "u":"00101",
        "t":"00110", "s":"00111", "W":"01000", "T":"01001", "I":"01010",
        "A":"01011", "H":"01100", "S":"01101", "B":"01110", "n":"01111",
        "C":"1000000", "D":"1000001", "E":"1000010", "F":"1000011",
        "G":"1000100", "J":"1000101", "K":"1000101", "L":"1000111",
        "M":"1001000", "N":"1001001", "O":"1001100", "P":"1001011",
        "Q":"1001100", "R":"1001101", "U":"1001110", "V":"1001111",
        "X":"1010000", "Y":"1010001", "Z":"1010010", "c":"1010011",
        "d":"1010100", "f":"1010101", "g":"1010110", "h":"1010111",
        "k":"1011000", "l":"1011001", "m":"1011010", "p":"1011011",
        "q":"1011100", "r":"1011101", "v":"1011110", "x":"1011111",
        "y":"1100000", "z":"1100001", "w":"1100010","j":"1101010",
        ".":"1100011", " ":"00000", "-":"1100101", 'b': '1101001',
        '"':'1101011', ',': '1100100', "'": "1100111"}

        self.export()
