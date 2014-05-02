

import os
import platform

# Definimos la funcion para obtener la informacion del software.

def SOFTinfo():
  softinfo={}
  SO=platform.platform()
  softinfo["S.O"]=SO
  pv=platform.python_version()
  softinfo['Pythons Version']=pv
  pd=platform.python_build
  softinfo['Python Date']=pd
  return softinfo
  
# Definimos la funcion para obtener la informacion del hardware.

def CPUinfo():
  infofile = '/proc/cpuinfo'
  cpuinfo = {}
  if os.path.isfile(infofile):
    f = open(infofile, 'r')
    for line in f:
      try:
	name, value = [w.strip() for w in line.split(':')]
      except:
	continue
      if name == 'model name':
	cpuinfo['CPU type'] = value
      elif name == 'cache size':
	cpuinfo['cache size'] = value
      elif name == 'cpu MHz':
	cpuinfo['CPU speed'] = value + 'Hz'
      elif name == 'vendor_id':
	cpuinfo['vendor ID'] = value
    f.close()
  return cpuinfo
  
# Definimos la funcion para almacenar los datos en un fichero.
  
def savetofile(fn, d1, d2):
  f=open(fn, 'w')
  f.write ('Hardware \n')
  f.write('============================ \n')
  for clave in d1:
    f.write(str(clave))             # Necesitamos convertir clave y el valor de la clave a una cadena de caracteres primero. Por ello, utilizamos str.
    f.write('\t')
    f.write(str(d1[clave]))
    f.write('\n')
    
  f.write ('Software \n')
  f.write('============================ \n')
  for clave in d2:
    f.write(str(clave))
    f.write('\t')
    f.write(str(d2[clave]))
    f.write('\n')
  f.close()
    
if __name__ == '__main__':
  softinfo=SOFTinfo()      #Almacenamos en softinfo el diccionario que se devuelve al llamar a la funcion SOFTinfo.
  cpuinfo=CPUinfo()        #Almacenamos en cpuinfo el diccionario que se devuelve al llamar a la funcion CPUinfo.
  nombref= raw_input("Introduzca el nombre del fichero para almacenar los resultados:")
  savetofile(nombref, cpuinfo, softinfo)
  
  
