import os

# Configure Postgres database based on connection string of the libpq Keyword/Value form
# https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING
conn_str = os.environ['POSTGRESQLCONNSTR_AZURE_POSTGRESQL_CONNECTIONSTRING ']
conn_str_params = {pair.split('=')[0]: pair.split('=')[1] for pair in conn_str.split(' ')}

DATABASE_URI = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    dbuser=conn_str_params['User Id'],
    dbpass=conn_str_params['Password'],
    dbhost=conn_str_params['Server']+':'+conn_str_params['Port'],
    dbname=conn_str_params['Database']
)