import pytest

from datatypes.security import encrypt_data, decrypt_data, flip_specific_bit

# Test data for encryption and decryption
test_cases = [
    (83, 42, 125),  # Example from the original code
    (60, 90, 102),
    (100, 111, 211)
]

@pytest.mark.parametrize("data, key, expected", test_cases)
def test_encryption_and_decryption(data, key, expected):
    encrypted = encrypt_data(data, key)
    decrypted = decrypt_data(encrypted, key)
    assert decrypted == data
    assert encrypted == expected

# Test cases for flipping a specific bit
flip_test_cases = [
    (15, 2, 19),  # Binary: 1111 -> 1011 after flipping bit 2
    (8, 3, 12),   # Binary: 1000 -> 1100 after flipping bit 3
    (4, 0, 5)     # Binary: 0100 -> 0101 after flipping bit 0
]

@pytest.mark.parametrize("number, bit_position, expected", flip_test_cases)
def test_flip_specific_bit(number, bit_position, expected):
    result = flip_specific_bit(number, bit_position)
    assert result == expected