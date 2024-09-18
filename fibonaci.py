def is_fibonacci(num):
    a, b = 0, 1
    if num == 0 or num == 1:
        return f"O número {num} pertence à sequência de Fibonacci."
    while b <= num:
        if b == num:
            return f"O número {num} pertence à sequência de Fibonacci."
        a, b = b, a + b
    return f"O número {num} **não** pertence à sequência de Fibonacci."

numero = int(input("Informe um número: "))
resultado = is_fibonacci(numero)
print(resultado)