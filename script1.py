#Check if `docker` and `docker-compose` is installed on the system. If not present, install the missing packages.

import os

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


#Create a WordPress site 
def create_wordpress_site():
    #checking if docker is installed or not
    check_docker_docker_compose()
    #creating a directory named wordpress
    os.system("mkdir wordpress")
    #changing directory to wordpress
    os.chdir("wordpress")
    #creating a file named docker-compose.yml
    os.system("touch docker-compose.yml")
    #open the file docker-compose.yml
    f = open("docker-compose.yml", "w")
    #code for the file docker-compose.yml
    f.write("version: '3.3'\n")
    f.write("services:\n")
    f.write("  db:\n")
    f.write("    image: mysql:5.7\n")
    f.write("    volumes:\n")
    f.write("      - db_data:/var/lib/mysql\n")
    f.write("    restart: always\n")
    f.write("    environment:\n")
    f.write("      MYSQL_ROOT_PASSWORD: somewordpress\n")
    f.write("      MYSQL_DATABASE: wordpress\n")
    f.write("      MYSQL_USER: wordpress\n")
    f.write("      MYSQL_PASSWORD: wordpress\n")
    f.write("  wordpress:\n")
    f.write("    depends_on:\n")
    f.write("      - db\n")
    f.write("    image: wordpress:latest\n")
    f.write("    ports:\n")
    f.write("      - '8000:80'\n")
    f.write("    restart: always\n")
    f.write("    environment:\n")
    f.write("      WORDPRESS_DB_HOST: db:3306\n")
    f.write("      WORDPRESS_DB_USER: wordpress\n")
    f.write("      WORDPRESS_DB_PASSWORD: wordpress\n")
    f.write("volumes:\n")
    f.write("  db_data: {}\n")
    #close the file docker-compose.yml
    f.close()
    #creating a file named .env to contain all the environments
    os.system("touch .env")
    #open the file .env
    f = open(".env", "w")
    #write the following code in the file .env
    f.write("MYSQL_ROOT_PASSWORD=somewordpress\n")
    f.write("MYSQL_DATABASE=wordpress\n")
    f.write("MYSQL_USER=wordpress\n")
    f.write("MYSQL_PASSWORD=wordpress\n")
    #close the file .env
    f.close()

    os.system("sudo docker-compose up -d")

    #ask for site name and add it to the /etc/hosts 
    site_name=input()
    with open("/etc/hosts","a") as h:
        h.write("\n127.0.0.1 {}".format(site_name))
    print("please open https://{} in your browser to access the site".format(site_name))


def enable():
    check_docker_docker_compose()
    create_wordpress_site()

#function to enable and enable the site
def enable():
    os.system("sudo docker-compose up -d")

def disable():
    os.system("sudo docker-compose down")

def delete():
    os.system("sudo docker-compose down")
    os.system("sudo sed -i /{}/d /etc/hosts".format(site_name))#to get we have to make them to global value

