def fibonacci(n):
    fib_sequencia = [0, 1]
    
    while fib_sequencia[-1] < n:
        fib_sequencia.append(fib_sequencia[-1] + fib_sequencia[-2])
    
    if n in fib_sequencia:
        print(f"O número {n} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {n} NÃO pertence à sequência de Fibonacci.")

numero_informado = 13 # Adicionar o numero manualmente
fibonacci(numero_informado)
