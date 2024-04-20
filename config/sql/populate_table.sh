#!/bin/bash

HOST="localhost"
DATABASE="your_database_name"
USER="jimenarioja"

INSERT_SQL="INSERT INTO table_test (first_name, last_name) VALUES
    ('Jimena', 'Rioja');"

psql -h "$HOST" -d "$DATABASE" -U "$USER" -c "$INSERT_SQL"
