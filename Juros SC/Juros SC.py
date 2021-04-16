p = float(input('Digite o valor solicitado: R$'))
i = float(input('Digite a taxa de Juros: %'))
n = int(input('Em quantas vezes quer pagar: '))
print(' ' * 1000 )

js = p * ((i / 100) * n)
parcelaS = (p + js) / n 
vjs = js + p
jc = p * ((1 + i / 100) ** n - 1)
parcelaC = (p + jc) / n 
vjc = jc + p
print(f'O valor do Juros Simples e de R${js:.2f}, totalizando {vjs:.2f}')
print(f'O valor do montante simples parcelado em {n}x e de R${parcelaS:.2f} por parcela')
print(f'O valor do Juros Composto e de R${jc:.2f}, totalizando {vjc:.2f}')
print(f'O valor do montante composto parcelado em {n}x e de R${parcelaC:.2f} por parcela')

input()
