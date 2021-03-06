#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 14:18:04 2020

@author: andresmpinzonv
"""
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import funciones



df = pd.read_csv('insdata.csv')
f = df[['Fecha de diagnóstico']].drop_duplicates()
#print(f[['Fecha de diagnóstico']])
#Parece ser q iterar un dataframe de pandas no es buena idea. Convertir mejor a lista
#https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas
ff = f.values.tolist()

#Definir listas para usar más abajo
allRel=[]
allImp=[]
allEst=[]
allCasos=[]
myFechas=[]

for row in ff:
    r = row[0]
    #Pandas y SQL:https://pandas.pydata.org/pandas-docs/stable/getting_started/comparison/comparison_with_sql.html

 
    rel = df[(df['Tipo*'] == 'Relacionado') & (df['Fecha de diagnóstico'] == r)].count()
    allRel.append(rel[0])
    
    imp = df[(df['Tipo*'] == 'Importado') & (df['Fecha de diagnóstico'] == r)].count()
    allImp.append(imp[0])
    
    est = df[(df['Tipo*'] == 'En estudio') & (df['Fecha de diagnóstico'] == r)].count()
    allEst.append(est[0])
    
    casos = df[(df['Fecha de diagnóstico'] == r)].count()
    allCasos.append(casos[0])
    
    myFechas.append(r)
    


print(sum(allCasos))
print(sum(allImp))
print(sum(allRel))
print(sum(allEst))
#--------------  RELACIONADOS - IMPORTADOS - EN ESTUDIO ------------------------ 
# PLOTEAR 
plot2Ydata=[]
plot2Ydata.append(allImp)
plot2Ydata.append(allRel)
plot2Ydata.append(allEst)
plot2Labels = ["Importados","Relacionados","En Estudio"]
plot2Title = "Importados, Relacionados y En Estudio por Fecha"

plotme(myFechas,plot2Ydata,plot2Labels,plot2Title)



#--------------  ACUMULADO E INCREMENTO POR FECHA -------------------- 
acum = []
inc = []

#Esta append es necesario porun error de "index out of range"
#https://www.stechies.com/indexerror-list-assignment-index-out-range/
inc.append(1)
acum.append(1)

for i in range(1,len(allCasos)):
    
    #Acumulado es igual a los casos de hoy mas los acumulados hasta ayer.
    v = allCasos[i] + acum[i-1]
    acum.append(v) 
    
    #Incremento es igual  los casos de hoy menos los casos de ayer.
    x = allCasos[i] - allCasos[i-1]
    inc.append(x)

# PLOTEAR 
fig1Ydata=[]
fig1Ydata.append(acum)
fig1Ydata.append(inc)
fig1Ydata.append(allCasos)
fig1labels = ["Acumulado","Incremento", "Casos Diarios"]
fig1Title =  "Acumulado, Incremento y Casos por fecha"

plotme(myFechas, fig1Ydata,fig1labels, fig1Title)




