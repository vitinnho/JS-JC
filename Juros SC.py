################################################
##### PROGRAMADO POR: LEANDRO L. MONTANARI #####
################################################


def ppv(x):
    nx = x.replace(',', '.')
    if nx.count('.') == 0:
        fx = int(nx)
    else:
        fx = float(nx)
    return fx


def msv(k):
    mf = '{:.2f}'.format(k)
    dec = mf[-2:]
    intf = '{:,}'.format(int(k))
    antes = str(intf).replace(',', '.')
    fn = '{}{}{}'.format(antes, ',', dec)
    return fn


def ciclo(m):
    while True:
        try:
            v = ppv(str(input(m)))
            return v
        except ValueError:
            print('\nVocê digitou um ou mais caracteres inválidos. '
                  'Digite apenas números, separando as casas decimais com ponto ou vírgula!\n')
            continue


div = ('=' * 85)

print()
print(div)
print('{:^85}'.format('SIMULADOR DE JUROS COMPOSTOS'))
print(div)
print()

ii = ciclo('Digite o investimento inicial (digite 0 para nenhum): R$ ')
ad = ciclo('Digite o valor fixo que deseja depositar todo mês (digite 0 para nenhum)? R$ ')
jr = ciclo('Digite a porcentagem de rendimento mensal dos juros compostos: ')
anos = ciclo('Digite a quantidade de anos que quer deixar rendendo: ')
meses = int(anos * 12)
total = ii
dep = 0

for vezes in range(1, (meses + 1)):
    dep += ad
    total += (total * jr / 100)
    total += ad

dep = dep + ii
jcom = total - dep

ii = msv(ii)
ad = msv(ad)
jr = msv(jr)
total = msv(total)
dep = msv(dep)
jcom = msv(jcom)

if anos == 1:
    man = 'ANO'
else:
    man = 'ANOS'

print()
print(div)
print()

print('''INVESTIMENTO INICIAL: R$ {}
DEPÓSITO MENSAL: R$ {}
TAXA DOS JUROS COMPOSTOS: {}%
TOTAL DE MESES: {}

VALOR ACRESCIDO DO PRÓPRIO DINHEIRO: {}
VALOR ACRESCIDO EM JUROS COMPOSTOS: {}
VALOR FINAL APÓS {} {} RENDENDO: R$ {}'''.format(ii, ad, jr, meses, dep, jcom, anos, man, total))

print()
print(div)

input()