#Calculadora completa
def cal():
    n1 = input("Insira o primeiro número na calculadora: \n")
    n2 = input("Insira o segundo número na calculadora: \n")
    operador = input("Qual operação deseja realizar:\n1 - Soma (+)\n2 - Subtração (-)\n3 - Multiplicação (×)\n4 - Divisão (÷)\n")
    try:
        nn1 = float(n1)
        nn2 = float(n2)
        op = int(operador)
        if op == 1:
            result = (nn1 + nn2)
            print (f"{nn1} + {nn2} = {result}")
        elif op == 2:
            result = (nn1 - nn2)
            print (f"{nn1} - {nn2} = {result}")
        elif op == 3:
            result = (nn1 * nn2)
            print (f"{nn1} × {nn2} = {result}")
        elif op == 4:
            result = (nn1 / nn2)
            print (f"{nn1} ÷ {nn2} = {result}")
        else:
            print("Insira o valor corretamente")
    except:
        print ("Insira corretamente.")   
#cal()

#Média Alunos

def media():
    notas = [] 
    
    while True:
        entrada = input("Digite as notas para o ćaluculo da média (ou 'fim' para sair): ")
        
        if entrada.lower() == 'fim':
            break
            
        try:
            nota = float(entrada) # Converte o texto para número
            notas.append(nota)    # Adiciona a nota na lista
        except ValueError:
            print("Por favor, digite um número válido ou 'fim'.")

    if notas:
        resultado = sum(notas) / len(notas)
        print(f"A média das {len(notas)} notas é: {resultado:.2f}")
    else:
        print("Nenhuma nota foi inserida.")

#media()

#Senha critérios

def criterio():
    while True:
        entrada = input("Insira uma senha: ")

        try:
            senha = str(entrada)
        except ValueError:
            print ("Não insira somente números.")

        if len(senha) >= 8 and any(c.isdigit() for c in senha):
            print("Senha válida")
            break
        else:
            print ("A senha deve ter as seguintes condições:\nMínimo 8 caracteres;\nAo menos 1 número.")
        if not entrada:
            print("Insira algo.")
#criterio()

#Contagem de números pares e impares

def contagem():
    impares = []
    pares = []
    numeros = []

    while True:
        entrada = input("Digite o número para análise (ou 'fim' para terminar): ")
        if entrada.lower() == 'fim':
            break
        if entrada.isdigit():
            numeros.append(int(entrada))
        else:
            print("Digite apenas números inteiros")
    
    for n in numeros:
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)
    
    print(f"Exitem {len(numeros)} números ao todo, sendo:\n{len(pares)} Par(es): {pares}\n{len(impares)} Ímpar(es): {impares}")
#contagem()
        
        