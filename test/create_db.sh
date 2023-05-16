#!/bin/bash

# Variables de configuración
DB_NAME="db_test"
DB_USER="user_test"
DB_PASSWORD="password"

# Comando para crear la base de datos
psql -c "CREATE DATABASE $DB_NAME;" -U postgres

# Comando para crear el usuario y asignarle privilegios en la base de datos
psql -c "CREATE USER $DB_USER WITH ENCRYPTED PASSWORD '$DB_PASSWORD';" -U postgres
psql -c "GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;" -U postgres