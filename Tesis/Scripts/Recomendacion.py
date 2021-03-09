import pandas as pd
import math
import numpy as np

df = pd.read_excel('Datos.xlsx', engine='openpyxl')
df3 = pd.read_excel('df.xlsx', engine='openpyxl')
df4 = pd.read_excel('df.xlsx', engine='openpyxl')
#df3 = pd.DataFrame(df3)
vector = df['User Mec']
#print(df['Mecnica'][5])
#print(df[["Mecnica", "User Mec"]].sum(axis=1))
#print(df['Mecnica'].mul(vector, axis=0)) 
#print(df['User Mec']*df['Mecnica'])

#df2 = df['User Mec']*df['Mecnica']


#print(df2.sum())
#print(df['Telecomunicaciones']/math.sqrt(df['Telecomunicaciones'].sum()))
#print(math.sqrt(df['Telecomunicaciones'].sum()))
user_profiles  = df4.iloc[-1:,:-4]

#print(user_profiles)
#print(df3.iloc[0:19, 1:8])
#print(df3)
prom = df4
df3 = df3.iloc[0:19, 1:8]
df4 = df4.iloc[0:19, 1:9]
#print(df4.conteo[0])
#print(df3['Mecanica']/math.sqrt(3))
df3['Mecanica'] = df3['Mecanica']/math.sqrt(3)
df3['Telecomunicaciones'] = df3['Telecomunicaciones']/math.sqrt(3)
#df3 = df3[[df3['Telecomunicaciones']/math.sqrt(df3['Telecomunicaciones'].sum())]]
#df3.sum(axis=1)
#print(df4)
x = pd.DataFrame(df3.sum(axis=1))
y = prom.iloc[25:26, 1:8]
#print(x , "++++++++++++++++")
#print(df3['Mecanica']/math.sqrt(x))

feature_name = ['Mecanica', 'Telecomunicaciones', 'Electronica', 'Fundicion', 'Electricidad', 'Dibujo', 'Diseño']

#Se normaliza la matriz de preguntas con un valor entre 0 y 1 dividiendo entre la raiz de la cantidad de ocurrencias
#De una pregunta en la especialiad tecnica

norm_rating = df4.apply(lambda row:row[feature_name]/np.sqrt(row['conteo']),axis=1)
#producto = df4.apply(lambda row:row[feature_name]/np.sqrt(row[y]),axis=1)
#print("Prueba***** ",df4['Mecanica'],"++++", row['Mecanica'])
#for feature in feature_name:
    #print(user_profiles.loc[-1:,feature])
    #print(user_profiles[feature]  * df4[feature],"*****")
    #print("")
    #user_profiles.loc[-1:,feature] = (df4[feature] * user_profiles[feature]).sum()
    #mer = np.dot(df4[feature],y)
for i in range (19):
    #print(df4.iloc[0:i], "Filas ", i)
    #mul = (df4.iloc[0:i , 0:7] * y).sum()
    df4.conteo[i] = np.array(np.multiply(df4.iloc[i:i+1, 0:7], y)).sum()
#print(mul)
#print(np.array(user))
for feature in feature_name:
    y[feature] = (df4['conteo'] * df4[feature]).sum()
#print(df4['conteo'])
print("*********RECOMENDACION************")
print(y)
print("**********************************")
#print((df4['conteo'] * df4['Mecanica']).sum())
#print(df4.iloc[0:1, 0:7])
#print(y)
#print((df4.iloc[0:2, 0:7]).sum())
#print(df4.iloc[0:1, 0:7])
#print(norm_rating.loc[:,feature_name])
#a = np.array([[1, 0], [2, -1]])
#print((np.multiply(df4.iloc[0:1, 0:7], y)).sum())
#r = pd.DataFrame(np.multiply(df4.iloc[4:5, 0:7], y))

#print(np.array(r).sum())
#norm_ratingw= np.dot(rating[feature],y)

#print(norm_rating)
#print("")

#print(prom.iloc[25:26, 1:8])
