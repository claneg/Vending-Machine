from vendingMachineFuncts import vendingMachine

while(1):
    inp = input("\nType a command:\n")
    inp = inp.replace("$", "")
    inp = inp.lower().split()


    match inp[0]:
        case "add":
            if len(inp) > 5:
                vendingMachine.addItem(inp[2] + " " + inp[3], int(inp[4]), float(inp[5]))
            else:
                vendingMachine.addItem(inp[2], int(inp[3]), float(inp[4]))
        case "exit":
            vendingMachine.exit()
        case "buy":
            if len(inp) > 8:
                vendingMachine.buyItem(inp[2] + " " + inp[3] , int(inp[4]), int(inp[5]), int(inp[6]), int(inp[7]), int(inp[8]))
            else:
                vendingMachine.buyItem(inp[2], int(inp[3]), int(inp[4]), int(inp[5]), int(inp[6]), int(inp[7]))
        case "help":
            vendingMachine.help()
        case "inventory":
            vendingMachine.inventory()
        case "balance":
            vendingMachine.balance()
        case "history":
            vendingMachine.history()
            
        
        
        
        


