# yeah
try:
    valor = int(input('Qual sera o valor para ser sacado?: '))
except ValueError:
    print("Um erro ocorreu em sua resposta.")
if valor <= 0:
    raise Exception("O valor de saque deve ser maior que 0")

cinquenta = int(valor/50)
valor = valor % 50

vinte = int(valor/20)
valor = valor % 20

dez = int(valor/10)
valor = valor % 10

um = valor

if cinquenta >= 1:
    print("Sacar",cinquenta,"de R$50,00")
if vinte >= 1:    
    print("Sacar",vinte,"de R$20,00")
if dez >= 1:
    print("Sacar",dez,"de R$10,00")
if um >= 1:
    print("Sacar",um,"de R$1,00")