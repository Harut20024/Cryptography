# 2^m-m-2>=k
# k - yndhanur qanak
# m stugox tveri qanak(syndrome)

import random

def hamming_encode(data_bits):
    k = len(data_bits)
    m = 0
    while 2 ** m - m - 1 < k:
        m += 1
    
    n = k + m
    code = [0] * (n + 2)   
    j = 0
    
    for i in range(1, n + 1):
        if (i & (i - 1)) != 0:   
            code[i] = data_bits[j]
            j += 1

    for i in range(m):
        parity_pos = 2 ** i
        parity = 0
        for j in range(1, n + 1):
            if j & parity_pos:
                parity ^= code[j]
        code[parity_pos] = parity

    overall_parity = 0
    for i in range(1, n + 1):
        overall_parity ^= code[i]
    code[n + 1] = overall_parity  

    return code[1:]  

def hamming_decode(code):
    n = len(code) - 1   
    m = 0
    while 2 ** m <= n:
        m += 1

    code = [0] + code

    syndrome = 0
    for i in range(m):
        parity_pos = 2 ** i
        parity = 0
        for j in range(1, n + 1):
            if j & parity_pos:
                parity ^= code[j]
        if parity != code[parity_pos]:
            syndrome += parity_pos

    overall_parity = 0
    for i in range(1, n + 2):
        overall_parity ^= code[i]

    if overall_parity == 0 and syndrome == 0:
        print("No error detected")
    elif overall_parity == 1 and syndrome != 0:
        print(f"Single error detected at position {syndrome}")
        if syndrome <= n + 1:
            code[syndrome] ^= 1
            print(f"Corrected the error at position {syndrome}")
    elif overall_parity == 1 and syndrome == 0:
        print("Error detected in the overall parity bit")
        code[n + 1] ^= 1
        print("Corrected the error in the overall parity bit")
    else:
        print("Double-bit error detected. Unable to correct.")

    data_bits = []
    for i in range(1, n + 1):
        if (i & (i - 1)) != 0:
            data_bits.append(code[i])

    return data_bits


data_bits = [random.randint(0, 1) for _ in range(8)]
encoded = hamming_encode(data_bits)

error_pos1 = random.randint(0, len(encoded) - 1)
encoded_with_one_error = encoded.copy()
encoded_with_one_error[error_pos1] ^= 1

print("\n--- Example with One Error ---")
print(f"Original data bits: {data_bits}")
print(f"Encoded bits: {encoded}")
print(f"Encoded bits with error at position {error_pos1 + 1}: {encoded_with_one_error}")

decoded_one_error = hamming_decode(encoded_with_one_error)
print(f"Decoded data bits after correction: {decoded_one_error}")

error_pos2 = random.randint(0, len(encoded) - 1)
while error_pos2 == error_pos1:
    error_pos2 = random.randint(0, len(encoded) - 1)

encoded_with_two_errors = encoded.copy()
encoded_with_two_errors[error_pos1] ^= 1
encoded_with_two_errors[error_pos2] ^= 1

print("\n--- Example with Two Errors ---")
print(f"Original data bits: {data_bits}")
print(f"Encoded bits: {encoded}")
print(f"Encoded bits with errors at positions {error_pos1 + 1} and {error_pos2 + 1}: {encoded_with_two_errors}")

decoded_two_errors = hamming_decode(encoded_with_two_errors)
print(f"Decoded data bits after decoding: {decoded_two_errors}")

encoded_with_parity_error = encoded.copy()
encoded_with_parity_error[-1] ^= 1  

print("\n--- Example with Overall Parity Bit Error ---")
print(f"Original data bits: {data_bits}")
print(f"Encoded bits: {encoded}")
print(f"Encoded bits with error in the overall parity bit: {encoded_with_parity_error}")

decoded_parity_error = hamming_decode(encoded_with_parity_error)
print(f"Decoded data bits after correction: {decoded_parity_error}")
