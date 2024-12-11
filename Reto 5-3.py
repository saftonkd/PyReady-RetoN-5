def cantidad_de_carne(gallinas, gallos, pollitos) :
    total_carne_gallina : int = 6 * gallinas
    total_carne_gallo : int = 7 * gallos
    total_carne_pollitos : int = 1 * pollitos
    return total_carne_gallina + total_carne_gallo + total_carne_pollitos

if __name__ == "__main__" :
    gallinas = int(input("Ingrese la cantidad de gallinas: "))
    gallos = int(input("Ingrese la cantidad de gallos: "))
    pollitos = int(input("Ingrese la cantidad de pollitos: "))
    total_carne : int = cantidad_de_carne(gallinas, gallos, pollitos)
    print("La cantidad total de carne de las aves en kilogramos es: " + str(total_carne))