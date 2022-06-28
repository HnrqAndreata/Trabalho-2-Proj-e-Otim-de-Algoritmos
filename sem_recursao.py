#Henrique Andreata
import sys
from random import randint
from collections import Counter

#Versao 100% gambiarra
#peço perdão caso pegue fogo no computador dos indios pq ta terrívelmente mal otimizado, mas é a única versão que consegui algo correto (｡◕‿‿◕｡)
#resultado pode ter erro de 1ou2 por causa do jeito que eu monto a lista de possibilidades
def __Check__(Caminho, Teste):
    n = 0
    prev = 0
    for i in Teste:
        if prev == 3 and i == prev:
            return 0
        prev = i
        n += i
        if Caminho[n] == '0':
            return 0

    return 1


def __Caminho__(num):
    COUNT = Counter(num)
    CAMINHOS = []
    for _ in range(5**((len(num) - 1))):#quanto maior esse range, mais chances de achar resultado certo, mas tbm mais pesado fica de rodar
        POSSIVEL = list(randint(0, 3) for _ in range(len(num) - 1 - COUNT['0']))
        if sum(POSSIVEL) == (len(num) - 1):
            #if POSSIVEL

            if 0 in POSSIVEL:
                POSSIVEL = tuple(filter(lambda i: i > 0, POSSIVEL))
            if POSSIVEL not in CAMINHOS:
                CAMINHOS.append(POSSIVEL)

    res = (__Check__(num, j) for j in CAMINHOS)
    #print(CAMINHOS)

    #print(len(CAMINHOS))
    return sum(res)

print("Sem Recursao =",__Caminho__(sys.argv[1]),"caminhos")
