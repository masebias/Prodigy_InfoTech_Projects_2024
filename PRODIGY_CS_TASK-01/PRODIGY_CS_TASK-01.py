

# Define the alphabet
letter = "abcdefghijklmnopqrstuvwxyz"

# Get user input for encryption or decryption
mode = ""
print("Tools for Encrypting or Decrypting Caesar Cipher")
print()

while mode not in ['e', 'd']:
    mode = input("Please select an option: \n\nEnter e for ENCRYPTION, d for DECRYPTION: ").lower()

# Get user input for the shift value
shift = int(input("Enter the shift value: "))

# Define function for encryption
def encrypt(text, shift):
    result = ""
    for char in text:
        if char in letter:
            index = letter.index(char)
            new_index = (index + shift) % 26
            result += letter[new_index]
        else:
            result += char
    return result

# Define function for decryption
def decrypt(text, shift):
    result = ""
    for char in text:
        if char in letter:
            index = letter.index(char)
            new_index = (index - shift) % 26
            result += letter[new_index]
        else:
            result += char
    return result

# Get user input for the text to encrypt/decrypt
text = input("Enter the text to encrypt/decrypt: ")

# Perform encryption or decryption based on user choice
if mode == 'e':
    print("The encrypted text: ", encrypt(text.lower(), shift))
else:
    print("The decrypted text: ", decrypt(text.lower(), shift))

