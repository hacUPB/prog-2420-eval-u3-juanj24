
def obtener_peliculas():
    peliculas = ["el paseo", "cars", "nemo", "capitan america"]
    return peliculas


def elegir_pelicula(peliculas):
    print("Películas disponibles:")
    numero_pelicula = 1
    for pelicula in peliculas:
        print(f"{numero_pelicula} {pelicula}")
        numero_pelicula += 1

    opcion = int(input("Elige el número de la película que quieres ver: "))
    return peliculas[opcion - 1] 

def asientos(filas, columnas):
    asientos_totales = []
    
    for i in range(filas):
        fila = []
        for i in range(columnas):
            fila.append("🟩")  # Asiento libre
        asientos_totales.append(fila)
    
    return asientos_totales 


def reservar_asientos(asientos_totales, personas):
    for i in range(personas):
        print("elige un asiento ingresando la fila y la columna .")
        fila = int(input("fila 1 al 5: ")) - 1
        columna = int(input("columna 1 al 5: ")) - 1

        if verificar_disponibilidad(asientos_totales, fila, columna):
            asientos_totales[fila][columna] = "🟥"  
        else:
            print("asiento ocuoado")

    return asientos_totales  


def verificar_disponibilidad(asientos_totales, fila, columna):
    return asientos_totales[fila][columna] == "🟩"


def mostrar_asientos(asientos_totales):
    print("Asientos disponibles:")
    for fila in asientos_totales:
        for asiento in fila:
            print(asiento, end=" ")
        print()


def numero_personas():
    personas = int(input("¿Cuantas personas van a ingresar? "))
    return personas


def calcular_costo(personas, costo_por_asiento=25):
    return personas * costo_por_asiento


def main():
    
    peliculas = obtener_peliculas()

    
    pelicula_elegida = elegir_pelicula(peliculas)
    print(f"Has elegido la película: {pelicula_elegida}")

   
    personas = numero_personas()

    
    asientos_totales = asientos(5, 5)

    
    mostrar_asientos(asientos_totales)

    
    asientos_totales = reservar_asientos(asientos_totales, personas)

   
    mostrar_asientos(asientos_totales)

   
    costo_total = calcular_costo(personas)

  
    print(f"se  reservvaron {personas} asientos para ver {pelicula_elegida}")
    print(f"debes pagar: {costo_total} ")


def menu_principal():
    while True:
        
        print("1 Ver películas disponibles")
        print("2 Reservar asientos")
        print("3 Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            peliculas = obtener_peliculas()
            print("peliculas disponibles:")
            for i, pelicula in enumerate(peliculas, 1):
                print(f"{i}. {pelicula}")  
        elif opcion == "2":
            main()  
        elif opcion == "3":
            print("Saliendo..")
            break
        else:
            print("opcion no válida")


if __name__ == "__main__":
    menu_principal()
