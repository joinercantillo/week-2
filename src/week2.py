
lista = []
option = 5 
totalcost = 0
while option != 4: 
    print("\n--- MENU DE OPCIONES ---")
    print("1 - Agregar un producto")
    print("2 - Mostrar inventario")
    print("3 - Calcular estadísticas")
    print("4 - Salir")
    
    option = int(input("Seleccione una opción (1-4): "))

    if option == 1:
        
        validation = int(input("¿Quiere ingresar un nuevo producto? (si=1/no=0): "))
        
        while validation == 1:
            name = input("Nombre del producto: ")
            cost = float(input("Costo: "))
            quantity = int(input("Cantidad: "))
            
            productos = {'producto': name, 'costo': cost, 'cantidad': quantity}
            lista.append(productos)
            
            validation = int(input("¿Añadir otro? (si=1/no=0): "))
            
        
        
        print("Regresando al menú principal...")

    elif option == 2:
        print("\n--- INVENTARIO ---")
        
        
        
        if not lista:
            print("La lista está vacía.")
        for p in lista:
            print(f"- {p['producto']}: ${p['costo']} (stock: {p['cantidad']})")
            
            
    elif option == 3:
        total = sum (p['costo'] for p in lista)
        totalcost = total * len(lista)
        print("CALCULAR ESTADISTICAS")
        print(f"TOTAL COSTO ${totalcost}")

    elif option == 4:
        print("Saliendo del sistema...")
