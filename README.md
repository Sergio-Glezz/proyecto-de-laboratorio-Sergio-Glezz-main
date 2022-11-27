# Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso  \<XX\>/\<YY\>)
Autor/a: \<Sergio Arsenio González Collado\>   uvus:\<WXB6580\>

Es un fivhero de datos sobre 50 películas con distintos datos los cuales han sido recopilados tanto del publico como el número de espectadores, la recaudación o la puntuación, o datos más generales como el titulo de cada película, su fecha de estreno, sus temáticas, etc...


## Estructura de las carpetas del proyecto

* **/src**: Contiene los diferentes módulos de Python que conforman el proyecto.
  * **\<peliculas_50.py\>**: En este módulo principal encontramos la lectura del dataset que he escogido, en este caso sobre 50 películasy diversa información sobre ellas como el título, la temática, la recaudación, etc...
  * **\<peliculas_50_test.py\>**: En este otro módulo dedicado a las pruebas del principal, encontramos ejemplos para comprobar que el módulo principal vaya funcionando como es debido y no haya errores.
* **/data**: Contiene el dataset del proyecto.
    * **\<peliculas_50.csv\>**: Este dataset incluye información y datos recogidos de 50 películas distintas.
    
## Estructura del *dataset*

El dataset está compuesto por \<8\> columnas, con la siguiente descripción:

* **\<id>**: de tipo \<int\>, representa el número en el que están ordenadas las películas.
* **\<título>**: de tipo \<tipo\>, representa el título de cada película.
* **\<temáticas>**: de tipo \<tupla\>, representa los distintos géneros de la película.
* **\<fecha_estreno>**: de tipo \<datetime.strptime\>, representa la fecha concreta en la que se estrenó la película.
* **\<recaudación>**: de tipo \<float\>, representa la cantidad en millones de dolares que recaudó la película en total.
* **\<espectadores>**: de tipo \<int\>, representa el número de espectadores que asistieron a ver la película.
* **\<puntuación>**: de tipo \<float\>, representa la puntuación media que le han dado los espectadores del 0 al 5.
 **\<estreno_mundial>**: de tipo \<boolean\>, representa el si la película se estrenó mundialmente o solo en algunos países.


## Tipos implementados

peliculas_50=namedtuple('peliculas_50','id,titulo,tematicas,fecha_estreno,recaudacion,epectadores,puntuacion,estreno_mundial')
peliculas_50(int(id),titulo,tupla(tematicas),datetime.strptime (fecha_estreno,'%d/%m/%Y').date(),float(cambiar_coma(recaudacion)),int(espectadores),float(cambiar_coma(puntuacion)),cambiar_boolean(estreno_mundial))

## Funciones implementadas
Añade aquí descripciones genéricas de las funciones, que luego debes acompañar con comentarios de tipo documentación en el código

### \<modulo 1\>

* **<funcion 1>**: Descripción de la función 1.
* **<funcion 2>**: Descripción de la función 2.
* ...

### \<test modulo 1\>

* **<test funcion 1>**: Descripción de las pruebas realizadas a la función 1.
* **<test funcion 2>**: Descripción de las pruebas realizadas a la función 2.
* ...
* 
### \<modulo 2\>

* **<funcion 1>**: Descripción de la función 1.
* **<funcion 2>**: Descripción de la función 2.
* ...
