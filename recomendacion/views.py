from django.shortcuts import render
from django.http import JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
import math
import numpy as np
import json
from rest_framework.parsers import JSONParser
import os
from math import log

# Create your views here.
def Resultado(self):
    df = pd.read_excel('recomendacion/Datos.xlsx', engine='openpyxl')
    df3 = pd.read_excel('recomendacion/df.xlsx', engine='openpyxl')
    df4 = pd.read_excel('recomendacion/df.xlsx', engine='openpyxl')
    vector = df['User Mec']
    user_profiles  = df4.iloc[-1:,:-4]
    prom = df4
    df3 = df3.iloc[0:19, 1:8]
    df4 = df4.iloc[0:19, 1:9]
    df3['Mecanica'] = df3['Mecanica']/math.sqrt(3)
    df3['Telecomunicaciones'] = df3['Telecomunicaciones']/math.sqrt(3)
    x = pd.DataFrame(df3.sum(axis=1))
    y = prom.iloc[25:26, 1:8]
    feature_name = ['Mecanica', 'Telecomunicaciones', 'Electronica', 'Fundicion', 'Electricidad', 'Dibujo', 'Diseño']
    norm_rating = df4.apply(lambda row:row[feature_name]/np.sqrt(row['conteo']),axis=1)
    for i in range (19):
        df4.conteo[i] = np.array(np.multiply(df4.iloc[i:i+1, 0:7], y)).sum()
    for feature in feature_name:
        y[feature] = (df4['conteo'] * df4[feature]).sum()
    print(y['Mecanica'])
    print(y.Mecanica)
    
    result = y.to_json(orient="split")
    parsed = json.loads(result)
    json.dumps(parsed, indent=4)
    return JsonResponse(parsed)


#Se define un metodo para visualizar la presicion del algoritmo por medio de una
# Ruta que llama al archivo JSON donde se almacenan los datos 
def Estadistica(self):
    filename = 'recomendacion/Presicion.json'
    with open(filename, 'r') as f:
        data = json.load(f)
    return JsonResponse(data[0])
    

#Funcion de tipo post que recibe la calificacion del estudiante y hace una recomendacion 
# con respecto a la matriz representada en el excel
@csrf_exempt
def Post(request):
    print(request.method == "POST")
    x12 = JSONParser().parse(request)
    print(x12)
    #print(x['prueba'])
    #print(request.POST.get('body'))
    #body = json.loads(request.body.decode('utf-8'))
    #print(str(body["prueba"]))
    #print(request.POST.get('prueba'))
    #/auth/get-token/
    df = pd.read_excel('recomendacion/Datos.xlsx', engine='openpyxl')
    df3 = pd.read_excel('recomendacion/df.xlsx', engine='openpyxl')
    df4 = pd.read_excel('recomendacion/df.xlsx', engine='openpyxl')
    df5 = pd.read_excel('recomendacion/df-Prueba.xlsx', engine='openpyxl')
    df6 = pd.read_excel('recomendacion/df-Prueba.xlsx', engine='openpyxl')
    vector = df['User Mec']
    user_profiles  = df4.iloc[-1:,:-4]
    #user2 = df6.iloc[-1:,:-4]
    prom = df4
    prom2 = df5
    df3 = df3.iloc[0:19, 1:8]
    #df5 = df5.iloc[0:28, 1:8]
    #df4 = df4.iloc[0:19, 1:9]
    df4 = df5.iloc[0:28, 1:9]
    df3['Mecanica'] = df3['Mecanica']/math.sqrt(3)
    df3['Telecomunicaciones'] = df3['Telecomunicaciones']/math.sqrt(3)
    x = pd.DataFrame(df3.sum(axis=1))
    y = prom.iloc[25:26, 1:8]
    #z = prom2.iloc[34:35, 1:8]
    
    cars = {'Mecanica': [x12['Mecanica']],
            'Telecomunicaciones': [x12['Telecomunicaciones']],
            'Electronica': [x12['Electronica']],
            'Fundicion': [x12['Fundicion']],
            'Electricidad': [x12['Electricidad']],
            'Dibujo': [x12['Dibujo']],
            'Diseño': [x12['Diseño']]
        
        }
    calif = pd.DataFrame(cars, columns = ['Mecanica', 'Telecomunicaciones', 'Electronica', 'Fundicion', 'Electricidad', 'Dibujo', 'Diseño'])
    print(calif)
    y = calif
    feature_name = ['Mecanica', 'Telecomunicaciones', 'Electronica', 'Fundicion', 'Electricidad', 'Dibujo', 'Diseño']
    norm_rating = df4.apply(lambda row:row[feature_name]/np.sqrt(row['conteo']),axis=1)
    for i in range (28):#19
        df4.conteo[i] = np.array(np.multiply(df4.iloc[i:i+1, 0:7], y)).sum()
    for feature in feature_name:
        y[feature] = (df4['conteo'] * df4[feature]).sum()
    print(y['Mecanica'])
    print(y.Mecanica)
    
    
    result = y.to_json(orient="split")
    parsed = json.loads(result)
    json.dumps(parsed, indent=4)
     



    return JsonResponse(parsed)

#Funcion tipo post que compara los items relevantes para y usuario y los items
# relevantes para el sistema de recomendacion calculando la precision del algoritmo
# utilizando el metodo MRR y el metodo IDG los cuales se almacenan en un archivo JSON
@csrf_exempt
def Precision(request):
    req = JSONParser().parse(request)
    #print(req["SR"][0])
    #print("Top User : ---")
    #print(req["Top"])
    lista = req["SR"][1]
    cal2 = req["SR"][0]
    for x in range(1, len(lista)):
        for posicion in range (len(lista) - x):
            if lista[posicion] < lista[posicion + 1]:
                temp = lista[posicion]
                lista[posicion] = lista[posicion + 1]
                lista[posicion + 1 ] = temp 

                temp2 = cal2[posicion]
                cal2[posicion] = cal2[posicion + 1]
                cal2[posicion + 1 ] = temp2 

    MRR = 0
    for i in range (7):
        if req["Top"][0] == cal2[i]:
            MRR = 1/(i+1)

    puntos = [0,0,0]

    if (cal2[0] in req["Top"]):
        puntos[0] = 1

    if (cal2[1] in req["Top"]):
        puntos[1] = 1
    
    if (cal2[2] in req["Top"]):
        puntos[2] = 1
        

    ideal = sorted(puntos)
    ideal.reverse()


    DCG = 0
    IDCG = 0
    for i in range (3):
        ide = ((2**puntos[i]) - 1)/(log(i+2,2))
        DCG = DCG + ide

        norm = ((2**ideal[i]) - 1)/(log(i+2,2))
        IDCG = IDCG + norm
    
    Total = DCG/IDCG
    
    #print(lista)
    #print(cal2)
    #print(MRR)
    #print(puntos)
    #print(ideal)
    
    #print(Total)
    print(DCG)
    print(IDCG)

    filename = 'recomendacion/Presicion.json'
    with open(filename, 'r') as f:
        data = json.load(f)
    #print(data[0]["Total"])TotalUser
    data[0]["Total"]["NDCG"] = data[0]["Total"]["NDCG"] + Total
    data[0]["Total"]["MRR"] = data[0]["Total"]["MRR"] + MRR
    data[0]["Total"]["TotalUser"] = data[0]["Total"]["TotalUser"] + 1
    #PonderadoMRR": 1,"PonderadoNDCG"
    data[0]["Total"]["PonderadoNDCG"] = data[0]["Total"]["NDCG"] / data[0]["Total"]["TotalUser"]
    data[0]["Total"]["PonderadoMRR"] = data[0]["Total"]["MRR"] / data[0]["Total"]["TotalUser"]

    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    return JsonResponse({"Respuesta": "Exito"})

#Esta funcion se encarga de almacenar los likes y dislikes con los que los usuarios
# califican la aplicacion almacenandolos en un archivo JSON
@csrf_exempt
def likes(request):
    req = JSONParser().parse(request)
    filename = 'recomendacion/Presicion.json'
    with open(filename, 'r') as f:
        data = json.load(f)
    if(req["calif"] == 1):
        data[0]["Total"]["Likes"] = data[0]["Total"]["Likes"] + 1
    if(req["calif"] == 0):
        data[0]["Total"]["Dislikes"] = data[0]["Total"]["Dislikes"] + 1

    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    
    return JsonResponse({"Respuesta": "Exito"})