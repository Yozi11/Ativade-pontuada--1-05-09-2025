preco_alcool = 3.79
preo_gasolina = 6.59

litros = float(input("digite a quantidade de litros vendidos: "))
tipos = input("digite o tipo de combustivel (A alcool, G - gasolina): ")

if tipo == "A":
    if litros <= 25:
        desconto = o.10
    else:
        desconto = 0.20
    preco_final = litros * preco_alcool * (1 - desconto)

 elif tipo == "G":
    if litros <= 25:
        desconto = 0.15
    else:
        desconto = 0.30
    preco_final = litros * preco_gasolina * (1 - desconto)
else:
    print("tipos de combustivel invalido")
    exit()
print(f"valor a ser pago: R$ {preco_final:.2f}")