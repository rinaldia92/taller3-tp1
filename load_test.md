# Tests de carga: Page Visits Counter
## Taller de Programación III (75.61)

<h1 align="center">
  <img src="./images/logofiuba.jpg" alt="logo fiuba">
</h1>

## Autor: Alan Rinaldi
## Fecha: 6 de mayo 2021




## Indice:

- [1- Casos propuestos](#1--casos-propuestos)
- [2- Sin cache](#2--sin-cache)
    - [2.1- Maximo 1 instancia](#21--maximo-1-instancia)
    - [2.2- Maximo 3 instancias](#22--maximo-3-instancias)
- [3- Con cache 1 seg](#3--con-cache-1-seg)
    - [3.1- Maximo 1 instancia](#31--maximo-1-instancia)
    - [3.2- Maximo 3 instancias](#32--maximo-3-instancias)
    - [3.3- Maximo 3 instancias con mas carga](#33--maximo-3-instancias-con-mas-carga)

## 1- Casos propuestos

Se proponen los siguientes casos:

* Sin utilizar cache:
    * Maximo 1 instancia
    * Maximo 3 instancias

* Utilizando cache:
    * Maximo 1 instancia
    * Maximo 3 instancias

El test de carga utilizado es:

```
stages = [
    {"duration": 180, "users": 100, "spawn_rate": 1},
    {"duration": 300, "users": 500, "spawn_rate": 10},
    {"duration": 600, "users": 1000, "spawn_rate": 10},
    {"duration": 800, "users": 300, "spawn_rate": 20},
    {"duration": 900, "users": 1000, "spawn_rate": 20},
    {"duration": 1100, "users": 1, "spawn_rate": 20},
]
```

## 2- Sin cache
### 2.1- Maximo 1 instancia

El reporte completo se encuentra [aqui](./reportes/sin_cache_1_instancia_report.html)

Se observa que empieza a fallar cuando empieza a alcanzar a los 500 usuarios concurrentes. En ese momento se observa que empieza a oscilar las requests por segundo aumentando levemente a medida que el sistema se estabiliza. Pasa lo mismo al ir subiendo de 500 a 1000 usuarios. En ambos casos aproximadamente un 10% de las requests fallan. Cuando se vuelve a subir a los 1000 usuarios pero con una tasa mas alta vemos que fallan aproximadamente 20% de las requests.

<img src="/images/sin_cache_1_instancia_requests.png">
<img src="/images/sin_cache_1_instancia_response_time.png">
<img src="/images/sin_cache_1_instancia_users.png">
<img src="/images/sin_cache_1_instancia_instancias.png">

### 2.2- Maximo 3 instancias

El reporte completo se encuentra [aqui](./reportes/sin_cache_3_instancia_report.html)

A diferencia del caso anterior, al tener la posibilidad de tener mas instancias disponibles, observamos que tenemos un poco mas de requests por segundo. Las fallas ocurren al subir a los 1000 usuarios pero representan un 5% de las requests.

<img src="/images/sin_cache_3_instancia_requests.png">
<img src="/images/sin_cache_3_instancia_response_time.png">
<img src="/images/sin_cache_3_instancia_users.png">
<img src="/images/sin_cache_3_instancia_instancias.png">

## 3- Con cache 1 seg
### 3.1- Maximo 1 instancia

El reporte completo se encuentra [aqui](./reportes/con_cache_1_instancia_report.html)

A diferencia de los casos anteriores, observamos que el response time baja siendo la mediana la mitad del tiempo. Esto tambien provocó un aumento de RPS. Las fallas se presentaron al subir a 1000 usuarios pero con una tasa de aproximadamente del 1% de error.

<img src="/images/con_cache_1_instancia_requests.png">
<img src="/images/con_cache_1_instancia_response_time.png">
<img src="/images/con_cache_1_instancia_users.png">
<img src="/images/con_cache_1_instancia_instancias.png">

### 3.2- Maximo 3 instancias

El reporte completo se encuentra [aqui](./reportes/con_cache_3_instancia_report.html)

En este caso observamos que la tasa de error baja a menos del 1%.
Aca tambien observamos que la primera vez que subimos a 1000 usuarios solamente tenemos activas hasta 2 instancias. Pero en la segunda vez, al subir con una tasa mas alta, se llegan a activar las 3 instancias.

<img src="/images/con_cache_3_instancia_requests.png">
<img src="/images/con_cache_3_instancia_response_time.png">
<img src="/images/con_cache_3_instancia_users.png">
<img src="/images/con_cache_3_instancia_instancias.png">

### 3.3- Maximo 3 instancias con mas carga

El reporte completo se encuentra [aqui](./reportes/con_cache_3_instancia_mayor_carga_report.html)

Para este caso particular, aumentamos la carga hasta 2000 usuarios. Los pasos son:

```
stages = [
    {"duration": 30, "users": 50, "spawn_rate": 10},
    {"duration": 70, "users": 500, "spawn_rate": 30},
    {"duration": 120, "users": 1000, "spawn_rate": 50},
    {"duration": 350, "users": 2000, "spawn_rate": 50},
    {"duration": 450, "users": 300, "spawn_rate": 20},
    {"duration": 500, "users": 2000, "spawn_rate": 50},
    {"duration": 800, "users": 1, "spawn_rate": 20},
]
```
A medida que vamos sumando usuarios vemos como la cantidad de requests van cayendo. Las fallas estan entre el 10 y 15%. A medida que se va estabilizando va subiendo la cantidad de requests. La segunda vez que sube a 2000 usuarios pero con una tasa mas alta llegamos a tener mas del 30% de requests fallidas. Ademas, en comparación a los anteriores casos, la cantidad de requests es menor y, en ciertos casos, la mediana del response time es mayor que el primer caso.
Tambien, al tener menor RPS, tenemos menos instancias activas.

<img src="/images/con_cache_3_instancia_mayor_carga_requests.png">
<img src="/images/con_cache_3_instancia_mayor_carga_response_time.png">
<img src="/images/con_cache_3_instancia_mayor_carga_users.png">
<img src="/images/con_cache_3_instancia_mayor_carga_instancias.png">



