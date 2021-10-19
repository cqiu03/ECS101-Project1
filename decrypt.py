class Decrypt:
    def __init__(self, filename):
        #Read the file
        self.file = open(filename)
        self.binary = self.file.read()

        #A dictionary containing the key pair values that convert binary into str
        self.CONVERSION_TABLE = {"00001":"a", "00010":"e", "00011":"i", "00100":"o", "00101":"u",
        "00110":"t", "00111":"s", "01000":"W", "01001":"T", "01010":"I",
        "01011":"A", "01100":"H", "01101":"S", "01110":"B", "01111":"n",
        "1000000":"C", "1000001":"D", "1000010":"E", "1000011":"F",
        "1000100":"G", "1000101":"J", "1000110":"K", "1000111":"L",
        "1001000":"M", "1001001":"N", "1001010":"O", "1001011":"P",
        "1001100":"Q", "1001101":"R", "1001110":"U", "1001111":"V",
        "1010000":"X", "1010001":"Y", "1010010":"Z", "1010011":"c",
        "1010100":"d", "1010101":"f", "1010110":"g", "1010111":"h",
        "1011000":"k", "1011001":"l", "1011010":"m", "1011011":"p",
        "1011100":"g", "1011101":"r", "1011110":"v", "1011111":"x",
        "1011110":"v", "1100000":"y", "1100001":"z", "1100010":"w","1101010":"j",'1100110':'!',
        "1100011":".", "00000":" ", "1100101":"-", '1101001': 'b',
        '1101011':'"', '1100100': ',', "1100111": "'", "1101000":"\n",
         '1101100': 'the', '1101101': 'and', '1101110': 'are', '1101111': 'for',
         '1110000': 'not', '1110001': 'but', '1110010': 'that', '1110011': 'with', '1110100': 'have',
         '1110101': 'this', '1110110': 'will', '1110111': 'be', '1111000': 'it', '1111001': 'to', '1111010': 'of',
         '1111011': 'in', '1111100': 'is', '1111101': 'as', '1111110': 'ing', '1111111':'ed'
         }

        self.export()

    #Take in a string of binary and converts it back to text using the converstion table
    def decrypt(self):
        #find the index of the first binary bit after the index
        pindex = self.binary.index(".") + 1
        decrypt = ""

        while pindex < len(self.binary):
            #check for the starting bit either 0 or 1 for short or long
            if(self.binary[pindex] == '0'):
                decrypt += self.CONVERSION_TABLE[self.binary[pindex:pindex+5]]
                pindex+=5
            else:
                decrypt += self.CONVERSION_TABLE[self.binary[pindex:pindex+7]]
                pindex+=7
        return decrypt

    #Write to a file
    def export(self):
        outFile = open('decompress.txt', 'w')
        outFile.write(self.decrypt())
        outFile.close()
