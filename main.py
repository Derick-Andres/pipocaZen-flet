from __future__ import annotations

import flet as ft

from app import dados
from app.telas.cadastro import tela_cadastro
from app.telas.humor import tela_humor
from app.telas.inicio import tela_inicio
from app.telas.login import tela_login
from app.telas.tarefas import tela_tarefas


def main(page: ft.Page) -> None:
    dados.garantir_arquivos()

    page.title = "PipocaZen"
    page.window.width = 420
    page.window.height = 760
    page.padding = 20
    page.bgcolor = "#FFF8F2"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.scroll = ft.ScrollMode.AUTO

    usuario_logado: dict | None = None

    def ajustar_layout(_e=None) -> None:
        largura = page.width or 420
        page.padding = min(20, largura * 0.04)
        for controle in page.controls:
            controle.width = min(600, max(0, largura - 2 * page.padding))
        if _e is not None:
            page.update()

    page.on_resize = ajustar_layout

    def mostrar_tela(controle: ft.Control) -> None:
        page.clean()
        page.add(controle)
        ajustar_layout()
        page.update()

    def mostrar_mensagem(texto: str, cor: str = "#4F8A8B") -> None:
        page.show_dialog(
            ft.SnackBar(
                content=ft.Text(texto, color="white"),
                bgcolor=cor,
                behavior=ft.SnackBarBehavior.FLOATING,
                duration=3000,
            )
        )

    def ir_para_login() -> None:
        mostrar_tela(
            tela_login(
                on_entrar=fazer_login,
                on_ir_cadastro=ir_para_cadastro,
            )
        )

    def ir_para_cadastro() -> None:
        mostrar_tela(
            tela_cadastro(
                on_cadastrar=fazer_cadastro,
                on_voltar=ir_para_login,
            )
        )

    def ir_para_inicio() -> None:
        if usuario_logado is None:
            ir_para_login()
            return
        mostrar_tela(
            tela_inicio(
                usuario=usuario_logado,
                on_ir_humor=ir_para_humor,
                on_ir_tarefas=ir_para_tarefas,
                on_sair=fazer_logout,
            )
        )

    def ir_para_humor() -> None:
        if usuario_logado is None:
            ir_para_login()
            return
        mostrar_tela(
            tela_humor(
                usuario=usuario_logado,
                on_salvar=salvar_humor,
                on_voltar=ir_para_inicio,
            )
        )

    def ir_para_tarefas() -> None:
        if usuario_logado is None:
            ir_para_login()
            return
        mostrar_tela(
            tela_tarefas(
                usuario=usuario_logado,
                listar_tarefas=dados.listar_tarefas_do_usuario,
                on_adicionar=adicionar_tarefa,
                on_alternar=alternar_tarefa,
                on_excluir=excluir_tarefa,
                on_voltar=ir_para_inicio,
            )
        )

    def fazer_login(email: str, senha: str) -> None:
        nonlocal usuario_logado
        usuario = dados.buscar_usuario_por_email_e_senha(email, senha)
        if usuario is None:
            mostrar_mensagem("Email ou senha incorretos. Tente novamente.", "#C96C6C")
            return
        usuario_logado = usuario
        mostrar_mensagem(f"Oi, {usuario['nome']}! Login realizado com sucesso.")
        ir_para_inicio()

    def fazer_cadastro(nome: str, idade: str, email: str, senha: str) -> None:
        nonlocal usuario_logado
        resultado = dados.cadastrar_usuario(nome, idade, email, senha)
        if not resultado["sucesso"]:
            mostrar_mensagem(resultado["mensagem"], "#C96C6C")
            return
        usuario_logado = resultado["usuario"]
        mostrar_mensagem("Conta criada com sucesso!")
        ir_para_inicio()

    def salvar_humor(humor: str, comentario: str, data_atual: str) -> bool:
        if usuario_logado is None:
            mostrar_mensagem("Faça login novamente para continuar.", "#C96C6C")
            ir_para_login()
            return False
        dados.salvar_humor(usuario_logado, data_atual, humor, comentario)
        mostrar_mensagem("Registro de humor salvo com sucesso!")
        return True

    def adicionar_tarefa(titulo: str) -> tuple[bool, str]:
        if usuario_logado is None:
            return False, "Faça login novamente para continuar."
        return dados.salvar_tarefa(usuario_logado, titulo)

    def alternar_tarefa(tarefa_id: str, concluida: bool) -> None:
        dados.atualizar_tarefa(tarefa_id, concluida)
        mostrar_mensagem("Tarefa atualizada.")

    def excluir_tarefa(tarefa_id: str) -> None:
        dados.excluir_tarefa(tarefa_id)
        mostrar_mensagem("Tarefa removida.")

    def fazer_logout() -> None:
        nonlocal usuario_logado
        usuario_logado = None
        mostrar_mensagem("Voce saiu da sua conta.")
        ir_para_login()

    ir_para_login()


ft.run(main)
