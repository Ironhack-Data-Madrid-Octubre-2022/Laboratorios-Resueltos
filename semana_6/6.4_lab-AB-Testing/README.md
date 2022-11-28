![Ironhack logo](https://i.imgur.com/1QgrNNw.png)

# Lab | AB-Testing

![cats](images/cats.jpeg)


## Introduction

Imaginad que somos los científicos de datos de la empresa de videojuegos Tactile Entertainment. 

Los desarrolladores del juego Cookie Cats pretenden introducir un cambio en el juego para aumentar la retencion de los jugadores. En cierto nivel del juego los jugadores se encuentran una puerta que les obliga a esperar o a pagar la app. 

Actualmente la puerta se encuentra en nivel 30 y se pretende pasar al nivel 40, para comprobar la retencion a 1 y 7 dias. Antes de realizar el cambio definitivo en el juego se raliza un test AB.

## Data description

+ **UserID**: Numero único que identifica a cada jugador.
+ **Version**: Si el jugador se colocó en el grupo de control (puerta_30 - una puerta en el nivel 30) o en el grupo con la puerta movida (puerta_40 - una puerta en el nivel 40).
+ **sum_gamerounds**: El número de rondas de juego jugadas por el jugador durante los primeros 14 días después de la instalación.
+ **retention_1**: ¿Regresó el jugador y jugó 1 día después de la instalación?
+ **retention_7**: ¿Regresó el jugador y jugó 7 días después de la instalación?


## Getting Started

Los datos estan alojados en `data/cookie_cats.csv`. Nuestro grupo de control sera la version actual `gate_30` y el grupo de tratamiento sera la version `gate_40`. Debemos realizar el test para 1 dia de retencion `retention_1` y para 7 dias `retention_7`. 

## Deliverables

* Jupyter Notebook con AB testing.
