# My-first-Blog
This is my First blog consisting of a number of apps in Django Framework. This was done for learning purpose.

* **Python** version: 3.6

* **Django** version: 2.2.10

* Database: **Postgresql**

* Using **virtualenv** for virtual environment.


### Installation

* Clone the repository and make your branch from **master**.

* Install **virtualenv** on your system. For linux: ```pip install virtualenv```.

* Install and setup Postgresql database on your system if not done already.

* Clone the repo: ```https://github.com/Sajzad/My-first-Blog.git```

* Go to **business_consultancy_firm** dir. And create virtual environment with virtualenv: ```virtualenv -p /usr/bin/python3.6 .env```.

* Activate the virtual environment: ```source .env/bin/activate```.

* Install required dependencies: ```pip install -r requirements.txt```.

* Set these environment variables **DB_NAME, DB_USER, DB_PASSWORD, SECRET_KEY, INTERNAL_IP, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD** with corresponding values.
  e.g, ```export DB_NAME='consultancy_db'```.

* Go to **website** dir where the **manage.py** file exists.

* Create migrations files: ```./manage.py makemigrations```.

* Update the database with migrations: ```./manage.py migrate```.

* Create superuser: ```./manage.py createsuperuser```.

* Start the server: ```./manage.py runserver```.
