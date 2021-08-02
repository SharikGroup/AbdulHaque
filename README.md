# Project Setup

## 1. Install python 3.9.5 & mysql on your system
(You can skip this if python 3.8+ is already installed in your system)

## 2. Project Setup

i. Clone Project Repository, Cretae VirtualEnv & Install python dependencies
```shell
cd <YOUR_WORKING_DIRECTORY>
git clone https://github.com/abutalhadanish/zhcet-information-sharing-system.git
cd zhcet-information-sharing-system
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

ii. Add local settings & run migrations

Add ```supplyr/settings_local.py``` with following contents:
```python
from .settings import *

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Enter yout database credentials in the following fields
# DATABASES['default']['NAME'] = 'dbname'
DATABASES['default']['USER'] = 'dbuser'
DATABASES['default']['PASSWORD'] = 'dbpasss'
```
(replace `dbuser` and `dbpass` with your actual database username and password)

iii. Create a database named `zhcet_iss` in your database shell:
```sql
CREATE DATABASE supplyr CHARACTER SET utf8mb4;
```

iv. Run in shell to create tables
```shell
python manage.py migrate
```


v. Run server to start the backend.
```shell
python manage.py runserver
```