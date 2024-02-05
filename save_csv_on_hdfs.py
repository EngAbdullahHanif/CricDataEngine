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
    
    # Connect to HDFS
    # hdfs_client = InsecureClient('http://<HDFS-NAMENODE-HOST>:<HDFS-NAMENODE-PORT>', user='<HDFS-USERNAME>')
    # hdfs_client = InsecureClient('http://100.80.154.9:9000', user='hanif')
    print('Connecting to HDFS')
    try:
        hdfs_client = InsecureClient('http://master-node:9870', user='hanif')
        print('Connected to HDFS')
    except Exception as e:
        print('Failed to connect to HDFS')
        print(e)
        return

    try:
        with hdfs_client.write(hdfs_path, encoding='utf-8') as hdfs_file:
            hdfs_file.write(csv_data)
        print('Data written to HDFS')
    except Exception as e:
        print('Failed to write data to HDFS')
        print(e)



data = {'match_name': ['Match1', 'Match2', 'Match3'],
        'venue': ['Venue1', 'Venue2', 'Venue3'],
        'result': ['Win', 'Loss', 'Draw']}

print('Creating DataFrame')
cricbuzz_data = pd.DataFrame(data)
print('DataFrame created')

print('Saving to HDFS')
# hdfs_path = '/home/notebook/CricDataEngine/Data/cricbuzz_data.csv' 
hdfs_path = '/home/hanif/CricDataEngine/data/cricbuzz_data.csv' 
# find this file and print if found using import os; os.listdir('/home/hanif/CricDataEngine/data')
print(os.listdir('/home/hanif/CricDataEngine/data'))

save_to_hdfs(cricbuzz_data, hdfs_path)
print('Data saved to HDFS')
