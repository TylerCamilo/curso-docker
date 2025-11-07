FROM python:3.12-alpine3.17 
# imagen que usa

# Establece la carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de requerimientos al contenedor
COPY requirements.txt requirements.txt

# Instala las dependencias de Python definidas en requirements.txt
RUN pip install -r requirements.txt

# Copia el resto de los archivos del proyecto al contenedor
COPY . .

# Establece el comando para iniciar la aplicación Flask, accesible desde cualquier IP
CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0" ]