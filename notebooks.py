import csv
prestamos = {}

def validar_rut(rut):
    if len(rut)> 7 and len(rut) <10:
        print("Rut válido")
        return True
    else:
        print("Ingrese rut válido")

def prestar_notebooks(prestamos, nombre, rut, documento, numero_notebook):        
        if validar_rut(rut):
            prestamos [rut] ={
                'Nombre':nombre,
                'Documento':documento,
                'Numero_Notebook':numero_notebook
            }
            print(f"Notebook número {numero_notebook} prestado a {nombre} (Rut: {rut})")
        else:
            print("Ingrese rut válido")
    

def devolver_notebooks(prestamos, rut):
    if rut in prestamos:
        print(f"Notebook devuelto por Rut: {rut}")
        del prestamos[rut]
    else:
        print("Rut no encontrado en prestamos")

def modificar_notebook(prestamos, rut):
    if rut in prestamos:
        numero = int(input("Que número de notebook desea elegir: "))
        prestamos[rut]['numero_notebook'] = numero
        print(f"Número de notebook cambiado para rut {rut}")
    else:
        print("Rut no encontrado en prestamos")

def imprimir_lista(prestamos, docente, sigla_ramo, seccion):
    filename = f"{docente.replace(' ', '_')}_{sigla_ramo}-{seccion}.csv"
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Rut', 'Nombre', 'Documento', 'Numero_Notebook']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for rut, info in prestamos.items():
            writer.writerow({
                'Rut': rut,
                'Nombre': info['Nombre'],
                'Documento': info['Documento'],
                'Numero_Notebook': info['Numero_Notebook']
            })
    print(f"Lista de préstamos guardada en {filename}")

def menu():
    while True:
        print("1. Prestar Notebooks")
        print("2. Devolver Notebooks")
        print("3. Modificar Préstamo de Notebook")
        print("4. Imprimir Lista de Notebooks Prestados")
        print("5. Terminar Clase")
        opc = int(input("Ingrese opción: "))
        if opc == 1:
            nombre = input("Ingrese su nombre:" )
            rut = input("Ingrese su rut sin guión: ")
            documento = input("Que documento desea entregar (Carnet o Pase): ")
            numero_notebook = int(input("Ingrese que numero de notebook desea (1-30): "))
            if documento.lower() == "carnet" or documento.lower() == "pase":
                if numero_notebook >= 1 and numero_notebook <=30:
                    prestar_notebooks(prestamos, nombre, rut, documento, numero_notebook)
                else:
                    print("Ingrese un numero de notebook válido")
            else:
                print("Entrege un documento válido")
        elif opc == 2:
            rut = input("Ingrese su rut para devolver notebook: ")
            devolver_notebooks(prestamos, rut)
        elif opc == 3:
            rut = input("Ingrese su rut para poder modificar su notebook: ")
            modificar_notebook(prestamos, rut)
        elif opc == 4:
            docente = input("Ingrese Nombre del docente: ")
            sigla_ramo = input("Ingrese Sigla del ramo: ")
            seccion = input("Ingrese Sección del ramo: ")
            imprimir_lista(prestamos, docente, sigla_ramo, seccion)
        elif opc == 5:
            if len(prestamos) == 0:
                break
            else:
                print("Aún hay notebooks prestados")
            

menu()