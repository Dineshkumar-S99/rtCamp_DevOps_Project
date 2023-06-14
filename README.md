# rtCamp_DevOps_Project
This repo will contain the scripts and other md for the project given by rtCamp

# Task

To create a command-line script, preferably in Bash, PHP, Node, or Python to perform the following tasks:

- tasks and guidelines
    1. Check if `docker` and `docker-compose` is installed on the system. If not present, install the missing packages.
    2. The script should be able to create a WordPress site using the latest WordPress Version. Please provide a way for the user to provide the site name as a command-line argument.
    3. It must be a LEMP stack running inside containers (Docker) and a docker-compose file is a must.
    4. Create a `/etc/hosts` entry for *example.com* pointing to localhost. Here we are assuming the user has provided *example.com* as the site name.
    5. Prompt the user to open *example.com* in a browser if all goes well and the site is up and healthy.
    6. Add another subcommand to enable/disable the site (stopping/starting the containers)
    7. Add one more subcommand to delete the site (deleting containers and local files).
    
    ### Submission Guidelines
    
    - **CLIG Guidelines ➞** Please follow [Command Line Interface Guidelines](https://clig.dev/).
    - **Source Code Hosting** ➞ You must use GitHub *(recommended)* or GitLab for source code hosting.
    - **Readme.md** ➞ Your must have a very well written readme describing how to install your script, how to run different command & sub-commands in markdown format.

## pre-requisite

1. preferable have a Linux based OS.

and that’s it we use terminal to execute the tasks and most Linux based OS comes with Python, so we are ready to write and execute the code.

### Step 1: check if docker and docker compose files are present.

first of all, to check if the dependencies are present or not, we have to interact with the current OS we are running on, so we import the required modules to interact with OS and other modules to interact using arguments in the terminal. 

```python
import os
import argparse
import webbrowser
```

> **os** module - help us to interact with the OS of the system and perform OS operations like listing directories, manipulating paths, and executing system commands.
> 

> **argparse** module - helps us to this will help us to create a command line interface for our script. so that we can run our script from the command line and also can use arguments to perform different actions in our script.
> 

> **webbrowser** module - helps us to view our deployed website from the web browser by opening it automatically.
> 

```python
class Check_Docker_and_DockerCompose:
    def __init__(self):
        self.docker="docker"
        self.docker_compose="docker-compose"

    def ispresent(self):
        if os.system("docker --version") == 0:
            print("Docker is already installed on the system")
        else:
            print("Docker is not installed on the system")
            #install docker
            os.system("curl -fsSL https://get.docker.com -o get-docker.sh")
            os.system("sh get-docker.sh")
            print("Docker is installed on the system")
            os.remove("get-docker.sh")
    #check if docker-compose is installed or not
        if os.system("docker-compose --version") == 0:
            print("Docker-compose is already installed on the system")
        else:
            print("Docker-compose is not installed on the system")
            #install docker-compose
            os.system("sudo apt install docker-compose")
            print("Docker-compose is installed on the system")
```