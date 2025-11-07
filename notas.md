**docker file**

ES el archivo base para crear una imagen trae algunas configuiraciones minimas necesarias para la correcta ejecucion.

# DOCKER DAEMON: Es el corazon de docker es el enccargado de crear y ejecutar los contenedores
    con este tambien administramos imagenes, redes y volumenes. Tambien se comunica con otros
    daemons si trabajas en un cluster por ejemplo con docker swarm o Kubernetes

    ESte funciona a traves de la CLI que se comunica con el daemon mediante un API-REST interna usualmente
    ubicado en la ruta /var/run/docker.sock (es un socket unix)

# COMANDOS: escenciales de docker*

- docker help: Documentacion
- Docker images --help: Documentacion del recurso que requires ayuda.
- docker image: lista de las imagenes que tengo creadas
- Docker Info: todo lo que usa docker
- Docker build : coonstruye una imagen
  - docker build -t sitioweb:latest . 
- DOcker run: corre contenedor con la imagen ya construida
- docker run -it --rm -d -p XXXX --NAME       : corre una imagen de manera interactiva
        -it: container interactivo me mostrara logs y prints saber la termina de mi proyecto
        --rm: me eliminara versiones anteriores de este mismo conetenedor
        -d: que se ejecute en un segundo plano
        -p: puerto de exposicion de comunicacion 8081:80
        --name: nombre del contenedor y enseguida nombre de la iamgen que se va usar, quedando
                el comando de la siguiente manera.

- docker run -it --rm -p 8081:80 --name web sitioweb
            una vez ejecutado y considerando el puerto 8081 en el navegadior revisamos si qiuedo o no


TENGO PROBLEMAS CON LA IMAGEN NGINX SIRVE SU HTML POR DEFECTO Y NO EL MIO:

Solucion:
    ingrear al contenedor desplegado: usando:
        # docker exec -it <container_name_or_id> bash

    ir al fichero:
        /etc/nginx/conf.d/

        verificar que la linea de index tenga el archivo correspondiente. 

# Gestion de imagenes y contenedores:


### Para filtrar imagenes cuando tenemos varias imagenes montadas podemos hacer lo siguiente:
    
    * docker images --no-trunc
      * ESto nos da el image id de una forma mas extendida la real.  en forma 256

        - filtro 1: docker images --filter=reference'*:1.0' 
        - filtro 2: docker images sitioweb  ---> usando el nombre de la imagen

        crear un nuevio tag para una imagen ya creada.

    - Filtrar por nombre:
      - docker images --filter=reference='*:1.0' 
        - Lo que hara este comando ser afiltrar todas las iamgenes que contengan "cualquier cosa" segiuda de :1.0
                        anterior        nuevo
    * docker image tag sitioweb:latest amin-sitioweb:latest
    * docker image tag respository:tag  camilo/sitioweb:latest

    # Eliminar imagenes ya creadas

    *   docker rmi camilo-sitioweb:latest

        ELimnar una o varias imagenes basandome en el ID de la imagen

            ```docker
            docker rmi -f id-image , para esto debe estan detenidas
            ```
    ## NO DEBEN ESTAR EN FUNCIONAMIENTO POR ALGUN CONTENEDOR

    ### CAMBIAR NOMBRE DE UNA IMAGE
        docker image tag sitioweb:latest amin/sitioweb:latest



# Administracion de conetenedores: comandos y practicas

### Listado de contenedores
    Docker ps -a
    docker ps --size : nos dice que tamano que usa el contenedor

### Detener contenedores:
    Docker stop CONTAINER_ID: detiene la imagen que le indiquemos
    Docker stats : nos muestra el comportamiento del contenedor

# DESPLIEGUE DE UNA API FLASK EN DOCKER PASO A PASO

Se crea un docker file donde usamos un archivo que tiene dos lineas
que indica las librerias que quiero usar.
Creamos el directorio de trabajo y copiamos alli nuestro requirenments.txt
Despues lanza un cmd con algunas instrucciones


# Gestión de Volúmenes en Docker para Desarrollo Web

### LOs volumenes espacios compartidos entre local y el contenedor. ES una especie de carpeta de unidad de disco compartida, puente de comunicacion entre el local  el contenedor. ES posible cambiar en caliente. Es muy util para analisis de datos. 

Entonces creamos un contenedor basados en una imagen lanzando, para ver interaccion con volumnenes:

docker run -it --rm -d -p 8081:80 -V ./sitio:/usr/share/nginx/html/sitio --name sitioweb nginx

## DIFERENCIA ENTRE CREAR UN VOLUMEN DESDE EL COPY Y EL VOLUME

FROM nginx:latest

COPY /sitio /usr/share/nginx/html

VOLUME ["/sitio","/usr/share/nginx/html"]  ---> copiar la informacion en una iamgen de docker

La diferencia es que entre el COPY y el VOLUMEN es:

- En el copy quedara guaradada de manera permanente en la imagen de docker.
- EN el volumen la informacion esta suceptible a cambios.

    Hay escenarios para cada caso, para generar neuvo contenido para la imagen VOLUMEN es el caso, en el caso de querer tenerlo estatico copy es mejor ya que no cambiara. 


# Redes en Docker: Configuración y Gestión Eficiente de Contenedores

docker inspect web  : esto nos genera el json con algunas caracteristicas del contenedor.

docker run -it --rm -d -p 127.0.0.1:8081:80 --name web nginx :
    ES la manera es como asignamos una ip a cada uno de los contenedores, para orquestar sin problema, sino se asigna queda asignada de manera automatica. 

    bridge: lo que hace es un puente entre entorno local o caulquier otro entorno y el entorno interdo de docker.

    docker network ls, esto nos despliega o nos indica algunas categorias

    ### bridge:
            Presente en la mayoria de contenedores, es la red predeterminada en docker cuando no especificas una red al ejecutar el contenedor, los contenedores en esta red pueden comunicarsen entre si, pero no tienen acceso directo al exterior a menos que se exponga un puerto.
    ### host:
            esta red conecta al contenedor directamente con la red de la maquina host. No hay aislamiento de red entre el contenedor y la maquina. util cuando necesitas que el contenedor tenga acceso total a las interfases de red del host. 
            establece comunicacion exclusica entre dos conetenedores que no quieren compartir red entre otros dos contenedores. 
    ### none: 
            Este tipo de red no conecta el contenedor a nunfuna red, lo que significa que no tendra acceso de red en lo absoluto. 

            TAmbien podemos personalziar una red

            docker network create "nombreREd"