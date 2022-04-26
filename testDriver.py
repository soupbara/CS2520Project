# the following is a user defined module, you can import it similarly to how you've imported other libraries
import caesarCipher
import vigenere


def main():
    plaintxt = input("Please enter a message to encrypt: ")
    '''
    shiftKey = input("Please enter a key. This must be a value between 0-25: ")
    result = caesarCipher.shiftEncrypt(plaintxt, shiftKey)
    print(result)
    print(caesarCipher.shiftDecrypt(result, shiftKey))    
    '''


    keyVignere = input("Please enter a word to encrypt your message: ")
    keyVignere = vigenere.createKey(plaintxt, keyVignere)
    print("key for vignere: ", keyVignere)
    result = vigenere.encrypt(plaintxt, keyVignere)
    print(result)
    print(vigenere.decrypt(result, keyVignere))


def test():
    plain = "hi bye"
    key = "tytyty"
    cipher = ""
    index = 0
    for char in plain:
        if char.islower():
            p_index = ord(char)
            print("plain[", index, "] = ", p_index)
            key_index = ord(key[index])
            print("key[", index, "] = ", key_index)
            cipher += ord((p_index + key_index) % 26)
            print(cipher)



main()
