import os

def archivo():
    os.system("touch /root/infection/README.txt /root/infection/README.pdf")
    os.system("touch /root/infection/comentsds.txt /root/infection/palabaras.pdf")
    os.system("touch /root/infection/casas.txt /root/infection/comida.pdf")
    # creamos un archivo con el contenido de la variable
    archivo = open("/root/infection/prueba1000000000.txt", "w")
    archivo.write("sajdhsajkdhjksaksa")
    archivo.close()

archivo()
