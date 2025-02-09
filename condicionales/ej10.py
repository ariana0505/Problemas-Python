pizza = ["mozzarella","tomate"]

pizzaVegetariana = input("Desea una pizza vegetariana o no?(S/N): ").lower()

if(pizzaVegetariana == "s"):
    print("Nuetro menu es: \n-> Pimiento\n-> tofu ")
    ingrediente = input("Ingrese un ingrediente para su pizza: ").lower()
    match(ingrediente):
        case "pimiento": 
            pizza.insert(len(pizza),ingrediente)
        case "tofu":
            pizza.insert(len(pizza),ingrediente)
        case _ :
            print("Ingrese una de las opciones")

elif(pizzaVegetariana == "n"):

    print("Nuetro menu es: \n-> Peperoni\n-> Jamón\n-> Salmón")
    ingrediente = input("Ingrese un ingrediente para su pizza: ").lower()
    match(ingrediente):
        case "Peperoni": 
            pizza.insert(len(pizza),ingrediente)
        case "Jamón":
            pizza.insert(len(pizza),ingrediente)
        case "Salmón":
            pizza.insert(len(pizza),ingrediente)
        case _ :
            print("Ingrese una de las opciones")
else:
    print("Ingrese una de las opciones")

print(f"Listo los ingredientes de su pizza son : {pizza}")