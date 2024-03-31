# univesp-projeto-integrador-I
Univesp PI I

## Como instalar as dependências?
Execute o comando:
```
pip install -r requirements.txt
```

## Configurações necessárias
Crie um arquivo .env seguindo o exemplo de .env.sample e passe as credenciais do banco

No caso do banco ser um contianer será necessário executar o seguinte comando e passar o IP como valor da variável DB_HOST
```
docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <nome_do_seu_contêiner_mysql>
```

## Comandos básicos
Criar migration:
```
python manage.py makemigrations
```
Aplicar migration ao banco de dados:
```
python manage.py migrate
```
