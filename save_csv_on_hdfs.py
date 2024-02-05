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
from hdfs.ext.kerberos import KerberosClient
import os

def save_to_hdfs(data, hdfs_path):
    csv_data = data.to_csv(index=False)
    
    try:
        hdfs_client = InsecureClient('http://master-node:9870', user='hanif')
        print("hdf_client: ", hdfs_client)
        print('Connected to HDFS')
    except Exception as e:
        print('Failed to connect to HDFS')
        print(e)
        return

    try:
        print('Writing data to HDFS before with')
        with hdfs_client.write(hdfs_path, encoding='utf-8') as hdfs_file:
            print('Writing data to HDFS')
            hdfs_file.write(csv_data)
            print('Data written to HDFS')

    except Exception as e:
        print('Failed to write data to HDFS')
        print(e)



data = {'match_name': ['Match1', 'Match2', 'Match3'],
        'venue': ['Venue1', 'Venue2', 'Venue3'],
        'result': ['Win', 'Loss', 'Draw']}

cricbuzz_data = pd.DataFrame(data)


hdfs_path = '/home/hanif/CricDataEngine/data/cricbuzz_data.csv' 

# check if the file exists, print the file path, if not print file not found
if os.path.exists(hdfs_path):
    print(f'File path: {hdfs_path}')
else:
    print('File not found')

save_to_hdfs(cricbuzz_data, hdfs_path)

