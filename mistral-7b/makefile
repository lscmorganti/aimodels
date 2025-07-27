# Makefile para facilitar uso do projeto Mistral 7B com Docker

# 1-Constrói a imagem Docker
build:
	docker compose build

# 1-Sobe os containers com GPU
up:
	docker compose up

# 1-Sobe os containers em segundo plano
up-detach:
	docker compose up -d

# 1-Para os containers
down:
	docker compose down

# 1-Mostra os logs da API
logs:
	docker compose logs -f

# 1-Acessa o terminal do container
bash:
	docker exec -it mistral-api bash

# 1-Remove imagem e volumes (cuidado!)
nuke:
	docker compose down --volumes --rmi all
