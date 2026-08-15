# ClinicaEstetica
Desafio prático de um sistema de agendamento para o processo seletivo da COMPEX

## Time 8
* Samuel da Silva Cruz
* Romell Santos Portela Júnior
* Sávio Ricardo Morais Ramos Pereira

## Sobre o Projeto
O objetivo é desenvolver um sistema simples para organizar clientes, horários disponíveis e agendamentos de uma clínica estética, evitando conflito de horários entre os agendamentos.

## Tecnologias Utilizadas
* **Linguagem** : Python
* **Framework** : Django
* **Banco de Dados** : SQLite
* **Gerenciador de Dependências** : Poetry
* **Controle de Versão** : Git / GitHub

## Funcionalidades
1. **Cadastro de Clientes**: Registro e armazenamento dos dados dos clientes
2. **Cadastro de Horários Disponíveis**: Definição Prévia dos horários de atendimento da clínica
3. **Agendamento de Horário**: Vinculação de um cliente registrado a um horário livre
4. **Cancelamento de Agendamento**: Remoção ou desativação de uma consulta previamente agendada
5. **Validação Anti-Conflito**: Bloqueio automático para impedir que dois clientes sejam agendados no mesmo horário
6. **Tela de Listagem**: Visualização centralizada dos próximos agendamentos confirmados

## Pré-requisitos
Antes de iniciar a execução local do projeto, certifique-se de possuir em seu ambiente:
* Git instalado.
* Python (versão 3.10 ou superior).
* Gerenciador de dependências Poetry instalado.

## Como Executar o Projeto 
1. **Clonar o repositório:**
```bash
git clone https://github.com/samuelslv7/ClinicaEstetica.git https://github.com/samuelslv7/ClinicaEstetica.git
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

