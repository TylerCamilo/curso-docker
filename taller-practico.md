# Taller Práctico de Docker - Fundamentos

Este taller te guiará paso a paso a través de los conceptos esenciales de Docker, desde lo básico hasta el despliegue de aplicaciones completas con Docker Compose.

---

## 📋 Requisitos Previos

- Docker instalado y funcionando
- Terminal/CLI disponible
- Editor de texto
- Navegador web

**Verificar instalación:**
```bash
docker --version
docker info
```

---

## 🎯 Módulo 1: Primeros Pasos con Docker

### Ejercicio 1.1: Explorar el Docker Daemon

**Objetivo:** Entender cómo funciona el daemon de Docker y su comunicación.

**Pasos:**

1. Verificar el estado del daemon:
```bash
docker info
```

2. Verificar el socket de comunicación:
```bash
ls -la /var/run/docker.sock
```

3. Obtener ayuda sobre comandos:
```bash
docker help
docker images --help
```

**Resultado esperado:** Deberías ver información del sistema Docker y el socket Unix disponible.

---

### Ejercicio 1.2: Trabajar con Imágenes Base

**Objetivo:** Descargar y explorar imágenes base de Docker Hub.

**Pasos:**

1. Descargar la imagen oficial de Nginx:
```bash
docker pull nginx:latest
```

2. Listar las imágenes disponibles:
```bash
docker images
```

3. Ver detalles de una imagen específica:
```bash
docker images nginx
```

4. Ver el ID completo de la imagen:
```bash
docker images --no-trunc
```

**Resultado esperado:** Deberías ver la imagen `nginx:latest` en tu lista de imágenes.

---

## 🎯 Módulo 2: Construir y Ejecutar Contenedores

### Ejercicio 2.1: Crear un Dockerfile Básico

**Objetivo:** Crear tu primera imagen personalizada con un Dockerfile.

**Pasos:**

1. Crear un directorio para el ejercicio:
```bash
mkdir ejercicio-nginx
cd ejercicio-nginx
```

2. Crear un archivo `index.html` simple:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Mi Primer Contenedor Docker</title>
</head>
<body>
    <h1>¡Hola desde Docker!</h1>
    <p>Este es mi primer contenedor personalizado.</p>
</body>
</html>
```

3. Crear un `Dockerfile`:
```dockerfile
FROM nginx:latest

# Copiar nuestro archivo HTML al directorio por defecto de Nginx
COPY index.html /usr/share/nginx/html/index.html

# Exponer el puerto 80
EXPOSE 80
```

4. Construir la imagen:
```bash
docker build -t mi-sitio:1.0 .
```

5. Verificar que la imagen se creó:
```bash
docker images mi-sitio
```

**Resultado esperado:** Imagen `mi-sitio:1.0` creada exitosamente.

---

### Ejercicio 2.2: Ejecutar un Contenedor

**Objetivo:** Ejecutar y gestionar contenedores con diferentes opciones.

**Pasos:**

1. Ejecutar el contenedor en modo interactivo (verás los logs):
```bash
docker run -it --rm -p 8080:80 --name mi-web mi-sitio:1.0
```

2. En otra terminal, verificar que el contenedor está corriendo:
```bash
docker ps
```

3. Detener el contenedor (Ctrl+C en la primera terminal o):
```bash
docker stop mi-web
```

4. Ejecutar en segundo plano (detached):
```bash
docker run -d -p 8080:80 --name mi-web-bg mi-sitio:1.0
```

5. Ver los logs del contenedor en segundo plano:
```bash
docker logs mi-web-bg
```

6. Ver logs en tiempo real:
```bash
docker logs -f mi-web-bg
```

7. Detener y eliminar:
```bash
docker stop mi-web-bg
docker rm mi-web-bg
```

**Resultado esperado:** 
- Contenedor ejecutándose y accesible en `http://localhost:8080`
- Logs visibles en la terminal

---

### Ejercicio 2.3: Solucionar Problema de Nginx

**Objetivo:** Aprender a depurar contenedores y configurar Nginx correctamente.

**Problema simulado:** Nginx muestra su página por defecto en lugar de tu HTML.

**Pasos:**

1. Ejecutar un contenedor Nginx:
```bash
docker run -d -p 8081:80 --name nginx-debug nginx:latest
```

2. Entrar al contenedor:
```bash
docker exec -it nginx-debug bash
```

3. Dentro del contenedor, explorar la configuración:
```bash
ls -la /etc/nginx/conf.d/
cat /etc/nginx/conf.d/default.conf
```

4. Verificar el directorio de archivos HTML:
```bash
ls -la /usr/share/nginx/html/
```

5. Salir del contenedor:
```bash
exit
```

6. Limpiar:
```bash
docker stop nginx-debug
docker rm nginx-debug
```

**Resultado esperado:** Entendimiento de la estructura interna de un contenedor Nginx.

---

## 🎯 Módulo 3: Gestión de Imágenes

### Ejercicio 3.1: Filtrar y Etiquetar Imágenes

**Objetivo:** Aprender a gestionar múltiples versiones de imágenes.

**Pasos:**

1. Crear varias versiones de la misma imagen:
```bash
cd ejercicio-nginx
docker build -t mi-sitio:1.0 .
docker build -t mi-sitio:1.1 .
docker build -t mi-sitio:2.0 .
```

2. Listar todas las imágenes:
```bash
docker images
```

3. Filtrar imágenes por referencia:
```bash
docker images --filter=reference='mi-sitio:*'
docker images --filter=reference='*:1.0'
```

4. Filtrar por nombre específico:
```bash
docker images mi-sitio
```

5. Crear un nuevo tag (alias) para una imagen:
```bash
docker image tag mi-sitio:1.0 mi-sitio:latest
docker image tag mi-sitio:1.0 usuario-docker/mi-sitio:1.0
```

6. Verificar los nuevos tags:
```bash
docker images mi-sitio
docker images usuario-docker/mi-sitio
```

**Resultado esperado:** Múltiples versiones y tags de la misma imagen.

---

### Ejercicio 3.2: Eliminar Imágenes

**Objetivo:** Aprender a limpiar imágenes no utilizadas.

**Pasos:**

1. Listar todas las imágenes:
```bash
docker images
```

2. Intentar eliminar una imagen (asegúrate de que no esté en uso):
```bash
docker rmi mi-sitio:1.1
```

3. Eliminar por ID (obtener el ID primero):
```bash
docker images --no-trunc | grep mi-sitio
docker rmi <IMAGE_ID>
```

4. Forzar eliminación (si está en uso):
```bash
docker rmi -f mi-sitio:2.0
```

5. Limpiar imágenes no utilizadas:
```bash
docker image prune
```

**⚠️ Advertencia:** Asegúrate de detener contenedores que usen las imágenes antes de eliminarlas.

**Resultado esperado:** Imágenes eliminadas correctamente.

---

## 🎯 Módulo 4: Gestión de Contenedores

### Ejercicio 4.1: Listar y Monitorear Contenedores

**Objetivo:** Aprender a gestionar el ciclo de vida de contenedores.

**Pasos:**

1. Ejecutar varios contenedores:
```bash
docker run -d -p 8080:80 --name web1 mi-sitio:1.0
docker run -d -p 8081:80 --name web2 mi-sitio:latest
docker run -d -p 8082:80 --name web3 nginx:latest
```

2. Listar contenedores en ejecución:
```bash
docker ps
```

3. Listar todos los contenedores (incluyendo detenidos):
```bash
docker ps -a
```

4. Ver el tamaño de los contenedores:
```bash
docker ps --size
```

5. Monitorear recursos en tiempo real:
```bash
docker stats
```

6. Monitorear un contenedor específico:
```bash
docker stats web1
```

**Resultado esperado:** Vista completa de todos los contenedores y su uso de recursos.

---

### Ejercicio 4.2: Detener, Iniciar y Reiniciar Contenedores

**Objetivo:** Gestionar el estado de los contenedores.

**Pasos:**

1. Detener un contenedor:
```bash
docker stop web1
```

2. Verificar que está detenido:
```bash
docker ps -a
```

3. Iniciar un contenedor detenido:
```bash
docker start web1
```

4. Reiniciar un contenedor:
```bash
docker restart web2
```

5. Pausar un contenedor (sin detenerlo):
```bash
docker pause web3
```

6. Reanudar un contenedor pausado:
```bash
docker unpause web3
```

7. Limpiar contenedores detenidos:
```bash
docker container prune
```

**Resultado esperado:** Control total sobre el estado de los contenedores.

---

## 🎯 Módulo 5: Despliegue de API Flask

### Ejercicio 5.1: Crear una API Flask Simple

**Objetivo:** Containerizar una aplicación Python/Flask.

**Pasos:**

1. Crear un directorio para la API:
```bash
mkdir api-flask
cd api-flask
```

2. Crear `app.py`:
```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "mensaje": "¡Hola desde Flask en Docker!",
        "version": "1.0"
    })

@app.route('/saludo/<nombre>')
def saludo(nombre):
    return jsonify({
        "saludo": f"¡Hola {nombre}!",
        "desde": "Docker"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

3. Crear `requirements.txt`:
```
Flask==2.3.3
```

4. Crear `Dockerfile`:
```dockerfile
FROM python:3.11-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar requirements e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY app.py .

# Exponer el puerto
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
```

5. Construir la imagen:
```bash
docker build -t mi-api:1.0 .
```

6. Ejecutar el contenedor:
```bash
docker run -d -p 5000:5000 --name api-flask mi-api:1.0
```

7. Probar la API:
```bash
curl http://localhost:5000
curl http://localhost:5000/saludo/Camilo
```

**Resultado esperado:** API Flask funcionando en `http://localhost:5000`.

---

## 🎯 Módulo 6: Volúmenes en Docker

### Ejercicio 6.1: Usar Volúmenes para Desarrollo

**Objetivo:** Entender la diferencia entre COPY y volúmenes.

**Pasos:**

1. Crear un directorio con contenido:
```bash
mkdir sitio-desarrollo
cd sitio-desarrollo
echo "<h1>Página Inicial</h1>" > index.html
```

2. Ejecutar un contenedor con volumen montado:
```bash
docker run -d -p 8083:80 \
  -v $(pwd):/usr/share/nginx/html \
  --name web-volumen nginx:latest
```

3. Verificar que funciona:
```bash
curl http://localhost:8083
```

4. Modificar el archivo local:
```bash
echo "<h1>Página Modificada en Caliente</h1>" > index.html
```

5. Verificar el cambio (sin reiniciar el contenedor):
```bash
curl http://localhost:8083
```

6. Crear un Dockerfile con COPY (sin volumen):
```dockerfile
FROM nginx:latest
COPY index.html /usr/share/nginx/html/index.html
```

7. Construir y ejecutar:
```bash
docker build -t sitio-estatico:1.0 .
docker run -d -p 8084:80 --name web-estatico sitio-estatico:1.0
```

8. Modificar el archivo local y reconstruir:
```bash
echo "<h1>Nueva Versión</h1>" > index.html
docker build -t sitio-estatico:1.1 .
docker stop web-estatico
docker rm web-estatico
docker run -d -p 8084:80 --name web-estatico sitio-estatico:1.1
```

**Resultado esperado:** 
- Volumen: cambios en tiempo real sin reconstruir
- COPY: requiere reconstruir la imagen para ver cambios

---

### Ejercicio 6.2: Declarar Volúmenes en Dockerfile

**Objetivo:** Entender la declaración de volúmenes.

**Pasos:**

1. Crear un Dockerfile con VOLUME:
```dockerfile
FROM nginx:latest

# Declarar un volumen
VOLUME ["/usr/share/nginx/html"]

# Exponer puerto
EXPOSE 80
```

2. Construir la imagen:
```bash
docker build -t nginx-con-volumen:1.0 .
```

3. Ejecutar con montaje de volumen:
```bash
docker run -d -p 8085:80 \
  -v $(pwd)/sitio-desarrollo:/usr/share/nginx/html \
  --name web-vol-decl nginx-con-volumen:1.0
```

**Resultado esperado:** Entendimiento de la diferencia entre declarar y montar volúmenes.

---

## 🎯 Módulo 7: Redes en Docker

### Ejercicio 7.1: Explorar Redes por Defecto

**Objetivo:** Entender los tipos de red en Docker.

**Pasos:**

1. Listar redes disponibles:
```bash
docker network ls
```

2. Inspeccionar la red bridge por defecto:
```bash
docker network inspect bridge
```

3. Ejecutar un contenedor y ver su configuración de red:
```bash
docker run -d -p 8086:80 --name web-red nginx:latest
docker inspect web-red | grep -A 20 "NetworkSettings"
```

4. Ver la IP asignada:
```bash
docker inspect web-red | grep IPAddress
```

---

### Ejercicio 7.2: Crear y Usar Redes Personalizadas

**Objetivo:** Crear redes personalizadas para conectar contenedores.

**Pasos:**

1. Crear una red personalizada:
```bash
docker network create mi-red
```

2. Verificar que se creó:
```bash
docker network ls
docker network inspect mi-red
```

3. Ejecutar contenedores en la misma red:
```bash
docker run -d --name web1-red --network mi-red nginx:latest
docker run -d --name web2-red --network mi-red nginx:latest
```

4. Verificar que pueden comunicarse por nombre:
```bash
docker exec -it web1-red ping -c 3 web2-red
```

5. Ejecutar un contenedor en modo host:
```bash
docker run -d --name web-host --network host nginx:latest
```

6. Ejecutar un contenedor sin red:
```bash
docker run -d --name web-none --network none alpine:latest sleep 3600
docker exec -it web-none ping google.com
# Esto fallará porque no tiene red
```

**Resultado esperado:** Entendimiento de los diferentes tipos de red y su uso.

---

### Ejercicio 7.3: Asignar IP Específica

**Objetivo:** Configurar IPs específicas para contenedores.

**Pasos:**

1. Crear una red con subred específica:
```bash
docker network create --subnet=172.20.0.0/16 mi-red-subnet
```

2. Ejecutar contenedor con IP específica:
```bash
docker run -d --name web-ip \
  --network mi-red-subnet \
  --ip 172.20.0.10 \
  nginx:latest
```

3. Verificar la IP:
```bash
docker inspect web-ip | grep IPAddress
```

**Resultado esperado:** Contenedor con IP específica asignada.

---

## 🎯 Módulo 8: Publicar Imágenes en Docker Hub

### Ejercicio 8.1: Publicar una Imagen

**Objetivo:** Compartir imágenes en Docker Hub.

**Pasos:**

1. Iniciar sesión en Docker Hub:
```bash
docker login
```

2. Etiquetar la imagen con tu usuario de Docker Hub:
```bash
docker image tag mi-sitio:1.0 <tu-usuario>/mi-sitio:1.0
docker image tag mi-sitio:1.0 <tu-usuario>/mi-sitio:latest
```

3. Verificar los tags:
```bash
docker images <tu-usuario>/mi-sitio
```

4. Publicar la imagen:
```bash
docker push <tu-usuario>/mi-sitio:1.0
docker push <tu-usuario>/mi-sitio:latest
```

5. Verificar en Docker Hub (navegador):
   - Visita: `https://hub.docker.com/r/<tu-usuario>/mi-sitio`

6. Probar descargar tu propia imagen (desde otra máquina o después de eliminar localmente):
```bash
docker pull <tu-usuario>/mi-sitio:latest
```

**Resultado esperado:** Imagen disponible públicamente en Docker Hub.

---

## 🎯 Módulo 9: Docker Compose - Aplicación Completa

### Ejercicio 9.1: Crear una Aplicación Frontend + Backend

**Objetivo:** Orquestar múltiples contenedores con Docker Compose.

**Estructura del proyecto:**
```
mi-app/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── sitio/
│   │   └── index.html
│   └── Dockerfile
└── docker-compose.yml
```

**Pasos:**

1. Crear la estructura de directorios:
```bash
mkdir -p mi-app/{backend,frontend/sitio}
cd mi-app
```

2. Crear `backend/app.py`:
```python
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/saludo', methods=['GET'])
def saludo():
    nombre = request.args.get('nombre', 'Usuario')
    return jsonify({
        "mensaje": f"¡Hola {nombre}!",
        "servidor": "Backend Flask"
    })

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

3. Crear `backend/requirements.txt`:
```
Flask==2.3.3
flask-cors==4.0.0
```

4. Crear `backend/Dockerfile`:
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
EXPOSE 5000
CMD ["python", "app.py"]
```

5. Crear `frontend/sitio/index.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <title>App con Docker Compose</title>
    <style>
        body { font-family: Arial; padding: 20px; }
        button { padding: 10px 20px; margin: 10px; }
        #resultado { margin-top: 20px; padding: 10px; background: #f0f0f0; }
    </style>
</head>
<body>
    <h1>Frontend + Backend con Docker Compose</h1>
    <input type="text" id="nombre" placeholder="Tu nombre">
    <button onclick="saludar()">Saludar</button>
    <div id="resultado"></div>

    <script>
        async function saludar() {
            const nombre = document.getElementById('nombre').value || 'Usuario';
            try {
                const response = await fetch(`http://localhost:5000/api/saludo?nombre=${nombre}`);
                const data = await response.json();
                document.getElementById('resultado').innerHTML = 
                    `<p><strong>${data.mensaje}</strong></p><p>${data.servidor}</p>`;
            } catch (error) {
                document.getElementById('resultado').innerHTML = 
                    `<p style="color: red;">Error: ${error.message}</p>`;
            }
        }
    </script>
</body>
</html>
```

6. Crear `frontend/Dockerfile`:
```dockerfile
FROM nginx:latest
COPY sitio/ /usr/share/nginx/html/
EXPOSE 80
```

7. Crear `docker-compose.yml`:
```yaml
version: '3.8'

services:
  backend:
    build: ./backend
    container_name: mi-backend
    ports:
      - "5000:5000"
    networks:
      - mi-red-app
    restart: unless-stopped

  frontend:
    build: ./frontend
    container_name: mi-frontend
    ports:
      - "8080:80"
    depends_on:
      - backend
    networks:
      - mi-red-app
    restart: unless-stopped

networks:
  mi-red-app:
    driver: bridge
```

8. Construir y ejecutar con Docker Compose:
```bash
docker-compose up --build -d
```

9. Verificar que ambos contenedores están corriendo:
```bash
docker-compose ps
```

10. Ver los logs:
```bash
docker-compose logs
docker-compose logs backend
docker-compose logs -f frontend
```

11. Probar la aplicación:
   - Frontend: `http://localhost:8080`
   - Backend API: `http://localhost:5000/api/health`

12. Detener los servicios:
```bash
docker-compose down
```

13. Detener y eliminar volúmenes:
```bash
docker-compose down -v
```

**Resultado esperado:** Aplicación completa funcionando con frontend y backend comunicándose.

---

## 🎯 Módulo 10: Comandos Avanzados y Depuración

### Ejercicio 10.1: Inspeccionar Contenedores

**Objetivo:** Aprender a obtener información detallada de contenedores.

**Pasos:**

1. Ejecutar un contenedor:
```bash
docker run -d -p 8087:80 --name web-inspect nginx:latest
```

2. Inspeccionar el contenedor (JSON completo):
```bash
docker inspect web-inspect
```

3. Inspeccionar campos específicos:
```bash
docker inspect web-inspect | grep IPAddress
docker inspect -f '{{.NetworkSettings.IPAddress}}' web-inspect
docker inspect -f '{{.Config.Image}}' web-inspect
```

4. Ver información de red:
```bash
docker inspect web-inspect | grep -A 10 "Networks"
```

**Resultado esperado:** Capacidad de extraer información específica de contenedores.

---

### Ejercicio 10.2: Exportar e Importar Imágenes

**Objetivo:** Guardar y compartir imágenes sin Docker Hub.

**Pasos:**

1. Exportar una imagen a archivo tar:
```bash
docker save mi-sitio:1.0 > mi-sitio-1.0.tar
```

2. Verificar que se creó el archivo:
```bash
ls -lh mi-sitio-1.0.tar
```

3. Eliminar la imagen local:
```bash
docker rmi mi-sitio:1.0
```

4. Importar la imagen desde el archivo:
```bash
docker load < mi-sitio-1.0.tar
```

5. Verificar que se restauró:
```bash
docker images mi-sitio
```

**Resultado esperado:** Imagen exportada e importada correctamente.

---

## 🧹 Limpieza Final

### Ejercicio de Limpieza

**Objetivo:** Limpiar todos los recursos creados durante el taller.

**Pasos:**

1. Detener todos los contenedores:
```bash
docker stop $(docker ps -aq)
```

2. Eliminar todos los contenedores:
```bash
docker rm $(docker ps -aq)
```

3. Eliminar imágenes no utilizadas:
```bash
docker image prune -a
```

4. Eliminar redes no utilizadas:
```bash
docker network prune
```

5. Eliminar volúmenes no utilizados:
```bash
docker volume prune
```

6. Limpieza completa (cuidado, elimina todo):
```bash
docker system prune -a --volumes
```

---

## 📝 Checklist de Evaluación

Marca cada ejercicio cuando lo completes:

- [ ] Módulo 1: Primeros Pasos
- [ ] Módulo 2: Construir y Ejecutar Contenedores
- [ ] Módulo 3: Gestión de Imágenes
- [ ] Módulo 4: Gestión de Contenedores
- [ ] Módulo 5: Despliegue de API Flask
- [ ] Módulo 6: Volúmenes en Docker
- [ ] Módulo 7: Redes en Docker
- [ ] Módulo 8: Publicar Imágenes
- [ ] Módulo 9: Docker Compose
- [ ] Módulo 10: Comandos Avanzados

---

## 🎓 Desafíos Adicionales

### Desafío 1: Multi-stage Build
Crea un Dockerfile que use multi-stage build para optimizar el tamaño de una imagen de Node.js.

### Desafío 2: Healthcheck
Agrega un healthcheck a tu API Flask y verifica su estado con `docker ps`.

### Desafío 3: Variables de Entorno
Crea un contenedor que use variables de entorno para configuración (usando `-e` o archivo `.env` con Docker Compose).

### Desafío 4: Base de Datos
Agrega un servicio de PostgreSQL a tu `docker-compose.yml` y conecta el backend a la base de datos.

---

## 📚 Recursos Adicionales

- Documentación oficial: https://docs.docker.com/
- Docker Hub: https://hub.docker.com/
- Docker Compose: https://docs.docker.com/compose/

---

**¡Felicitaciones por completar el taller!** 🎉

Ahora tienes una base sólida en Docker. Continúa practicando y experimentando con diferentes escenarios.

