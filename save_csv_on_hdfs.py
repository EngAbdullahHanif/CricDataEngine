import pandas as pd
from pydoop import hdfs

def save_to_hdfs(data, hdfs_path):
    csv_data = data.to_csv(index=False)
    
    with hdfs.open(hdfs_path, 'wb') as hdfs_file:
        hdfs_file.write(csv_data.encode())

cricbuzz_data = pd.DataFrame(...)  
hdfs_path = '/user/your_username/cricbuzz_data.csv'  
save_to_hdfs(cricbuzz_data, hdfs_path)
