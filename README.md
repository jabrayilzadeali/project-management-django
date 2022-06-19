Installiation

in terminal run 

first make sure python3 is installed
then make sure pip is working(in windows there is checkbox you need to check to add path in installiation)
(in linux you need to additionally install pip)
[for installing pip in linux](https://www.tecmint.com/install-pip-in-linux/)
#### ubuntu
```py
apt install python3-pip
```

#### Install Django
```py
pip install django
```
#### in my system: 
django-admin -- 4.0.4
python --version => 3.10.4
#### make migrations
```py
python manage.py makemigrations
```

#### migrate
```py
python manage.py migrate
```

Note if you are on linux instead of 'python' use 'python3'

#### createSuperUser
```py
python manage.py createsuperuser
```
It will ask you create username, password etc. make sure you remember them!

#### Run Server
```py
python manage.py runserver
```