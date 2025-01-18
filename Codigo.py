import math
#Menu de Funciones en Python
def calculo_cubo_cuadrado():
    while True:
        try:
          opc = int(input("¿que desea calcular? 1. cuadrado, 2. cubo"))
          if opc not in [1, 2]:
            print("ingrese una de las opciones que se desea porfavor")
            continue
          break
        except:
            print("ingrese un dato numerico porfavor")
    match opc:
        case 1:
            num = float(input("digite el dato que desea calcular al cuadrado: \n "))
            resultado = math.pow(num, 2)
            print(f"el resultado de {num} al cuadrado es: {resultado}")
        case 2:
            num = float(input("digite el dato que desea calcular al cuadrado: \n "))
            resultado = math.pow(num, 3)
            print(f"el resultado de {num} al cubo es: {resultado}")
                
def calculo_media():
    suma_de_numeros = 0
    numeros_totales = 0
    
    numeros_a_sumar = int(input("ingrese la cantidad de numeros a escribir: "))       
    if(numeros_a_sumar < 0):
        print("no se permite numeros negativos")
        return
        
    while numeros_totales < numeros_a_sumar:
        try:
            valor = float(input("ingrese numero a sumar: "))
            suma_de_numeros = suma_de_numeros + valor
            numeros_totales+=1
        except:
            print("ingrese un valor numerico valido")
    if numeros_a_sumar == 0:
        print("no se ingresaron numeros a sumar")
    else: 
        media = suma_de_numeros / numeros_totales
        print(f"la media es: {media}")    

def mayor_menor():
    numeros = []
    numeros_totales = 0
    numeros_a_ordenar = int(input("ingrese los numeros: \n"))
    while(numeros_totales < numeros_a_ordenar):
        numero = int(input("ingrese numero: "))
        numeros.append(numero) 
        numeros_totales = numeros_totales + 1
    
    #funcion para ordenar las cifras
    numeros.sort()
    
    print("Números ordenados:")
    for num in numeros:
        print(num)

while True:
    print("<--Bienvenido al menu de las operaciones, escoga una de las siguientes operaciones: 1.Suma, 2. Producto entre dos numeros, 3. Divisiones\n 4. factoriales, 5. tabla de multiplicar del 1 al 10, 6. calculo al cuadrado o cubo \n 7. calcular la media, 8. ordenar numeros-->")
    try:
        opc = int(input())
        break
    except:
        print("ingrese un dato de tipo numerico:")
match opc: 
    case 1:
        print("sumas")
    case 2: 
        print("multiplicacion")
    case 3:
        print("division entre dos numeros ")
    case 4:
        print("Factoriales")
    case 5:
        print("tablas de multiplicar")
    case 6:
        calculo_cubo_cuadrado()
    case 7:
        calculo_media()
    case 8: 
        mayor_menor()
    case _:
        print("se debe ingresar las opciones que se indican.")