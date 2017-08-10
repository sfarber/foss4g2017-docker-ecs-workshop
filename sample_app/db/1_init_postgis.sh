psql -v ON_ERROR_STOP=1 -U "$POSTGRES_USER" template1 <<-EOSQL

create extension postgis;

EOSQL
