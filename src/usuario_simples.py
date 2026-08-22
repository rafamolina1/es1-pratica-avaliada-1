"""Gerenciamento simples de usuários.

Prática Avaliada 1 — Engenharia de Software I
Aluno: Rafael Oliveira Molina

A implementação contém somente cadastro, login e listagem, conforme o
princípio YAGNI. O hash SHA-256 foi mantido por ser uma proteção básica pedida
no enunciado da atividade.
"""

import hashlib
from typing import List, Optional


class Usuario:
    """Representa os dados mínimos necessários de um usuário."""

    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = self._hash_senha(senha)

    @staticmethod
    def _hash_senha(senha: str) -> str:
        """Retorna o hash usado para não guardar a senha em texto puro."""
        return hashlib.sha256(senha.encode("utf-8")).hexdigest()

    def validar_senha(self, senha: str) -> bool:
        """Informa se a senha recebida corresponde à senha cadastrada."""
        return self._hash_senha(senha) == self.senha


class GerenciadorUsuarios:
    """Cadastra, autentica e lista usuários em memória."""

    def __init__(self):
        self.usuarios: List[Usuario] = []

    def cadastrar(self, nome: str, email: str, senha: str) -> Usuario:
        """Cadastra um usuário, desde que o e-mail ainda não exista."""
        if any(usuario.email == email for usuario in self.usuarios):
            raise ValueError("Email já cadastrado")

        usuario = Usuario(nome, email, senha)
        self.usuarios.append(usuario)
        return usuario

    def fazer_login(self, email: str, senha: str) -> Optional[Usuario]:
        """Retorna o usuário quando as credenciais são válidas; senão, None."""
        for usuario in self.usuarios:
            if usuario.email == email and usuario.validar_senha(senha):
                return usuario
        return None

    def listar_todos(self) -> List[Usuario]:
        """Retorna todos os usuários cadastrados."""
        return self.usuarios


if __name__ == "__main__":
    gerenciador = GerenciadorUsuarios()
    gerenciador.cadastrar("Ana Silva", "ana@email.com", "senha123")
    gerenciador.cadastrar("João Souza", "joao@email.com", "senha456")

    usuario_logado = gerenciador.fazer_login("ana@email.com", "senha123")
    print("Login realizado:", usuario_logado.nome if usuario_logado else "falhou")

    print("Usuários cadastrados:")
    for usuario in gerenciador.listar_todos():
        print(f"- {usuario.nome} ({usuario.email})")

