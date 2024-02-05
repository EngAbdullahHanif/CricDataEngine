import subprocess

def run_command(command):
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return e.stderr.strip()

def check_hadoop_status():
    namenode_status = run_command(['hdfs', 'haadmin', '-getServiceState', 'nn1'])
    print(f'Hadoop Namenode Status: {namenode_status}')

    datanode_status = run_command(['hdfs', 'dfsadmin', '-report'])
    print(f'Hadoop Datanode Status: {datanode_status}')

if __name__ == "__main__":
    check_hadoop_status()