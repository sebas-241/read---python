archivoExternoViejo =  open("textos/texto1.txt", "r")
archivoExterno =  open("textos/texto2.txt", "r")

opcion = int(input("Desea escribir un mensaje en el texto externo? \n1. Si \n2. No \n"))
if(opcion == 1):
    archivoExternoViejo =  open("textos/texto1.txt", "w")
    texto = input("Ingrese un texto: \n")
    archivoExternoViejo.write(texto)
    archivoExternoViejo =  open("textos/texto1.txt", "r")
    copy = int(input("Deseas hacer una copia de este texto en otro archivo? \n1. Si \n2. No \n")) 
    if(copy == 1):
        archivoExterno =  open("textos/texto2.txt", "w")
        archivoExterno.write("#Este texto es una copa del archivo nombrado \"texto1\"\n")
        archivoExterno.write(archivoExternoViejo.read())
        print("Listo")   
    else:
        print("Ayos")     
else:
    print("Ayos")    



archivoExterno.close()
archivoExternoViejo.close()