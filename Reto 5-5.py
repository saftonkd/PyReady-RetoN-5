def promedio_aritmetico(lista) :
    return sum(lista) / 5

def promedio_geometrico(lista) :
    promedio_geometrico : float = (primer_numero * segundo_numero * tercer_numero * cuarto_numero * quinto_numero) / 5
    return promedio_geometrico

def potencia_mayor_numero(lista) :
    potencia = max(lista)**min(lista)
    return potencia

def raiz_menor_numero(lista) :
    raiz_cubica : float =  min(lista)**(1/3)
    return raiz_cubica

if __name__ == "__main__" :
    primer_numero = float(input("Ingrese el primer número: "))
    segundo_numero = float(input("Ingrese el segundo número: "))
    tercer_numero = float(input("Ingrese el tercer número: "))
    cuarto_numero = float(input("Ingrese el cuarto número: "))
    quinto_numero = float(input("Ingrese el quinto número: "))
    lista : list = []
    lista.append(primer_numero)
    lista.append(segundo_numero)
    lista.append(tercer_numero)
    lista.append(cuarto_numero)
    lista.append(quinto_numero)
    media_aritmetica : float = promedio_aritmetico(lista)
    media_geometrica : float = promedio_geometrico(lista)
    potencia : float = potencia_mayor_numero(lista)
    raiz_cubica: float = raiz_menor_numero(lista)
    print("La media aritmética de los números es: " + str(media_aritmetica))
    print("La media geométrica de los números es: " + str(media_geometrica))
    print("El resultado de elevar el mayor número al menor número es: " + str(potencia))
    print("La raíz cúbica del menor número es: " + str(raiz_cubica))
    print(lista)

    