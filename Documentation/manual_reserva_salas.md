# 📅 Manual do Usuário: Sistema de Reserva de Salas - Unieuro

**Versão:** 1.0  
**Última atualização:** [Inserir Data]

## 1. Introdução

Bem-vindo ao **Sistema de Reserva de Salas da Unieuro**. Esta plataforma foi desenvolvida para facilitar o gerenciamento de espaços da instituição, permitindo que colaboradores visualizem a disponibilidade e realizem agendamentos de forma simples, centralizada e segura.

## 2. Perfis de Acesso

O sistema divide os usuários em dois grupos principais para garantir a segurança e a organização das reservas.

| Perfil | Quem são? | Permissões |
| :--- | :--- | :--- |
| **🛡️ Administrador** | Diretor, Assessor Administrativo, NTI | • Visualizar agenda completa<br>• Criar e cancelar reservas<br>• Cadastrar novas salas<br>• Gerenciar usuários |
| **👀 Visualizador** | Coordenador, Secretário, NAPI, Manutenção | • Visualizar agenda completa<br>• Consultar detalhes das reservas<br>*(Não podem criar ou alterar reservas)* |

---

## 3. Conhecendo o Sistema (Estrutura)

### 🔐 Módulo de Acesso e Segurança

* **Login:** Tela inicial para acesso via matrícula e senha.
* **Recuperação de Senha:** Fluxo seguro para redefinição de credenciais:
    1.  Envio de e-mail institucional.
    2.  Validação via código de segurança.
    3.  Definição de nova senha.
* **Logout:** Encerra a sessão e retorna à tela de login.

### 🏠 Painel Principal (Home)

A tela principal é o coração do sistema.
* **Calendário/Listagem:** Exibe todas as reservas ativas.
* **Filtros:** Permite buscar reservas por data ou sala específica.
* **Status:** Diferenciação visual para salas livres e ocupadas.

### 📝 Módulo de Reservas

* **Exibir Salas:** Catálogo de todas as salas disponíveis na instituição.
* **Formulário de Reserva:** Onde o Administrador define a data, horário e finalidade da utilização da sala selecionada.

### ⚙️ Módulo Administrativo (Restrito)

Disponível apenas para o perfil **Administrador**:
* **Cadastro Geral:** Páginas para registrar novas **Salas** (bloco, número, capacidade) e novos **Usuários**.
* **Painel Admin (Django):** Área técnica para manutenção avançada de dados (acesso restrito ao NTI).

### 👤 Perfil do Usuário
Área para atualização de dados cadastrais do próprio usuário (Nome, Telefone e Data de Nascimento).

---

## 4. Guia Passo a Passo

### 4.1 Como Acessar o Sistema
1.  Acesse o endereço web do sistema.
2.  Insira sua **matrícula** e **senha**.
3.  Clique no botão **Entrar**.

### 4.2 Esqueci Minha Senha
1.  Na tela de login, clique no link **"Esqueci a senha"**.
2.  Digite seu e-mail institucional e confirme.
3.  Verifique sua caixa de entrada e copie o **código de verificação**.
4.  Insira o código no sistema e crie sua nova senha.

### 4.3 Como Reservar uma Sala (Apenas Administradores)
1.  No menu, clique em **"Exibir Salas"**.
2.  Localize a sala desejada na lista e clique em **"Selecionar"**.
3.  Preencha o formulário com data, horário de início/fim e motivo.
4.  Clique em **"Salvar Reserva"**.
    > **Nota:** O sistema alertará caso já exista uma reserva para o horário escolhido (conflito de horário).

### 4.4 Cadastros Administrativos
1.  No menu, acesse a área de **Cadastro**.
2.  Selecione a opção desejada: **Cadastrar Sala** ou **Cadastrar Usuário**.
3.  Preencha todos os campos obrigatórios.
4.  Clique em **Salvar** para efetivar o registro.

---

## 5. Dúvidas Frequentes e Soluções

| Problema | Causa Provável | Solução |
| :--- | :--- | :--- |
| **"Usuário ou senha inválidos"** | Erro de digitação ou senha antiga. | Utilize a opção "Esqueci a senha" para redefinir seu acesso. |
| **Botão "Salvar" não funciona** | Campos obrigatórios em branco. | Verifique se todos os campos marcados com um asterisco (*) foram preenchidos. |
| **Não consigo reservar** | Perfil de usuário sem permissão. | Verifique se seu perfil é "Visualizador". Apenas Administradores podem criar reservas. |

---

## 6. Suporte

Encontrou um erro não listado ou precisa de ajuda técnica?

📞 **Entre em contato com o NTI**
* **Ramal:** [Inserir Ramal]
* **E-mail:** [Inserir Email]

---
*Documento confidencial e de uso interno da Unieuro.*