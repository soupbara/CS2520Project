def encode(msg):
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
    file = 
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
    print(key)



    return ciphertxt
print(encode("hello"))
print(encode("hello"))