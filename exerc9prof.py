litros = float(input("Quantos litros"))
tipo = input("Qual o combustível: ")

if tipo == "G" or tipo == "g":
    valor = litros * 5.8
    print(f" olá você abasteceu {litros} litros de Gasolina {tipo}\n"
          f" e gastou {valor} ")
elif tipo == "E" or tipo == "e":
    valor = litros * 4.9
    print(f" Olá você abasteceu {litros} litros de Etanol \n"
          f"e gastou {valor} ")
else:
    print("invalido")