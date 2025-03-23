import random

def private_key(prime):
    return random.randint(2, prime - 2)

def public_key(base, private, prime):
    return (base ** private) % prime

def shared_secret(public, private, prime):
    return (public ** private) % prime

prime = 23
base = 5

# alice_private = private_key(prime)
# alice_public = public_key(base, alice_private, prime)

bob_private = private_key(prime)
bob_public = public_key(base, bob_private, prime)

print(f"Bob Private: {bob_private}")
print(f"Bob Public: {bob_public}")
other_public = int(input("Enter public key: "))
# alice_secret = shared_secret(bob_public, alice_private, prime)
bob_secret = shared_secret(other_public, bob_private, prime)

# print(f"Alice Private: {alice_private}")
# print(f"Alice Public: {alice_public}")
# print(f"Alice Secret: {alice_secret}")
print(f"Bob Secret: {bob_secret}")
