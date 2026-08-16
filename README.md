# ClinicaEstetica
Desafio prático de um sistema de agendamento para o processo seletivo da COMPEX

## Time 8
* Samuel da Silva Cruz
* Romell Santos Portela Júnior
* Sávio Ricardo Morais Ramos Pereira

## Objetivo do Sistema
O objetivo é desenvolver um sistema simples para organizar clientes, horários disponíveis e agendamentos de uma clínica estética, evitando conflito de horários entre os agendamentos.

## Tecnologias Utilizadas
* **Linguagem** : Python
* **Framework** : Django
* **Banco de Dados** : SQLite
* **Gerenciador de Dependências** : Poetry
* **Controle de Versão** : Git / GitHub

## Pré-requisitos
Antes de iniciar a execução local do projeto, certifique-se de possuir em seu ambiente:
* Git instalado.
* Python (versão 3.10 ou superior).

## Como Executar o Projeto 
1. **Clonar o repositório:**
```bash
git clone https://github.com/samuelslv7/ClinicaEstetica.git
```
2. **Acessar a pasta do projeto:**
```Bash
cd ClinicaEstetica
```
3. **Instalar as dependências:**
```Bash
poetry install
```
4. **Criar e estruturar o Banco de Dados (SQLite):**
```Bash
poetry run python gerenciar.py migrate
```
5. **Iniciar o servidor de desenvolvimento:**
```Bash
poetry run python gerenciar.py runserver
```

## Funcionalidades Implementadas
1. Cadastro de clientes.
2. Cadastro de horários disponíveis.
3. Agendamento de horário para um cliente.
4. Cancelamento de agendamento.
5. Validação para impedir que dois clientes sejam agendados no mesmo horário.
6. Tela de listagem dos próximos agendamentos.

## Principais Dificuldades Encontradas
* Compreender a estrutura do Django, por ser um novo framework para a equipe
* Estruturar o banco de dados relacional


