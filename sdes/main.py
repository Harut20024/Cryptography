key = input("Enter a 10-bit key: ")

if len(key) != 10 or not all(c in '01' for c in key):
    print("Invalid input. Please enter a 10-bit binary key.")
else:
    P10 = [2, 4, 1, 6, 3, 9, 0, 8, 7, 5]
    key = [key[i] for i in P10]

    left, right = key[:5], key[5:]
    left = left[1:] + [left[0]]
    right = right[1:] + [right[0]]
    combined = left + right
    
    P8 = [5, 2, 6, 3, 7, 4, 9, 8]
    key1 = ''.join([combined[i] for i in P8])

    left = left[2:] + left[:2]
    right = right[2:] + right[:2]
    combined = left + right
    key2 = ''.join([combined[i] for i in P8])

    plaintext = input("Enter an 8-bit plaintext: ")
    if len(plaintext) != 8 or not all(c in '01' for c in plaintext):
        print("Invalid plaintext. Please enter an 8-bit binary value.")
    else:
        IP = [1, 5, 2, 0, 3, 7, 4, 6]
        IP_inverse = [3, 0, 2, 4, 6, 1, 7, 5]
        EP = [3, 0, 1, 2, 1, 2, 3, 0]
        P4 = [1, 3, 2, 0]
        S0 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
        S1 = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]

        def permute(block, table):
            return ''.join([block[i] for i in table])

        def fk(bits, subkey):
            left, right = bits[:4], bits[4:]
            expanded = permute(right, EP)
            xor_result = ''.join(['1' if expanded[i] != subkey[i] else '0' for i in range(8)])
            row0, col0 = int(xor_result[0] + xor_result[3], 2), int(xor_result[1] + xor_result[2], 2)
            row1, col1 = int(xor_result[4] + xor_result[7], 2), int(xor_result[5] + xor_result[6], 2)
            s0, s1 = bin(S0[row0][col0])[2:].zfill(2), bin(S1[row1][col1])[2:].zfill(2)
            p4 = permute(s0 + s1, P4)
            return ''.join(['1' if p4[i] != left[i] else '0' for i in range(4)]) + right

        permuted_text = permute(plaintext, IP)
        first_round = fk(permuted_text, key1)
        swapped = first_round[4:] + first_round[:4]
        second_round = fk(swapped, key2)
        ciphertext = permute(second_round, IP_inverse)

        print("Ciphertext:", ciphertext)

        permuted_cipher = permute(ciphertext, IP)
        first_decrypt = fk(permuted_cipher, key2)
        swapped_decrypt = first_decrypt[4:] + first_decrypt[:4]
        second_decrypt = fk(swapped_decrypt, key1)
        decrypted = permute(second_decrypt, IP_inverse)

        print("Decrypted plaintext:", decrypted)
