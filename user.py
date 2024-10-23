import sqlite3
import bcrypt
from database import conectar_banco

def adicionar_usuario(nome, email, senha, cargo, equipe, instagram):
    senha_hashed = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())

    try:
        conn = conectar_banco()
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO usuarios (nome, email, senha, cargo, equipe, instagram)
            VALUES (?, ?, ?, ?, ?, ?);  
        ''', (nome, email, senha, cargo, equipe, instagram))
        
        conn.commit()
        print(f'Usuário {nome} foi adicionado com sucesso!')
    except sqlite3.IntegrityError:

        print('Erro: O email já foi registrado.')
    finally:
        conn.close()
def main():
    print('Cadastro do usuário')

    nome = input('Nome: ')
    email = input('Email: ')
    senha = input('Senha: ')
    cargo = input('Cargo: ')
    equipe = input('Equipe: ')
    instagram = input('Instagram: ')
    
    adicionar_usuario(nome, email, senha, cargo, equipe, instagram)
if __name__ == '__main__':
    main()