# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 22:44:08 2022

@author: david
"""

#Importamos la librería de pandas y la librería que hemos creado con las funciones que utilizaremos en este código.
import pandas as pd
import LibEuromillonMultiple_DAS_MDAN

#Pintamos un enunciado orientativo.
print ("Vamos a jugar a los Euromillones. Podrás rellenar entre 1 y 5 apuestas a elegir.")
print ()
print("|----------------------------------------------------------------------------------------------|")
print("|                                    ¡¡EUROMILLONES!!                                          |")
print("|----------------------------------------------------------------------------------------------|")
print("| 1 10 19 28 37 46 | 1 10 19 28 37 46 | 1 10 19 28 37 46 | 1 10 19 28 37 46 | 1 10 19 28 37 46 |")
print("| 2 11 20 29 38 47 | 2 11 20 29 38 47 | 2 11 20 29 38 47 | 2 11 20 29 38 47 | 2 11 20 29 38 47 |")
print("| 3 12 21 30 39 48 | 3 12 21 30 39 48 | 3 12 21 30 39 48 | 3 12 21 30 39 48 | 3 12 21 30 39 48 |")
print("| 4 13 22 31 40 49 | 4 13 22 31 40 49 | 4 13 22 31 40 49 | 4 13 22 31 40 49 | 4 13 22 31 40 49 |")
print("| 5 14 23 32 41 50 | 5 14 23 32 41 50 | 5 14 23 32 41 50 | 5 14 23 32 41 50 | 5 14 23 32 41 50 |")
print("| 6 15 24 33 42    | 6 15 24 33 42    | 6 15 24 33 42    | 6 15 24 33 42    | 6 15 24 33 42    |")
print("| 7 16 25 34 43    | 7 16 25 34 43    | 7 16 25 34 43    | 7 16 25 34 43    | 7 16 25 34 43    |")
print("| 8 17 26 35 44    | 8 17 26 35 44    | 8 17 26 35 44    | 8 17 26 35 44    | 8 17 26 35 44    |")
print("| 9 18 27 36 45    | 9 18 27 36 45    | 9 18 27 36 45    | 9 18 27 36 45    | 9 18 27 36 45    |")
print("|----------------------------------------------------------------------------------------------|")
print("|   1     5      9 |   1     5      9 |   1     5      9 |   1     5      9 |   1     5      9 |")
print("|   2     6     10 |   2     6     10 |   2     6     10 |   2     6     10 |   2     6     10 |")
print("|   3     7     11 |   3     7     11 |   3     7     11 |   3     7     11 |   3     7     11 |")
print("|   4     8     12 |   4     8     12 |   4     8     12 |   4     8     12 |   4     8     12 |")
print("|----------------------------------------------------------------------------------------------|\n") 

#Creamos las listas vacías que llenaremos más tarde con los elementos necesarios.
listaNumeros = []
listaDeListasNumeros = []

listaEstrellas = []
listaDeListasEstrellas = []

#Tenemos que crear una variable que contenga un input. Este input contendrá la cantidad de apuestas que queremos realizar,
#o lo que es lo mismo, cuantas veces se va a ejecutar nuestro código.
nApuestas = int(input("Introduce, entre 1 y 5, el número de apuestas que quieres realizar: "))

#Con este bucle while, controlamos que el número de apuestas seleccionadas por el usuario estén dentro del rango permitido.
while nApuestas <= 0 or nApuestas > 5:
    print ("¡Has escogido una cantidad de apuestas inferior o fuera del rango permitido! Selecciona una cantidad válida.")
    nApuestas = int(input("Introduce, entre 1 y 5, el número de apuestas que quieres realizar: "))

#Ahora, si se cumplen las condiciones controladas en el while anterior...
if nApuestas > 0 and nApuestas <= 5:
#...creamos un bucle con un rango igual al número de apuestas elegidas. Esto hará que el bucle for se ejecute el número de veces deseado.
    for i in range (1, nApuestas +1):
#Marcamos con una cadena "f" el número de apuesta que estamos rellenando y pedimos números...
        print (f"Vamos a realizar la apuesta número {i}.")
        print ("Escoge cinco números entre el 1 y el 50.")
#...que guardamos en una lista de números. Utilizaremos la misma función que utilizamos en el anterior ejercicio del euromillón,
#con las mismas estructuras de control y selección. Una vez seleccionados los números, se añadirán a la lista. Es importante remarcar que esta
#lista (listaNumeros) se verá sobreescrita en cada ciclo del bucle.
        LibEuromillonMultiple_DAS_MDAN.tuBoletoN(listaNumeros)
#Como listaNumeros se sobreescribe en cada ciclo, tenemos que guardar los números elegidos para el boleto. Para ello, en cada ciclo, la lista
#de números completa se guardará en listaDeListasNumeros, una lista de listas con todos los números seleccionados para cada boleto.
#Cada conjunto de números irá en una lista que se reseteará en el próximo ciclo, y antes del reseteo guardamos esa lista en listaDeListasNumeros.
        listaDeListasNumeros.append(listaNumeros)
#Reseteamos la listaNumeros para el siguiente ciclo.
        listaNumeros = []

#Aplicamos todo lo explicado con los números, ahora con las estrellas.        
        print ("Escoge dos estrellas entre el 1 y el 12.")
        LibEuromillonMultiple_DAS_MDAN.tuBoletoE(listaEstrellas)
        listaDeListasEstrellas.append(listaEstrellas)
        listaEstrellas = []

#Al final, tendremos una lista que contiene todas las listas de números para cada boleto, y lo mismo para las estrellas.    
print (listaDeListasNumeros)
print (listaDeListasEstrellas)

#Ahora vamos a generar los distintos dataframes para cada boleto, que iremos concatenando dependiendo del número de apuestas seleccionadas.
#Si solo queremos una apuesta, el código se ejecutará hasta aquí.
if nApuestas >= 1:
#Esto es importante. Programando el DataFrame final nos encontramos con el problema de que se sobrescribía todo el rato el mismo DataFrame.
#Esto ocurría porque, en un inicio, pusimos el mismo nombre a las columnas. Si para cada uno de los posibles DataFrames para cada apuesta
#ponemos nombres diferentes a las columnas, esto se resuelve. Así que para la primera apuesta iremos desde Columna1 a columna6, para la segunda
#apuesta utilizaremos dede Columna7 a Columna12, etc. Al final de cada serie de Columnas, añadiremos otra columna también numerada solo de barras
#que nos servirá para separar los distintos dataframes.
    df1 = pd.DataFrame(columns = ['Columna1', 'Columna2', 'Columna3', 'Columna4', 'Columna5', 'Columna6', 'barra1'])
#Aplicamos la función boletoMarcado sobre la primera apuesta, añadiendo el boleto a nuestro DataFrame df1.
#Es importante marcar las posiciones de las dos listaDeListas, para operar con los números y estrellas de cada apuesta.
    LibEuromillonMultiple_DAS_MDAN.boletoMarcado(listaDeListasNumeros[0], listaDeListasEstrellas[0], df1)
#Crearemos estas variables para posteriormente utilizarlas en la comprobación de aciertos.
    numeros1 = listaDeListasNumeros[0]
    estrellas1 = listaDeListasEstrellas[0]
#Añadimos df1 a nuestro DataFrame final. Como de momento solo es la primera apuesta, nuestro DataFrame final será el mismo que df1.
    dfBoletos = df1
#Si hemos seleccionado 2 apuestas, nuestro código se ejecutará hasta el final de este segundo if.    
if nApuestas >= 2:
#Segundo dataframe con columnas con nombres distintos, para no sobreescribir al concatenar.
    df2 = pd.DataFrame(columns = ['Columna7', 'Columna8', 'Columna9', 'Columna10', 'Columna11', 'Columna12', 'barra2'])
#Operamos exactamente de la misma manera que con la primera apuesta.
    LibEuromillonMultiple_DAS_MDAN.boletoMarcado(listaDeListasNumeros[1], listaDeListasEstrellas[1], df2)
    numeros2 = listaDeListasNumeros[1]
    estrellas2 = listaDeListasEstrellas[1]
#Y, ahora sí, concatenamos con la función concat el nuevo DataFrame con la apuesta 2 al DataFrame anterior, apareciendo una apuesta al lado de
#la otra. Esto lo hacemos con axis = 1.
#Importante colocar ignore_index=True para que no nos aparezca el índice del segundo DataFrame entorpeciendo la información.
    dfBoletos = pd.concat([dfBoletos, df2], ignore_index=True, axis=1)
#De la misma forma, si se han elegido 3 apuestas, tendremos preparado un tercer DataFrame para operar con el y generar un nuevo boleto.
if nApuestas >= 3:
    df3 = pd.DataFrame(columns = ['Columna13', 'Columna14', 'Columna15', 'Columna16', 'Columna17', 'Columna18', 'barra3'])
    LibEuromillonMultiple_DAS_MDAN.boletoMarcado(listaDeListasNumeros[2], listaDeListasEstrellas[2], df3)
    numeros3 = listaDeListasNumeros[2]
    estrellas3 = listaDeListasEstrellas[2]
#De nuevo, concatenamos el tercer boleto al DataFrame final con las dos apuestas anteriores.
    dfBoletos = pd.concat([dfBoletos, df3], ignore_index=True, axis=1)
#El mismo procedimiento en caso de haber cuarta apuesta...
if nApuestas >= 4:
    df4 = pd.DataFrame(columns = ['Columna19', 'Columna20', 'Columna21', 'Columna22', 'Columna23', 'Columna24', ' barra4'])
    LibEuromillonMultiple_DAS_MDAN.boletoMarcado(listaDeListasNumeros[3], listaDeListasEstrellas[3], df4)
    numeros4 = listaDeListasNumeros[3]
    estrellas4 = listaDeListasEstrellas[3]
    dfBoletos = pd.concat([dfBoletos, df4], ignore_index=True, axis=1)
#...y exactamente lo mismo para la quinta apuesta.
if nApuestas == 5:
    df5 = pd.DataFrame(columns = ['Columna25', 'Columna26', 'Columna27', 'Columna28', 'Columna29', 'Columna30', 'barra5'])
    LibEuromillonMultiple_DAS_MDAN.boletoMarcado(listaDeListasNumeros[4], listaDeListasEstrellas[4], df5)
    numeros5 = listaDeListasNumeros[4]
    estrellas5 = listaDeListasEstrellas[4]
    dfBoletos = pd.concat([dfBoletos, df5], ignore_index=True, axis=1)
    
#Se pinta el boleto final, aunque el DataFrame es muy largo y en consola saldrá mal. Para ver el boleto con toda su información, 
#abrimos el DataFrame "dfBoletos" en la ventana de variables.    
print ("Este es tu boleto:")
print()
print(dfBoletos)

print()
#Utilizamos nuestro comandoContinuar para hacer una pausa y permitir leer la información pintada.
LibEuromillonMultiple_DAS_MDAN.comandoContinuar()
print()

#Generamos un boleto randomizado (exactamente el mismo código que el ejercicio de un solo euromillón, ya que solo va a haber un boleto ganador).
#Creamos las listas vacías que se rellenarán con el boleto...
numerosRandom = []
estrellasRandom = []

#Y aplicamos la función de nuestra librería, que generará un boleto aleatorio.
LibEuromillonMultiple_DAS_MDAN.boletoGanador(numerosRandom, estrellasRandom)
LibEuromillonMultiple_DAS_MDAN.boletoGanadorMarcado(numerosRandom, estrellasRandom)

#Llegamos a la parte del código que comprueba los aciertos de cada apuesta con el boleto randomizado ganador.
#Creamos un contador para aciertos de números, otro contador para las estrellas, y una lista de aciertosTotales que contendrá tuplas de los aciertos
#de estrellas y números de cada boleto. 
aciertosN = 0
aciertosE = 0
aciertosTotales = []

#Como hicimos anteriormente, ejecutaremos más o menos veces el código dependiendo del número de apuestas que queramos realizar.
if nApuestas >= 1:   
#Con un bucle for dentro de otro bucle for, recorreremos tanto la lista de números elegidos en nuestro boleto como la lista de números ganadores.    
    for valor1 in numeros1:
        for valor2 in numerosRandom:
#Si los valores son iguales...
            if valor1 == valor2:
#...se sumará uno al contador de aciertos.
                aciertosN = aciertosN + 1
              
#Hacemos exactamente lo mismo con las estrellas.                
    for valor1 in estrellas1:
        for valor2 in estrellasRandom:
            if valor1 == valor2:
                aciertosE = aciertosE + 1

#Aciertos1 será una tupla compuesta por la cantidad de aciertos en los números y la de las estrellas.                
    aciertos1 = (aciertosN, aciertosE) 
#Añadimos dicha tupla a la lista vacía de aciertosTotales.           
    aciertosTotales.append(aciertos1)
#Y reseteamos las variables para el próximo ciclo en el bucle.
    aciertosN = 0
    aciertosE = 0

#Lo mismo en caso de que queramos dos apuestas.    
if nApuestas >= 2:
    for valor1 in numeros2:
        for valor2 in numerosRandom:
            if valor1 == valor2:
                aciertosN = aciertosN + 1
              
    for valor1 in estrellas2:
        for valor2 in estrellasRandom:
            if valor1 == valor2:
                aciertosE = aciertosE + 1
                
    aciertos2 = (aciertosN, aciertosE)            
    aciertosTotales.append(aciertos2)
    aciertosN = 0
    aciertosE = 0

#Tres apuestas...
if nApuestas >= 3:
    for valor1 in numeros3:
        for valor2 in numerosRandom:
            if valor1 == valor2:
                aciertosN = aciertosN + 1
              
    for valor1 in estrellas3:
        for valor2 in estrellasRandom:
            if valor1 == valor2:
                aciertosE = aciertosE + 1
    
    aciertos3 = (aciertosN, aciertosE)
    aciertosTotales.append(aciertos3)
    aciertosN = 0
    aciertosE = 0

#Cuatro apuestas...
if nApuestas >= 4: 
    for valor1 in numeros4:
        for valor2 in numerosRandom:
            if valor1 == valor2:
                aciertosN = aciertosN + 1
              
    for valor1 in estrellas4:
        for valor2 in estrellasRandom:
            if valor1 == valor2:
                aciertosE = aciertosE + 1
    
    aciertos4 = (aciertosN, aciertosE)
    aciertosTotales.append(aciertos4)
    aciertosN = 0
    aciertosE = 0

#Y hasta cinco apuestas.    
if nApuestas == 5:
    for valor1 in numeros5:
        for valor2 in numerosRandom:
            if valor1 == valor2:
                aciertosN = aciertosN + 1
                        
    for valor1 in estrellas5:
        for valor2 in estrellasRandom:
            if valor1 == valor2:
                aciertosE = aciertosE + 1
    
    aciertos5 = (aciertosN, aciertosE)  
#En este punto, y siempre que lleguemos a cinco apuestas, nuestra lista de aciertos totales contendrá cinco tuplas
#(o las tuplas relativas al número de apuestas si nos hemos quedado en cualquiera de los if anteriores.)          
    aciertosTotales.append(aciertos5)
    aciertosN = 0
    aciertosE = 0

#Creamos una lista vacía que contendrá el total de premios.
totalPremios = []

#Y, para cada boleto, utilizaremos nuestra función "lanzaderaPremios", que calculará la cantidad ganada con cada apuesta y se añadirá a
#la lista creada.    
if nApuestas >= 1:
    LibEuromillonMultiple_DAS_MDAN.lanzaderaPremios(aciertos1, aciertosTotales, totalPremios)
if nApuestas >= 2:
    LibEuromillonMultiple_DAS_MDAN.lanzaderaPremios(aciertos2, aciertosTotales, totalPremios)
if nApuestas >= 3:
    LibEuromillonMultiple_DAS_MDAN.lanzaderaPremios(aciertos3, aciertosTotales, totalPremios)
if nApuestas >= 4:
    LibEuromillonMultiple_DAS_MDAN.lanzaderaPremios(aciertos4, aciertosTotales, totalPremios)
if nApuestas == 5:
    LibEuromillonMultiple_DAS_MDAN.lanzaderaPremios(aciertos5, aciertosTotales, totalPremios)

#Por último, lanzaremos un print con una cadena f con una etiqueta que contendrá y pintará el sumatorio de todos los premios conseguidos.    
print(f"La cantidad total de dinero conseguido con tus apuestas es de {sum(totalPremios)}€")