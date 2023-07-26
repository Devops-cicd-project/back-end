DROP DATABASE IF EXISTS postgres_db;
CREATE DATABASE postgres_db;
CREATE USER postgres WITH PASSWORD 'devops19psql89';
ALTER ROLE postgres SET client_encoding TO 'utf8';
ALTER ROLE postgres SET default_transaction_isolation TO 'read committed';
ALTER ROLE postgres SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE postgres_db TO postgres;