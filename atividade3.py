#Classificador de Idade

def faixa_etaria():
    idade = input("Digite sua idade:")
    try:
        valor = int(idade)
        if valor >= 60:
            print ("Parabéns, você é um Idoso.")        
        elif valor >= 18:
            print ("Parabéns, você é um Adulto.")
        elif valor >= 13:
            print ("Parabéns, você é um Adolescente.")
        else:
            print ("Parabéns, você é uma Criança.")
    except ValueError:
        print("Erro, o valor digitado não é um número inteiro")
#faixa_etaria()

# Calculadora de IMC
def cal_imc():  
    peso = (input("Seu peso em kg:"))
    altura = (input("Sua altura em m:"))
    if peso:
        try:
            v1 = float(peso)
        except:
            print("Erro de letra em peso.")        
    else:
        if altura:
            print("Digite algo em peso")
        else:
            print("Digite algo em ambas")          
    if altura:
        try:
            v2 = float(altura)
            imc = v1/(v2 ** 2)
            if imc > 30:
                grupo = "Obeso"
            elif imc >= 25:
                grupo = "Sobrepeso"
            elif imc >= 18.5:
                grupo = "Peso Normal"
            else:
                grupo = "Abaixo do peso"
                
            
            print(f"Seu imc é igual a {imc}.\nVoce se enquadra como {grupo}.")
            
        except:
            print ("Erro de letra em altura\n")
    else:
        print("Digite algo em altura")
               
        
#cal_imc()

# Conversor de temperatura
def con_temp():
    unidade_origem = input("Qual a unidade de origem?\n1 - Celsius,\n2 - Fahrenheit,\n3 - Kelvin.\n")
    numero = input("Qual a temperatura?")
    unidade_destino = input("Para qual unidade deseja converter?\n1 - Celsius,\n2 - Fahrenheit,\n3 - Kelvin.\n")    
   #1 = Celsius
   #2 = Fahrenheit
   #3 = Kelvin
    try:
        origem = int(unidade_origem) 
        n = float(numero)
        destino = int(unidade_destino)
        # Celsius
        if origem == 1:
            if destino == origem:
                print(f"Não é possível converter algo para si mesmo. Portanto {n}°C é igual a {n}°C.")            
            elif destino ==2:
                x = (n * 1.8) + 32
                print(f"Resultado: {n:.1f}°C = {x:.1f}°F.")           
            elif destino ==3:
                x = 273.15 + n
                print(f"Resultado: {n:.1f}°C = {x:.1f} K.")
            else:
                print("Insira um número válido.")
        # Fahrenheit
        elif origem == 2:
            if destino == origem:
                print(f"Não é possível converter algo para si mesmo. Portanto {n}°F é igual a {n}°F.")            
            elif destino == 1:
                x = (n - 32)/1.8
                print(f"Resultado: {n:.1f}°F = {x:.1f}°C.")
            elif destino ==3:
                x = ((n - 32)/1.8) + 273.15
                print(f"Resultado: {n:.1f}°C = {x:.1f}°F.")
            else:
                print("Insira um número válido.")
        # Kelvin
        else:
            if destino == origem:
                print(f"Não é possível converter algo para si mesmo. Portanto {n} K é igual a {n} K.")            
            elif destino ==1:
                x = n - 273.15
                print(f"Resultado: {n:.1f} K = {x:.1f}°C.")
            elif destino ==2:
                x = ((n - 273.15)*1.8) + 32
                print(f"Resultado: {n:.1f} K = {x:.1f}°F.")
            else:
                print("Insira um número válido.")
        
    # Erro na validação                
    except:    
        if not unidade_origem.isdigit() or len(origem) > 1:
             unidade_origem += input("Reinsira qual a unidade de origem corretamente.\n1 - Celsius,\n2 - Fahrenheit,\n3 - Kelvin\n")
        else:
            pass
        if not unidade_destino.isdigit() or len(destino) > 1:
             unidade_destino += input("Reinsira qual a unidade de destino corretamente.\n1 - Celsius,\n2 - Fahrenheit,\n3 - Kelvin\n")
        else:
            pass
        if not numero.isdigit() or len(numero) > 1:
            numero += input("Reinsira um número válido para a temperatura.\n")   
        else:
            pass
#con_temp()

# Verificar se o ano é bisexto

def bissexto():
    ano = int(input("Qual o ano que deseja verificar: "))
    
    # Traduzindo a regra para o Python:
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"O ano {ano} é BISSEXTO!")
    else:
        print(f"O ano {ano} NÃO é bissexto.")
#bissexto()