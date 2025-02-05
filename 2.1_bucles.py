# Definimos la contraseña correcta
contrasena_correcta = "1234"

# Pedimos al usuario que ingrese la contraseña
contrasena_ingresada = input("Ingrese la contraseña: ")

# Repetir la solicitud de contraseña hasta que sea correcta
while contrasena_ingresada != contrasena_correcta:
    print("Contraseña incorrecta. Inténtelo de nuevo.")
    contrasena_ingresada = input("Ingrese la contraseña: ")

print("Contraseña correcta. ¡Bienvenido!")