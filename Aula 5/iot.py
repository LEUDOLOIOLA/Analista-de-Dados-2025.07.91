while True:
    temp_atual = float(input("Digite a temperatura atual: "))

    if temp_atual < -50 or temp_atual > 50:
        print("Leitura inválida (Erro de sensor)")
    elif temp_atual > 40:
        print("Alerta: temperatura muito alta!")
    else:
        print("Temperatura dentro do normal.") 



