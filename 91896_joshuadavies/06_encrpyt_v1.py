# encrypts the text
def encrypt(alphabet, text, shift):
    result = ""
    alphabet_length = len(alphabet)
    text = text.lower()
    for char in text:
        if char in alphabet:
            old_index = alphabet.index(char)
            new_index = (old_index + shift) % alphabet_length
            if new_index > 26:
                print("hi")
            result += alphabet[new_index]
        else:
            result += char
    
    return result


shift = 2
alphabet = "abcdefghijklmnopqrxtuvwxyz"
max = 100
min = 1

text = "hello"
print(encrypt(alphabet, text, shift))
text = "Hello"
print(encrypt(alphabet, text, shift))
text = "Hello, World!"
print(encrypt(alphabet, text, shift))
text = "123"
print(encrypt(alphabet, text, shift))