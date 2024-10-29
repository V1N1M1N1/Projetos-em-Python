def verificar_par_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

print("Verificador de números pares e ímpares")
numero = int(input("Digite um número inteiro: "))
resultado = verificar_par_impar(numero)
print("O número", numero, "é", resultado)
