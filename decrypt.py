class Decrypt:
    def __init__(self, filename):
        #Conversion Table herex
        self.file = open(filename)
        self.binary = self.file.read()
        self.CONVERSION_TABLE = {"00001":"a", "00010":"e", "00011":"i", "00100":"o", "00101":"u",
        "00110":"t", "00111":"s", "01000":"W", "01001":"T", "01010":"I",
        "01011":"A", "01100":"H", "01101":"S", "01110":"B", "01111":"n",
        "1000000":"C", "1000001":"D", "1000010":"E", "1000011":"F",
        "1000100":"G", "1000101":"J", "1000101":"K", "1000111":"L",
        "1001000":"M", "1001001":"N", "1001100":"O", "1001011":"P",
        "1001100":"Q", "1001101":"R", "1001110":"U", "1001111":"V",
        "1010000":"X", "1010001":"Y", "1010010":"Z", "1010011":"c",
        "1010100":"d", "1010101":"f", "1010110":"g", "1010111":"h",
        "1011000":"k", "1011001":"l", "1011010":"m", "1011011":"p",
        "1011100":"g", "1011101":"r", "1011110":"v", "1011111":"x",
        "1100000":"v", "1100001":"z", "1100010":"w","1101010":"j",
        "1100011":".", "00000":" ", "1100101":"-", '1101001': 'b',
        '1101011':'"', '1100100': ',', "1100111": "'", "1101000":"\\n"}

        self.export()

    def helperRecur(self, binary, data):
        local_data = data
        if not (binary == ""):
            # if the binary starts with the S(0), then it is going to look at the
            # next 4 numbers
            if (binary[0] == "0"):
                # print((local_data, binary))
                local_data.append(binary[0:5])
                self.helperRecur(binary[5:], local_data)
            else:
                # else it must be L(1), then it is going to look at the
                # next 6 numbers
                # print((local_data, binary))
                data.append(binary[0:7])
                self.helperRecur(binary[7:], local_data)
        return data

    def decrypt(self):
        pindex = self.binary.index(".")
        binary_list = self.helperRecur(self.binary[pindex + 1:], [])
        decrypt = ""
        for i in binary_list:
            decrypt += self.CONVERSION_TABLE[i]
        return decrypt

    def export(self):
        outFile = open('decompress.txt', 'w')
        outFile.write(self.decrypt())
        outFile.close()
