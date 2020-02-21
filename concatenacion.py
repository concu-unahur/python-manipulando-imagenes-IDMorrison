import numpy as np
from PIL import Image
from archivos import leer_imagen, escribir_imagen
from api import PixabayAPI
import sys
import logging
import threading

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

def concatenar_horizontal(imagenes):
  min_img_shape = sorted([(np.sum(i.size), i.size) for i in imagenes])[0][1]
  return np.hstack(list((np.asarray(i.resize(min_img_shape, Image.ANTIALIAS)) for i in imagenes)))

def concatenar_vertical(imagenes):
  min_img_shape = sorted([(np.sum(i.size), i.size) for i in imagenes])[0][1]
  return np.vstack(list((np.asarray(i.resize(min_img_shape, Image.ANTIALIAS)) for i in imagenes)))

#imagen1 = leer_imagen('1.jpg')
#imagen2 = leer_imagen('2.jpg')

#escribir_imagen('concatenada-vertical.jpg', concatenar_vertical([imagen1, imagen2]))    
#escribir_imagen('concatenada-horizontal.jpg', concatenar_horizontal([imagen1, imagen2]))    

carpeta_imagenes = './imagenes'
api = PixabayAPI('15310696-a36d5271d753011e61a4139d8', carpeta_imagenes)

urls = api.buscar_imagenes('culos', 5)

for u in urls:
  api.descargar_imagen(u)
  #thread = threading.Thread(target=api.descargar_imagen, name='Thread Loco', args=[u])
  #thread.start()
  logging.info(f'Descargando {u}')

rutas = api.rutasImagenesDescargadas
sizeRutas = len(rutas)

for i in range(0,sizeRutas-1):
  ruta1 = leer_imagen(rutas[i])
  ruta2 = leer_imagen(rutas[i+1])

  escribir_imagen(f"imagenConcatenada{i}.jpg", concatenar_horizontal([ruta1, ruta2]))   
