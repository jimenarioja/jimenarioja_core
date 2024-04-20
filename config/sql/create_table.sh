#!/bin/bash

HOST="localhost"
DATABASE="your_database_name"
USER="jimenarioja"

CREATE_TABLE_SQL="CREATE TABLE IF NOT EXISTS table_test (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INT
);"


psql -h "$HOST" -d "$DATABASE" -U "$USER" -c "$CREATE_TABLE_SQL"
