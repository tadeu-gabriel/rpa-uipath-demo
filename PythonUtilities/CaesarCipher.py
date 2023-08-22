def decrypt(ciphertext, key):
    letters = "abcdefghijklmnopqrstuvwxyz"
    letters_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    message = ""

    for char in ciphertext:
        if char in letters:      
            position = letters.find(char)
            new_pos = (position - key) % 26
            new_char = letters[new_pos]
            message += new_char
        elif char in letters_upper:
            position = letters_upper.find(char)
            new_pos = (position - key) % 26
            new_char = letters_upper[new_pos]
            message += new_char
        else:
            message += char
        return message

print(decrypt(cipher, 5))