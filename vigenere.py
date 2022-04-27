'''
symbol legend:
        C = cipher text
        p = plain text
        k = key
        m = number of characters in key

the general equation of the encryption process is:
    C[i] = (p[i] + k[i%m])%26

the decryption process is:
    p[i] = (C[i] + k[i%m])%26

ascii: 
    A-Z = 65-90
    a-z = 97-122
'''

def createKey(msg, key):
    '''
    The purpose of this function is to make sure that the key is the same length as the
    message 
    '''
    if len(key) < len(msg):
        newKey = key
        # finding how many chars key is shorter than msg = len(msg) - len(key)
        for c in range(len(msg) - len(key)):
            newKey += key[c % len(key)]
        return newKey
    else:
        return key

def encrypt(plaintxt, key):
    '''
    The encryption method can be represented by the following equation:
        C[i] = (p[i] + k[i%m])%26
    Note that the symbol legend is:
        C = cipher text
        p = plain text
        k = key
        m = number of characters in key
    '''
    # the following is an empty string to hold the resulting cipher text
    ciphertxt = ''
    #iterating over every letter in the plaintext
    for index,char in enumerate(plaintxt):
        if char.isupper():
            tempP = ord(char) - 65
            print("plaintext[" + str(index) + "] " + str(tempP))
            tempK = ord(key[index]) - 65
            print("key[" + str(index) + "] " + str(tempK))
            print(((tempP + tempK) % 26))
            ciphertxt += chr(((tempP + tempK) % 26) + 65)
            print("Current Cipheretxt: " + ciphertxt)

        elif char.islower():
            tempP = ord(char) - 97
            print("plaintext[" + str(index) + "] " + str(tempP))
            tempK = ord(key[index]) - 97
            print("key[" + str(index) + "] " + str(tempK))
            print(((tempP + tempK) % 26))
            ciphertxt += chr(((tempP + tempK) % 26) + 97)
            print("Current Cipheretxt: " + ciphertxt)
        elif ord(char) == 32: #for spaces
            ciphertxt += " "
            continue
        else:
            #the islower() and isupper() should always return FALSE for anything else that is not a letter
            ciphertxt += char
            continue
    return ciphertxt







def decrypt(ciphertxt, key):
    '''
    The decryption method can be represented by the following equation:
        p[i] = (C[i] - k[i%m])%26
    Note that the symbol legend is:
        C = cipher text
        p = plain text
        k = key
        m = number of characters in key
    '''
    index = 0
    # the following is an empty string to hold the resulting cipher text
    plaintxt = ''
    #iterating over every letter in the plaintext
    for char in ciphertxt:
        if char.isupper():
            #NOTE: no modulus on the index for the key, since we generate a key that is the same size as the message
            #  C[i]   =    p[i]      -         k[i]         % 26   + adding the offset
            print((ord(char) - ord(key[index]) ) % 26   +         65)
            plaintxt += chr((ord(char) - ord(key[index]) ) % 26   +         65 ) 
            index += 1
        elif char.islower():
            #  C[i]   =      p[i]       -         k[i%m]    % 26   + adding the offset
            print((ord(char) - ord(key[index]))  % 26   +         97)
            plaintxt += chr((ord(char) - ord(key[index]))  % 26   +         97 )
            index += 1
        elif ord(char) == 32: #for spaces
            plaintxt += " "
            index += 1
            continue
        else:
            #the islower() and isupper should always return FALSE for anything else that is not a letter
            index += 1
            continue
    return plaintxt
