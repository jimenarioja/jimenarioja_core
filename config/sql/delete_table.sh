#!/bin/bash

HOST="localhost"
DATABASE="your_database_name"
USER="jimenarioja"

DELETE_TABLE_SQL="DROP TABLE IF EXISTS your_table_name;"

psql -h "$HOST" -d "$DATABASE" -U "$USER" -c "$DELETE_TABLE_SQL"
