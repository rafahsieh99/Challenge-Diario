claves_us = input("ingrese palabra clave:")
valores_us = input("ingrese un valor:")

claves = claves_us.split()
valores = valores_us.split()


diccionario = {}
for i in range (len(claves)):
    diccionario[claves[i]] = valores [i]

print ("Diccionario creado:", diccionario)
