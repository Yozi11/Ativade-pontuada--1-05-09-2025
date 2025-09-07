
tabela_precos = {
    "verde": 10.00,
    "azul": 20.00,
    "amarelo": 30.00,
    "vermelho": 40.00
}


cor = input("Digite a cor do CD (verde, azul, amarelo, vermelho): ")


if cor in tabela_precos:
    preco = tabela_precos[cor]
    print(f"O preco do CD da cor {cor} e R$ {preco:.2f}")
else:
    print("Cor invalida por favor, digite uma cor valida.")
