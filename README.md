# 📝 Gerenciador de Tarefas com Django

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.0-green?logo=django)](https://www.djangoproject.com/)

---

## 📘 Descrição

Este é um projeto simples de **Lista de Tarefas (To-Do List)** desenvolvido em **Python com o framework Django**.  
O objetivo principal é demonstrar o uso de **Models, Views e Templates** para criar uma lógica de negócios visual:  
**identificar tarefas atrasadas automaticamente**.

---

## 🚀 Funcionalidades

- **Listagem de Tarefas**: Exibe todas as tarefas cadastradas no banco de dados.
- **Status Visual**:
  - ✅ **Concluída**: A tarefa aparece riscada e em cinza.
  - 🚨 **Atrasada**: Se a data limite já passou e a tarefa não foi feita, ela é destacada em vermelho.
  - 📅 **Em dia**: Tarefas futuras aparecem com destaque padrão (azul).
- **Painel Administrativo**: Interface pronta do Django para adicionar, editar e excluir tarefas.

---

## 📂 Estrutura e Explicação do Código

O projeto segue a arquitetura **MVT (Model-View-Template)** do Django. Abaixo, explicamos como cada parte funciona:

### 1. 🧱 Modelo (`models.py`)

Define a estrutura do banco de dados:

- `titulo`: O nome da tarefa  
- `data_conclusao`: A data limite para entrega  
- `concluida`: Campo booleano (checkbox) que indica se a tarefa foi feita

---

### 2. 🧠 Lógica (`views.py`)

Aqui está a "inteligência" do backend:

- A view `listar_tarefas` busca todas as tarefas no banco
- Importa `from datetime import date` para capturar a data atual
- Envia as tarefas e a data de hoje para o HTML, permitindo a comparação

---

### 3. 🎨 Interface (`index.html`)

O HTML usa a linguagem de template do Django para aplicar estilos visuais:

```django
<tr class="{% if tarefa.data_conclusao < hoje and not tarefa.concluida %}atrasada{% endif %}">
🛠️ Como Rodar o Projeto
✅ Pré-requisitos
- Python instalado
🔧 Passo 1: Instalação

# (Opcional) Crie e ative um ambiente virtual

python -m venv venv
# Windows: venv\Scripts\activate
# Linux/Mac: source venv/bin/activate

# Instale o Django
pip install django



🔧 Passo 2: Configuração do Banco de Dados
python manage.py migrate



🔧 Passo 3: Criar Usuário Admin
python manage.py createsuperuser


(Siga as instruções na tela para definir nome e senha)

🔧 Passo 4: Executar o Servidor
python manage.py runserver


- Acesse o site: http://127.0.0.1:8000/
- Acesse o admin: http://127.0.0.1:8000/admin/

🎨 Estilização
O projeto utiliza CSS embutido no arquivo index.html, com:
- Design responsivo
- Cartões centralizados
- Badges coloridas para facilitar a leitura do status da tarefa

🖼️ Evidência Visual
Abaixo está um print demonstrando o funcionamento da aplicação:

Visual da Lista de Tarefas

📌 Observações
- O projeto utiliza db.sqlite3 como banco de dados padrão
- A interface administrativa do Django já vem pronta para uso






