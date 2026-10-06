from __future__ import annotations

import flet as ft

from app.componentes import botao_principal, botao_secundario, campo_texto, cartao, mensagem, subtitulo, titulo


def tela_tarefas(usuario: dict, listar_tarefas, on_adicionar, on_alternar, on_excluir, on_voltar) -> ft.Control:
    campo_tarefa = campo_texto("Digite uma nova tarefa")
    aviso = mensagem("")
    lista_tarefas = ft.Column(spacing=10)

    def montar_item_tarefa(tarefa: dict) -> ft.Container:
        checkbox = ft.Checkbox(
            value=tarefa.get("concluida", False),
            label=tarefa.get("titulo", ""),
            label_style=ft.TextStyle(weight=ft.FontWeight.BOLD, color="#3D2C29"),
            expand=True,
            on_change=lambda e, tarefa_id=tarefa["id"]: alternar_tarefa(
                e, tarefa_id, bool(e.control.value)
            ),
        )

        return ft.Container(
            padding=12,
            border_radius=14,
            bgcolor="#FFFDFB",
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=6,
                color="#F0E1D6",
                offset=ft.Offset(0, 2),
            ),
            content=ft.Column(
                spacing=8,
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            checkbox,
                            ft.IconButton(
                                icon=ft.Icons.DELETE,
                                icon_color="#C96C6C",
                                tooltip="Excluir tarefa",
                                on_click=lambda e, tarefa_id=tarefa["id"]: excluir_tarefa(e, tarefa_id),
                            ),
                        ],
                    ),
                    ft.Text(
                        f"Criada em: {tarefa.get('data_criacao', '-')}",
                        size=12,
                        color="#8A7A77",
                    ),
                    ft.Text(
                        "Concluida" if tarefa.get("concluida") else "Pendente",
                        size=12,
                        color="#5E9C76" if tarefa.get("concluida") else "#C38B5F",
                    ),
                ],
            ),
        )

    def recarregar_lista() -> None:
        tarefas = listar_tarefas(usuario["email"])
        lista_tarefas.controls.clear()

        if not tarefas:
            lista_tarefas.controls.append(
                mensagem("Ainda nao ha tarefas. Que tal criar a primeira?")
            )
            return

        for tarefa in tarefas:
            lista_tarefas.controls.append(montar_item_tarefa(tarefa))

    def atualizar_tela(evento=None) -> None:
        recarregar_lista()
        if evento and getattr(evento, "page", None):
            evento.page.update()

    def adicionar(_e) -> None:
        sucesso, texto = on_adicionar(campo_tarefa.value or "")
        aviso.value = texto
        aviso.color = "#5E9C76" if sucesso else "#C96C6C"
        if sucesso:
            campo_tarefa.value = ""
        atualizar_tela(_e)

    def alternar_tarefa(_e, tarefa_id: str, concluida: bool) -> None:
        on_alternar(tarefa_id, concluida)
        atualizar_tela(_e)

    def excluir_tarefa(_e, tarefa_id: str) -> None:
        on_excluir(tarefa_id)
        atualizar_tela(_e)

    recarregar_lista()

    return ft.Column(
        controls=[
            cartao(
                [
                    titulo("Gerenciador de tarefas"),
                    subtitulo(f"Tarefas de {usuario['nome']}"),
                    campo_tarefa,
                    botao_principal("Adicionar tarefa", adicionar),
                    aviso,
                    lista_tarefas,
                    botao_secundario("Voltar", lambda _e: on_voltar()),
                ]
            )
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
