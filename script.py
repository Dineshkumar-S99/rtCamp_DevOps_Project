#!/usr/bin/env python3

import os
import argparse
import webbrowser
import subprocess

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


class create_WordPress_site:
    def __init__(self,site_name):
        self.siteName = site_name
        os.system("mkdir wordpress")
        os.system("cp -r s1.py wordpress/")
        os.chdir("wordpress")
        os.system("touch docker-compose.yml")
        f = open("docker-compose.yml", "w")
    #compose file
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
        subprocess.run(["docker-compose", "up", "-d"])
        with open("/etc/hosts","a") as f:
            f.write("\n127.0.0.1 {}".format(self.siteName))

        print("WordPress site is now running, access it with http://{}:8080".format(self.siteName))
        webbrowser.open("https://{}/8080")

class EnableDisable_or_DeleteSite:
    def __init__(self,site_name):
        self.siteName=site_name

    def enable(self):
        os.chdir("wordpress")
        subprocess.run(["docker-compose", "start"])
        print("WordPress site is now running, access it with http://{}:8080".format(self.siteName))

    def disable(self):
        os.chdir("wordpress")
        subprocess.run(["docker-compose", "stop"])

    def delete(self):
        os.chdir("wordpress")
        subprocess.run(["docker-compose", "down"])
        #os.system("sudo rm -rf {}".format(self.siteName))
        #os.system("cd ..")
        os.system("sudo rm -rf wordpress/")
        os.system("sudo sed -i /{}/d /etc/hosts".format(self.siteName))


def main():
    parser = argparse.ArgumentParser(description='Create, enable, disable, or delete a WordPress site using Docker')
    subparsers = parser.add_subparsers(dest='command')

    # Command: create
    create_parser = subparsers.add_parser('create', help='Create a new WordPress site')
    create_parser.add_argument('site_name', help='Name of the site')
    
    # Command: enable
    enable_parser = subparsers.add_parser('enable', help='Enable a WordPress site')
    enable_parser.add_argument('site_name', help='Name of the site')
    
    # Command: disable
    disable_parser = subparsers.add_parser('disable', help='Disable a WordPress site')
    disable_parser.add_argument('site_name', help='Name of the site')
    
    # Command: delete
    delete_parser = subparsers.add_parser('delete', help='Delete an existing WordPress site')
    delete_parser.add_argument('site_name', help='Name of the site')

    args = parser.parse_args()
    if args.command == 'create':
      Check_Docker_and_DockerCompose().ispresent()
      create_WordPress_site(args.site_name).create()
    elif args.command == 'enable':
        EnableDisable_or_DeleteSite(args.site_name).enable()
    elif args.command == 'disable':
        EnableDisable_or_DeleteSite(args.site_name).disable()
    elif args.command == 'delete':
        EnableDisable_or_DeleteSite(args.site_name).delete()
    else:
        parser.print_help()

if __name__=="__main__":
    main()