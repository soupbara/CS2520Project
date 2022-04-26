'''
The Caesar cipher can be represented by the following mathematical formula:
encryption(letter) = (letter + key) mod 26
decryption(symbol) = (symbol - key) mod 26
'''
def shiftEncrypt(plaintxt, key):
    '''
    The encryption method can be represented by the following mathematical formula:
        encryption(letter) = (letter + key) mod 26
    '''
    #Something to hold the resulting ciphertext 
    result = ""
    key = int(key)
    #A loop to traverse the message to encrypts
    for l in range(len(plaintxt)):
        #A variable to hold each letter of the message
        letter = plaintxt[l]
        #print("ascii value for ", letter, ord(letter))
        #check for uppcase letters
        if (letter.isupper()):
        # adding the shifted letters:
            result += chr((ord(letter) + key - 65) % 26 + 65) # a = 65
        elif ord(letter) == 32: #for spaces
            result += " "
        else:
            result += chr((ord(letter) + key - 97) % 26 + 97) # A = 97
    return result

#Caesar Cipher Decryption function
def shiftDecrypt(ciphertxt, key):
    '''
    The decryption method can be represented by the following mathematical formula:
        decryption(symbol) = (symbol - key) mod 26
    '''
    #Something to hold the resulting ciphertext 
    result = ""
    key = int(key)
    #A loop to traverse the message to encrypts
    for l in range(len(ciphertxt)):
        #A variable to hold each letter of the message
        letter = ciphertxt[l]
        #check for uppcase letters
        #print("ascii value for ", letter, ord(letter))
        if (letter.isupper()):
        # adding the shifted letters:
            result += chr((ord(letter) - key - 65) % 26 + 65) # a = 65
        elif ord(letter) == 32: #for spaces
            result += " "
        else:
            result += chr((ord(letter) - key - 97) % 26 + 97) # A = 97
    return result
