import getpass

encrypt_rules = {
    'A': '4',
    'E': '3',
    'I': '1',
    'O': '0',
    'U': 'ü',
    'S': '5',
    'T': '7',
    'G': '6',
    'B': '8',
    ',': '^',
    '.': '*',
    '?': '#',
}


decrypt_rules = {value: key for key, value in encrypt_rules.items()}

print(encrypt_rules)
print(decrypt_rules)

def encrypt():
    text_input = (getpass.getpass('Ingresa un mensaje para encriptarlo => ')).upper()

    final_text = ''

    for letter in text_input:
        if letter in encrypt_rules:
            final_text += encrypt_rules[letter]
        else:
            final_text += letter

    print('Mensaje encriptado =>')
    print(final_text)

def decrypt():
    text_input = input('Ingresa un mensaje para desencriptarlo => ').upper()

    final_text = ''

    for letter in text_input:
        if letter in decrypt_rules:
            final_text += decrypt_rules[letter]
        else:
            final_text += letter

    print('Mensaje desencriptado =>')
    print(final_text)
