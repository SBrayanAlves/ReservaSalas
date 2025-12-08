# Reserva de Salas - Unieuro

Manual do Usuário

## 1. Introdução

O sistema Reserva de Salas - Unieuro permite que usuários autorizados
visualizem, reservem e administrem salas da instituição de forma simples
e segura.\
Cada usuário possui permissões específicas.

## 2. Tipos de Usuário

### Administradores

-   Diretor
-   Assessor Administrativo
-   NTI

### Usuários com Acesso Somente à Visualização

-   Coordenador
-   Secretário
-   NAPI
-   Manutenção

## 3. Estrutura das Páginas

### 3.1 Página de Login

Permite que qualquer usuário cadastrado acesse o sistema inserindo
matrícula e senha.

### 3.2 Página de Enviar E-mail (Redefinição de Senha)

Usuário informa o e-mail institucional para receber um código de verificação.

### 3.3 Página de Confirmação de Código

O usuário informa o código recebido para continuar o processo de
redefinição de senha.

### 3.4 Página de Nova Senha

O usuário define uma nova senha após validar o código.

### 3.5 Página Home

Exibe **todas as reservas feitas**, com filtros e listagem completa.\
Usuários apenas visualizadores enxergam todas as reservas, porém não
criam.

### 3.6 Página de Cadastro

Disponível apenas para administradores.\
Permite cadastrar **salas** e **usuários**.

### 3.7 Página Exibir Salas

Lista todas as salas já cadastradas para permitir a seleção para
reserva.

### 3.8 Página de Reserva de Sala

Após selecionar uma sala, o usuário é levado a um formulário para
reservar a sala escolhida.

### 3.9 Página de Perfil

Permite alterar dados pessoais:\
- Nome\
- Telefone\
- Data de nascimento

### 3.10 Página de Administração

Redireciona para o painel administrativo do Django.

### 3.11 Logout

Sai da conta e retorna para a página de login.

------------------------------------------------------------------------

## 4. Fluxos de Uso

### 4.1 Como Fazer Login

1.  Acesse a página inicial.\
2.  Insira seu matrícula e senha.\
3.  Clique em **Entrar**.

### 4.2 Como Redefinir a Senha

1.  Na página de login, clique em **Esqueci a senha**.\
2.  Informe seu e-mail.\
3.  Insira o código recebido.\
4.  Defina uma nova senha.

### 4.3 Como Reservar uma Sala

1.  Acesse **Exibir salas**.\
2.  Escolha a sala desejada.\
3.  Clique em **Selecionar**.\
4.  Preencha o formulário.\
5.  Clique em **Salvar reserva**.

### 4.4 Como Cadastrar Sala ou Usuário (Administradores)

1.  Vá para **Cadastro**.\
2.  Escolha **Cadastrar sala** ou **Cadastrar usuário**.\
3.  Preencha o formulário.
4.  Clique em **Salvar**.

------------------------------------------------------------------------

## 5. Erros Comuns e Soluções

### Senha incorreta

**Solução:** Redefina a senha pela opção "Esqueci a senha".

### Campos obrigatórios faltando

**Solução:** Preencha todos os campos marcados com \*.

------------------------------------------------------------------------

## 6. Contato

Em caso de dúvidas, contate a equipe de TI da instituição.
