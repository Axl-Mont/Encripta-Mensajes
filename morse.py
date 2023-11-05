#Esta es una vacion de 

"""
    Diccionario de traducción Morse.

    Este diccionario mapea caracteres en lenguaje natural a sus equivalentes en código Morse.
    Cada clave es un carácter en lenguaje natural y
    su valor es la representación en código Morse.
    Este diccionario es utilizado porlas funciones de traducción
    para convertir entre texto y código Morse.
"""
morse_rules = {
    'A': '.-', 
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'Ñ': '--.--',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '.': '.-.-.-',
    ',': '--..--',
    ';': '-.-.-.',
    ':': '---...',
    '?': '..--..',
    '!': '-.-.--',
    '-': '-....-',
    '_': '..--.-',
    '$': '...-..-',
    '@': '.--.-.',
    ' ': '/',
}

translator_rules = {value: key for key, value in morse_rules.items()}

def convert_morse():
    """
        Convierte un mensaje de texto en código Morse.
        
        El usuario ingresa un mensaje de texto. 
        Cada letra del mensaje se convierte en su equivalente en código Morse,
        Si un carácter no se puede convertir, se muestra tal cual.
    """
    message_input = input('\nIngresa un mensaje para convertirlo a código Morse \n=> ').upper()
    morse_text = ''

    for character in message_input:
        if character in morse_rules:
            morse_text += morse_rules[character] + ' '
        else:
            print(f'El caracter {character} no se pudo convertir a Morse, se mostrará {character}')
            morse_text += character + ' '

    print('Tu mensaje en Morse =>')
    print(morse_text)

def morse_translator():
    """
        Traduce un mensaje en código Morse a texto.
    
        El usuario ingresa un mensaje en código Morse. 
        Cada secuencia Morse se traduce a su equivalente en texto,
        Si una secuencia Morse no se puede traducir, se muestra tal cual fue ingresada.
    """
    morse_input = input('\nIngresa un mensaje en Morse para traducirlo \n=> ')
    morse_characters = morse_input.split(' ')

    message = []

    for morse in morse_characters:
        if morse in translator_rules:
            message.append(translator_rules[morse])
        else:
            print(f'El caracter {morse} no está en Morse, se imprimirá {morse}')
            message.append(morse)

    translated_message = ''.join(message)
    print('Mensaje traducido =>')
    print(translated_message)

def main():
    """
        Función principal para ejecutar el traductor de Morse.
        
        El usuario elige entre convertir un mensaje a Morse o traducir un mensaje en Morse a texto. 
        Se proporcionan instrucciones claras y se maneja la interacción con el usuario.
    """
    option = ('1', '2', '3')
    print('Bienvenido a Morse Code Translator, por favor elige una opción:')

    while True:
        choice_user = input('\n1_ Convertir a Morse \n2_ Traducir de Morse \n3_ Salir\n==>')

        if choice_user not in option:
            print('\nIngresa una opción correcta')
        if choice_user in option:
            if choice_user == '1':
                convert_morse()
            elif choice_user == '2':
                morse_translator()
            else:
                print('\n¡Hasta la próxima!')
                break

if __name__ == "__main__":
    main()
input()
