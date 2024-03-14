# Chuck Norris Jokes API - 2.0

## Visão Geral

Este projeto é uma API simples para consumir e armazenar piadas do Chuck Norris. A API segue uma arquitetura em camadas, incluindo Controller, Service, Repository e Models.

## Funcionalidades

- Consumir piadas do Chuck Norris da API externa.
- Armazenar piadas no banco de dados MongoDB.
- Listar piadas consumidas e armazenadas no histórico.

## Requisitos

- Python 3.x
- MongoDB
- FastAPI

## Instalação

1. Clone o repositório:

    ```
    git clone https://github.com/KevinSoffa/API_Chuck_Norris-2.0
    ```

2. Instale as dependências:

    ```
    pip install -r requirements.txt
    ```

3. Configure as variáveis de ambiente em um arquivo `.env` na raiz do projeto:

    ```
    MONGO_URL=sua_url_do_mongo
    MONGO_DB=nome_do_banco_de_dados
    URL=url_da_api_do_chuck_norris
    ```

## Uso

1. Inicie o servidor FastAPI:

    ```
    uvicorn main:app --reload
    ```

2. Acesse a documentação interativa da API em `http://localhost:8000/docs` para visualizar e testar os endpoints disponíveis.

## Estrutura do Projeto

- **controllers**: Contém os controladores que definem os endpoints da API.
- **models**: Contém os modelos de dados e DTOs (Data Transfer Objects).
- **repository**: Contém os métodos para interação com o banco de dados.
- **service**: Contém a lógica de negócios da aplicação.

## Contribuição

Contribuições são bem-vindas! Para contribuir com este projeto, siga estas etapas:

1. Faça um fork do repositório.
2. Crie uma branch com a sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas alterações (`git commit -am 'Adiciona nova feature'`).
4. Push para a branch (`git push origin feature/nova-feature`).
5. Abra um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).
