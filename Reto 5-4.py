def calcular_interes_compuesto(capital_inicial: float, tasa_interes: float, meses: float) :
    porcentaje_interes : float = (tasa_interes / 100)
    capital_final: float = capital_inicial * (1 + porcentaje_interes)**meses
    return capital_final

if __name__ == "__main__" :
    capital_inicial = float(input("Ingrese el capital inicial del préstamo: "))
    tasa_interes = float(input("Ingrese la tasa de interés del banco prestador (%): "))
    meses = float(input("Ingrese el periodo de duración del préstamo en meses: "))

    capital_final = calcular_interes_compuesto(capital_inicial, tasa_interes, meses)
    print("El valor final del préstamo es: " + str(capital_final))