# This code was written by Mane Avoyan at the National Polytechnic University of Armenia. 
# This assignment was completed as part of the "Information Security" training program for group 255-3. 
# All rights to this code belong to the author. 
# This code may not be copied or used without the author's permission. 
# Citing the author is mandatory when using this code. 
# You can take this if you need, only with respect of author and its knowledge.
import random

def generate_private_key(prime):
    return random.randint(1, prime - 1)

def compute_public_key(prime, base, private_key):
    return pow(base, private_key, prime)

def compute_shared_secret(prime, other_public_key, private_key):
    return pow(other_public_key, private_key, prime)

N = 23
G = 5


alice_private_key = generate_private_key(N)
alice_public_key = compute_public_key(N, G, alice_private_key)

print(f"Alice's Private Key: {alice_private_key}")
print(f"Alice's Public Key: {alice_public_key}")
other_public = int(input("Give your pubilc key: "))
# bob_private_key = generate_private_key(N)
# bob_public_key = compute_public_key(N, G, bob_private_key)

alice_shared_secret = compute_shared_secret(N, other_public, alice_private_key)
# bob_shared_secret = compute_shared_secret(N, alice_public_key, bob_private_key)

# print(f"Bob's Private Key: {bob_private_key}")
# print(f"Bob's Public Key: {bob_public_key}")
print(f"Alice's Shared Secret: {alice_shared_secret}")
# print(f"Bob's Shared Secret: {bob_shared_secret}")
