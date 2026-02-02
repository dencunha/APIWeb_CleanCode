# 🚀 2nd Project - Web User Management API
## 🇺🇸 English Version

### 📌 About the Project
This project is a robust **REST API** developed in Python, focused on applying **Clean Code** concepts, layered architecture, and software engineering best practices. The system allows registering and searching for users using a relational database.

> **Personal Note:** As someone transitioning from a career in Law to Web Development, this project was a milestone. It represents the shift from "the logic of laws" to "the logic of systems," where code organization and precision are the foundations for a reliable application.

### 🏛️ Architecture & Best Practices
The project follows **Clean Architecture** and **SOLID** principles:
* **Dependency Inversion:** Using interfaces (ABC) to decouple Controllers from Repositories.
* **Composer Pattern:** Centralizing dependency injection.
* **Global Error Handling:** Custom handlers for standardized HTTP responses.

### 🛠️ Tech Stack
* **Language:** Python 3.12+ | **Framework:** Flask | **ORM:** SQLAlchemy | **Validation:** Pydantic | **Testing:** Pytest

### 🛣️ API Routes
| Method | Route | Description |
| :--- | :--- | :--- |
| `POST` | `/user` | Registers a new user (Name, Age, Height). |
| `GET` | `/user/find/<name>` | Searches for users by name in the database. |

### 🚀 How to Run
1. **Clone the repository:** `git clone https://github.com/dencunha/APIWeb_CleanCode`
2. **Setup environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

# 🚀 2º Projeto - API Web de Gerenciamento de Usuários

### 📌 Sobre o Projeto
Este projeto é uma **API REST** robusta desenvolvida em Python, focada em aplicar conceitos de **Clean Code**, arquitetura em camadas e boas práticas de engenharia de software. O sistema permite o registro e a busca de usuários utilizando persistência em banco de dados relacional.

> **Nota Pessoal:** Como alguém que está transicionando de uma carreira em Direito para o Desenvolvimento Web, este projeto foi um marco. Ele representa a mudança da "lógica das leis" para a "lógica dos sistemas", onde a organização e a precisão do código são as bases para uma aplicação confiável.

---

### 🏛️ Arquitetura e Boas Práticas
O projeto foi estruturado seguindo princípios de **Clean Architecture** e **SOLID**:
* **Inversão de Dependência:** Uso de interfaces (ABC) para desacoplar o Controller dos Repositórios.
* **Pattern Composer:** Centralização da injeção de dependências para facilitar a montagem das rotas.
* **Gerência de Erros:** Handlers personalizados para respostas HTTP padronizadas (404, 400, 422, 500).
* **Camada de View:** Isolamento total da lógica de entrada/saída através de classes `HttpRequest` e `HttpResponse`.

### 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.12+
* **Framework:** Flask (Leve e eficiente)
* **ORM:** SQLAlchemy (Mapeamento Objeto-Relacional)
* **Banco de Dados:** SQLite (com suporte do DBeaver)
* **Validação:** Pydantic (Garantia de integridade dos dados)
* **Testes:** Pytest (Testes unitários e de integração)
* **Qualidade:** Pylint (Seguindo as convenções da PEP 8)

---

### 🛣️ Rotas da API
| Método | Rota | Descrição |
| :--- | :--- | :--- |
| `POST` | `/user` | Cadastra um novo usuário (Nome, Idade, Altura). |
| `GET` | `/user/find/<name>` | Busca usuários por nome no banco de dados. |

---

### 🚀 Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/dencunha/APIWeb_CleanCode](https://github.com/dencunha/APIWeb_CleanCode)