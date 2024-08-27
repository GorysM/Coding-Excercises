text = 'Hello World'
shift = 3

def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''
    decrypted_text=''

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
            decrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
            original_index = (new_index - offset) % len(alphabet)
            decrypted_text += alphabet[original_index]

    print('plain text:', message)
    print('encrypted text:', encrypted_text)
    print('decrypted text: ', decrypted_text)
# Call the function to see the result
caesar(text, shift)
