nomecompleto = str(input('Qual é o seu nome? '))
print('Em letras maiúsculas: {}'.format(nomecompleto.upper()))
print('Em letras minúsculas: {}'.format(nomecompleto.lower()))
print('Tudo junto: {}'.format(nomecompleto.replace(' ', '')))
nomes_separados = nomecompleto.split()
primeiro_nome = nomes_separados[0]
print('Qual é o primeiro nome: {}'.format(primeiro_nome))
print('Quantas letras tem o primeiro nome: {}'.format(len(primeiro_nome)))