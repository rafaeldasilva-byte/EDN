# Conversor de Moedas
def conversor():
    # Variáveis
    real = 100.00
    taxa_dolar = 5.20
    taxa_euro = 6.15

    # Cálculos
    dolar = real * taxa_dolar
    euro = real * taxa_euro

    # Resultado
    print (f"R$ {real:.2f} convertido para: \nDólar: ${dolar:.2f}")
    print (f"Euro: €{euro:.2f}")
conversor()

# Calculadora de Desconto
def desconto():
    # Variáveis
    produto = "Camisa"
    preco = 50.00
    porcentagem = int(input ("Insira a porcentagem de desconto (somente números):"))
    desc = porcentagem * 0.01
    valor_desc = preco * desc 
    preco_final = preco - valor_desc

    # Resultado
    print (f"Ao comprar {produto}, você terá um desconto de R${valor_desc:.2f}, pagando R${preco_final:.2f} no final.")
desconto()

# Calculadora de Média Escolar
def media(*notas):
    # Variáveis
    n = len(notas)
    cal_media = (sum(notas))/n

    # Aprovação ou Reprovação
    if cal_media >= 6.00:
        resultado = "Aprovado"
    else:
        resultado = "Reprovado"
    # Resultado
    print ("O aluno(a) obteve as seguintes resultados:")
    for i, notas in enumerate(notas, start=1):
        print(f"Nota {i}: {notas:.2f}")
    print (f"Média: {cal_media:.2f}")
    print (f"Portanto, o aluno está {resultado}")
    
media(7.5,8,6.5)

# Calculadora de Consumo de Combustível
def calculo_consumo():
    # Imputação de valores
    distancia_percorrida = float(input("Qual a distância percorrida em km:"))
    combustivel_gasto = float(input("Quanto de combustível foi gasto em L:"))

    # Resposta
    consumo_medio = distancia_percorrida/combustivel_gasto

    #Resultado
    print (f"Dados da viagem: \nDistância: {distancia_percorrida} km;\nCombustível Gasto: {combustivel_gasto} L; \nConsumo Médio: {consumo_medio:.2f} km/L.")

calculo_consumo()
