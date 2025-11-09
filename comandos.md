## Guía de comandos Docker del proyecto

Esta guía explica los comandos que usas en este repo para construir imágenes, ejecutar contenedores, gestionar redes, publicar imágenes y exportarlas/importarlas.

### Requisitos

- Docker instalado y con sesión iniciada cuando se empujen imágenes a Docker Hub.

---

### Construir imágenes

- Construir con nombre y tag (frontend sitio web):

```bash
docker build -t sitioweb:latest .
```

- Formato general:

```bash
docker build -t <NOMBRE_IMAGEN>:<TAG> .
```

- `-t`: asigna nombre y etiqueta a la imagen.
- `.`: usa el Dockerfile del directorio actual.

---

### Ejecutar contenedores

- Ejecutar el sitio Nginx mapeando el puerto local 8080 al 80 del contenedor:

```bash
docker run -it --rm -d -p 8080:80 --name web sitioweb
```

- Formato general:

```bash
docker run -it --rm -d -p <PUERTO_HOST>:<PUERTO_CONT> --name <NOMBRE_CONTAINER> <NOMBRE_IMAGEN>
```

Notas de flags:

- `-it`: modo interactivo (útil para ver logs o abrir shell).
- `--rm`: elimina el contenedor al detenerse.
- `-d`: ejecuta en segundo plano (detached).
- `-p HOST:CONT`: mapea puertos. Izquierda = puerto en tu máquina, derecha = puerto expuesto en el contenedor.
- `--name`: asigna nombre legible al contenedor.

---

### Ejecutar la app de Python (ejemplo)

- Exponer el puerto 5000 interno en el 8081 local:

```bash
docker run -it --rm -d -p 8081:5000 --name web_app_python app_python
```

---

### Montar volúmenes (desarrollo en vivo)

- Sincronizar el directorio local `./sitio` con el del contenedor:

```bash
docker run -it --rm -d -p 8080:80 -v ./sitio:/usr/share/nginx/html/sitio --name web sitioweb
```

- `-v LOCAL:RUTA_CONT`: monta un volumen para editar archivos localmente y ver cambios en el contenedor.

### Declarar volúmenes en el Dockerfile

- **Importante**: La instrucción `VOLUME` en el Dockerfile solo **declara** un punto de montaje, no monta un volumen desde el host. El montaje real se hace en tiempo de ejecución con `docker run -v` o en `docker-compose.yml`.

- Sintaxis en el Dockerfile:

```dockerfile
VOLUME ["/ruta/en/contenedor"]
```

- Ejemplo completo:

```dockerfile
FROM nginx:latest

# Declara que este directorio será un volumen
VOLUME ["/usr/share/nginx/html"]
```

- **Diferencia clave**:
  - `COPY`: Los archivos quedan guardados permanentemente en la imagen (estáticos).
  - `VOLUME`: Declara un directorio que será un volumen (susceptible a cambios en tiempo de ejecución).

---

### Redes personalizadas

- Crear una red tipo bridge:

```bash
docker network create marimoon
```

Útil para conectar múltiples contenedores entre sí por nombre.

---

### Publicar imágenes en Docker Hub

1. Iniciar sesión:

```bash
docker login <username>
```

2. Construir la imagen con tu namespace:

```bash
docker build -t <USUARIO>/<NOMBRE>:<TAG> .
# Ejemplo:
docker build -t mlunat/sitioweb:latest .
```

3. Publicar (push):

```bash
docker push <USUARIO>/<NOMBRE>:<TAG>
# Ejemplo:
docker push mlunat/sitioweb:latest
```

---

### Ejecutar una imagen publicada

- Usando `usuario/imagen:tag`:

```bash
docker run --name amiweb --rm -it -p 8080:80 mlunat/sitioweb:latest
```

- Abrir una shell dentro del contenedor (útil para depurar):

```bash
docker run --name amiweb --rm -it -p 8080:80 mlunat/sitioweb:latest /bin/bash
# o
docker run --name amiweb --rm -it -p 8080:80 mlunat/sitioweb:latest sh
```

---

### Inspeccionar un contenedor

- Ver detalles (red, volúmenes, puertos, etc.):

```bash
docker inspect <ID_O_NOMBRE_CONTAINER>
```

---

### Exportar e importar imágenes

- Guardar una imagen a un archivo tar:

```bash
docker save mlunat/sitioweb > sitioweb.tar
# o
docker save <NOMBRE_IMAGEN> > <ARCHIVO>.tar
```

- Cargar una imagen desde archivo:

```bash
docker load --input sitioweb.tar
```

Notas:

- Aunque a veces se le llame “.rar”, `docker save` genera un tarball; usa extensión `.tar` para evitar confusiones.