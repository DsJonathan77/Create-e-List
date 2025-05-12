from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

app = Flask(__name__)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo da tabela de Alunos
class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    matricula = db.Column(db.String(50), nullable=False, unique=True)
    senha = db.Column(db.String(100), nullable=False)

# Rota para cadastrar aluno
@app.route('/alunos', methods=['POST'])
def cadastrar_aluno():
    dados = request.get_json()
    nome = dados.get('nome')
    email = dados.get('email')
    matricula = dados.get('matricula')
    senha = dados.get('senha')

    aluno = Aluno(nome=nome, email=email, matricula=matricula, senha=senha)

    db.session.add(aluno)
    db.session.commit()

    return jsonify({"message": "Aluno cadastrado com sucesso!"}), 201

# Rota para listar alunos
@app.route('/alunos', methods=['GET'])
def listar_alunos():
    alunos = Aluno.query.all()
    lista_alunos = [{"nome": aluno.nome, "email": aluno.email, "matricula": aluno.matricula} for aluno in alunos]
    return jsonify(lista_alunos)

if __name__ == '__main__':
    app.run(debug=True)
