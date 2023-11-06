"""
    Importamos el módulo 'getpass' para que no se muestre el input del mensaje.
"""
import getpass

# Reglas de cifrado y descifrado
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

def encrypt():
    """
        Función que encripta un mensaje ingresado por el usuario.

        Esta función solicita al usuario un mensaje,
        lo encripta utilizando las reglas de cifrado definidas en `encrypt_rules`.
        Imprime el mensaje encriptado.

    """
    text_input = (getpass.getpass('\nIngresa un mensaje para encriptarlo \n=> ')).upper()

    encrypted_message = ''

    for letter in text_input:
        if letter in encrypt_rules:
            encrypted_message += encrypt_rules.get(letter)
        else:
            encrypted_message += letter

    print('Mensaje encriptado =>')
    print(encrypted_message[::-1])

def decrypt():
    """
        Función que desencripta un mensaje ingresado por el usuario.

        Esta función solicita al usuario un mensaje encriptado, 
        lo desencripta utilizando las reglas de descifrado definidas en `decrypt_rules`.
        Imprime el mensaje desencriptado.
    """
    text_input = input('\nIngresa un mensaje para desencriptarlo \n=> ').upper()

    dencrypted_message = ''

    for character in text_input:
        if character in decrypt_rules:
            dencrypted_message += decrypt_rules.get(character)
        else:
            dencrypted_message += character

    print('Mensaje desencriptado =>')
    print(dencrypted_message[::-1])

def main():
    """
        Función principal que maneja el flujo de ejecucion.

        Muestra un menú al usuario que permite seleccionar entre tres opciones:
        1 encriptar, 2 desencriptar o 3 salir.
        El usuario ingresa su elección y se ejecuta la función correspondiente.
    """
    print('Bienvenido a tu encriptador de confianza, por favor elije una opcion')

    option = ('1','2','3')

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

if __name__ == "__main__":
    main()
input()
