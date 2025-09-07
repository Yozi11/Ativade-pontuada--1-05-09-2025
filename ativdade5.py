      
operacao = input("Digite o codigo da operacao (+, -, *, ou /): ")
num1 = int(input("Digite o primeiro valor inteiro (A): "))   
num2 = int(input("Digite o segundo valor inteiro (B): "))
print("Erro: Por favor, insira valores inteiros validos.")

        

    
if operacao == '+':
        resultado = num1 + num2
        print(f"O resultado de {num1} + {num2} e: {resultado}")
elif operacao == '-':
        resultado = num1 - num2
        print(f"O resultado de {num1} - {num2} e: {resultado}")
elif operacao == '*':
        resultado = num1 * num2
        print(f"O resultado de {num1} * {num2} e: {resultado}")
elif operacao == '/':
        
        if num2 != 0:
            resultado = num1 / num2
            print(f"O resultado de {num1} / {num2} e: {resultado}")
        else:
            print("Erro: Divisao por zero nao e permitida.")
else:
        print("Erro: Operacao invalida. Use +, -, * ou /.")


