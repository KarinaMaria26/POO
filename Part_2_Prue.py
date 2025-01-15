import math

# Clase Círculo
def calcular_area_circulo(radio):
    return math.pi * radio**2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# Clase Rectángulo
def calcular_area_rectangulo(base, altura):
    return base * altura

def calcular_perimetro_rectangulo(base, altura):
    return 2 * (base + altura)

# Clase Cuadrado
def calcular_area_cuadrado(lado):
    return lado**2

def calcular_perimetro_cuadrado(lado):
    return 4 * lado

# Clase Triángulo Rectángulo
def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_hipotenusa(base, altura):
    return math.sqrt(base**2 + altura**2)

def calcular_perimetro_triangulo(base, altura):
    return base + altura + calcular_hipotenusa(base, altura)

def determinar_tipo_triangulo(base, altura):
    hipotenusa = calcular_hipotenusa(base, altura)
    if base == altura == hipotenusa:
        return "Equilátero"
    elif base != altura and base != hipotenusa and altura != hipotenusa:
        return "Escaleno"
    else:
        return "Isósceles"

# Método principal (main)
def main():
    # Crear las figuras
    radio = 2
    base_rect = 1
    altura_rect = 2
    lado_cuadrado = 3
    base_triangulo = 3
    altura_triangulo = 5

    # Círculo
    area_circulo = calcular_area_circulo(radio)
    perimetro_circulo = calcular_perimetro_circulo(radio)
    print(f"El área del círculo es = {area_circulo:.2f}")
    print(f"El perímetro del círculo es = {perimetro_circulo:.2f}\n")

    # Rectángulo
    area_rectangulo = calcular_area_rectangulo(base_rect, altura_rect)
    perimetro_rectangulo = calcular_perimetro_rectangulo(base_rect, altura_rect)
    print(f"El área del rectángulo es = {area_rectangulo}")
    print(f"El perímetro del rectángulo es = {perimetro_rectangulo}\n")

    # Cuadrado
    area_cuadrado = calcular_area_cuadrado(lado_cuadrado)
    perimetro_cuadrado = calcular_perimetro_cuadrado(lado_cuadrado)
    print(f"El área del cuadrado es = {area_cuadrado}")
    print(f"El perímetro del cuadrado es = {perimetro_cuadrado}\n")

    # Triángulo Rectángulo
    area_triangulo = calcular_area_triangulo(base_triangulo, altura_triangulo)
    perimetro_triangulo = calcular_perimetro_triangulo(base_triangulo, altura_triangulo)
    tipo_triangulo = determinar_tipo_triangulo(base_triangulo, altura_triangulo)
    print(f"El área del triángulo es = {area_triangulo}")
    print(f"El perímetro del triángulo es = {perimetro_triangulo}")
    print(f"El triángulo es {tipo_triangulo}")

if __name__ == "__main__":
    main()