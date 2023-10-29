import getpass

rules = {
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
    '0': 'O',
    '?': '#',
    '1': 'L'
}

encript_text = ''

text_input =(getpass.getpass('Ingresa una frase para encriptarla => ')).upper()

for letter in text_input:
    if letter in rules:
        encript_text += rules.get(letter)
    else:
        encript_text += letter

print('Frace encriptada =>')
print(encript_text[::-1])
