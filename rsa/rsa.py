from sympy import mod_inverse, randprime
import json
import base64
from sympy import mod_inverse, gcd
import random


def generate_keys():
    p = randprime(10**50, 10**51)
    q = randprime(10**50, 10**51)
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = find_coprime(phi_n) 
    d = mod_inverse(e, phi_n)
    public_key = (e, n)
    private_key = (d, n)
    return public_key, private_key

def find_coprime(phi_n):
    common_exponents = [3, 5, 17, 257, 65537]
    for e in common_exponents:
        if e < phi_n and gcd(e, phi_n) == 1:
            return e
    while True:
        e = random.randrange(2, phi_n)
        if gcd(e, phi_n) == 1:
            return e
        
        
def save_keys(file_name, key_data):
    with open(file_name, 'w') as f:
        json.dump(key_data, f)

def load_keys(file_name):
    with open(file_name, 'r') as f:
        return json.load(f)

def string_to_base64_number(string):
    base64_bytes = base64.b64encode(string.encode('utf-8'))
    return int.from_bytes(base64_bytes, 'big')

def base64_number_to_string(number):
    try:
        base64_bytes = number.to_bytes((number.bit_length() + 7) // 8, 'big')
        decoded_string = base64.b64decode(base64_bytes).decode('utf-8')
        return decoded_string
    except Exception as e:
        return f"Error decoding number {number}: {str(e)}"

def encrypt(message, public_key):
    e, n = public_key
    return pow(message, e, n)

def decrypt(ciphertext, private_key):
    d, n = private_key
    return pow(ciphertext, d, n)

def first_run():
    public_key, private_key = generate_keys()
    save_keys('private_key_Harut.json', {"d": private_key[0], "n": private_key[1]})
    save_keys('public_key_Harut.json', {"e": public_key[0], "n": public_key[1]})
    
    print("Public Key:", public_key)
    print("Private Key:", private_key)

def second_run():
    public_key_data = load_keys('public_key_Mane.json')
    public_key = (public_key_data['e'], public_key_data['n'])
    
    private_key_data = load_keys('private_key_Harut.json')
    private_key = (private_key_data['d'], private_key_data['n'])
    
    choice = input("Encrypt or Decrypt? (e/d): ").strip().lower()
    if choice == 'e':
        message = input("Enter message to encrypt: ")
        message_number = string_to_base64_number(message)
        ciphertext = encrypt(message_number, public_key)
        print("Encrypted Message:", ciphertext)
    elif choice == 'd':
        ciphertext = int(input("Enter message to decrypt: "))
        decrypted_number = decrypt(ciphertext, private_key)
        decrypted_message = base64_number_to_string(decrypted_number)
        print("Decrypted Message:", decrypted_message)

if __name__ == "__main__":
    print("1: Generate keys")
    print("2: Encrypt or Decrypt")
    choice = input("Enter 1 or 2: ").strip()
    if choice == '1':
        first_run()
    elif choice == '2':
        second_run()
