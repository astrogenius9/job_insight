import nltk
from nltk.corpus import words

# Point to the local NLTK data folder
nltk.data.path.append('/Users/Aditya/COLLEGE_WORK/nltk_data')


def caesar_encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result


def caesar_decrypt(text, key):
    return caesar_encrypt(text, -key)


def are_mostly_valid_words(text, threshold=0.75):
    """
    Check if a high percentage of words in the text are valid English words.

    Parameters:
    text (str): The text to check
    threshold (float): The minimum percentage of valid words to consider it valid (default 75%)

    Returns:
    bool: True if the percentage of valid words is above the threshold, False otherwise
    """
    word_list = set(words.words())

    # Split the text into words
    words_in_text = text.lower().split()

    # Count valid words
    valid_words_count = sum(1 for word in words_in_text if word in word_list)

    # Check if the valid words count exceeds the threshold percentage
    return valid_words_count / len(words_in_text) >= threshold


def caesar_brute_force_with_validation(ciphertext):
    for key in range(26):  # All possible keys (0-25)
        decrypted_text = caesar_decrypt(ciphertext, key)

        # Only print the decrypted text if a high percentage of words are valid
        if are_mostly_valid_words(decrypted_text):
            print(f"Possible key {key}: {decrypted_text}")


# Take plaintext input from the user
plaintext = input("Enter the text you want to encrypt: ")
shift_value = int(input("Enter the shift value (key) for encryption: "))

# Encrypt the plaintext using the Caesar cipher
ciphertext = caesar_encrypt(plaintext, shift_value)

print("\nEncrypted Text (Ciphertext):")
print(ciphertext)

print("\nBrute Force Results:")
caesar_brute_force_with_validation(ciphertext)
