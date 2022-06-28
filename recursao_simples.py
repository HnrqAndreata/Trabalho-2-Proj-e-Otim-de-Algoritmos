#Henrique Andreata
import sys
global caminhoRec 

#Recursivo Simples
def caminho_recursao_simples(n, cansado):
    if n==1:
        return 1
    if n<1:
        return 0
    if caminhoRec[n-1]=='0':
        return 0
    if(not cansado):
        return caminho_recursao_simples(n-1,False) + caminho_recursao_simples(n-2,False) + caminho_recursao_simples(n-3,True)
    else:
        return caminho_recursao_simples(n-1,False) + caminho_recursao_simples(n-2,False)


caminhoRec=sys.argv[1]
print("Recursao Simples =",caminho_recursao_simples(len(caminhoRec),False),"caminhos possiveis")