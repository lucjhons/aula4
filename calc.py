def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

if __name__ == "__main__":
    print("Teste de operações matemáticas:")
    print(f"Somar 5 + 3 = {somar(5, 3)}")
     
