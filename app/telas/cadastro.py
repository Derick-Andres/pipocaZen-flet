from __future__ import annotations

import flet as ft

from app.componentes import botao_principal, botao_secundario, campo_texto, cartao, subtitulo, titulo


def tela_cadastro(on_cadastrar, on_voltar) -> ft.Control:
    campo_nome = campo_texto("Nome")
    campo_idade = campo_texto("Idade")
    campo_email = campo_texto("Email")
    campo_senha = campo_texto("Senha", senha=True)

    def cadastrar(_e) -> None:
        on_cadastrar(
            campo_nome.value or "",
            campo_idade.value or "",
            campo_email.value or "",
            campo_senha.value or "",
        )

    return ft.Column(
        controls=[
            cartao(
                [
                    titulo("Criar conta"),
                    subtitulo("Preencha seus dados para entrar no mundo do PipocaZen."),
                    campo_nome,
                    campo_idade,
                    campo_email,
                    campo_senha,
                    botao_principal("Cadastrar", cadastrar),
                    botao_secundario("Voltar para login", lambda _e: on_voltar()),
                ]
            )
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
