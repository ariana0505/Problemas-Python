#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

winning_numbers = []
while True:
    if len(winning_numbers) == 0:
        winning_numbers.append(int(input("Enter the first winning number: ")))
        continue
    winning_number = input("Enter the next winning number: ")
    winning_numbers.append(winning_number)
    decision = input("Do you want to continue entering the winning numbers?(y/n): ").lower().strip()
    if decision == "y":
        print("OK!")
    elif decision == "n":
        print("See you tomorrow!")
        break
    else:
        print("invalid format")