from multiprocessing import pool
import random
#EJ 1
listadoPlantas = []
def Ejercicio1():
    print("Insert Name:")
    name = input()
    print("Insert Age:")
    age = input()
    days =str(int(age)*365)
    print("Name: "+name+" days: "+days)
#Ejercicio1()
#EJ 2
def Ejercicio2():
    try:
        print("Height: ")
        height= float(input())
        print("Width: ")
        width = float(input())
        if height and width > 0:
            area = str((height*width)/2)
            print("Area: "+area)
    except:
        print("Solo se admiten números positivos")
        Ejercicio2()
#Ejercicio2()
#EJ 3
def Ejercicio3():
    try:
        numRep = int(input("Numero de elementos: "))
        numList = []
        for x in range(numRep):
            num = int(input("Numero para poder introducir: "))
            numList.append(num)
        #numList = [0,1,2,7,"a",-5]
        numList.sort()
        print(numList)
    except:
        print("Uno de los valores introducidos no es correcto")
        Ejercicio3()
#Ejercicio3()
#EJ 4
def Ejercicio4():
    try:
        numEjer = int(input("Para el ejercicio 1 pulse el 1, para el ejercicio 2 pulse el 2, si quiere el ejercicio 3 pulse el 3"))
        if numEjer == 1:
            Ejercicio1()
        elif numEjer == 2:
            Ejercicio2()
        elif numEjer == 3:
            Ejercicio3()
        else:
            print("No existe el ejercicio"+str(numEjer))
    except:
        print("El comando escrito no es un número")
#Ejercicio4()
#EJ 5
def Ejercicio5():
    plantDic = {"name":{},"type":{},"place":{}, "days":{},"size":{}}
    while True:
        global listadoPlantas
        name = input("Nombre de la planta: ")
        if len(listadoPlantas) <= 0:
            plantDic["name"] = name
            break
        else:
            for x in listadoPlantas:
                if name == x["name"]:
                    print("ERROR")
                else:
                    plantDic["name"] = name
            if name != None:
                break
    plantDic["type"]=input("Tipo de la planta: ")
    place = input("Lugar donde está la planta: ")
    plantDic["place"] = place
    wateringDays = input("Cada cuanto se riega la planta: ")
    if wateringDays.isnumeric() and int(wateringDays) > 0:
        plantDic["days"] = wateringDays
    else:
        print("El valor introducido no es un número entero positivo")
    size = input("Introduce las medidas de la planta (en cm)")
    if size.isnumeric() and int(size) > 0:
        plantDic["size"] = str(size)+" cm"
    else:
        print("El valor introducido no es un número entero positivo")
    print(plantDic)
    return plantDic
#Ejercicio5()

#EJ 6
def Ejercicio6():
    global    listadoPlantas
    def crearPlanta():
        listadoPlantas.append(Ejercicio5())
        print()
    for x in range(2):
        crearPlanta()
    def mostrarInformacion(mostrar):
        if mostrar:
            for y in listadoPlantas:
                print(y["name"])
        else:
            mostrarPlantas()
            print("False")
    def mostrarPlantas():
        while True:
            userInput = input("Quieres ver el nombre: y/n      ")
            if userInput == "y":
                mostrarInformacion(True)
                break
            elif userInput == "n":
                while True:
                    userInput = input("¿Quieres ver las plantas con los atributos?: y/n")
                    if userInput == "y":
                        mostrarInformacion(False)
                        break
                    elif userInput == "n":
                        break
                    else:
                        print("No se reconoce el comando")
                break
            else:
                print("No se reconoce el comando")

    def modificarPlanta():
        mostrarPlantas()
        while True:
            namePlant = input("Nombre de planta para cambiar: ")
            for n in listadoPlantas:
                if n["name"] == namePlant:
                    atriChange = input("Atributo a cambiar: ")
                    valorAtri = input("Valor nuevo: ")
                    n[atriChange] = valorAtri
                    return
            print("No se encuentra la planta")
    modificarPlanta()
    print(listadoPlantas)
    print("EJERCICIO 6")
Ejercicio6()
myTupla = ("UNO","DOS","TRES")
#EJ 7
def modTupla():
    global myTupla
    myTupla = list(myTupla)
    myTupla[1] = "CUATRO"
    myTupla = tuple(myTupla)
    return myTupla


def Ejercicio7():
    #myTupla = ("UNO","DOS","TRES")
    global myTupla
    modTupla()
    print(myTupla)

#Ejercicio7()
