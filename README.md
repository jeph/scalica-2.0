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
Remember to configure custom inbound TCP rule on port 8000 if running on EC2. 

## How to run on port 80 on Ubuntu 16.04 LTS
Run the setup above

Configure HTTP custom inbound rule if running on EC2.

Install pip if you don't have it already
```
sudo apt install python-pip
```

Start in the root directory.
```
sudo pip install -r requirements.txt

cd web/scalica

sudo python manage.py runserver 0.0.0.0:80
```
If port is already taken, run the following command to kill the processes occupying the port
```
sudo fuser -k 80/tcp
```
