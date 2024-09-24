# selfprojectdjango

# Description
This is a basic warehouse management project, which is created by using ORM models , PostgreSQL and Python Django framework. 


# Version applied in this project
vDjango: 4.12
PostgreSQL: 14.13

# User who use this repository
## Admin
Admin can edit, delete, make any modification of records from the database.
They can also choose to list out the warehouse whether its storage quota is full or not.
## Registered User 
Registered User can view the orders, including when and where to rent
## Unregistered User
Unregistered user can only view the ,but cannot access the 

# Overview of the models

# How to apply to your database?

## Please input the following commands in your command terminal (Ubuntu)
curl -fsS https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo gpg --dearmor -o /usr/share/keyrings/packages-pgadmin-org.gpg\n

sudo sh -c 'echo "deb [signed-by=/usr/share/keyrings/packages-pgadmin-org.gpg] https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/jammy pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'

apt list --upgradable
sudo apt install pgadmin4
sudo -u postgres psql

You are advised to make connection and changes in the DATABASE array from the path "newprojecttrial/settings.py".


# Navbar Should Contain
* About
* Districts
* Services
* Login
* Register

# URL Path Planning
## Example from Sir
| Url      | App | REST Method | Description |
| -------- | ---- | ----------- | --- |
| admin    | None   | GET        | Admin Page    |
| about    | Page     | GET        |  About Page  |
| listings |   listings   |    GET         | Overview of Building    |
| listings/<int:id> |  listings    | GET             | Building Specific Information    |
| listings/?page=<number:int> | listings | POST | Show Building in pages
| listings/search?<parameters:int> | listings | POST | Search Any Results
| accounts     | accounts     | GET         |     |
| accounts/login     | accounts     | POST         |  Registered User Login   |
| accounts/register     | accounts     | GET         |  Create a user    |
| accounts/dashboard | accounts     |   GET          | Dashboard of registered user    |
| contacts     |  contacts    | GET         |     |

| Url      | App | REST Method | Description |
| -------- | ---- | ----------- | --- |
| admin    | None   | GET       | Admin Page    |
| about    | user     | GET        | About Page    |
| warehouses | warehouse   |    GET         | Overview of all warehouse    |
| warehouses/<district:char> | warehouse   | GET | Show warehouses from that district |
| warehouses/?page=<number:int> | | | Show warehouses in pages|
| warehouses/<int:id> | warehouse   |    POST         |      |
| transfer | transfer   |    GET         | show records  |
| transfer/ | transfer |   | |
| user | user | |
| user/dashboard | | GET | Show his record
| user/login | | |
| user/logout | | |
