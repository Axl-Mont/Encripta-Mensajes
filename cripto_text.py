import getpass

text_input =(getpass.getpass('Ingresa una frase para encriptarla => ')).lower()

encript_text = ''

for letter in text_input:
    if letter == 'a':
        encript_text += '4'
    elif letter == 'e':
        encript_text += '3'
    elif letter == 'i':
        encript_text += '1'
    elif letter == 'o':
        encript_text += '0'
    elif letter == 'u':
        encript_text += 'ü'
    elif letter == ' ':
        encript_text += '-'
    elif letter == 's':
        encript_text += '5'
    elif letter == 't':
        encript_text += '7'
    elif letter == 'g':
        encript_text += '6'
    elif letter == 'b':
        encript_text += '8'
    elif letter == ',':
        encript_text += '^'
    elif letter == '.':
        encript_text += '*'
    else:
        encript_text += letter

print('Frace encriptada =>')
print(encript_text.upper()[::-1])
