items = {
}

machineBalance = 0
id = 0

transactions = []

class vendingMachine:
    def balance():
        global machineBalance
        print("The machine has $" + str(machineBalance))
        pass

    def history():
        global transactions
        for x in transactions:
            print(x)
        pass

    def inventory():
        print()
        for key in items:
            if(items[key][0] > 0):
                
                print("Item: " + str(key))
                print("ID: " + str(items[key][2]))
                print()
        pass

    def help(): 
        print("\nUse one of the following commands:")
        print("exit - exits program")
        print("balance - displays the amount of money in the machine")
        print("history - displays transaction history")
        print("inventory - displays available items and IDs")
        print("add item (name) (quanty) (price) - adds item to machine with given attributes")
        print("buy item (name) (dollars) (quarters) (dimes) (nickels) (pennies) - buys item based on given parameters\n")

        pass

    def exit():
        exit()

    def addItem(name, qty, price):
        global id
        if name in items:
            items[name][0] += qty
            items[name][1] = price
        else:
            items[name] = [qty, price, id]
            id += 1
        pass

    def buyItem(name, dollar, quarter, dime, nickel, penny):
        global machineBalance
        global transactions
        total = dollar + (quarter * .25) + (dime * .1) + (nickel * .05) + (penny * .01)

        if name in items and items[name][0] > 0:
            if total >= items[name][1]:
                #give item, return change, subtract from inventory
                print("*dispensing " + name + "*")

                items[name][0] -= 1
                machineBalance += items[name][1]

                ret = (total - items[name][1]) * 100
                retDollars = int(ret // 100)
                ret -= retDollars * 100
                retQuarters = int(ret // 25)
                ret -= retQuarters * 25
                retDimes = int(ret // 10)
                ret -= retDimes * 10
                retNickels = int(ret // 5)
                ret -= retNickels * 5
                retPennies = int(ret)

                print("Returning " + str(retDollars) + " dollars, " + str(retQuarters) + " quarters, " + str(retDimes) + " dimes, " + str(retNickels) + " nickles, and " + str(retPennies) + " pennies.")
                transactions.append(name + " sold for $" + str(items[name][1]))
                pass
            else:
                print("You do not have enough money, returning $" + str(total))
                pass
        else:
            print("Item not in inventory")



   


#dictionary
 