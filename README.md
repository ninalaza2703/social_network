# socail_network

Basic ETL using PYTHON and SQL

## Prerequisites

- Python (version 3.11.4)
- PostgreSQL
- Pip (Python package manager)

## Usage

```python
Preparation and Usage

# db_config.cfg
necessary database credentials for logging into the database

# 'raw_data' folder
Place the CSV data files in the 'raw_data' folder

# 'queries' folder
Place the SQL scripts in the 'queries' folder
```
## Project Structure and Description
- 'raw_data' - contains the raw CSV data files.
- 'queries' - contains SQL scripts for creating the database, tables and inserting data.
- 'config.py' - stores project configurations.
- 'utils.py' - 
Utility functions for processing data and working with SQL scripts. It contains the functions: epoch_to_datetime, which converts dates from epoch to datetime, get_query_files which returns the paths to the SQL that create and inserts into the tables, execute_sql_script_1 which executes one SQL scrip and  execute_sql_script_3, which helps when inserting.
- 'task.py' - 
Tasks for creating tables, processing data, and ingesting data. The file contains the functions: execute_sql_script_2, which uses execute_sql_script_1 and executes all SQL scripts that create a database or the tables, read_and_process_raw_data, which reads the data and processes it(using epoch_to_datetime function, also slightly modifies the 'friends_table') and the ingest_data_into_tables function.
- 'flow.py' - Executes tasks in the desired order.
