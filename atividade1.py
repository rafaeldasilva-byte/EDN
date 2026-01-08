
# 1- Programa de Saudação
def saudacao():
    print ("Hello world!")
saudacao()

# 2- Calculadora de Soma
def soma():
    numero1 = 12
    numero2 = 14
    result = numero1 + numero2
    print (f"A soma é igual a: {result}")
soma()

# 3- Calculadora de Volume
def volume():
    comprimento = 12
    largura = 14 
    altura = 20
    result = comprimento * largura * altura 
    print (f"O volume é igual a: {result} cm³")
volume()

# 4- Calculadora de Preço Total
def preco():
    produto = "Cadeira Infantil"
    preco_unit = 12.40
    qntd = 3
    result = preco_unit * qntd
    print(f"Ao comprar {qntd} {produto} a R${preco_unit} a unidade, gasta-se R${result}.")
preco()