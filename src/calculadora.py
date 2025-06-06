def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "No se puede dividir por cero"
    return a / b

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

def calcular(opcion, a, b):
    operaciones = {
        "1": suma,
        "2": resta,
        "3": multiplicacion,
        "4": division,
        "5": potencia
    }

    funcion = operaciones.get(opcion)
    if not funcion:
        return "Opción inválida"
    if opcion == "5":
        return funcion(a, int(b))
    return funcion(a, b)
    
def mostrar_menu():
    print("Calculadora")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")


if __name__ == "__main__":
    mostrar_menu()
    opcion = input("Seleccioná una opción: ")

    num1 = float(input("Ingresá el primer número: "))
    num2 = float(input("Ingresá el segundo número: "))

    resultado = calcular(opcion, num1, num2)
    print("Resultado:", resultado)
