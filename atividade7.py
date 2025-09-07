
descricao_produto = input("Digite a descricao do produto: ")
quantidade_adquirida = int(input("Digite a quantidade adquirida: "))
preco_unitario = float(input("Digite o preco unitario: "))


total = quantidade_adquirida * preco_unitario


if quantidade_adquirida <= 5:
    percentagem_desconto = 2
elif 5 < quantidade_adquirida <= 10:
    percentagem_desconto = 3
else:
    percentagem_desconto = 5


desconto = total * (percentagem_desconto / 100)


total_a_pagar = total - desconto


print(f"\ndescricao do produto: {descricao_produto}")
print(f"total Bruto: ${total:.2f}")
print(f"desconto ({percentagem_desconto}%): ${desconto:.2f}")
print(f"total a pagar: ${total_a_pagar:.2f}")