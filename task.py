from utils import epoch_to_datetime, execute_sql_script_1, execute_sql_script_3
import pandas as pd
import os


def execute_sql_script_2(script_paths, connection_params):
    for script_path in script_paths:
        execute_sql_script_1(script_path, connection_params)



def read_and_process_raw_data():
    try:
        users_data = pd.read_csv('raw_data/user_table.csv')
        friends_data = pd.read_csv('raw_data/friends_table.csv')
        posts_data = pd.read_csv('raw_data/posts_table.csv')
        reactions_data = pd.read_csv('raw_data/reactions_table.csv')

        # epoch_to_datetime
        users_data['Subscription Date'] = users_data['Subscription Date'].apply(epoch_to_datetime)
        posts_data['Post Date'] = posts_data['Post Date'].apply(epoch_to_datetime)
        reactions_data['Reaction Date'] = reactions_data['Reaction Date'].apply(epoch_to_datetime)

        friends_data['sorted_pair'] = friends_data[['Friend 1', 'Friend 2']].apply(sorted, axis=1)
        friends_data = friends_data.drop_duplicates(subset='sorted_pair')
        friends_data = friends_data.drop(columns=['sorted_pair'])

        return users_data, friends_data, posts_data, reactions_data

    except FileNotFoundError as e:
        print("File not found:", e)
    except pd.errors.EmptyDataError as e:
        print("Empty data in CSV file:", e)
    except pd.errors.ParserError as e:
        print("Error parsing CSV file:", e)
    except Exception as e:
        print("An error occurred:", e)


def ingest_data_into_tables(connection_params, insert_script_paths):
    data = read_and_process_raw_data()
    table_order = {'users': 0, 'friends': 1, 'posts': 2, 'reactions': 3}

    for script_path in insert_script_paths:
        with open(script_path, 'r') as script_file:
            sql_script = script_file.read()

        table_name = os.path.basename(script_path).split('_')[2].split('.')[0]
        table_index = table_order[table_name]
        table_data = data[table_index]


        execute_sql_script_3(connection_params,sql_script,table_data)










