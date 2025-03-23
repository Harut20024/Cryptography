def text_to_matrix(text):
    text = text.replace(" ", "").lower()
    matrix = [list(text[i:i + 5].ljust(5, 'z')) for i in range(0, len(text), 5)]
    return matrix

def encrypt_text(matrix):
    columns = len(matrix[0])
    encrypted_text = ""
    for col in range(columns):
        for row in matrix:
            if col < len(row):
                encrypted_text += row[col]
    return encrypted_text

def decrypt_text(encrypted_text, rows):
    columns = [encrypted_text[i:i + rows] for i in range(0, len(encrypted_text), rows)]
    original_text = ""
    for row in range(rows):
        for col in columns:
            if row < len(col):
                original_text += col[row]
    return original_text.rstrip('z')  

text = "Computer Systems and Informatics Department"
matrix = text_to_matrix(text)

print("Matrix:")
for row in matrix:
    print(" ".join(row))


encrypted_text = encrypt_text(matrix)
print("\nEncrypted text:", encrypted_text)


rows = len(matrix)
decrypted_text = decrypt_text(encrypted_text, rows)
print("\nDecrypted text:", decrypted_text)
