import os

#crear carpeta si no existe 
carpeta = "Holabeba"
if not os.path.exists(carpeta):
    os.mkdir(carpeta)
    print(f"carpeta ' {carpeta} ' creada exitosamente.")
else:
    print(f"carpeta ' {carpeta} ' ya existe.")
