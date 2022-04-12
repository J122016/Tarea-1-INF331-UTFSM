#=== Generals ===
# Logs
import logging
logging.basicConfig(filename='T1.log', encoding='utf-8', filemode='w', format='%(asctime)s | %(message)s', level=logging.DEBUG)

# Struct
STACK = list()

# Internal functions
def addToLog(text, display=True):
    '''
    @param text: text to save in the log (auto timestamp)
    @param display: if print text to user, default True
    @return: error or True
    '''
    try:
        logging.info(text)
        print(text+"\n") if display else None
    except Exception as e:
        raise e


def selectStringStack(amount=2):
    '''
    @self: select amount of strings from the STACK handling some possible errors
    @param amount: amount of strings to ask (to return, default 2)
    @return: list of required strings
    '''
    selStrings = []
    while len(selStrings) < amount:
            try:
                index = input("Enter list N° of the"+ str(len(selStrings)+1) +" string to compare (keys ctrl+c, Delete to go back): ")
                index = int(index) #Separates from input to save value of index if raise error int cast
                selStrings.append(STACK[index])
                addToLog(" Input '{N}', string '{p}' selected".format(N=index, p=STACK[index]))
            except (ValueError, IndexError):
                addToLog(" Input '{N}' invalid.".format(N=index))
                continue
            except EOFError:
                addToLog(" Invalid input (no data, ^Z).")
                continue
            except Exception as e:
                raise e

    return selStrings


def compare():
    # Process, print STACK of strings and compare 2 strings to select
    if len(STACK) == 0:
        addToLog(" No strings found in the stack, comare -> menu")
        return

    print("\nString saved in stack:")
    for index, string in enumerate(STACK):
        print(str(index) + ") '" + string + "'")
    print("---")
    
    # select strings
    try:
        stringOne, stringTwo = selectStringStack()
    except KeyboardInterrupt:
        addToLog( " Input ctrl+c or Delete key, compare -> menu", display=False)
        print("")
        return
    except Exception as e:
        raise e

    # comparing
    result = "are equals" if stringOne == stringTwo else "are different"
    # save result
    ok = addToLog(" Comparing '" + stringOne + "' and '" + stringTwo + "', " + result) # to do verify result
        
    compare() #To do: print saved stack only 1 time


def add():
    # Process, adds string to stack and log file
    try:
        string = str(input("Enter the string to save (key ctrl+c or Delete to go back):\n > "))
        STACK.append(string)
        logText = " Add '" + string + "' string successfully"
        ok = addToLog(logText)  # to do verify result
    except KeyboardInterrupt:
        addToLog(" Input ctrl+c or Delete key, add -> menu", display=False)
        print("")
        return
    except EOFError:
        addToLog(" Invalid character or string, no data (maybe ^Z)")
    except Exception as e:
        addToLog(" An unexpected error occurred while saving the string, error:", str(e))
        
    add()


#=== MAIN (menu) ===
def main():
    try:
        addToLog("Principal menu", display=False)
        while True:
            print("\n=== MENU ===")
            print("---")
            print("1: Add a string sequence")
            print("2: Compare two strings sequence")
            print("3: Exit (q | exit | combination keys ctrl+c o Delete)")
            print("---")
            select = str(input("Enter section: "))
            if select == "1":
                addToLog("Input '1', Menu -> Add", display=False)
                add()
            elif select == "2":
                addToLog("Input '2', Menu -> Compare", display=False)
                compare()
            elif select in ["3", "quit", "q", "exit", "Salir"]:
                raise KeyboardInterrupt("Input '" + select +"'")
            else:
                addToLog("Input '"+ select +"', invalid, Menu")
                
    except KeyboardInterrupt as e:
        e = "Input ctrl+c o Delete key" if str(e) == "" else e
        addToLog(str(e) + ", Exit program", display=False)
        print("Exit program")
        return 0
    except Exception as e:
        main()

if __name__ == "__main__":
    main()
