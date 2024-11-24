FROM postgres:1.17@sha256:163763c8afd28cae69035ce84b12d8180179559c747c0701b3cad17818a0dbc5

COPY dockerfile/postgres/db/init.sql /docker-entrypoint-initdb.d/
# TODO COPY migrate files