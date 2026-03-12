linhas = int(input("Digite o tamanho da base: "))
colunas = int(input("Digite o tamanho dos lados: "))
print(linhas)
print(colunas)
if linhas>0 and colunas>0:
    for l in range (linhas):
        for c in range (colunas):
            if l == 0:
                x = colunas*"* "
                print(x)