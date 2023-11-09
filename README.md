# A Todo List demo App
Spinoff of todolist application available at https://github.com/a2975667/flask-gcp-mysql-demo. 

## Requirements

```
python >= 3.5
podman 
mysql client
```

## Getting started

## Get the code
```bash
git clone https://github.com/a2975667/flask-gcp-mysql-demo.git
cd flask-mysql-todolist
```

## Run mysql server (as a local container) 
```bash
podman run -d -p 3306:3306 -v $(pwd):/data -e MYSQL_ROOT_PASSWORD=<your-choice-of-password> --name mysql mysql
```

## Create and initialize database
```bash
mysql -uroot -ppassw0rd --host=localhost < init.sql
```

## Run the application (locally)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
source env.sh
python main.py
```