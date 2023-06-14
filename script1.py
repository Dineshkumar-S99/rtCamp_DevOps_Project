#Check if `docker` and `docker-compose` is installed on the system. If not present, install the missing packages.

import os
import subprocess

'''
os module - help us to interact with the OS of the system and perform OS operations like listing directories, manipulating paths, and executing system commands.

subprocess module: Allows the execution of system commands from within a Python script and provides facilities for running subprocesses, capturing their output, and managing input/output streams.
Why we use it: We use the subprocess module to interact with external programs, execute system commands, and manage subprocesses within our Python script. 
It enables us to integrate with the underlying system and perform tasks like running Docker commands, installing packages, or managing system processes.'''


#function to check if the docker and docker compose are prsent or not

#without using subprocess
def check_docker_docker_compose():
    #check if docker is installed or not
    if os.system("docker --version") == 0:
        print("Docker is already installed on the system")
    else:
        print("Docker is not installed on the system")
        #install docker
        os.system("curl -fsSL https://get.docker.com -o get-docker.sh")
        os.system("sh get-docker.sh")
        print("Docker is installed on the system")
    #check if docker-compose is installed or not
    if os.system("docker-compose --version") == 0:
        print("Docker-compose is already installed on the system")
    else:
        print("Docker-compose is not installed on the system")
        #install docker-compose
        os.system("sudo apt install docker-compose")
        print("Docker-compose is installed on the system")

'''
os.system("curl -fsSL https://get.docker.com -o get-docker.sh")
os.system("sh get-docker.sh")

here -fsSL stands for 
  -f = fail silently, 
  -s = silent mode, 
  -S = show error messages, 
  -L = follow redirects

  -o stands for output
  sh stands for shell

here get-docker.sh is the file which we are downloading from the url https://get.docker.com and saving it as get-docker.sh and then we are running the file get-docker.sh'''