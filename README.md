# kiwi
Todo app.

### Initialize Project

```
virtualenv -p python3.8 venv
source venv/bin/activate

pip3 install django
pip install djangorestframework
pip install django-cors-headers

django-admin startproject todo_server
django-admin startapp todos

python manage.py migrate

# Add Todo model

python manage.py makemigrations todos
python manage.py migrate todos

# create django admin super user
python manage.py createsuperuser

# test
python manage.py test

# run server
python manage.py runserver
```

### Installation

```
git clone https://github.com/fruit-team/kiwi.git
cd kiwi/todo_servers
virtualenv -p python3.8 venv
source venv/bin/activate
pip install -r requirements.txt
```