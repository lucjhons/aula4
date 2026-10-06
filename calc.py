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
    print(f"Subtrair 10 - 4 = {subtrair(10, 4)}")
    print(f"Multiplicar 7 * 6 = {multiplicar(7, 6)}")
    print(f"Dividir 8 / 2 = {dividir(8, 2)}")
    print(f"Dividir 8 / 0 = {dividir(8, 0)}")  