r1 = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(r1))
print('O caractere é do tipo numérico?', r1.isnumeric())
print('O caractere é do tipo alfanumérico?', r1.isalnum())
print('O caractere é do tipo alfabético?', r1.isalpha())
print('O caractere está em letras maiúsculas?', r1.isupper())
print('O caractere está em letras minúsculas?', r1.islower())
print('O caractere está capitalizado?', r1.istitle())
print('O caractere é um caractere ascii?', r1.isascii())
print('Só possui espaços?',  r1.isspace())
