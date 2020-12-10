# <comentario>
def verif():
    if precoProduto <= 0:
        raise Exception("O preço do produto deve ser maior que 0")

def choice():
    if (metodoPagamento <1) or (metodoPagamento >4):
        raise Exception("O metodo de pagamento deve ser escolhido entre 1 a 4")

try:
    precoProduto = float(input("Insira o preço do produto: "))
    verif()
    metodoPagamento = int(input("Escolha o metodo de pagamento \n 1 - a vista\n 2 - a prazo em 1x no cartão\n 3 - a prazo da loja em 5x\n 4 - a prazo da loja em 10x\nInsira o numero correspondente ao metodo de pagamento que você deseja: "))
    choice()
except ValueError:
    print("Um erro ocorreu em sua resposta.")

if metodoPagamento == 1:
    precoProduto = precoProduto/2
if metodoPagamento == 2:
    precoProduto = precoProduto - (precoProduto * 0.1)
if metodoPagamento == 3:
    x = 5
    precoProduto = precoProduto + ((precoProduto/100)* 10)
    parcelas = precoProduto / x
if metodoPagamento == 4:
    x = 10
    precoProduto = precoProduto * 2     
    parcelas = precoProduto / x

print("O preço do produto é: R$ %.2f" %precoProduto)
if metodoPagamento >= 3:
    print("O preço do produto em",x,"parcelas é de R$ %.2f" % parcelas)