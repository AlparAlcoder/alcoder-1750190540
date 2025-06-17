# API FastAPI para Gerenciamento de Itens

Este é um servidor API utilizando o FastAPI para gerenciar itens. Cada item possui `name`, `description` e `price`. A API fornece endpoints para criar e recuperar itens.

## Endpoints

### POST /items/

Este endpoint é usado para criar um novo item.

#### Parâmetros

- **item**: Um objeto `Item`, que inclui as seguintes propriedades:
  - **name** (string): O nome do item. Deve ser único.
  - **description** (string): Uma descrição curta do item.
  - **price** (float): O preço do item.

#### Exemplo de uso

```bash
curl -X POST "http://localhost:8000/items/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"name\":\"foo\",\"description\":\"A foo item\",\"price\":15.0}"
```

### GET /items/{item_name}

Este endpoint é usado para recuperar um item existente pelo nome.

#### Parâmetros

- **item_name** (string): O nome do item.

#### Exemplo de uso

```bash
curl -X GET "http://localhost:8000/items/foo" -H  "accept: application/json"
```

## Notas Importantes

- O nome do item deve ser único. Se um item com o mesmo nome for enviado para o endpoint POST, um erro 400 será retornado.
- Se um nome de item que não existe for enviado para o endpoint GET, um erro 404 será retornado.

## Dependências

Para executar este código, você precisará ter as seguintes dependências instaladas:

- Python 3.6 ou superior
- FastAPI
- Pydantic
- Uvicorn (para executar o servidor)

Você pode instalar as dependências com o seguinte comando:

```bash
pip install fastapi pydantic uvicorn
```

Para executar o servidor, use o seguinte comando:

```bash
uvicorn main:app --reload
```