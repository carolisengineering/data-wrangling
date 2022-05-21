# data-wrangling

## initialize virtual environment

- **pre-requisite:** install [poetry](https://python-poetry.org) 

```
poetry install
poetry shell
```

## setup flask app

- copy `sample.env` and save as `.env`
- paste correct values for each environment variable in `.env`

```bash
export $(xargs <.env)
```


## setup database

```sql
psql
    create database data_wrangling;
\q
```

```bash
python data_wrangling/db/db_setup.py
```


## run application

```bash
cd data_wrangling
python -m flask run
```

## test application

```bash
pytest tests
```