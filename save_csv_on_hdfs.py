# import pandas as pd
# from pydoop import hdfs

# def save_to_hdfs(data, hdfs_path):
#     csv_data = data.to_csv(index=False)
    
#     with hdfs.open(hdfs_path, 'wb') as hdfs_file:
#         hdfs_file.write(csv_data.encode())

# cricbuzz_data = pd.DataFrame(...)  
# hdfs_path = '/home/hanif/CricDataEngine/Data/cricbuzz_data.csv'  
# save_to_hdfs(cricbuzz_data, hdfs_path)


import pandas as pd
from hdfs import InsecureClient

def save_to_hdfs(data, hdfs_path):
    csv_data = data.to_csv(index=False)
    
    # Connect to HDFS
    hdfs_client = InsecureClient('http://<HDFS-NAMENODE-HOST>:<HDFS-NAMENODE-PORT>', user='<HDFS-USERNAME>')

    # Write CSV data to HDFS
    with hdfs_client.write(hdfs_path, encoding='utf-8') as hdfs_file:
        hdfs_file.write(csv_data)

data = {'match_name': ['Match1', 'Match2', 'Match3'],
        'venue': ['Venue1', 'Venue2', 'Venue3'],
        'result': ['Win', 'Loss', 'Draw']}

cricbuzz_data = pd.DataFrame(data)

hdfs_path = '/user/hanif/CricDataEngine/Data/cricbuzz_data.csv'  # Example HDFS path, adjust as needed
save_to_hdfs(cricbuzz_data, hdfs_path)
