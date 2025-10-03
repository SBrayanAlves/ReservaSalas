**# 📌 Sistema de Reserva de Salas

O sistema tem como objetivo **automatizar a reserva e distribuição de salas de aula** na instituição, substituindo o processo manual feito atualmente em planilhas.  

## 🚀 Visão Geral
- Sistema **web-based** (via navegador).
- Voltado para uso da **Assessoria Administrativa** e setores relacionados.
- Permite reservas **semestrais e avulsas**.
- Elimina conflitos de horário e melhora a **visualização e gestão** das salas.

---

## ✅ Requisitos Funcionais
- [ ] **Cadastro e Gerenciamento de Salas**
  - Bloco, número, capacidade, TV, pódio.
  - Apenas o NTI pode cadastrar/editar.
- [ ] **Cadastro de Turmas**
  - Nome/código da turma.
  - Suporte a turmas mistas.
- [ ] **Cadastro de Usuários**
  - Nome, matrícula, e-mail, telefone, data de nascimento, sexo, cargo.
- [ ] **Permissões de Acesso**
  - Visualização → Coordenação, secretarias, manutenção.
  - Moderado → NTI (salas e turmas).
  - Total → Tatiana e Diretor.
- [ ] **Reserva de Salas**
  - Até **4 períodos por turno** (manhã/tarde/noite).
  - Impedir conflitos por sala/turno/período.
- [ ] **Relatórios**
  - Mensal, semestral e personalizado.
  - Por curso, bloco, sala ou período.
- [ ] **Visualização**
  - Principal em **tabela** (não cards).
  - Filtros: bloco, sala, curso, turno, período.
  - Detalhes ao clicar em uma sala.

---

## 🔒 Requisitos Não Funcionais
- [ ] **Plataforma**
  - 100% web, responsivo, acessível de qualquer lugar.
- [ ] **Usabilidade**
  - Interface simples e intuitiva.
  - Pouca digitação para evitar erros.
- [ ] **Banco de Dados**
  - Atualização de turmas/códigos a cada semestre.
  - Edição e inclusão simples.
- [ ] **Segurança**
  - Controle de acesso baseado em perfis.
  - Senhas criptografadas no banco.

---

## 📊 Critérios de Sucesso
- [ ] Processo de distribuição automatizado.
- [ ] Interface intuitiva para reservas.
- [ ] Relatórios gerados para apoio institucional.
- [ ] Flexibilidade para ajustes e alterações.
- [ ] Disponibilidade de salas visível por período (manhã/tarde/noite).

---

## 📅 Próximos Passos
- [ ] Analisar planilhas atuais da assessoria.
- [ ] Desenvolver cadastro de salas e turmas.
- [ ] Criar interface de calendário e reservas.
- [ ] Implementar relatórios visuais (PDF/Exportação).

---

## 👥 Stakeholders
- Assessoria administrativa (Tatiana)
- Diretor
- Coordenadores
- NTI
- Professores
- Alunos
- Manutenção

---

## ⚠️ Riscos Identificados
- Conflito de horários entre reservas.
- Sobrecarga de salas no período matutino.
- Realocações por manutenção/reformas.
- Ocupação indevida de salas já reservadas.
**
