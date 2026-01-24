# Cálculo da gorjeta baseado na conta
def gorjeta():
    entrada = input("Insira o valor total da conta: R$")
    entrada2 = float(input("Quanto deseja deixar de gorjeta (ex: 10 para 10%): "))
    try:
        valor_conta = float(entrada)
        porcentagem_gorjeta = float(entrada2/100)
        real_gorjeta = (valor_conta * porcentagem_gorjeta)
    except ValueError:
        print("Insira um valor válido.")
    print (f"Gorjeta: R${real_gorjeta:,.2f}")
#gorjeta()

# Teste de Palíndromo
def palindromo():
    entrada = input("Insira a palavra: ")
    try:
        palavra = str(entrada)
        #Análise
        invertida = palavra[::-1]
        if invertida in palavra:
            resposta = "é"
        else:
            resposta = "não é"
    except ValueError:
        print("Insira uma palavra.")
    print(f"A palavra {palavra} {resposta} um palíndromo.")
palindromo()

#Preço final após desconto
def preco_final():
    entrada1 = input("Qual o preço do produto: R$")
    entrada2 = input("Qual a porcentagem de desconto (ex: 10 para 10%): ")
    try:
        preco_produto = float(entrada1)
        porcentagem_desconto = float(entrada2)    
    except ValueError:
        print("Insira valores válidos.")
    calculo_desconto = (preco_produto * (porcentagem_desconto/100))
    preco_desconto = preco_produto - calculo_desconto
    print (f"Após o desconto de {porcentagem_desconto}% o preço final será de R${preco_desconto:,.2f}.")
#preco_final()

#Dias vividos
def vida():
    from datetime import date
    hoje = date.today()
    
    try:
        entrada1 = int(input("Insira seu ano de nascimento: "))
        y = entrada1
        entrada2 = int(input("Insira seu mês de nascimento (ex: Janeiro = 1): "))
        m =entrada2
        entrada3 = int(input("Insira o dia me que nascestes: "))
        d = entrada3
        nascimento = date(y,m,d)
    except ValueError:
        print("Insira apenas números inteiros.")
    dias = hoje - nascimento
    print(f"Você está vivo a {dias}.")
#vida()