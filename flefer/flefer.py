import numpy as np

def generate_key_matrix(key):
    key = ''.join(filter(str.isalpha, key.lower())).replace('j', 'i')
    key = "".join(sorted(set(key), key=key.index))
    alphabet = "abcdefghiklmnopqrstuvwxyz"
    key += ''.join([letter for letter in alphabet if letter not in key])
    return np.array(list(key)).reshape(5, 5)

def find_position(matrix, letter):
    pos = np.where(matrix == letter)
    return pos[0][0], pos[1][0]

def prepare_text(text):
    text = text.replace(" ", "").lower().replace('j', 'i')
    pairs, i = [], 0
    while i < len(text):
        if i + 1 == len(text):
            pairs.append(text[i] + 'x')
            i += 1
        elif text[i] == text[i + 1]:
            pairs.append(text[i] + 'x')
            i += 1
        else:
            pairs.append(text[i] + text[i + 1])
            i += 2
    return pairs

def clean_decrypted_text(text):
    cleaned_text = ""
    for i in range(len(text)):
        if text[i] == 'x' and (i == len(text) - 1 or text[i - 1] == text[i + 1]):
            continue
        cleaned_text += text[i]
    return cleaned_text

def encrypt_playfair(plaintext, key):
    matrix = generate_key_matrix(key)
    pairs = prepare_text(plaintext)
    ciphertext = ""
    for pair in pairs:
        row1, col1 = find_position(matrix, pair[0])
        row2, col2 = find_position(matrix, pair[1])
        if row1 == row2:
            ciphertext += matrix[row1, (col1 + 1) % 5] + matrix[row2, (col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5, col1] + matrix[(row2 + 1) % 5, col2]
        else:
            ciphertext += matrix[row1, col2] + matrix[row2, col1]
    return ciphertext

def decrypt_playfair(ciphertext, key):
    matrix = generate_key_matrix(key)
    pairs = prepare_text(ciphertext)
    plaintext = ""
    for pair in pairs:
        row1, col1 = find_position(matrix, pair[0])
        row2, col2 = find_position(matrix, pair[1])
        if row1 == row2:
            plaintext += matrix[row1, (col1 - 1) % 5] + matrix[row2, (col2 - 1) % 5]
        elif col1 == col2:
            plaintext += matrix[(row1 - 1) % 5, col1] + matrix[(row2 - 1) % 5, col2]
        else:
            plaintext += matrix[row1, col2] + matrix[row2, col1]
    return clean_decrypted_text(plaintext)

key = "State University of Armenia"
plaintext = "jazz Harut"
ciphertext = encrypt_playfair(plaintext, key)
print(f"Encrypted text: {ciphertext}")
decrypted_text = decrypt_playfair(ciphertext, key)
print(f"Decrypted text: {decrypted_text}")
