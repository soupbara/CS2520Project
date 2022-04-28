def randEncode(msg):
    '''
            This method requires a message to encrypt, it will return a list 
        with the resulting ciphertext and a set of the letters in a randomized
        order (deal with casing, choose either upper or lower for the key, deal with 
        case of each char as we iterate)

        write the key to file, return a string with the name of 
    '''
    alphabetLower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', \
                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabetUpper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', \
                    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    key = set(alphabetLower) #same order for ssame run, random seed reset with each program run
    key = list(key)
    try:
        keyFile = open("key.txt", "w")
        tempKey  = " "
        print(tempKey.join(key))
        keyFile.write(tempKey.join(key)) 
        keyFile.close()
    except:
        print("error with key file")

    ciphertxt = ""
    for char in msg:
        if char.islower():
            offset = ord(char) - 97
            ciphertxt += key[offset]
            print("offset =" , offset)
            print(ciphertxt)
        elif char.isupper():
            offset = ord(char) - 65
            ciphertxt += key[offset]
            print("offset =" , offset)
            print(ciphertxt)
        else: #isupper and islower will return false for a character that is not a letter
            ciphertxt += char
            print(ciphertxt)
            continue         
    print(str(key))
    return ciphertxt

def randDecode(cipher, keyFile):
    '''
    This method requires the cipher text and its corresponding key that is generated 
    and written to a file from the randEncode() as a txt file (provide the absolute file path)
    '''
    key = []
    plaintxt = ""
    try:
        keyFile = open(keyFile, "r")
        key = keyFile.readline().split()
        print(key)
        keyFile.close()
    except:
        print("error with key file")
    for char in cipher:
        if char.islower():
            offset = key.index(char) + 97
            plaintxt += chr(offset)
            print("offset =" , offset)
            print(plaintxt)
        elif char.isupper():
            offset = key.index(char) + 65
            plaintxt += chr(offset)
            print("offset =" , offset)
            print(plaintxt)
        else: #isupper and islower will return false for a character that is not a letter
            plaintxt += char
            print(plaintxt)
            continue        
        
cipher = randEncode("banana")
print(cipher)
randDecode(cipher, "C:/Users/alexa/Documents/Documents/learning hard/SPRING_2022/CS 2520 Python/key.txt")