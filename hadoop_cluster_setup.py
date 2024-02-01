import os
import subprocess

# Configuration
master_node = "your_master_node"  # Replace with your master node's IP or hostname
worker_nodes = ["worker_node1", "worker_node2"]  # Replace with your worker nodes' IPs or hostnames
hadoop_home = "/path/to/hadoop"  # Replace with the path to your Hadoop installation
java_home = "/path/to/java"  # Replace with the path to your Java installation

def execute_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return process.returncode, output.decode("utf-8"), error.decode("utf-8")

def configure_master_node():
    # Update Hadoop configurations on the master node
    command = f"{hadoop_home}/bin/hadoop namenode -format"
    _, output, error = execute_command(command)
    print(output)
    print(error)

def start_hadoop_services():
    # Start Hadoop services on the master node
    command = f"{hadoop_home}/sbin/start-dfs.sh"
    _, output, error = execute_command(command)
    print(output)
    print(error)

def configure_worker_nodes():
    # Update Hadoop configurations on the worker nodes
    for node in worker_nodes:
        command = f"scp -r {hadoop_home}/etc/hadoop {node}:{hadoop_home}/etc/"
        _, output, error = execute_command(command)
        print(output)
        print(error)

def main():
    # Configure the master node
    configure_master_node()

    # Start Hadoop services on the master node
    start_hadoop_services()

    # Configure the worker nodes
    configure_worker_nodes()

if __name__ == "__main__":
    main()
