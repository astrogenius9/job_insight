def pad_data(data, block_size=8):
    """Pad data to be a multiple of the block size (8 bytes for DES)."""
    padding_len = block_size - (len(data) % block_size)
    padding = chr(padding_len) * padding_len
    return data + padding

def unpad_data(data):
    """Remove padding from the data."""
    padding_len = ord(data[-1])
    return data[:-padding_len]

def generate_key():
    """Generate a simple 64-bit (8-byte) key for demonstration."""
    return "secret_k"

def split_blocks(data, block_size=8):
    """Split data into blocks of 8 bytes."""
    return [data[i:i + block_size] for i in range(0, len(data), block_size)]

def xor_block(block, key):
    """XOR each byte of the block with the key."""
    return ''.join(chr(ord(b) ^ ord(k)) for b, k in zip(block, key))

def to_hex(data):
    """Convert a string to its hexadecimal representation."""
    return ''.join(f'{ord(c):02x}' for c in data)

def from_hex(hex_data):
    """Convert a hexadecimal string back to a normal string."""
    return ''.join(chr(int(hex_data[i:i+2], 16)) for i in range(0, len(hex_data), 2))

def des_encrypt(plaintext, key):
    """Encrypt data using a simplified DES approach."""
    # Pad plaintext to a multiple of block size
    padded_data = pad_data(plaintext)
    blocks = split_blocks(padded_data)

    # Encrypt each block
    encrypted_blocks = []
    for block in blocks:
        # Simplified round (no S-boxes or P-boxes, just XOR)
        encrypted_block = xor_block(block, key)
        encrypted_blocks.append(encrypted_block)

    # Concatenate encrypted blocks and convert to hex
    return to_hex(''.join(encrypted_blocks))

def des_decrypt(hex_ciphertext, key):
    """Decrypt data using a simplified DES approach."""
    # Convert hex ciphertext back to normal string
    ciphertext = from_hex(hex_ciphertext)

    # Split ciphertext into blocks
    blocks = split_blocks(ciphertext)

    # Decrypt each block
    decrypted_blocks = []
    for block in blocks:
        # Simplified round (no S-boxes or P-boxes, just XOR)
        decrypted_block = xor_block(block, key)
        decrypted_blocks.append(decrypted_block)

    # Concatenate decrypted blocks and remove padding
    decrypted_data = ''.join(decrypted_blocks)
    return unpad_data(decrypted_data)

# Example usage
plaintext = "Hello, World!"
key = generate_key()

# Encrypt
ciphertext_hex = des_encrypt(plaintext, key)
print("Encrypted (Hex):", ciphertext_hex)

# Decrypt
decrypted_text = des_decrypt(ciphertext_hex, key)
print("Decrypted:", decrypted_text)
