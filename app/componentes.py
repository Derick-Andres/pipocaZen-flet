from __future__ import annotations

import flet as ft


def titulo(texto: str) -> ft.Text:
    return ft.Text(
        texto,
        size=28,
        weight=ft.FontWeight.BOLD,
        color="#5B4B49",
        text_align=ft.TextAlign.CENTER,
    )


def subtitulo(texto: str) -> ft.Text:
    return ft.Text(
        texto,
        size=14,
        color="#7A6A67",
        text_align=ft.TextAlign.CENTER,
    )


def campo_texto(rotulo: str, senha: bool = False, multiline: bool = False) -> ft.TextField:
    return ft.TextField(
        label=rotulo,
        hint_text=rotulo if multiline else None,
        password=senha,
        can_reveal_password=senha,
        multiline=multiline,
        min_lines=3 if multiline else 1,
        max_lines=5 if multiline else 1,
        border_radius=12,
        filled=True,
        bgcolor="#FFFDFB",
        color="#5B4B49",
        label_style=ft.TextStyle(color="#8D7A74", size=14),
        hint_style=ft.TextStyle(color="#B7AAA3", size=14),
        border_color="#E7D8CC",
        focused_border_color="#F4A261",
        cursor_color="#8D5A43",
    )


def botao_principal(texto: str, on_click) -> ft.ElevatedButton:
    return ft.ElevatedButton(
        content=ft.Text(texto, color="#FFFFFF", size=15, weight=ft.FontWeight.W_600),
        on_click=on_click,
        width=260,
        height=46,
        style=ft.ButtonStyle(
            bgcolor="#F4A261",
            shape=ft.RoundedRectangleBorder(radius=12),
        ),
    )


def botao_secundario(texto: str, on_click) -> ft.OutlinedButton:
    return ft.OutlinedButton(
        content=ft.Text(texto, color="#8D5A43", size=15, weight=ft.FontWeight.W_600),
        on_click=on_click,
        width=260,
        height=44,
        style=ft.ButtonStyle(
            side=ft.BorderSide(1, "#D9B8A2"),
            shape=ft.RoundedRectangleBorder(radius=12),
        ),
    )


def cartao(conteudo: list[ft.Control]) -> ft.Container:
    return ft.Container(
        content=ft.Column(
            controls=conteudo,
            spacing=14,
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
        ),
        padding=22,
        border_radius=18,
        bgcolor="#FFF4EA",
        shadow=ft.BoxShadow(
            spread_radius=0,
            blur_radius=10,
            color="#EAD7C8",
            offset=ft.Offset(0, 3),
        ),
    )


def mensagem(texto: str, cor: str = "#5B4B49") -> ft.Text:
    return ft.Text(texto, size=13, color=cor, text_align=ft.TextAlign.CENTER)
