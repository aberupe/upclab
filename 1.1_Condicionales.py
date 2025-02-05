# Almacenar la contraseña en una variable
contraseña_guardada = "4456"

# Pedir al usuario que ingrese la contraseña
contraseña_ingresada = input("Ingrese la contraseña: ")

# Verificar si la contraseña ingresada coincide con la guardada
if contraseña_ingresada.lower() == contraseña_guardada.lower():print("La contraseña es correcta.")
else:print("La contraseña es incorrecta." + contraseña_guardada)