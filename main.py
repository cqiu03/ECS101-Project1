hash_table = {"0000":"a", "0001":"b", "0010":"c", "0011":"d"}
encrypt_table = {"a":"0000", "b":"0001", "c":"0010", "d":"0011"}

print(hash_table["0000"])
print(encrypt_table["a"])

def encrypt(word):
    encrypted = ""

    #use the i value as the key for the hash table and return the
    #corresponding value
    for i in word:
        encrypted += encrypt_table[i]

    return encrypted

print(encrypt("aaaa"))
x= (encrypt("aaaa"))

def helperRecur(binary, data):
    local_data = data
    if not(binary == ""):
        #if the binary starts with the S(0), then it is going to look at the
        #next 4 numbers
        if(binary[0] == "0"):
             local_data.append(binary[0:4])
             print(local_data)
             helperRecur(binary[4:],local_data)
        else:
            # else it must be L(1), then it is going to look at the
            # next 6 numbers
            data.append(binary[0:6])
            helperRecur(binary[6:],local_data)
    return data

def decrypt(binary):
    decrypt = ""
    for i in binary:
        decrypt += hash_table[i]
    return decrypt

#Decrypts the list
decryption_List = helperRecur(x,[])

#print out the decryption list
print(decrypt(decryption_List))