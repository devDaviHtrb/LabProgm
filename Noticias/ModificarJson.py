import json

# Caminho para o arquivo JSON
DB = 'USERS.json'

# Ler o conteúdo do arquivo JSON
try:
    with open(DB, 'r') as f:
        USERS = json.load(f)
except FileNotFoundError:
    USERS = {}  # Se o arquivo não existir, começa com um dicionário vazio

# Modificar os dados (exemplo: adicionar um novo par chave-valor)
USERS['ADMIN'] = {"USERNAME":"admin", "PASSWORD":"admin123"}
USERS["GUEST"] = {"USERNAME":"guest", "PASSWORD":"123"}


# Escrever os dados de volta no arquivo JSON
with open(DB, 'w') as f:
    json.dump(USERS, f, indent=4)  # `indent=4` para formatar o JSON