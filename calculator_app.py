from calculator_core import Calculate

calc = Calculate()
print("Calculator — type a sum like 12 / 4, or: history, clear, quit")

while True:
    text = input("> ").strip()
    if text == "quit":
        print ("Goodbye")
        break    
    elif text == "history" :
        calc.show_history()
    elif text == "clear" :
        calc.clear_history()
        print("History cleared")
    else :
        parts = text.split()
        if len(parts) != 3:
            print("please type it like 12 / 4")
        else :
            try :
                a = float(parts[0])
                op = parts[1]
                b = float(parts[2])
            except ValueError:
                print("Please use numbers only")
                continue    
            result = calc.operation(a,op,b)
            print(result)    