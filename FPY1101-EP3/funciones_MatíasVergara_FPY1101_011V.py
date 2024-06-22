import os 
total_libros = []

# Opción 1. "Registro de libro"
def registro():

    try:
        titulo = input("Ingrese el nombre del libro.\n - ")
        autor = input("Ingrese el autor del libro.\n - ")
        año_publicacion = input("Ingrese el año de publicación.\n - ")
        sku = input("Ingrese el identificador único del libro (SKU).\n - ")

        if titulo or autor or año_publicacion or sku != str and int:
            print("Error. El dato ingresado, no es válido.")
        

        libro = {
            'TÍTULO': titulo,
            'AUTOR': autor,
            'AÑO DE PUBLICACIÓN': año_publicacion,
            'SKU': sku
        }


        total_libros.append(libro)
        print("El registro se ha realizado con exito.")
    except ValueError:
        print("El tipo de dato ingresado no es válido. Vuelva a intentarlo.")    

# Opción 2. "Prestamo de libro"
def prestar_libro():
    try:
        nombre_usuario = input("Ingrese el nombre del usuario: ")
        sku_libro = input("Ingrese el identificador único del libro (SKU): ")

    except ValueError:
        print("El tipo de dato ingresado, no es válido. Vuelva a intentarlo")



# Opción 3. "Listado de libros"
def listado():
    if total_libros ==" ":
        print("El libro indicado, no se encuentra dentro del registro.")   
    else: 
        for libro in total_libros:
            print(f"TÍTULO:{libro['TÍTULO']}\t AUTOR: {libro['AUTOR']}\t AÑO DE PUBLICACIÓN: {libro['AÑO DE PUBLICACIÓN']} \t SKU: {libro['SKU']}")


# Opción 4. "Impresión del reporte de préstamos"
def imprimir():
    try:
        eleccion = int(input("Por favor. Seleccione una opcíon de impresión para la plantilla.\n 1. Planilla completa de prestamos.\n 2. Libro específico"))

        if eleccion == 1:
            with open("planilla_prestamos.txt""w") as archivo:
                for libro in total_libros: #Corregir planila de prestamos
                    archivo.write(f"TÍTULO: {libro['TÍTULO']}\t AUTOR: {libro['AUTOR']}\t AÑO DE PUBLICACIÓN: {libro['AÑO DE PUBLICACIÓN']} \t SKU: {libro['SKU']}")
            print("La planilla se creó exitosamente en:\n", os.getcwd())
        elif eleccion == 2: #cOMPLETAR
            libro_especifico = input("Ingrese el título del libro para generar la plantilla: ").lower()
            with open(f"planilla_{'titulo'}.txt", "w") as archivo:
                for libro in total_libros:
                    if libro ['TÍTULO'].lower() == titulo:
                        archivo. write(f"TÍTULO: {libro['TÍTULO']}\t AUTOR: {libro['AUTOR']}\t AÑO DE PUBLICACIÓN: {libro['AÑO DE PUBLICACIÓN']} \t SKU: {libro['SKU']}")
            print("La planilla se creó exitosamente en:\n", os.getcwd())
  
    except ValueError:
        print("El tipo de dato ingresado, no es válido. Vuelva a intentarlo")
            
   
#Menú
def menu ():
    while True:
        try:
            print("\n---------------INICIO------------------\n")
            print(" 1. Registar libro\n 2. Prestar libro\n 3. Listar todos los libros\n 4. Imprimir reporte de préstamos.\n 5. Salír del programa ")
            eleccion = int(input("\n\nIngrese una opción (1 a 5):\n "))

            if eleccion == 1:
                registro()
            elif eleccion == 2:
                prestar_libro()
            elif eleccion == 3:
                listado()
            elif eleccion == 4:
                imprimir()
            elif eleccion == 5:
                print("""
+----------------------------------------------+
|   Programa Finalizado_                       | 
|   Desarrollado por Matías Vergara Arriagada  |
|   RUN: 20.746.089-3                          | 
|                                              |         
+----------------------------------------------+      
""")
                break
            else:
                print("Opción no válida. Vuelva a ingresar una opción (1 a 5): ")
        except ValueError:
            print("El tipo de dato ingresado, no es válido. Vuelva a intentarlo")









