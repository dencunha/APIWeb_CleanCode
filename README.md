# 🚀 2nd Project - Web User Management API

[English Version Below] | [Versão em Português Abaixo]

---

##  English Version

###  About the Project
This project is a robust **REST API** developed in Python, focused on applying **Clean Code** concepts, layered architecture, and software engineering best practices. The system allows registering and searching for users using a relational database.

###  Architecture & Best Practices
The project follows **Clean Architecture** and **SOLID** principles:
* **Dependency Inversion:** Using interfaces (Abstract Base Classes) to decouple Controllers from Repositories.
* **Composer Pattern:** Centralizing dependency injection to build routes easily.
* **Global Error Handling:** Custom handlers for standardized HTTP responses (404, 400, 422, 500).
* **View Layer:** Total isolation of I/O logic using `HttpRequest` and `HttpResponse` classes.

### Tech Stack
* **Language:** Python 3.12+
* **Framework:** Flask
* **ORM:** SQLAlchemy
* **Database:** SQLite (managed with DBeaver)
* **Validation:** Pydantic (Data integrity guarantee)
* **Testing:** Pytest (Unit and Integration tests)
* **Quality:** Pylint (Following PEP 8 conventions)

---

##  Versão em Português

###  Sobre o Projeto
Este projeto é uma **API REST** robusta desenvolvida em Python, focada em aplicar conceitos de **Clean Code**, arquitetura em camadas e boas práticas de engenharia de software. O sistema permite o registro e a busca de usuários utilizando persistência em banco de dados relacional.

###  Arquitetura e Boas Práticas
O projeto foi estruturado seguindo princípios de **Clean Architecture** e **SOLID**:
* **Inversão de Dependência:** Uso de interfaces (Abstract Base Classes) para desacoplar o Controller dos Repositórios.
* **Pattern Composer:** Centralização da injeção de dependências para facilitar a montagem das rotas.
* **Gerência de Erros:** Handlers personalizados para respostas HTTP padronizadas (404, 400, 422, 500).
* **Camada de View:** Isolamento total da lógica de entrada/saída através de classes `HttpRequest` e `HttpResponse`.

###  Tecnologias Utilizadas
* **Linguagem:** Python 3.12+
* **Framework:** Flask
* **ORM:** SQLAlchemy
* **Banco de Dados:** SQLite (com suporte do DBeaver)
* **Validação:** Pydantic (Garantia de integridade dos dados)
* **Testes:** Pytest (Testes unitários e de integração)
* **Qualidade:** Pylint (Seguindo as convenções da PEP 8)

---

##  How to Run / Como Executar

1. **Clone the repository / Clone o repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)