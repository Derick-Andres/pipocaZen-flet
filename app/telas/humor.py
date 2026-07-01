from __future__ import annotations

from datetime import datetime

import flet as ft

from app.componentes import botao_principal, botao_secundario, campo_texto, cartao, mensagem, subtitulo, titulo


OPCOES_DE_HUMOR = [
    "😭 Muito triste",
    "😔 Triste",
    "😐 Neutro",
    "🙂 Feliz",
    "😄 Muito feliz",
]


def tela_humor(usuario: dict, on_salvar, on_voltar) -> ft.Control:
    data_atual = datetime.now().strftime("%d/%m/%Y")
    campo_comentario = campo_texto("Como foi o seu dia?", multiline=True)
    grupo_humor = ft.RadioGroup(
        content=ft.Column(
            controls=[ft.Radio(value=opcao, label=opcao) for opcao in OPCOES_DE_HUMOR],
            spacing=6,
        ),
        value=OPCOES_DE_HUMOR[2],
    )

    def salvar(_e) -> None:
        sucesso = on_salvar(
            grupo_humor.value or OPCOES_DE_HUMOR[2],
            campo_comentario.value or "",
            data_atual,
        )
        if sucesso:
            campo_comentario.value = ""
            grupo_humor.value = OPCOES_DE_HUMOR[2]
            campo_comentario.update()
            grupo_humor.update()

    return ft.Column(
        controls=[
            cartao(
                [
                    titulo("Registrar humor"),
                    subtitulo(f"Hoje e {data_atual}. Como voce esta se sentindo?"),
                    mensagem(f"Aluno(a): {usuario['nome']}"),
                    grupo_humor,
                    campo_comentario,
                    mensagem("Esses emojis podem virar pixel art no futuro."),
                    botao_principal("Salvar registro", salvar),
                    botao_secundario("Voltar", lambda _e: on_voltar()),
                ]
            )
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
