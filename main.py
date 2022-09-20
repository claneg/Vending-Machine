from ctypes import sizeof
from vendingMachineFuncts import vendingMachine

while(1):
    inp = input("\nType a command:\n")
    inp = inp.replace("$", "")
    inp = inp.lower().split()




    match inp[0]:
        case "add":
            if (len(inp) >= 5):
                inp[2] = inp[2] + ' ' + inp[3]
                inp[3] = inp [4]
                inp[4] = inp[5]
                vendingMachine.addItem(inp[2], int(inp[3]), float(inp[4]))
            else:
                vendingMachine.addItem(inp[2], int(inp[3]), float(inp[4]))
        case "exit":
            vendingMachine.exit()
        case "buy":
            if (len(inp) > 7):
                inp[2] = inp[2] + ' ' + inp[3]
                inp[3] = inp[4]
                inp[4] = inp[5]
                inp[5] = inp[6]
                inp[6] = inp[7]
                vendingMachine.buyItem(inp[2], int(inp[3]), int(inp[4]), int(inp[5]), int(inp[6]), int(inp[7]))
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
            
        
        
        
        


