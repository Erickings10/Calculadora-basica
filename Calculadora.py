def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    else:
        return a / b
    
def potencia(a,b):
    return a ** b

def raizcuadrada(a):
    return a ** 0.5

def raizcubica(a):
    return a ** (1/3)


def calculadora():
    print("Calculadora básica")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raiz Cuadrada")
    print("7. Raiz Cubica")
    
    opcion = input("Seleccione una opción: ")

    if opcion in ['1','2','3','4''5']:
        num1 = int (input("Ingrese el primer número: "))
        num2 = int (input("Ingrese el segundo número: ")) 
    elif opcion == '6':
        num1 = int (input("Ingrese el número: "))
        while num1 < 0:
            print("Error: La raíz cuadrada de un número debe ser positiva. Ingrese nuevamente")
            num1 = int (input("Ingrese un número nuevamente"))
        num2 = None
    elif opcion == "7":
        num1 = int (input("Ingrese el número: "))
        while num1 < 0:
            print("Error: La raíz cubica de un número debe ser positiva. Ingrese nuevamente")
            num1 = int (input("Ingrese un número nuevamente"))
        num2 = None

    else:
        print("Opcion no valida")
        return


    if opcion == '1':
        print("Resultado:", suma(num1, num2))
    elif opcion == '2':
        print("Resultado:", resta(num1, num2))
    elif opcion == '3':
        print("Resultado:", multiplicacion(num1, num2))
    elif opcion == '4':
        print("Resultado:", division(num1, num2))
    elif opcion == '5':
        print("Resultado:", potencia(num1,num2))
    elif opcion =='6':
        print("Resultado:", raizcuadrada(num1))
    elif opcion =='7':
        print("Resultado:", raizcubica(num1))
    else:
        print("Opción no válida")
        

calculadora()
