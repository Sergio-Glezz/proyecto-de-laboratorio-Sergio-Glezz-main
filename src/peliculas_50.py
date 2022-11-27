 
 
 
from collections import namedtuple
import csv
from datetime import datetime
from operator import attrgetter
 
 
peliculas_50=namedtuple('peliculas_50','id,titulo,tematicas,fecha_estreno,recaudacion,espectadores,puntuacion,estreno_mundial')
 
 
def lee_peliculas_50(datos):
    with open(datos, encoding='utf-8')as f:
        lector=csv.reader(f,delimiter=';')
        next(lector)
        return[peliculas_50(int(id),titulo,tupla(tematicas),datetime.strptime (fecha_estreno,'%d/%m/%Y').date(),float(cambiar_coma(recaudacion)),int(espectadores),float(cambiar_coma(puntuacion)),cambiar_boolean(estreno_mundial))for id,titulo,tematicas,fecha_estreno,recaudacion,espectadores,puntuacion,estreno_mundial in lector]
 
def tupla(nombre):
    return tuple(nombre.split('|'))
 
def cambiar_coma(r):
    return r.replace(',','.')
 
def cambiar_boolean(dato):
    if(dato=='S'):
        return True
    else:
        return False
 
def filtro_tematica(registro, categoria):
    lista = []
    for t in registro:
        if categoria in t.tematicas:
            lista.append(t)
    return lista
 
def calcular_media_puntuacion(registro):
    suma_total = 0
    for pelicula in registro:
        suma_total += pelicula.puntuacion
    return round(suma_total/(len(registro)),2)
 
def max_espectadores(registro):
    max_espect = 0
    for pelicula in registro:
        if pelicula.espectadores > max_espect:                
                max_espect = pelicula.espectadores
    peliculas_mas_vistas = [pelicula for pelicula in registro if pelicula.espectadores >= max_espect]
    return peliculas_mas_vistas
 
def mayor_menor (registro):
    return sorted(registro, key = attrgetter('recaudacion'), reverse = True)

def agrupar_por_tematica(registro):
    d=dict()
    for r in registro:
        f=r.tematicas
        if f not in d:
            d[f]=r
        d[f]=[r for r in registro if f==r.tematicas]
    return d.items()
    