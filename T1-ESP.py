# T1-ESP ver2.1
#=== Generales ===
# Logs
import logging
logging.basicConfig(filename='T1.log', encoding='utf-8', filemode='w', format='%(asctime)s | %(message)s', level=logging.DEBUG)

# Estructura
PILA = list()

# Funciones internas
def crearLog(texto, imprimir=True):
    '''
    @param texto: texto a ser guardado en log (auto timestamp)
    @param imprimir: si texto se imprime a usuario, por defecto True
    @return: error or True
    '''
    try:
        logging.info(texto)
        print(texto+"\n") if imprimir else None
    except Exception as e:
        raise e


def seleccionarPalabra(cantidad=2):
    '''
    @self: selecciona cantidad palabras desde PILA manejando posibles errores
    @param cantidad: cantidad de palabras a preguntar (2 por defecto)
    @return: lista de palabras obtenida
    '''
    palabraSel = []
    while len(palabraSel) < cantidad:
            try:
                index = input("Ingrese N° lista de "+ str(len(palabraSel)+1) +" a comparar (tecla ctrl+c, Delete para volver): ")
                index = index.replace(",",".")
                index = float(index)
                index = int(index) #Separado de input para guradar valor de index por si existe error
                if (index<0) or (index>len(PILA)):
                    raise ValueError
                else:
                    palabraSel.append(PILA[index])
                    crearLog(" Entrada '{N}', palabra '{p}' seleccionada".format(N=index, p=PILA[index]))
            except (ValueError, IndexError):
                crearLog(" Entrada '{N}' no valida.".format(N=index))
                continue
            except EOFError:
                crearLog(" Entrada no valida (no data, tecla ^Z ).")
                continue
            except Exception as e:
                raise e

    return palabraSel


def comparar():
    # Proceso que muestra PILA de palabras y compara las 2 cadenas de caracteres seleccionadas
    if len(PILA) == 0:
        crearLog(" No existen palabras en la Pila, comparar -> Menu")
        return

    print("\nPalabras guardadas en pila:")
    for index, palabra in enumerate(PILA):
        print(str(index) + ") '" + palabra + "'")
    print("---")
    
    # seleccionando palabras
    try:
        palabraUno, palabraDos = seleccionarPalabra()
    except KeyboardInterrupt:
        crearLog( " Entrada tecla ctrl+c o Delete, comparar -> menu", imprimir=False)
        print("")
        return
    except Exception as e:
        raise e

    # comparando
    resultado = "son iguales" if palabraUno == palabraDos else "son diferentes"
    # guardando resultado
    guardado = crearLog(" Comparando '" + palabraUno + "' y '" + palabraDos + "', " + resultado) # To do verificar resultado
        
    comparar() #Mejorable: imprimir 1 vez lista


def anadir():
    # Proceso para anadir a pila y a log, salir con teclas ctrl+c o Delete
    try:
        palabra = str(input("Ingrese secuencia de caracteres para guardar (tecla ctrl+c o Delete para volver):\n > "))
        palabra = palabra.strip()
        if palabra == "":
            crearLog("String vacio no valido")
            anadir()
        PILA.append(palabra)
        logText = " Palabra '" + palabra + "' agregada correctamente"
        guardado = crearLog(logText)
    except KeyboardInterrupt:
        crearLog(" Entrada tecla ctrl+c o Delete, anadir -> menu", imprimir=False)
        print("")
        return
    except EOFError:
        crearLog(" Entrada no valida (no data, tecla ^Z ).")
    except Exception as e:
        crearLog(" Error inesperado al guardar la palabra, error:"+ str(e))
        
    anadir()


#=== MAIN (menu) ===
def main():
    try:
        crearLog("Menu principal", imprimir=False)
        while True:
            print("\n=== MENU ===")
            print("---")
            print("1: Ingresar secuencia de caracteres")
            print("2: Comparar dos secuencia de caracteres")
            print("3: Salir (q | exit | teclas ctrl+c o Delete)")
            print("---")
            seleccion = str(input("Ingrese seccion: "))
            if seleccion == "1":
                crearLog("Entrada '1', Menu -> anadir", imprimir=False)
                anadir()
            elif seleccion == "2":
                crearLog("Entrada '2', Menu -> Comparar", imprimir=False)
                comparar()
            elif seleccion in ["3", "quit", "q", "exit", "Salir"]:
                raise KeyboardInterrupt("Entrada '" + seleccion +"'")
            else:
                crearLog("Entrada '"+ seleccion +"' invalida, Menu pruncipal")
                
    except KeyboardInterrupt as e:
        e = "Entrada tecla ctrl+c o Delete" if str(e) == "" else e
        crearLog(str(e) + ", terminar programa", imprimir=False)
        print("Saliendo")
        return 0
    except Exception as e:
        main()

if __name__ == "__main__":
    main()
