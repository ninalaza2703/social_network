import datetime
import os
from psycopg2 import connect, extensions

def epoch_to_datetime(epoch_time):
    return datetime.datetime.fromtimestamp(epoch_time)

def get_query_files(directory_path, create_prefix='create_table_', insert_prefix='insert_into_', extension='.sql'):
    create_query_files = []
    insert_query_files = []

    for file in os.listdir(directory_path):
        if file.startswith(create_prefix) and file.endswith(extension):
            create_query_files.append(os.path.join(directory_path, file))
        elif file.startswith(insert_prefix) and file.endswith(extension):
            insert_query_files.append(os.path.join(directory_path, file))


    return create_query_files, insert_query_files


def execute_sql_script_1(script_path, connection_params):
    connection = connect(**connection_params)
    connection.set_isolation_level(extensions.ISOLATION_LEVEL_AUTOCOMMIT)

    with connection.cursor() as cursor:
        with open(script_path, 'r') as script_file:
            sql_script = script_file.read()
            cursor.execute(sql_script)

    connection.close()

def execute_sql_script_3(connection_params,sql_script,table_data):
    from psycopg2 import connect, extensions
    connection = connect(**connection_params)
    connection.set_isolation_level(extensions.ISOLATION_LEVEL_AUTOCOMMIT)

    with connection.cursor() as cursor:
        for row in table_data.values:
            cursor.execute(sql_script, row)
    connection.close()

