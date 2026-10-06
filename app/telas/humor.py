from __future__ import annotations

from datetime import datetime

import flet as ft

from app.componentes import botao_principal, botao_secundario, campo_texto, cartao, mensagem, subtitulo, titulo


OPCOES_DE_HUMOR = [
    {"valor": "muito_triste", "imagem": "emocoes/muito_triste_icone.png", "titulo": "Muito triste"},
    {"valor": "triste", "imagem": "emocoes/triste_icone.png", "titulo": "Triste"},
    {"valor": "neutro", "imagem": "emocoes/neutro_icone.png", "titulo": "Neutro"},
    {"valor": "feliz", "imagem": "emocoes/feliz_icone.png", "titulo": "Feliz"},
    {"valor": "muito_feliz", "imagem": "emocoes/muito_feliz_icone.png", "titulo": "Muito feliz"},
]


def tela_humor(usuario: dict, on_salvar, on_voltar) -> ft.Control:
    data_atual = datetime.now().strftime("%d/%m/%Y")
    campo_comentario = campo_texto("Como foi o seu dia?", multiline=True)
    humor_selecionado = "neutro"
    grupo_humor = ft.Row(
        wrap=True,
        spacing=8,
        run_spacing=8,
        alignment=ft.MainAxisAlignment.CENTER,
    )

    def atualizar_destaque() -> None:
        for controle in grupo_humor.controls:
            selecionado = controle.data == humor_selecionado
            controle.border = ft.Border.all(2, "#F4A261" if selecionado else "#E7D8CC")
            controle.bgcolor = "#FFE3C9" if selecionado else "#FFFDFB"
            controle.opacity = 1.0 if selecionado else 0.65

    def selecionar_humor(e) -> None:
        nonlocal humor_selecionado
        humor_selecionado = e.control.data
        atualizar_destaque()
        grupo_humor.update()

    grupo_humor.controls = [
        ft.Container(
            content=ft.Image(
                src=opcao["imagem"],
                width=44,
                height=44,
                fit=ft.BoxFit.CONTAIN,
                semantics_label=opcao["titulo"],
            ),
            data=opcao["valor"],
            tooltip=opcao["titulo"],
            width=56,
            height=56,
            padding=4,
            border_radius=12,
            on_click=selecionar_humor,
        )
        for opcao in OPCOES_DE_HUMOR
    ]
    atualizar_destaque()

    def salvar(_e) -> None:
        nonlocal humor_selecionado
        sucesso = on_salvar(
            humor_selecionado,
            campo_comentario.value or "",
            data_atual,
        )
        if sucesso:
            campo_comentario.value = ""
            humor_selecionado = "neutro"
            atualizar_destaque()
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
                    botao_principal("Salvar registro", salvar),
                    botao_secundario("Voltar", lambda _e: on_voltar()),
                ]
            )
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
