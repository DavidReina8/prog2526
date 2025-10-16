#cuenta cuantas 'a' hay en una frase
#Definir fubción
def cuentaA(texto) :
    cuenta = texto.count("a") + texto.count("A")
    return cuenta

# Invocar función


frase = "Hola y Adios"
print(cuentaA(frase))
