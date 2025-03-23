def get_first_part(text: str):
    unique_chars = []
    for char in text.lower():
        if char not in unique_chars and char.isalpha():
            unique_chars.append(char)
    return ''.join(unique_chars)

def get_second_part(first_part: str):
    alpha_chars = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    missing_chars = [char for char in alpha_chars if char not in first_part]
    return ''.join(missing_chars)

def get_key(text: str):
    first_part = get_first_part(text)
    second_part = get_second_part(first_part)
    return first_part + second_part

def caesar_cipher(string_key: str, text: str, mode: str = "encrypt"):
    caesar_key = get_key(string_key)
    alpha_chars = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    
    if mode == "decrypt":
        alpha_mapper = {caesar_key[i]: alpha_chars[i] for i in range(26)}
    else:
        alpha_mapper = {alpha_chars[i]: caesar_key[i] for i in range(26)}

    result = []
    for char in text.lower():
        if char.isalpha():
            result.append(alpha_mapper[char])
        else:
            result.append(char)
    
    return ''.join(result)


key = "State University of Armenia"
text = input("input text: ")
chooseMode = input("input encrypt or decrypt(e or d): ")
mode = "encrypt" if chooseMode.lower() ==  "e" else "decrypt"
encrypted_text = caesar_cipher(key, text, mode)

print(f"Encrypted: {encrypted_text}")
