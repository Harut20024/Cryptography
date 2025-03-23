def rc4(key, text):
    key_length = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + ord(key[i % key_length])) % 256
        S[i], S[j] = S[j], S[i]

    i = j = 0
    result = []
    for char in text:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        result.append(chr(ord(char) ^ K))

    return ''.join(result)




key = "key"
text = "this is test@"

encrypted_text = rc4(key, text)
print("encripted text: ", encrypted_text)

decrypted_text = rc4(key, encrypted_text)
print("pain text:", decrypted_text)
