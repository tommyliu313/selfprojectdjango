# selfprojectdjango

# Description
This is a basic warehouse management project.

# Version applied in this project
Python: 3.8
Django: 4.12
PostgreSQL

# User who use this repository
## Admin
Admin can edit, delete, make any modification of records from the database.
## Registered User 

## Unregistered User
Unregistered user can only view the .....

# Overview of the models

# How to apply to your database?

## Please input the following commands in your command terminal (Ubuntu)
curl -fsS https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo gpg --dearmor -o /usr/share/keyrings/packages-pgadmin-org.gpg\n

sudo sh -c 'echo "deb [signed-by=/usr/share/keyrings/packages-pgadmin-org.gpg] https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/jammy pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'

apt list --upgradable
sudo apt install pgadmin4
sudo -u postgres psql

The repository is created by using ORM models and PostgreSQL. 
You have to make connection and changes in the DATABASE array from the path "newprojecttrial/settings.py".
