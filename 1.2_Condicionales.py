nombre = input("Ingrese su nombre: ")
sexo = input("Ingrese su sexo (M para mujer, H para hombre): ")

if (sexo == "m" and nombre.lower() < 'm') or (sexo == "h" and nombre.lower() > 'n'):
    grupo = "A"
else:
    grupo = "B"

print(f"Usted pertenece al grupo {grupo}")