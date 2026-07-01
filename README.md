# PipocaZen Flet

Projeto educativo em Python com Flet para alunos iniciantes aprenderem interface, organizacao de codigo e persistencia simples com arquivos JSON.

## Objetivo

O PipocaZen foi criado como uma base simples para estudar:

- Python na pratica
- criacao de telas com Flet
- cadastro e login simples
- persistencia local com JSON
- organizacao de projeto em pastas e arquivos

## Tecnologias usadas

- Python 3
- Flet
- JSON local

## Requisitos

Antes de rodar o projeto, voce precisa ter:

- Python 3 instalado
- `venv` disponivel no Python
- terminal com acesso aos comandos `python3` e `pip`

Para conferir:

```bash
python3 --version
python3 -m pip --version
```

## Instalacao

Em muitos sistemas Linux, instalar pacotes Python direto no sistema pode falhar por causa do ambiente gerenciado pelo sistema operacional. Por isso, o recomendado para este projeto e usar um ambiente virtual.

### 1. Entrar na pasta do projeto

```bash
cd pipocaZen-flet
```

### 2. Criar o ambiente virtual

```bash
python3 -m venv .venv
```

### 3. Ativar o ambiente virtual

No Linux ou macOS:

```bash
source .venv/bin/activate
```

No Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

No Windows CMD:

```cmd
.venv\Scripts\activate.bat
```

### 4. Instalar as dependencias

```bash
pip install -r requirements.txt
```

Se voce quiser instalar a versao completa do Flet com recursos extras, tambem pode usar:

```bash
pip install "flet[all]"
```

## Como executar

Com o ambiente virtual ativado:

```bash
python main.py
```

Se o comando `python` nao existir no seu sistema, use:

```bash
python3 main.py
```

## Como desativar o ambiente virtual

Quando terminar:

```bash
deactivate
```

## Estrutura de pastas

```text
pipocaZen-flet/
├── main.py
├── requirements.txt
├── README.md
├── dados/
│   ├── usuarios.json
│   ├── humores.json
│   └── tarefas.json
└── app/
    ├── dados.py
    ├── componentes.py
    └── telas/
        ├── login.py
        ├── cadastro.py
        ├── inicio.py
        ├── humor.py
        └── tarefas.py
```

## Funcionalidades atuais

- login com email e senha
- cadastro de usuario
- tela inicial com boas-vindas
- registro diario de humor
- gerenciador de tarefas
- salvamento local em JSON

## Onde os dados ficam salvos

Os dados do projeto ficam na pasta `dados/`:

- `dados/usuarios.json`
- `dados/humores.json`
- `dados/tarefas.json`

Esses arquivos sao criados automaticamente na primeira execucao, caso ainda nao existam.

## Arquivos principais

- `main.py`: inicia o Flet e controla a navegacao entre as telas
- `app/dados.py`: leitura e escrita dos arquivos JSON
- `app/componentes.py`: componentes visuais reutilizaveis
- `app/telas/`: telas do sistema

## Dicas para alunos personalizarem o app

- mudar cores, textos e estilos em `app/componentes.py`
- criar novas telas dentro de `app/telas/`
- adicionar novos campos aos JSON
- trocar os emojis de humor por imagens ou pixel art
- expandir o menu inicial com novas ideias

## Solucao de problemas comuns

### Erro `ModuleNotFoundError: No module named 'flet'`

Isso significa que o Flet nao foi instalado no ambiente atual. Ative a `.venv` e rode:

```bash
pip install -r requirements.txt
```

### Erro `externally-managed-environment`

Esse erro costuma acontecer ao tentar instalar pacotes Python direto no sistema no Linux. A solucao recomendada e:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### O comando `python` nao existe

Use:

```bash
python3 main.py
```

## Proximos passos

- mostrar historico de humor do usuario
- adicionar filtros de tarefas
- melhorar ainda mais o visual
- permitir novas categorias e recursos educativos
# pipocaZen-flet
