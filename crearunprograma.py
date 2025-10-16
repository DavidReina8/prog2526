def es_par_o_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

def main():
    numero = int(input("Introduce un número: "))
    resultado = es_par_o_impar(numero)
    print(f"El número {numero} es {resultado}.")

if __name__ == "__main__":
    main()
