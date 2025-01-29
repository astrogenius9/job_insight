def generate_key_table(key):
    key = "".join(dict.fromkeys(key.upper().replace("J", "I")))
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    table = [c for c in key if c in alphabet]
    table += [c for c in alphabet if c not in table]
    return [table[i:i+5] for i in range(0, 25, 5)]

def preprocess_text(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    text_pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else "X"
        if a == b:
            text_pairs.append(a + "X")
            i += 1
        else:
            text_pairs.append(a + b)
            i += 2
    if len(text_pairs[-1]) == 1:
        text_pairs[-1] += "X"
    return text_pairs

def find_position(table, char):
    for row in range(5):
        for col in range(5):
            if table[row][col] == char:
                return row, col
    raise ValueError(f"Character {char} not found in key table.")

def encrypt_pair(table, pair):
    row1, col1 = find_position(table, pair[0])
    row2, col2 = find_position(table, pair[1])
    if row1 == row2:
        return table[row1][(col1 + 1) % 5] + table[row2][(col2 + 1) % 5]
    elif col1 == col2:
        return table[(row1 + 1) % 5][col1] + table[(row2 + 1) % 5][col2]
    else:
        return table[row1][col2] + table[row2][col1]

def encrypt(plain_text, key):
    key_table = generate_key_table(key)
    text_pairs = preprocess_text(plain_text)
    cipher_text = "".join([encrypt_pair(key_table, pair) for pair in text_pairs])
    return cipher_text

# Input plaintext and key from user
key = input("Enter the key: ")
plain_text = input("Enter the plaintext: ")

cipher_text = encrypt(plain_text, key)
print(f"Cipher Text: {cipher_text}")