import random

plaintext = []
key = []
for i in range(65, 65+26):
    plaintext.append(chr(i))
    key.append(chr(i))

random.shuffle(key)

print(f'Plaintext : {plaintext}')
print(f'Key : {key}')

text = input('Enter text : ')

encoded = ''
for i in text:
    encoded += key[plaintext.index(i.upper())]
    # The index() method returns the position at the first occurrence of the specified value
    #The upper() method returns a string where all characters are in upper case.
print(f'Cipher text : {encoded}')

decoded = ''
for i in encoded:
    decoded += plaintext[key.index(i)]

print(f'decoded msg : {decoded}')

