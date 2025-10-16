def es_par_o_impar(número) :
    if numero % 2 == 0 :
        print("es par")
    else :
        print("es impar")

def main():
    numero = int(input("Introduce un número: "))
    resultado = es_par_o_impar(número)
    print(f"El número {numero} es {resultado}.")
    
if __name__ == "__main__":
    main()
