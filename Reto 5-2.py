import math

def calcular_area(radio: float, altura_rectangulo: float, base_rectangulo: float) :
    area_circunferencia : float = math.pi * radio**2
    area_rectangulo : float = altura_rectangulo *  base_rectangulo
    return (2 *area_circunferencia) + altura_rectangulo

def calcular_perimetro(radio: float, altura_rectangulo: float, base_rectangulo: float ) :
    perimetro_circunferencia : float = 2 * math.pi * radio
    perimetro_rectangulo : float = (2 * base_rectangulo) + (2 * altura_rectangulo)
    return (2 * perimetro_circunferencia) + altura_rectangulo

if __name__ == "__main__" :
    radio = float(input("Ingrese el radio de la circunferencia: "))
    altura_rectangulo = float(input("Ingrese la altura del rectángulo: "))
    base_rectangulo = float(input("Ingrese la base del rectángulo: "))
    if (radio or altura_rectangulo or base_rectangulo) < 0 :
        print("Solo son permitidos valores positivos")
    else :
        area_total : float = calcular_area(radio, altura_rectangulo, base_rectangulo)
        perimetro_total : float = calcular_perimetro(radio, altura_rectangulo, base_rectangulo)
        print("El área total es: "+ str(area_total))
        print("El perímetro total es: " + str(perimetro_total))
