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
input()