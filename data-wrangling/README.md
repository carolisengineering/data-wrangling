# data-wrangling

## initialize virtual environment

- **pre-requisite:** install [poetry](https://python-poetry.org) 

```
poetry install
poetry shell
```

## setup flask app

```
export FLASK_APP=data_wrangling
export FLASK_DEBUG=1
```

## setup database

```
export DB_USERNAME=<your_database_username>
export DB_PASSWORD=<your_database_password>

python data_wrangling/db/db_setup.py
```


## run application


## test application