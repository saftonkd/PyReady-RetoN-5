import math

def calcular_area_superficial(radio_esfera, radio_cono, altura_cono) :
    area_esfera : float = 4 * (math.pi * radio_esfera**2)
    generatriz : float = (radio_cono**2 + altura_cono**2)**0.5
    base_cono : float = math.pi * radio_cono**2
    lateral_cono : float = math.pi * radio_cono * generatriz
    area_cono : float = base_cono + lateral_cono
    return area_esfera + area_cono

def calcular_volumen(radio_esfera, radio_cono, altura_cono) :
    volumen_esfera : float = 4 * (math.pi * radio_esfera**3) / 3
    volumen_cono : float = 1 * (math.pi * altura_cono * radio_esfera**2) / 3
    return volumen_esfera + volumen_cono

if __name__ =="__main__" :
    radio_esfera = float(input("Digite el radio de la esfera en centímetros: "))
    radio_cono = float(input("Digite el radio del cono en centímetros: "))
    altura_cono = float(input("Digite la altura del cono en centímetros: "))
    if (radio_esfera or radio_cono or altura_cono) < 0 :
        print("Solo son permitidos valores positivos")
    else :
        area_total: float = calcular_area_superficial(radio_esfera, radio_cono, altura_cono)
        volumen_total : float = calcular_volumen(radio_esfera, radio_cono, altura_cono)
        print("El área superficial en centímetros cuadrados es: " + str(area_total))
        print("El volumen en centímetros cúbicos es: " + str(volumen_total))