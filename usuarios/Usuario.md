# 👥 App: Usuários

## 🎯 Função
Gerenciar o cadastro, autenticação e controle de acesso dos usuários do sistema de reserva de salas.

---

## ✅ Requisitos Funcionais

- [ ] **Cadastro de Usuários**
  - Campos obrigatórios:
    - Nome completo
    - Matrícula institucional
    - E-mail institucional
    - Telefone
    - Data de nascimento
    - Sexo
    - Cargo

- [ ] **Sistema de Login e Logout**
  - Autenticação via matrícula + senha.
  - Senhas criptografadas no banco.
  - Função de redefinir senha.

- [ ] **Controle de Acesso (Permissões)**
  - Tipos de acesso:
    - **Total**: Assessora Administrativa e Diretor.
    - **Moderado**: NTI.
    - **Visualização**: Coordenações, secretarias, manutenção.
  - Implementar com `User Groups` e `@permission_required`.

- [ ] **Gerenciamento de Perfis**
  - Cada usuário deve ter um perfil vinculado a um grupo.
  - Editar informações pessoais e cargo (somente admin).

---

## ⚙️ Tarefas Técnicas

- [ ] Criar modelo `Usuario` (extendendo `AbstractUser` ou `BaseUser`).
- [ ] Configurar autenticação no `settings.py`.
- [ ] Criar formulários de registro e edição (`forms.py`).
- [ ] Implementar views para:
  - Login
  - Logout
  - Cadastro
  - Edição de perfil
- [ ] Restringir acesso por nível de permissão.
- [ ] Criar página de administração para usuários.

---

## 🧱 Banco de Dados
Tabela: `usuarios_usuario`
Campos principais:
- `id`, `nome`, `matricula`, `email`, `telefone`, `cargo`, `data_nascimento`, `sexo`, `password`, `grupo`.

---

## 📊 Critérios de Sucesso
- [ ] Apenas usuários autenticados podem acessar o sistema.
- [ ] Níveis de permissão respeitados.
- [ ] Senhas seguras e criptografadas.
- [ ] Cadastro e edição funcionais via formulário e admin.

