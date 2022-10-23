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
            num = int(input("Numero para introducir: "))
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
