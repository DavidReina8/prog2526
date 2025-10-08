nota = int(input("introduzca una nota"))
match nota:
    case 1 | 2 | 3 | 4 :
        print(nota ," es un insuficiente")
    case 5:
        print(nota ," es un suficiente")
    case 6 :
        print(nota ," es un bien")
    case 7 | 8 :
        print(nota ," es un notable")
    case 9 | 10 :
        print(nota ," es un sobresaliente")
    case _:
        print(" a ocurrido un error (recuerda que no admite decimales")
        
