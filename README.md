# Trabajo práctico N° 1: Page Visits Counter
## Taller de Programación III (75.61)

<h1 align="center">
  <img src="./images/logofiuba.jpg" alt="logo fiuba">
</h1>

## Autor: Alan Rinaldi
## Fecha: 6 de mayo 2021




## Indice:

   - [1- Objetivo](#1--objetivo)
      - [1.1- Requerimientos funcionales](#11--requerimientos-funcionales)
      - [1.2- Requerimientos no funcionales](#11--requerimientos-no-funcionales)
   - [2- Casos de uso](#2--casos-de-uso)
   - [3- Vista Logica](#3--vista-logica)
        - [3.1- Diagrama de clases](#3.1--diagrama-de-clases)
   - [4- Vista de Desarrollo](#4--vista-de-desarrollo)
        - [4.1- Diagrama de paquetes](#4.1--diagrama-de-paquetes)
   - [5- Vista de Proceso](#5--vista-de-proceso)
        - [5.1- Diagrama de secuencua](#5.1--diagrama-de-secuencia)
            - [5.1.1- Obtener pagina con dato en cache](#5.1.2--obtener-pagina-con-dato-en-cache)
            - [5.1.2- Obtener pagina sin dato en cache](#5.1.2--obtener-pagina-sin-dato-en-cache)
            - [5.1.3- Actualizar contador](#5.1.3--actualizar-contador)
        - [5.2- Diagrama de actividades](#5.2--diagrama-de-actividades)
   - [6- Vista Fisica](#6--vista-fisica)
        - [6.2- Diagrama de robustez](#6.2--diagrama-de-robustez)
   - [7- Test de carga](#7--test-de-carga)
   - [8- Futura mejora](#8--futura-mejora)


## 1- Objetivo

### 1.1- Requerimientos funcionales

Los requerimientos funcionales del correspondiente proyecto son:
* Se solicita el diseño de un sistema web institucional que posea las siguientes secciones:
    * Home
    * Jobs
    * About
    * Legals
* Este debe registrar y mostrar la cantidad de visitas que tuvo cada sección de manera individual.

### 1.2- Requerimientos no funcionales

Los requerimientos no funcionales del correspondiente proyecto son:
* El sistema de conteo de visitas debe ser programado de forma tal que se permita su reuso en otros sitios de la empresa.
* El sistema de conteo de visitas debe ser desarrollado con tecnologías Google AppEngine.
* Se requiere mostrar cómo se comporta la aplicación bajo diferentes niveles de carga. Para esto se deberá proporcionar los resultados de pruebas de carga y stress.
* El sistema debe soportar escalamiento al tráfico recibido.
* El sistema debe mostrar alta disponibilidad hacia los clientes.
* El sistema debe ser tolerante a fallos como la caída de procesos.

&nbsp;

## 2- Casos de uso

Como fue explicado en los objetivos hay 4 casos de uso:
* El user visita la sección Home.
* El user visita la sección Jobs.
* El user visita la sección About.
* El user visita la sección Legals.

<img src="/images/casosdeuso.jpg">

## 3- Vista Logica

### 3.1- Diagrama de clases

El sistema web cuenta con las siguientes clases:
* Counter: Clase encargada de establecer la conexión con el datastore y obtener/guardar los datos.
* Task: Clase encargadada de conectarse con cloud task y agregarle tareas.
* Cache: Clase encargada de simular una cache en memoria.
* Logger: Clase encargada de loggear. El proceso principal y las clases utilizan este logger y se mantiene la traza.

<img src="/images/clases.jpg">

## 4- Vista de Desarrollo

### 4.1- Diagrama de paquetes

El sistema cuenta con tres paquetes:
* Web Server
* Queue Task: GCP Cloud Task
* DB: GCP Datastore

<img src="/images/paquetes.jpg">

## 5- Vista de Proceso

### 5.1- Diagrama de secuencia

#### 5.1.1- Obtener pagina con dato en cache

<img src="/images/secuenciaconcache.jpg">

#### 5.1.2- Obtener pagina sin dato en cache

<img src="/images/secuenciasincache.jpg">

#### 5.1.3- Actualizar contador

<img src="/images/secuenciaupdate.jpg">

### 5.2- Diagrama de actividades

<img src="/images/actividades.jpg">

## 6- Vista Fisica

### 6.1- Diagrama de robustez

<img src="/images/robustez.jpg">

## 7- Test de carga

Los resultados del test de carga se encuentran [aqui]("/Load Test.md")

## 8- Futura mejora

Para mejorar los tiempos de respuesta se debe implementar que sea otro proceso el encargado de agregar una tarea a la queue task.