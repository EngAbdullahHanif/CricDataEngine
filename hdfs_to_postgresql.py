import pandas as pd
from sqlalchemy import create_engine
from pydoop import hdfs


def hdfs_to_postgres(hdfs_path, table_name, postgres_conn_str):
    with hdfs.open(hdfs_path, 'rb') as hdfs_file:
        csv_data = hdfs_file.read().decode()
    
    data = pd.read_csv(pd.compat.StringIO(csv_data))
    
    engine = create_engine(postgres_conn_str)
    
    data.to_sql(table_name, con=engine, if_exists='replace', index=False)

table_name = 'cricbuzz_data'
postgres_conn_str = 'postgresql://hanif:test123@localhost:5432/cricdataengine' 
hdfs_to_postgres(hdfs_path, table_name, postgres_conn_str)