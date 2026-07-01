from __future__ import annotations

import flet as ft

from app.componentes import botao_principal, botao_secundario, campo_texto, cartao, subtitulo, titulo


def tela_login(on_entrar, on_ir_cadastro) -> ft.Control:
    campo_email = campo_texto("Email")
    campo_senha = campo_texto("Senha", senha=True)

    def entrar(_e) -> None:
        on_entrar(campo_email.value or "", campo_senha.value or "")

    return ft.Column(
        controls=[
            cartao(
                [
                    titulo("PipocaZen"),
                    subtitulo("Um espacinho calmo para aprender, sentir e se organizar."),
                    campo_email,
                    campo_senha,
                    botao_principal("Entrar", entrar),
                    botao_secundario("Criar conta", lambda _e: on_ir_cadastro()),
                ]
            )
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
