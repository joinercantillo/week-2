
list = []
option = 5 
totalcost = 0
while option != 4: 
    print("\n--- MENU---")
    print("1 - Add a product")
    print("2 - Show the inventory")
    print("3 - Calculate statistics")
    print("4 - EXIT")
    
    option = int(input("Select an option (1-4): "))

    if option == 1:
        
        validation = int(input("Do you wanna add any product? (si=1/no=0): "))
        
        while validation == 1:
            name = input("Name that product: ")
            cost = float(input("Cost: "))
            quantity = int(input("Quantity: "))
            
            products = {'product': name, 'cost': cost, 'Quantity': quantity}
            list.append(products)
            
            validation = int(input("¿Añadir otro? (si=1/no=0): "))
            
        
        
        print("Return to main menu...")

    elif option == 2:
        print("\n--- Inventory ---")
        
        
        
        if not list:
            print("The list is empty")
        for p in list:
            print(f"- {p['product']}: ${p['cost']} (stock: {p['Quantity']})")
            
            
    elif option == 3:
        total = sum (p['cost'] for p in list)
        totalcost = total * len(list)
        print("CALCULATE STATISTICS")
        print(f"TOTAL COST ${totalcost}")

    elif option == 4:
        print("GOOD BYE...")
