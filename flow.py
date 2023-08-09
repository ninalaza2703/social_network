from task import execute_sql_script_2, ingest_data_into_tables
from utils import get_query_files, execute_sql_script_1
import configparser
import config
import os
import numpy
from psycopg2.extensions import register_adapter, AsIs
def addapt_numpy_float64(numpy_float64):
    return AsIs(numpy_float64)
def addapt_numpy_int64(numpy_int64):
    return AsIs(numpy_int64)
register_adapter(numpy.float64, addapt_numpy_float64)
register_adapter(numpy.int64, addapt_numpy_int64)

'''getting sql script paths'''
query_directory = config.queries_folder_path
create_script_paths, insert_script_paths = get_query_files(query_directory)
'''to create users_table the firs'''
create_script_paths.reverse()
insert_script_paths.reverse()
database_path = os.path.abspath(os.path.join('queries', 'database_creation.sql'))
no_db = os.path.abspath(os.path.join('queries', 'drop_db.sql'))

'''creating db_params'''
cnfg = configparser.ConfigParser()
cnfg.read('db_config.cfg')

database_host = cnfg.get('database', 'host')
database_name = cnfg.get('database', 'database')
database_user = cnfg.get('database', 'user')
database_password = cnfg.get('database', 'password')
database_port = cnfg.getint('database', 'port')

db_params = {
    'dbname': database_name,
    'user': database_user,
    'password': database_password,
    'host': database_host,
    'port': database_port
}

'''dropping db if exists'''
execute_sql_script_1(no_db,db_params)

'''create the database'''
execute_sql_script_1(database_path,db_params)

'''Create empty tables'''
execute_sql_script_2(create_script_paths, db_params)

'''ingest data into tables'''
ingest_data_into_tables(db_params, insert_script_paths)

