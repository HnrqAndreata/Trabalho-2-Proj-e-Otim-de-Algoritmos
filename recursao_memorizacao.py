#Henrique Andreata
import sys
global caminho_rec
global caminho_cache
caminho_cache = {}

#Recursão com Memorização
def caminho_recursao_mem(n, cansado):   
    key=(n,cansado)
    if key in caminho_cache:
        return caminho_cache[key]
        
    else:
        if n == 1:
            return 1
    
        if n < 1 :
            return 0
        
        if caminho_rec[n-1]=='0':
            return 0

        if(not cansado):
            value = caminho_recursao_mem(n-1,False) + caminho_recursao_mem(n-2,False) + caminho_recursao_mem(n-3,True)
            caminho_cache[n,cansado] = value
            return value

        else:
            value = caminho_recursao_mem(n-1,False) + caminho_recursao_mem(n-2,False)
            caminho_cache[n,cansado] = value
            return value

caminho_rec=sys.argv[1]
print("Memorizacao =",caminho_recursao_mem(len(caminho_rec),False),"caminhos possiveis")

