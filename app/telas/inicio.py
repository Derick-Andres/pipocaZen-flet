from __future__ import annotations

import flet as ft

from app.componentes import botao_principal, botao_secundario, cartao, subtitulo, titulo


def tela_inicio(usuario: dict, on_ir_humor, on_ir_tarefas, on_sair) -> ft.Control:
    return ft.Column(
        controls=[
            cartao(
                [
                    titulo(f"Bem-vindo, {usuario['nome']}!"),
                    subtitulo("Escolha uma opcao para continuar seu dia."),
                    botao_principal("Registrar humor", lambda _e: on_ir_humor()),
                    botao_principal("Gerenciador de tarefas", lambda _e: on_ir_tarefas()),
                    botao_secundario("Sair", lambda _e: on_sair()),
                ]
            )
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
