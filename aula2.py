def divisao():
        try:
            n1 = float(input("primeiro número:"))
            n2 = float(input("segundo número:")) 
            result = (n1 / n2)
            print (result)
        except ValueError:
            print("Insira números válidos.")
        except ZeroDivisionError:
            print("Não é possível divisão por zero.")

divisao()

