# 🏫 App: Salas

## 🎯 Função
Gerenciar o cadastro e as informações físicas das salas de aula da instituição.

---

## ✅ Requisitos Funcionais

- [x] **Cadastro de Salas**
  - Dados obrigatórios:
    - Bloco
    - Número da sala
    - Capacidade
    - Tamanho da TV
    - Possui pódio (Sim/Não)
  - Cadastro restrito ao setor NTI.

- [ ] **Gerenciamento de Salas**
  - Editar, remover e listar salas.
  - Filtrar por bloco, capacidade e turno.
  - Indicar se a sala está:
    - Disponível
    - Reservada
    - Em manutenção
OBS: Já é possível usando o sistema do Django Admin

- [ ] **Visualização**
  - Exibir todas as salas em tabela.
  - Mostrar detalhes da sala ao clicar.

---

## ⚙️ Tarefas Técnicas

- [x] Criar modelo `Sala` com os campos acima.
- [x] Adicionar relacionamento com `Reserva`.
- [x] Implementar CRUD completo no Django Admin.
- [ ] Criar views e templates:
  - Listagem (tabela com filtros)
  - Detalhes da sala
  - Cadastro (restrito ao NTI)
- [ ] Criar validações no formulário (ex: capacidade > 0).

---

## 🧱 Banco de Dados
Tabela: `salas_sala`
Campos principais:
- `id`, `bloco`, `numero`, `capacidade`, `tv_tamanho`, `possui_podio`, `status`.

Relacionamentos:
- `reservas` (One-to-Many)

---

## 📊 Critérios de Sucesso
- [x] Somente NTI pode cadastrar/editar salas.
- [ ] Listagem e filtro de salas funcionando.
- [ ] Integração com sistema de reservas ativa.
- [ ] Status visual (disponível/reservada/manutenção).

