
renda_mensal = float(input("Digite a renda mensal do solicitante: "))
valor_emprestimo = float(input("Digite o valor total do emprestimo solicitado: "))
numero_prestacoes = int(input("Digite o numero de prestacoes desejadas: "))


limite_emprestimo = renda_mensal * 10


valor_prestacao = valor_emprestimo / numero_prestacoes


limite_prestacao = renda_mensal * 0.30


if valor_emprestimo <= limite_emprestimo and valor_prestacao <= limite_prestacao:
    print("o emprestimo pode ser concedido.")
else:
    print("o emprestimo nao pode ser concedido.")
