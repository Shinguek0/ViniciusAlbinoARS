listanome = []
listanum = []
listandois = []
listamedia = []
pergunta=1
a=0
verify = 0
while pergunta == 1:
    nome = input("Digite o nome do aluno: ")
    listanome.append(nome)
    nota1 = float(input("Digite a primeira nota: "))
    listanum.append(nota1)
    nota2 = float(input("Digite a segunda nota: "))
    listandois.append(nota2)
    media = (nota1 + nota2)/2
    listamedia.append(media)
    a += 1
    pergunta = int(input("Você deseja cadastrar mais um aluno?\n 1 - sim\n 2 - não\nInsira o numero correspondente ao que você deseja responder:"))

for i in range(a):
    print("Nome:",listanome[i],"| Media:",listamedia[i],"\n")

print("--------------------------------------------------------------------------------------------------------------------------------")
print("Se voce deseja ver as notas de algum aluno apenas digite o nome dele, ou se você deseja finalizar o programa apenas digite(sair)")
espec = input("Digite o nome de um aluno para ver as notas: ")
if espec == "sair":
    exit()
else:
    aluno = [g.lower() for g in listanome] 
    for x in aluno:
        while espec.lower()==x:
            verify = 1
            for i in listamedia:
                if aluno.index(x) == listamedia.index(i):

                    b = listamedia.index(i)
                    b1 = aluno.index(x)
                    print("")
                    print("Nome:",listanome[b],"| Primeira nota:",listanum[b],"| Segunda nota:",listandois[b],"| Media:",listamedia[b],"\n")
            break
    if verify == 0:
        print("Ocorreu algum erro")
        print("voce pode ter digitado o nome errado tente novamente!")