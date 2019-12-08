# Scalica 2.0

## How to run on Ubuntu 16.04 LTS
```
sudo apt-get update; sudo apt-get install mysql-server libmysqlclient-dev python-dev python-virtualenv build-essential libssl-dev
```
Set a password when prompted. Do not leave it blank.
```
./first_install.sh

cd db

./install_db.sh

cd ..

source ./env/bin/activate

cd web/scalica

python manage.py makemigrations micro

python manage.py migrate

python manage.py runserver 0.0.0.0:8000
```
Remember to configure custom inbound TCP rule on port 8000. 
