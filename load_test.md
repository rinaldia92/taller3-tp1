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
- [4- Con cache 10 seg](#4--con-cache-10-seg)
    - [4.1- Maximo 3 instancias](#41--maximo-3-instancias)

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

El reportecompleto se encuentra [aqui](./reportes/sin_cache_1_instancia_response_time.html)

<img src="/images/sin_cache_1_instancia_requests.png">
<img src="/images/sin_cache_1_instancia_response_time.png">
<img src="/images/sin_cache_1_instancia_users.png">
<img src="/images/sin_cache_1_instancia_instancias.png">

### 2.2- Maximo 3 instancias

El reportecompleto se encuentra [aqui](./reportes/sin_cache_3_instancia_response_time.html)

<img src="/images/sin_cache_3_instancia_requests.png">
<img src="/images/sin_cache_3_instancia_response_time.png">
<img src="/images/sin_cache_3_instancia_users.png">
<img src="/images/sin_cache_3_instancia_instancias.png">

## 3- Con cache 1 seg
### 3.1- Maximo 1 instancia

El reportecompleto se encuentra [aqui](./reportes/con_cache_1_instancia_response_time.html)

<img src="/images/con_cache_1_instancia_requests.png">
<img src="/images/con_cache_1_instancia_response_time.png">
<img src="/images/con_cache_1_instancia_users.png">
<img src="/images/con_cache_1_instancia_instancias.png">

### 3.2- Maximo 3 instancias

El reportecompleto se encuentra [aqui](./reportes/con_cache_3_instancia_response_time.html)

<img src="/images/con_cache_3_instancia_requests.png">
<img src="/images/con_cache_3_instancia_response_time.png">
<img src="/images/con_cache_3_instancia_users.png">
<img src="/images/con_cache_3_instancia_instancias.png">

## 4- Con cache 10 seg
### 4.1- Maximo 3 instancias

