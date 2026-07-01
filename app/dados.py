from __future__ import annotations

import json
from pathlib import Path
from uuid import uuid4


BASE_DIR = Path(__file__).resolve().parent.parent
DADOS_DIR = BASE_DIR / "dados"
ARQUIVO_USUARIOS = DADOS_DIR / "usuarios.json"
ARQUIVO_HUMORES = DADOS_DIR / "humores.json"
ARQUIVO_TAREFAS = DADOS_DIR / "tarefas.json"


def garantir_arquivos() -> None:
    DADOS_DIR.mkdir(exist_ok=True)
    for caminho in [ARQUIVO_USUARIOS, ARQUIVO_HUMORES, ARQUIVO_TAREFAS]:
        if not caminho.exists():
            caminho.write_text("[]", encoding="utf-8")


def ler_json(caminho: Path) -> list:
    garantir_arquivos()
    try:
        conteudo = caminho.read_text(encoding="utf-8").strip()
        if not conteudo:
            return []
        dados = json.loads(conteudo)
        return dados if isinstance(dados, list) else []
    except (json.JSONDecodeError, OSError):
        return []


def salvar_json(caminho: Path, dados_lista: list) -> None:
    garantir_arquivos()
    caminho.write_text(
        json.dumps(dados_lista, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def listar_usuarios() -> list[dict]:
    return ler_json(ARQUIVO_USUARIOS)


def cadastrar_usuario(nome: str, idade: str, email: str, senha: str) -> dict:
    nome = nome.strip()
    idade = idade.strip()
    email = email.strip().lower()
    senha = senha.strip()

    if not nome or not idade or not email or not senha:
        return {"sucesso": False, "mensagem": "Preencha todos os campos para continuar."}

    usuarios = listar_usuarios()
    email_existe = any(usuario["email"].lower() == email for usuario in usuarios)
    if email_existe:
        return {"sucesso": False, "mensagem": "Esse email ja esta cadastrado."}

    novo_usuario = {
        "nome": nome,
        "idade": idade,
        "email": email,
        "senha": senha,
    }
    usuarios.append(novo_usuario)
    salvar_json(ARQUIVO_USUARIOS, usuarios)
    return {
        "sucesso": True,
        "mensagem": "Usuario cadastrado com sucesso.",
        "usuario": novo_usuario,
    }


def buscar_usuario_por_email_e_senha(email: str, senha: str) -> dict | None:
    email = email.strip().lower()
    senha = senha.strip()
    for usuario in listar_usuarios():
        if usuario["email"].lower() == email and usuario["senha"] == senha:
            return usuario
    return None


def salvar_humor(usuario: dict, data: str, humor: str, comentario: str) -> None:
    humores = ler_json(ARQUIVO_HUMORES)
    humores.append(
        {
            "email": usuario["email"],
            "nome": usuario["nome"],
            "data": data,
            "humor": humor,
            "comentario": comentario.strip(),
        }
    )
    salvar_json(ARQUIVO_HUMORES, humores)


def listar_humores_do_usuario(email: str) -> list[dict]:
    humores = ler_json(ARQUIVO_HUMORES)
    return [humor for humor in humores if humor.get("email") == email]


def salvar_tarefa(usuario: dict, titulo: str) -> tuple[bool, str]:
    titulo = titulo.strip()
    if not titulo:
        return False, "Digite uma tarefa antes de adicionar."

    from datetime import datetime

    tarefas = ler_json(ARQUIVO_TAREFAS)
    tarefas.append(
        {
            "id": str(uuid4()),
            "titulo": titulo,
            "concluida": False,
            "data_criacao": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "email": usuario["email"],
        }
    )
    salvar_json(ARQUIVO_TAREFAS, tarefas)
    return True, "Tarefa adicionada com sucesso."


def listar_tarefas_do_usuario(email: str) -> list[dict]:
    tarefas = ler_json(ARQUIVO_TAREFAS)
    return [tarefa for tarefa in tarefas if tarefa.get("email") == email]


def atualizar_tarefa(tarefa_id: str, concluida: bool) -> None:
    tarefas = ler_json(ARQUIVO_TAREFAS)
    for tarefa in tarefas:
        if tarefa.get("id") == tarefa_id:
            tarefa["concluida"] = concluida
            break
    salvar_json(ARQUIVO_TAREFAS, tarefas)


def excluir_tarefa(tarefa_id: str) -> None:
    tarefas = ler_json(ARQUIVO_TAREFAS)
    tarefas_filtradas = [tarefa for tarefa in tarefas if tarefa.get("id") != tarefa_id]
    salvar_json(ARQUIVO_TAREFAS, tarefas_filtradas)
