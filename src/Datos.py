
def obtener_peliculas():
    peliculas = ["el paseo", "ferrari", "interestelae", "america"]
    return peliculas


def elegir_pelicula(peliculas):
    print("pelculas dponibles:")
    numero_pelicula = 1
    for pelicula in peliculas:
        print(f"{numero_pelicula}. {pelicula}")
        numero_pelicula += 1

    opcion = int(input("Elige el nmero de la pecula que quieres ver "))
    return peliculas[opcion - 1]  


def obtener_asientos(filas, columnas):
    asientos_totales = []
    
    for _ in range(filas):
        fila = []
        for _ in range(columnas):
            fila.append("🟩")  
        asientos_totales.append(fila)
    
    return asientos_totales  

def disponibilidad(asientos_totales, fila, columna):
    return asientos_totales[fila][columna] == "🟩"


def reservar_asientos(asientos_totales, personas):
    for _ in range(personas):
        print("Elige un asiento ingresando la fila y la columna (números del 1 al 5)")
        fila = int(input("Fila (1-5): ")) - 1
        columna = int(input("Columna (1-5): ")) - 1

        if disponibilidad(asientos_totales, fila, columna):
            asientos_totales[fila][columna] = "🟥"  
        else:
            print(" asiento ya ocupado")

    return asientos_totales  



def mostrar_asientos(asientos_totales):
    print("\nAsientos disponibles:")
    for fila in asientos_totales:
        for asiento in fila:
            print(asiento)
        print()

# Función para obtener el número de personas que van al cine (retorna el número)
def obtener_numero_personas():
    personas = int(input("¿Cuántas personas van al cine? "))
    return personas



# Función para el menú principal
def menu_principal():
    while True:
        
        print("1. Ver peculas disponibls")
        print("2. reservar asientos")
        print("3. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            peliculas = obtener_peliculas()
        


def main():
    print("¡Bienvenido al sistema de reservas de cine!")
    menu_principal()


if __name__ == "__main__":
    main()




