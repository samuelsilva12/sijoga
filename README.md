# 🏐 Sijoga - Plataforma de Conexão entre Jogadores de Esportes

Sijoga é um sistema web que permite que pessoas interessadas em praticar esportes (como vôlei, futebol, etc.) encontrem e organizem jogos com outras pessoas da sua cidade. O objetivo é facilitar a conexão entre jogadores, promovendo o esporte, a saúde e a socialização.

## 🚀 Funcionalidades

- Cadastro e autenticação de usuários
- Criação de perfis com nome, cidade e esporte de interesse
- Marcação de jogos por localidade
- Listagem de jogadores e partidas
- Backend estruturado com FastAPI
- Integração com banco de dados PostgreSQL via SQLAlchemy
- Versionamento e migrações com Alembic

## 🛠 Tecnologias

- [FastAPI](https://fastapi.tiangolo.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Alembic](https://alembic.sqlalchemy.org/)
- [Pydantic](https://docs.pydantic.dev/)
- [Uvicorn](https://www.uvicorn.org/)

## 🧱 Estrutura de pastas

```bash
.
├── app/
│   ├── models/           # Modelos do banco de dados
│   ├── schemas/          # Schemas Pydantic (Entrada/Saída)
│   ├── crud/             # Funções CRUD organizadas
│   ├── database/         # Conexão com o banco e sessão
│   ├── routers/          # Rotas da aplicação (API)
│   └── main.py           # Ponto de entrada FastAPI
├── alembic/              # Migrações de banco de dados
├── requirements.txt      # Dependências do projeto
├── README.md             # Este arquivo
