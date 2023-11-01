import getpass

encrypt_rules = {
    'A': 'S',
    'B': '!',
    'C': '6',
    'D': '*',
    'E': '#',
    'F': '@',
    'G': '?',
    'H': 'P',
    'I': '<',
    'J': 'Æ',
    'K': '1',
    'L': '(',
    'M': '┬',
    'N': '/',
    'Ñ': 'R',
    'O': '5',
    'P': '4',
    'Q': '>',
    'R': ')',
    'S': '¿',
    'T': '-',
    'U': '&',
    'V': '÷',
    'W': ']',
    'X': '¥',
    'Y': '§',
    'Z': '0',
    '0': 'U',
    '1': '±',
    '2': 'V',
    '3': '$',
    '4': 'L',
    '5': 'Y',
    '6': '|',
    '7': 'T',
    '8': 'A',
    '9': 'Q',
    '.': '%',
    ',': '+',
    ':': '£',
    '?': 'N',
    '!': 'J',
    ' ': '¬',
    '@': '¤',
}

decrypt_rules = {value: key for key, value in encrypt_rules.items()}

option = ('1','2','3')

def encrypt():
    text_input = (getpass.getpass('\nIngresa un mensaje para encriptarlo => ')).upper()

    final_text = ''

    for letter in text_input:
        if letter in encrypt_rules:
            final_text += encrypt_rules[letter]
        else:
            final_text += letter

    print('Mensaje encriptado =>')
    print(final_text[::-1])

def decrypt():
    text_input = input('\nIngresa un mensaje para desencriptarlo => ').upper()

    final_text = ''

    for letter in text_input:
        if letter in decrypt_rules:
            final_text += decrypt_rules[letter]
        else:
            final_text += letter

    print('Mensaje desencriptado =>')
    print(final_text[::-1])

def main():
    print('Bienvenido a tu encriptador de confianza, por favor elije una opcion')

    while True:
        choice_user = input('\n1_ Encriptar \n2_ Desencriptar \n3_ Salir\n==>')

        if not choice_user in option:
            print('\nIngresa una opcion correcta')

        if choice_user in option:
            if choice_user == '1':
                encrypt()
            elif choice_user == '2':
                decrypt()
            else:
                print('\nHasta la proxima!!!')
                break

main()
