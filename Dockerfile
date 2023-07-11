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

# Configurar la contraseña del usuario root de MySQL
RUN service mysql start && \
    mysql -e "ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'ThunderGer'; FLUSH PRIVILEGES;" && \
    service mysql stop

# Configurar las variables de entorno para la conexión a la base de datos (si es necesario)
ENV DB_HOST=localhost
ENV DB_USER=root
ENV DB_PASSWORD=ThunderGer
ENV DB_NAME=APIGNews

# Copiar el archivo .sql al contenedor
COPY database.sql /docker-entrypoint-initdb.d/database.sql

# Exponer el puerto 5000
EXPOSE 5000

# Iniciar el servicio de MySQL
RUN service mysql start && mysql < /docker-entrypoint-initdb.d/database.sql

# Ejecutar el script index.py
CMD service mysql start && mysql < /docker-entrypoint-initdb.d/database.sql && python3 index.py
