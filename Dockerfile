# Utilizar una imagen base de Ubuntu
FROM ubuntu:latest

# Actualizar los paquetes y herramientas del sistema
RUN apt-get update && apt-get upgrade -y && apt-get autoremove -y

# Instalar Python y herramientas relacionadas
RUN apt-get install -y python3 python3-pip python3-dev build-essential

# Instalar el cliente de MySQL
RUN apt-get install -y mysql-client

# Instalar el servidor de MySQL
RUN apt-get install -y mysql-server

# Copiar los archivos de tu proyecto al contenedor
COPY . /app

# Establecer el directorio de trabajo
WORKDIR /app

# Instalar las dependencias del proyecto (si tienes un archivo requirements.txt)
RUN pip3 install -r requirements.txt

COPY database.sql /app/database.sql
RUN service mysql start && mysql -u root < /app/database.sql

# Exponer el puerto 5000
# EXPOSE 500

# Ejecutar el script index.py
CMD python3 index.py
