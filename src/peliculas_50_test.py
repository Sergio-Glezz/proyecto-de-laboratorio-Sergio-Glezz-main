from peliculas_50 import *
 
datos='data/peliculas_50.csv'
 
registro=lee_peliculas_50(datos)
 
print('\nLos tres primeros registros son: \n')
print(registro [:3])
 
print('\nLos tres ultimos registros son: \n')
print(registro [-3:])
 
print('\nDatos leidos:\n')
print(len(registro))
 
categoria = input('\nPor que tematica lo quiere flitar(War, Comedy, Drama ...)')
print('\nLas peliculas de la tematica '+categoria+' son:\n')
print(filtro_tematica(registro, categoria))
 
print('\nLa media de puntuacion de las peliculas es:\n')
print(calcular_media_puntuacion(registro))
 
print('\nLa pelicula con mas espectadores es:\n')
print(max_espectadores(registro))
 
print('\nLas peliculas ordenadas por recaudacion son: \n')
print(mayor_menor (registro))

print('\nLa agrupacion de peliculas por puntuacion es: \n')
print(agrupar_por_tematica(registro))
