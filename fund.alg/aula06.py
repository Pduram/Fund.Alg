n = int(input("Digite a quantidade de números: "))
primos = n
for i in range(n):
    x = int(input(f"Digite o número{i}: "))
    if x == 1:
        primos -= 1
    else:
        for j in range(2, x):
            if x%j == 0:
                primos -= 1
                break
print(primos,"números são primos")            