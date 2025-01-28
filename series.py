def suma_potencia():
    # Solicitar los dos números al usuario
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    
    # Calcular la suma
    suma = num1 + num2
    
    # Elevar la suma al segundo número ingresado
    resultado = suma ** num2
    
    return resultado

# Llamar a la función y mostrar el resultado
resultado_final = suma_potencia()
print(f"El resultado es: {resultado_final}")