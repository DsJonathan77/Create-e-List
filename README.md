# README.md

# API REST Flask - Cadastro de Alunos

Esta aplicação consiste em uma API REST desenvolvida com Flask e Python, utilizando MySQL para persistência de dados. O objetivo é cadastrar e listar alunos através de rotas HTTP.

## 🚀 Tecnologias utilizadas
- Python 3.x
- Flask
- Flask-SQLAlchemy
- MySQL
- python-dotenv

## ⚙️ Funcionalidades

- `POST /alunos` → Cadastra um novo aluno no banco de dados
- `GET /alunos` → Lista todos os alunos cadastrados

## 🛠 Como rodar o projeto

1. Clone este repositório:
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

2. Crie um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure o `.env` com base no `.env.example`

5. Crie o banco de dados e rode o seguinte script no Python:
```python
from app import db
db.create_all()
```

6. Execute o servidor:
```bash
python app.py
```

## 📂 Estrutura do projeto
```
📁 seu-repositorio
├── app.py
├── .env.example
├── README.md
├── requirements.txt
```

## 🧪 Testando a API
Utilize ferramentas como [Postman](https://www.postman.com/) ou [Insomnia](https://insomnia.rest/) para realizar requisições `POST` e `GET` para `http://localhost:5000/alunos`.

## 🔐 Segurança
As credenciais do banco de dados são carregadas por variáveis de ambiente para manter os dados sensíveis protegidos mesmo em repositórios públicos.

## 🧠 Autor
Desenvolvido por Alison Pires✌️
