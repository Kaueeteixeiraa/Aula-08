import os

lista = [] 

os.system("cls")
while True:
    print("Selecione uma opcao")
    opcao = input("[I]nserir [A]pagar [L]istar [E]ditar [S]air: ")

    if opcao == "i":
        os.system("cls")
        valor = input("Digite o valor: ")
        lista.append(valor)

    elif opcao == "a":
        os.system("cls")
        apagar = input("Qual valor deseja apagar? ")
        if apagar in lista:
            lista.remove(apagar)
            print("Valor apagado")
        else:
            print("Valor não encontrado na lista")

    elif opcao == "l":
        os.system("cls")
        if len(lista) == 0:
            print("Nada para listar")
        else:
            print("Lista de valores:")
            for valor in lista:
                print(valor)

    elif opcao == "s":
        os.system("cls")
        print("Saindo do programa...")
        break

    else:
        os.system("cls")
        print("Opção inválida! Escolha uma opção válida.")

    input("Pressione Enter para continuar...")
    os.system("cls")