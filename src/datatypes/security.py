# Example starter code
def encrypt_data(data, key):
    # Use XOR (^) bitwise operation to encrypt
    # Your code here
    pass

def decrypt_data(encrypted_data, key):
    # XOR is its own inverse, so the same operation decrypts!
    # Your code here
    pass

def flip_specific_bit(number, bit_position):
    # Flip just one bit in the number
    # Your code here
    pass

if __name__ == "__main__":

    # Test your functions
    original = 83  # Binary: 01010011
    key = 42       # Binary: 00101010
    encrypted = encrypt_data(original, key)
    decrypted = decrypt_data(encrypted, key)

    print(f"Original: {original} (Binary: {bin(original)})")
    print(f"Encrypted: {encrypted} (Binary: {bin(encrypted)})")
    print(f"Decrypted: {decrypted} (Binary: {bin(decrypted)})")

    # Test bit flipping
    number = 15    # Binary: 1111
    flipped = flip_specific_bit(number, 2)
    print(f"Original: {number} (Binary: {bin(number)})")
    print(f"After flipping bit 2: {flipped} (Binary: {bin(flipped)})")