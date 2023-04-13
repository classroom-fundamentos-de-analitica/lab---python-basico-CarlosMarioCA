import csv

"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

def read_csv():
    with open("data.csv", "r") as raw:
        table = csv.reader(raw, delimiter='	')
        data = list(table)
    return data


def pregunta_01():
    sum=0
    data = read_csv()
    for i in data:
        sum += int(i[1])
    
    return sum

    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """

def pregunta_02():

    lt = ["A","B","C","D","E"]
    listaR= []

    data = read_csv()
    
    for i in lt:
        count = 0
        for a in data:
            if(str(a[0])==i):
                count += 1
        listaR.append((i,count))

    return listaR

    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """

def pregunta_03():


    lt = ["A","B","C","D","E"]
    listaR= []

    data = read_csv()
    
    for i in lt:
        sum = 0
        for a in data:
            if(str(a[0])==i):
                sum += int(a[1])

        listaR.append((i,sum))

    return listaR

    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """

def pregunta_04():

    months = ["01","02","03","04","05","06","07","08","09","10","11","12"]
    data = read_csv()
    list = []

    for a in months:
        sum = 0
        for i in data:
            month = i[2][5:7]
            if a == (str(month)):
                sum += 1
        
        list.append((a,sum))

    return list

    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """

def pregunta_05():

    data = read_csv()
    lt = ["A","B","C","D","E"]
    list = []
    for i in lt:
        min = 10 
        max = 0
        for a in data:
            number = int(a[1])
            if i == a[0]:
                if (number>max):
                    max = number
                if (number<min):
                    min = number
        list.append((i,max,min))

    return list

    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """

def pregunta_06():

    dic = ["aaa","bbb","ccc","ddd","eee","fff","ggg","hhh","iii","jjj"]
    data = read_csv()
    list = []
    codes = []

    for a in dic:
        max = 0
        min = 20
        for i in data:
            dic = i[4]
            codes = dic.split(sep=",")
            for d in codes:
                key, value = d.split(sep=":")
                if key == a:
                    if int(value) > int(max):
                        max = value
                    if int(value) < int(min):
                        min = value
        
        list.append((a,int(min),int(max)))

    return list

    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """

def pregunta_07():

    data = read_csv()
    list = []
    for n in range(0,10):
        listNumber = []
        for i in data:
            number = int(i[1])
            if int(n) == number:
                listNumber.append(i[0])
        list.append((n,listNumber))
    return list

    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """

def pregunta_08():

    data = read_csv()
    list = []
    for n in range(0,10):
        listNumber = []
        for i in data:
            number = int(i[1])
            letter = i[0]
            if int(n) == number and letter not in listNumber:
                listNumber.append(i[0])
        listNumber.sort()
        list.append((n,listNumber))
    return list

    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """

def pregunta_09():
    dic = ["aaa","bbb","ccc","ddd","eee","fff","ggg","hhh","iii","jjj"]
    data = read_csv()
    list =[]
    dictionary = {}

    for d in dic:
        dictionary[d] = 0
        sum = 0
        for i in data:
            diclt = i[4]
            codes = diclt.split(sep = ",")
            for a in codes:
                key, value = a.split(sep=":")
                if key == d:
                    dictionary[d] = dictionary[d] + 1

    return dictionary

    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """

def pregunta_10():

    data = read_csv()
    list = []

    for i in data:
        num1 = len(i[3].split(sep=","))
        num2 = len(i[4].split(sep=","))
        list.append((i[0], num1, num2))

    return list

    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """

def pregunta_11():

    data = read_csv()
    dictionary = {}

    for i in data:
        listLt = i[3].split(",")
        for a in listLt:
            if a in dictionary:
                dictionary[a] = int(dictionary[a]) + int(i[1])
            else:
                dictionary[a] = int(i[1])

    keys = list(dictionary.keys())
    keys.sort()
    dictionary = {i: dictionary[i] for i in keys}
    return dictionary

    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """

def pregunta_12():

    data = read_csv()
    dictionary = {}

    for a in data:
        lt = a[0]
        listCode = a[4]
        codes = listCode.split(sep=",")
        for i in codes:
            num = int(i[4:])
            if lt in dictionary:
                dictionary[lt] = int(dictionary[lt])+ num
            else:
                dictionary[lt] = num

    keys = list(dictionary.keys())
    keys.sort()
    dictionary = {i: dictionary[i] for i in keys}
    return dictionary
