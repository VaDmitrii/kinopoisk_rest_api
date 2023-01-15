# REST Api of cinema portal

## Prepare database for a project
- Install requirements
```
pip install -r requirements.txt

pip install -r requirements.dev.txt
```

- Create models
```
python create_tables.py
```

- Upload data to database
```
python load_fixture.py
```
Script reads fixtures.json and uploads data to database. If the data has already been uploaded - return message. 

## Running a project

### Bash (Linux/MACOS)
```shell
export FLASK_APP=run.py
export FLASK_ENV='development'
flask run
```

### CMD (Windows)
```shell
set FLASK_APP=run.py
set FLASK_ENV=development
flask run
```

### PowerShell (Windows)
```shell
$env:FLASK_APP = "run"
$env:FLASK_ENV = "development"
flask run
```

## Running unit tests
```shell
pytest .
```

