# Programa que invierte un número de tres dígitos, usando isdigit() para validar la entrada
numero = input("Ingresa un número de tres dígitos: ")  # Pide un número de tres dígitos

# Verifica si el número tiene exactamente tres dígitos y si es un número válido
if numero.isdigit() and len(numero) == 3:
    numero_invertido = numero[::-1]  # Invierte el número usando slicing
    print(f"El número invertido es: {numero_invertido}")  # Muestra el número invertido
else:
    print("Por favor, ingresa un número válido de tres dígitos.")  # Mensaje de error si no es válido