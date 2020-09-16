Rodar a Aplicação

- python3 -m venv .venv
- source .venv/bin/activate
- pip install --upgrade pip
- pip install -r requirements.txt
- source .env
- flask run



Comandos BD Flask
- flask db init
- flask db migrate -m "<nome-alteração>" - Gravar alteração no migrations
- flask db upgrade -  realizar migrações no BD


Doc
- http://localhost:5000/api/v1/ui


