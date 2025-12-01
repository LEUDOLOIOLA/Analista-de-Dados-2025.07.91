while True:
    primeiro_numero = float(input("Digite o primeiro número: "))
    segundo_numero = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (+, -, *, /): ")

    if operacao == "+":
        print("Vamos somar...")
        print(f"O resultado é: {primeiro_numero + segundo_numero}")

    elif operacao == "-":
        print("Vamos subtrair...")
        print(f"O resultado é: {primeiro_numero - segundo_numero}")

    elif operacao == "*":
        print("Vamos multiplicar...")
        print(f"O resultado é: {primeiro_numero * segundo_numero}")

    elif operacao == "/":
        if segundo_numero == 0:
            print("Erro: o segundo número não pode ser zero!")
        else:
            print("Vamos dividir...")
            print(f"O resultado é: {primeiro_numero / segundo_numero}")

        

        
    

