import modulo
import time

nro_test=10
intervalos=[10, 50, 100, 150, 500, 550, 1000]
umbral=[1e-3, 1e-4, 1e-5, 1e-6, 1e-7]
nombre = "prct12.txt"

#Abrimos el archivo y escribimos, como cabecera, el orden en el que almacenaremos los datos.

f=open(nombre, 'w')
f.write ('Intervalos,  Valor aproximado,  Porcetaje de fallos, Tiempo CPU \n ')
f.write('============================ \n')
# Vamos a 
for n in intervalos:
  p=[]
  p=p+[n]                                                 #Introducimos el numero de intervalos en p.
  a=modulo.aproximacion(n)
  p=p+[a]                                                 #Introducimos la aproximacion calculada en p.
  ci=time.clock()
  for e in umbral:                                        #El cronometro comienza.
    e=modulo.error(n, nro_test, e)
    p=p+[e]                                               #Introducimos el porcentaje de errores en p.
  cf=time.clock()                                         #El cronometro termina.
  tp=cf-ci
  p=p+[tp]                                                #Se introduce el tiempo de CPU en p.
  f.write(str(p))                                         #Ahora que p almacena los datos que buscamos, la escribimos en el fichero.
  f.write("\n")
f.close()

  
