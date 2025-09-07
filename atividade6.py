
nota1 = float(input(" insira a primeira nota: "))
nota2 = float(input(" insira a segunda nota: "))


media = (nota1 + nota2) / 2


print(f"A media do aluno e: {media:.2f}")


if media >= 6.0:
    print(" o aluno esta aprovado.")
elif 4.1 <= media <= 5.9:
    print("o aluno esta em recuperacao.")
else:
    print("o aluno foi reprovado.")