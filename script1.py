#Check if `docker` and `docker-compose` is installed on the system. If not present, install the missing packages.

import os
import argparse
import webbrowser

'''
os module - help us to interact with the OS of the system and perform OS operations like listing directories, manipulating paths, and executing system commands.

subprocess module: Allows the execution of system commands from within a Python script and provides facilities for running subprocesses, capturing their output, and managing input/output streams.
Why we use it: We use the subprocess module to interact with external programs, execute system commands, and manage subprocesses within our Python script. 
It enables us to integrate with the underlying system and perform tasks like running Docker commands, installing packages, or managing system processes.'''



#Create class to check docker and docker present or not
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


class create_WordPress_site:
    def __init__(self,site_name):
        self.siteName = site_name
        os.system("mkdir wordpress")
        os.chdir("wordpress")
        os.system("touch docker-compose.yml")
        f = open("docker-compose.yml", "w")
    
        f.write("version: '3'\n")
        f.write("services:\n")
        f.write("  db:\n")
        f.write("    image: mysql:5.7\n")
        f.write("    restart: always\n")
        f.write("    environment:\n")
        f.write("      MYSQL_RANDOM_ROOT_PASSWORD: 1\n")
        f.write("      MYSQL_DATABASE: wordpress\n")
        f.write("      MYSQL_USER: wordpress\n")
        f.write("      MYSQL_PASSWORD: wordpress\n")
        f.write("    volumes:\n")
        f.write("      - db_data:/var/lib/mysql\n")
        f.write("  wordpress:\n")
        f.write("    depends_on:\n")
        f.write("      - db\n")
        f.write("    image: wordpress:latest\n")
        f.write("    restart: always\n")
        f.write("    ports:\n")
        f.write("      - '8080:80'\n")
        f.write("    environment:\n")
        f.write("      WORDPRESS_DB_HOST: db:3306\n")
        f.write("      WORDPRESS_DB_USER: wordpress\n")
        f.write("      WORDPRESS_DB_PASSWORD: wordpress\n")
        f.write("      WORDPRESS_DB_NAME: wordpress\n")
        f.write("    volumes:\n")
        f.write("      - wordpress:/var/www/html\n")
        f.write("volumes:\n")
        f.write("  db_data:\n")
        f.write("  wordpress:\n")
    #close the file docker-compose.yml
        f.close()
    #create a file named .env
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

    def create(self):
        os.system("sudo docker-compose up -d")
        with open("/etc/hosts","a") as f:
            f.write("\n127.0.0.1 {}".format(self.siteName))

        print("WordPress site is now running, access it with http://{}".format(self.siteName))
        webbrowser.open("https://{}/8000")

class EnableDisable_or_DeleteSite:
    def __init__(self,site_name):
        self.siteName=site_name

    def enable(self):
        os.system("sudo docker-compose up -d")

    def disable(self):
        os.system("sudo docker-compose down")

    def delete(self):
        os.system("sudo docker-compose down")
        os.system("sudo rm -rf {}".format(self.siteName))
        os.system("sudo sed -i /{}/d /etc/hosts".format(self.siteName))

def main():
    parser = argparse.ArgumentParser(description="Create a WordPress site using the latest WordPress Version")
    parser.add_argument("siteName", help="Site name")
    parser.add_argument("-c", "--create", help="Create a WordPress site using the latest WordPress Version", action="store_true")
    parser.add_argument("-e", "--enable", help="Enable the site (start the containers)", action="store_true")
    parser.add_argument("-d", "--disable", help="Disable the site (stop the containers)", action="store_true")
    parser.add_argument("-D", "--delete", help="Delete the site (delete the containers and local files)", action="store_true")
    args = parser.parse_args()

    if args.create:
        Check_Docker_and_DockerCompose().ispresent()
        create_WordPress_site(args.siteName).create()
    elif args.enable:
        EnableDisable_or_DeleteSite(args.siteName).enable()
    elif args.disable:
        EnableDisable_or_DeleteSite(args.siteName).disable()
    elif args.delete:
        EnableDisable_or_DeleteSite(args.siteName).delete()
    else:
        print("Please provide a subcommand, use -h or --help for help")

if __name__=="__main__":
    main()
