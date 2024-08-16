from wsgiref.util import shift_path_info


#decrypts the text
def decrypt(alphabet, text, shift):
    shift = shift - shift*2
    result = ""
    alphabet_length = len(alphabet)
    text = text.lower()
    
    for char in text:
        if char in alphabet:
            old_index = alphabet.index(char)
            new_index = (old_index + shift) % alphabet_length
            result += alphabet[new_index]
        else:
            result += char
    
    return result

shift = 2
alphabet = "abcdefghijklmnopqrxtuvwxyz"

text = "jgnnq"
print(decrypt(alphabet, text, shift))
text = "Jgnnq"
print(decrypt(alphabet, text, shift))
text = "Jgnnq, Yqtnf!"
print(decrypt(alphabet, text, shift))
text = "123"
print(decrypt(alphabet, text, shift))
