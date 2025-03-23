
# This code was written by Mane Avoyan at the National Polytechnic University of Armenia. 
# This assignment was completed as part of the "Information Security" training progracm for group 255-3. 
# All rights to this code belong to the author. 
# This code may not be copied or used without the author's permission. 
# Citing the author is mandatory when using this code. 


import string

def load_word_list(file_path):
    try:
        with open(file_path, 'r') as file:
            words = set(line.strip().lower() for line in file)
        return words
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        exit(1)

def is_word_valid(word, word_list):
    return word.lower() in word_list

def caesar_cipher_brute_force(ciphered, word_list):
    max_shifts = 26
    all_valid_words = []

    for key in range(max_shifts):
        plaintext = ''
        for char in ciphered:
            if char in string.ascii_uppercase:
                start = ord('A')
                offset = (ord(char) - start - key) % 26
                plaintext += chr(start + offset)
            elif char in string.ascii_lowercase:
                start = ord('a')
                offset = (ord(char) - start - key) % 26
                plaintext += chr(start + offset)
            elif char.isdigit():
                shifted = (int(char) - key) % 10
                plaintext += str(shifted)
            else:
                plaintext += char

        print(f"Key {key}: {plaintext}")

        words = plaintext.split(' ')
        valid_words = [word for word in words if is_word_valid(word, word_list)]
        
        if valid_words:
            all_valid_words.append((key, valid_words))
    
    return all_valid_words

word_list = load_word_list('words.txt')
ciphertext = input("Enter the encrypted text: ")
answer = caesar_cipher_brute_force(ciphertext, word_list)

if answer:
    for key, valid_words in answer:
        print(f"Key {key}  words are(is): {', '.join(valid_words)}")
else:
    print("No valid words found.")  
    
    
    # DOOV ZHOO WKDW HQGV ZHOO
