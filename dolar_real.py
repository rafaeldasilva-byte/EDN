# Verificar a cotação do dólar

# Importação da bibliioteca
import requests

# Conversão 

# valor = valor a ser adicionado
# lambda = função anônima
# cotacao: valor * cotacao = expressão matemática
converter_real = lambda valor, cotacao: valor * cotacao

# Cbtendo a cotação do dolár em tempo real
def obter_cotacao_dolar():
    try:
        url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
        resposta = requests.get(url)
        dados = resposta.json()

        #Validação 
        if "USDBRL" in dados:
            # USDBRL dentro de dados e o bid dentro de USDBRL, abra a api para saber
            return float(dados["USDBRL"]["bid"])
        else:
            return None
    except requests.exceptions.RequestException:
        print("Erro ao tentar acessar a API.")
        return None
    
# Imputação de dados
def main():
    try:
        # Variáveis
        valor_dolar = float(input("Digite o valor em Dólar (USD): "))

        #Função chamando outra
        cotacao = obter_cotacao_dolar()

        # Se a cotacao não é zero
        if cotacao:
            valor_real = converter_real(valor_dolar, cotacao)
            print(f"USD {valor_dolar:.2f}")
            print(f"Cotação: R${cotacao:.2f}")
            print(f"Valor em reais: R${valor_real:.2f}")
        else:
            print("Não foi possível obter a cotação.")
    except ValueError:
        print ("Digite um número válido")
    except Exception as erro:
        print ("Erro inesperado", erro)

main()
