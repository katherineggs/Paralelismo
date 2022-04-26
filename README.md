# Paralelismo
* Fabricio Juárez
* Katherine García
* Andrea Reyes


## Proyecto de Procesamiento Paralelo Sistemas Operativos


**Descripción:** Crear un programa que permita calcular en concurrencia la media, la deviación estándar, el conteo, el valor mínimo y máximo de las series de datos de 1,000 archivos con diferente data.


### Herramientas / Tecnologías utilizadas:
```
- Python
    - Pandas
- Concurrent.futures
    - thread pool excecuter
    - process pool excecuter
- Docker
- DockerHub
```

## Instrucciones para ejecución del proyecto
#### Docker
1. Comando para descargar la imagen de docker:
```
docker pull fabricio2000gjuarez/proyectoparalelismo2
```

2. Comando para correr el contenedor:
```
sudo docker run --cpus="cantidad de CPU's" --memory="1g" -it fabricio2000gjuarez/proyectoparalelismo2
```

**cantidad de CPU's** = Cantidad de CPU's que se le dará al contenedor.

## Ejecuciones
**1 CPU:**
1. Ejecución del escenario de 1 CPU 1 hilo con restricciones de 1G RAM
2. Ejecución del escenario de 1 CPU 4 hilo con restricciones de 1G RAM

![alt text](https://github.com/katherineggs/Paralelismo/blob/main/1%20core.png)



**2 CPU's:**
1. Ejecución del escenario de 2 CPU 2 hilos con restricciones de 1G RAM
2. Ejecución del escenario de 2 CPU 4 hilos con restricciones de 1G RAM
3. Ejecución del escenario de 2 CPU 8 hilos con restricciones de 1G RAM

![alt text](https://github.com/katherineggs/Paralelismo/blob/main/2cores.png)


**4 CPU's:**
1. Ejecución del escenario de 4 CPU 8 hilos con restricciones de 1G RAM
![alt text](https://github.com/katherineggs/Paralelismo/blob/main/core4.png)



## Gráficas del tiempo de ejecución de cada modelo en cada escenario
**Secuencial:**
![alt text](https://github.com/katherineggs/Paralelismo/blob/main/GrafsSecuenciales.png)

**Por funciones:**
![alt text](https://github.com/katherineggs/Paralelismo/blob/main/GrafsFunciones.png)

**Por archivos:**
![alt text](https://github.com/katherineggs/Paralelismo/blob/main/GrafsArchivos.png)

**Por archivos y funciones:**
![alt text](https://github.com/katherineggs/Paralelismo/blob/main/ArchivosFuncs.png)


## Conclusiones
1. Modelo de paralelismo más rápido en los 6 escenarios:

Los modelos de paralelismo más rápidos son:
![alt text](https://github.com/katherineggs/Paralelismo/blob/main/PREGUNTA1.jpeg)


2. ¿Cuál opción modelo de paralelismo escogeríamos y por qué?:

Depende de los recursos que tengamos y objetivo que el proyecto tenga. En este caso, el modelo más consistente fue la paralelización por archivos. A pesar de las restricciones que se tenían.

3. ¿Recomendaríamos paralelizar tanto archivos y funciones al mismo tiempo?:

En este caso, el modelo de paralelizacion por funciones y archivos, es el caso mas tardado. Por lo que no lo recomendariamos debido a la limitacion de recursos que se posee.

4. Factor de mejora de pasar de 1 Core a 2 Core para el proceso que paraleliza los archivos:

```
Cores (N) = 2                   |   Cores (N) = 1 
S = 0.10%                       |   S = 0.10%
Amdahl's Law = 1/((1-S)+(S/N))  |   Amdahl's Law = 1/((1-S)+(S/N))
Amdahl's Law = 1.00050025       |   Amdahl's Law = 1.00000000

Factor de mejora: 0.00050025
```

5. Factor teórico de mejora para el escenario de 2 Core (amdahl's law) al paralelizar por archivo:

```
Cores (N) = 2 
S = 0.10%
Amdahl's Law = 1/((1-S)+(S/N))  
Amdahl's Law = 1.00050025       
```

6. Factor teórico de mejora para el escenario de 2 Core (amdahl's law) al paralelizar por función estadística:

```
Cores (N) = 2 
S = 20%
Amdahl's Law = 1/((1-S)+(S/N))  
Amdahl's Law = 1.11111111      
```

7. Factor teórico de mejora para el escenario de 2 Core (amdahl's law) al paralelizar por función estadística y archivos:

```
Cores (N) = 2 
S = 0.02%
Amdahl's Law = 1/((1-S)+(S/N))  
Amdahl's Law = 1.00010001      
```




