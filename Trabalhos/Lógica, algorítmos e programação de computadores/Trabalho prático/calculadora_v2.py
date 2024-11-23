# Variável para controle de saída
saida = ''

# Função para adição
def adicao(a, b):
    return a + b

# Função para subtração
def subracao(a, b):
    return a - b

# Função para multiplicação
def multiplicacao(a, b):
    return a * b

# Função para divisão
def divisao(a, b):
    if b == 0:
        return "Não foi possível realizar a divisão por 0"
    return a / b

# Função calculadora
def calculadora(num1, num2, operacao):
    if operacao in ['+', 'adicao']:
        resultado = adicao(num1, num2)
    elif operacao in ['-', 'subtracao']:
        resultado = subracao(num1, num2)
    elif operacao in ['*', 'multiplicacao']:
        resultado = multiplicacao(num1, num2)
    elif operacao in ['/', 'divisao']:
        resultado = divisao(num1, num2)
    else:
        resultado = "Operação inválida"
    return resultado

# Laço para execução contínua
while saida.lower() != 'n':
    try:
        # Entrada dos números
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        # Entrada da operação
        operacao = input("Digite a operação desejada (+, -, *, / ou os nomes adicao, subtracao, multiplicacao, divisao): ").lower()
        
        # Chamando a função calculadora
        resultado = calculadora(num1, num2, operacao)
        print(f"Resultado da operação: {resultado}")
    except ValueError:
        print("Entrada inválida! Por favor, digite números válidos.")
    
    # Perguntar ao usuário se deseja continuar
    saida = input("Deseja continuar? (S/N): ").lower()
    if saida not in ['s', 'n']:
        print("Resposta inválida! Considerando como 'n'.")
        saida = 'n'

print("Programa encerrado.")