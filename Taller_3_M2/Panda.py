# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 18:46:37 2022

@author: jonat
"""

import pandas as pd
from datetime import datetime
import numpy as np

inf = pd.DataFrame({
                    'Nombre': ['ELSY YULIANA SILGADO RIVERA','DEIMER DAVID MORELO OSPINO','JESUS DAVID PORTILLO VILLA',
                                 'JONNIER ANDRES TERAN MORALES','JONATHAN EMILIO BRITO AVILEZ','GUSTAVO JAVIER BLANCO JARAMILLO',
                                 'DAYAN ALZATE HERNANDEZ','WENDY PAOLA MENDOZA BARRERA','ALVARO JOSE ZAMORA CURY','GABRIELA TORRES RAMOS',
                                 'MIGUEL ALFONSO FABRIS AVILA','JHONY ALBERTO MELENDEZ CAVADIA','ADRIANA LUCIA SUAREZ BALLESTEROS',
                                 'JAIDER STIVEN ECHEVERRI BEDOYA','NOIVER DARIO BARROSO RAMOS','Miriam Rosa Lopez Diaz','IVAN DARIO PALENCIA ALEAN',
                                 'ANGELA JOHANNA POSSO DIAZ'],
                      
                     'Edad': [20,20,20,20,21,22,22,24,23,23,21,21,20,22,24,24,25,25],  
                     
                     'Sexo': ['F','M','M','M','M','M','F','F','M','F','M','M','F','M','M','F','M','F'],
                     
                     'Peso': [60,70,72,72,74,74,62,61,76,63,78,80,59,74,70,63,73,64],
                     
                     'Altura': [172,160,158,170,168,167,180,167,169,170,172,162,175,173,165,172,168,168],
                        
                     'D.Invertido': [25000000,23500000,451000,4680000,5420000,48247000,82243540,54121470,5482170,
                                         5467318,34618500,67543200,24376100,90000000,50000000,62200000,58213400,81210000],
                    
                     'I.Anual': [0.05,0.06,0.055,0.063,0.0625,0.065,0.0675,0.07,0.0725,0.075,0.0775,0.05,0.06,0.055,0.063,0.0625,0.065,0.0725],
                     
                     'A.Inversion': [4,2,2,4,5,3,6,7,5,2,1,4,3,1,4,2,2,1], 
                                      
                     'Telefono': ['3174258015','3152656581','3265429658','3136956584','3245126585','3146598546',
                                  '3005659578','30065969658','3219133485','3012566589','3006329563','3216956585',
                                  '3011956758','3002826936','3004697858','3006499696','3012469635','3163533695'],
                     
                     'HCP':['7:00:00','7:15:00','11:15:00','13:20:00','18:30:00','21:15:00','16:05:00','14:05:00','18:10:00','19:35:00','20:30:00','8:30:00','17:40:00','20:15:00','12:15:00','5:05:00','7:30:00','10:45:00']})


# Ejercicio 1: 

for i in inf.index:
    imc = round(((inf["Peso"][i])/((inf["Altura"][i])/100)),2)
    print("""{} Tu índice de masa corporal es {}""".format(str(inf["Nombre"][i]),str(imc)))

# Otro método es agregarlo al DataFrame como una columna
inf["IMC"] = inf["Peso"]/(inf["Altura"]/100)


# Ejercicio 2

for i in inf.index:
    capital = round(inf["D.Invertido"][i]*(((inf["I.Anual"][i])/(100+1))**inf["A.Inversion"][i]),2)
    print("""{} tu capital obtenido en la inversión {}""".format(str(inf["Nombre"][i]),str(capital)))

# Otro método es agregarlo al DataFrame como una columna
inf["CAPITAL_INVERSION"] = round(inf["D.Invertido"]*(((inf["I.Anual"])/(100+1))**inf["A.Inversion"]),2)


#  Ejercicio 3

inf["HA.Hornear"] = ((pd.to_timedelta(inf["HCP"])-pd.to_timedelta("4:15:00")).dt.total_seconds())//3600

condiciones = [
    (inf["HA.Hornear"] >= 0) & (inf["HA.Hornear"]<6),
    (inf["HA.Hornear"] >= 6) & (inf["HA.Hornear"]<12),
    (inf["HA.Hornear"] <= 12) & (inf["HA.Hornear"]<18),
    (inf["HA.Hornear"] <= 18) & (inf["HA.Hornear"]<24)]
selecciones = [0.1, 0.2, 0.3, 0.4]

inf["Descuento"] =  np.select(condiciones, selecciones, default='Not Specified')
inf["T.Precui"] = 7000-(pd.to_numeric(inf["Descuento"], errors='coerce') *7000)

#  Ejercicio 4

condicion = [
    (inf["Sexo"] == "F"),
    (inf["Sexo"] == "M")]
seleccion= [10, 11]


inf["E.Cell"] = np.select(condicion, seleccion, default='Not Specified')