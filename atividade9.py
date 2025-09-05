
renda_mensal = float(input("Digite a renda mensal do solicitante: "))
valor_emprestimo = float(input("Digite o valor total do empréstimo solicitado: "))
numero_prestacoes = int(input("Digite o número de prestações desejadas: "))


limite_emprestimo = renda_mensal * 10


valor_prestacao = valor_emprestimo / numero_prestacoes


limite_prestacao = renda_mensal * 0.30


if valor_emprestimo <= limite_emprestimo and valor_prestacao <= limite_prestacao:
    print("O empréstimo pode ser concedido.")
else:
    print("O empréstimo NÃO pode ser concedido.")
