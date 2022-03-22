def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if(ord(char)==32):
            result += char
        elif (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result


inp_text = input("Enter Message:")
shift = int(input("shift:"))

encripted = encrypt(inp_text,shift)
print(encripted)

def decrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if(ord(char)==32): #The ord() function returns the number representing the unicode code
            result += char
        elif (char.isupper()): #The isupper() method returns True if all the characters are in upper case, otherwise False
            result += chr((ord(char) - s - 65) % 26 + 65)
        else: #The chr() function returns the character that represents the specified unicode.
            result += chr((ord(char) - s - 97) % 26 + 97)
    return result
#The lower() method returns a string where all characters are lower case.
decrypted = decrypt(encripted, shift)
print(decrypted)