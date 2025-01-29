def caesar_cipher(text, shift):
    result = ""

    # Traverse the text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char  # Non-alphabetic characters remain unchanged

    return result


# Input text and shift from user
text = input("Enter text to be encrypted: ")
shift = int(input("Enter shift number: "))

encrypted_text = caesar_cipher(text, shift)
print(f"Encrypted Text: {encrypted_text}")

