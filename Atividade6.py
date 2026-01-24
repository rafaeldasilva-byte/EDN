#Senhas automáticas
def senha_automatica():
    import secrets
    import string
    while True:
        try:
            tamanho_senha = int(input("Qual o tamanho da sua senha:"))
            combinacao = string.ascii_letters + string.digits + string.punctuation
            senha = ''.join(secrets.choice(combinacao) for i in range (tamanho_senha))
            print(f"Sua senha é: {senha}")
            return senha
        except ValueError:
            print("Insira somente valores inteiros.")
#senha_automatica()

#Usuário aleatório api

def API():
    import requests

    #Obtendo o nome, email e país
    try:
        url = "https://randomuser.me/api/?inc=name,email,location"
        resposta = requests.get(url)
        dados = resposta.json()

        if "results" in dados:
            usuario = dados["results"][0]
            primeiro_nome =  usuario["name"]["first"]
            ultimo_nome = usuario["name"]["last"]
            nome = " ".join([primeiro_nome, ultimo_nome])

            email = usuario["email"]
            pais = usuario["location"]["country"]
            return nome, email, pais
        else:
            return None, None, None
    except requests.exceptions.RequestException:
        print("Erro ao tentar acessar a API.")
        return None, None, None
    
# Resultado
def resultado():
    nome_fim, email_fim, pais_fim = API()
    if nome_fim:
        print(f"Nome: {nome_fim}\nE-mail: {email_fim}\nPaís: {pais_fim}")
    else:
        print("Não foi possível obter os resultados")

#API()
#resultado()

#Consultar CEP e retornar logradouro, bairro, cidade e estado 

# Consulta e e pesquisa
def obtendo_cep(cep):
    import requests
    try:
        url = (f"https://viacep.com.br/ws/{cep}/json/")
        resposta = requests.get(url)
        dados = resposta.json()

        if "erro" not in dados:
            return {
                "logradouro": dados.get("logradouro"),
                "bairro": dados.get("bairro"),
                "cidade": dados.get("localidade"),
                "estado": dados.get("estado")
            }
        else:
            print ("CEP não encontrado na base de dados.")
    except Exception as e:
        print(f"Ocorreum um erro ineserado: {e}")
        

# Imputação dos dados
def dados_cep():    
    while True:
        cep = input("Digite seu CEP: ").replace("-", "").replace(".", "").strip()
        if len(cep) == 8 and cep.isdigit():
            return cep
        else:
            print ("CEP inválido! O CEP deve conter exatamente 8 números.")
    
# Resultado
def cep_resultado():
    cep = dados_cep() 
    dados_tudo = obtendo_cep(cep)
    cep_limpo = f"{cep[:5]}-{cep[5:]}"
    if dados_tudo is not None:
        print (f"CEP: {cep_limpo}\nLogradouro: {dados_tudo['logradouro']}\nBairro: {dados_tudo['bairro']}\nCidade: {dados_tudo['cidade']}\nEstado: {dados_tudo['estado']}")
    else:
        print("Operação cancelada: O CEP digitado não existe ou é inválido")

#cep_resultado()

#  Cotações moedas

# Obtendo Cotações
def obtendo_cotacoes():
    import requests
    try:
        url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,GBP-BRL,JPY-BRL,ARS-BRL,BTC-BRL"
        resposta = requests.get(url)
        dados = resposta.json()

        if "erro" not in dados:
            dolar = dados['USDBRL']
            euro = dados['EURBRL']
            libra = dados['GBPBRL']
            iene = dados['JPYBRL']
            peso = dados['ARSBRL']
            bitcoin = dados['BTCBRL']
            return dolar, euro, libra, iene, peso, bitcoin, dados
        else:
            print("Valores não encontrados.")

    except Exception as erro:
        print(f"Operação improcessável, erro: {erro}")

# Resultado
def resultado():
    dolar, euro, libra, iene, peso, bitcoin, dados = obtendo_cotacoes()
    if dados:
        print("-----COTAÇÕES-----")
        print(f"DÓLAR: \nR${float(dolar['bid']):.2f}\nMáxima: {float(dolar['high']):.2f}\nMínima: {float(dolar['low']):.2f}\nÚltima atualização: {dolar['create_date']}\n")
        print(f"EURO: \nR${float(euro['bid']):.2f}\nMáxima: {float(euro['high']):.2f}\nMínima: {float(euro['low']):.2f}\nÚltima atualização: {euro['create_date']}\n")
        print(f"LIBRA: \nR${float(libra['bid']):.2f}\nMáxima: {float(libra['high']):.2f}\nMínima: {float(libra['low']):.2f}\nÚltima atualização: {libra['create_date']}\n")
        print(f"IENE: \nR${float(iene['bid']):.2f}\nMáxima: {float(iene['high']):.2f}\nMínima: {float(iene['low']):.2f}\nÚltima atualização: {iene['create_date']}\n")
        print(f"PESO ARG: \nR${float(peso['bid']):.2f}\nMáxima: {float(peso['high']):.2f}\nMínima: {float(peso['low']):.2f}\nÚltima atualização: {peso['create_date']}\n")
        print(f"BITCOIN: \nR${float(bitcoin['bid']):.2f}\nMáxima: {float(bitcoin['high']):.2f}\nMínima: {float(bitcoin['low']):.2f}\nÚltima atualização: {bitcoin['create_date']}")
    else:
        print("Cancelando a operação, valores não encontrados.")
#resultado()





