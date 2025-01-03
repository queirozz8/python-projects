def metade(preco=0, formato=False):
    """
    -> Retorna a metade do preço fornecido.
    preco é o preço que o usuário fornecer, se ele não fornecer nenhum preço, então o padrão é 0.
    formato é o formato que o preço vai ser mostrado. Por padrão ele é False, mas se for True, ele vai ser exibido de forma formatada, com a moeda e com vígulas ao invés de 
    pontos finais.
    Retorna res de forma não formatada se formato não for True, mas caso for, retorna com a formatação."""

    res = preco / 2
    return res if not formato else moeda(res)

def dobro(preco=0, formato=False):
    """
    -> Retorna o dobro do preço fornecido.
    preco é o preço que o usuário fornecer, se ele não fornecer nenhum preço, então o padrão é 0.
    formato é o formato que o preço vai ser mostrado. Por padrão ele é False, mas se for True, ele vai ser exibido de forma formatada, com a moeda e com vígulas ao invés de 
    pontos finais.
    Retorna res de forma não formatada se formato não for True, mas caso for, retorna com a formatação."""
    
    res = preco * 2
    return res if not formato else moeda(res)

def aumentar(preco=0, taxa=0, formato=False):
    """
    -> Retorna o preço fornecido, só que com um aumento de taxa%.
    preco é o preço que o usuário fornecer, se ele não fornecer nenhum preço, então o padrão é 0.
    taxa é a porcentagem de aumento/desconto no preço.
    formato é o formato que o preço vai ser mostrado. Por padrão ele é False, mas se for True, ele vai ser exibido de forma formatada, com a moeda e com vígulas ao invés de 
    pontos finais.
    Retorna res de forma não formatada se formato não for True, mas caso for, retorna com a formatação."""
    
    res = preco + (preco * taxa / 100)
    return res if not formato else moeda(res)

def diminuir(preco=0, taxa=0, formato=False):
    """
    -> Retorna o preço fornecido, só que com um desconto de taxa%.
    preco é o preço que o usuário fornecer, se ele não fornecer nenhum preço, então o padrão é 0.
    taxa é a porcentagem de aumento/desconto no preço.
    formato é o formato que o preço vai ser mostrado. Por padrão ele é False, mas se for True, ele vai ser exibido de forma formatada, com a moeda e com vígulas ao invés de 
    pontos finais.
    Retorna res de forma não formatada se formato não for True, mas caso for, retorna com a formatação."""

    res = preco - (preco * taxa / 100)
    return res if not formato else moeda(res)

def moeda(preco=0, moeda='R$'):
    """
    -> Mostra o preço de forma formatada, bonita.
    preco é o preço que o usuário fornecer, se ele não fornecer nenhum preço, então o padrão é 0.
    moeda é a moeda que vai ser mostrada antes do preço, você pode modificar ela se quiser, o padrão é R$, mas pode colocar USD$, etc.
    """
    
    return f'{moeda}{preco:<.2f}'.replace('.', ',')
