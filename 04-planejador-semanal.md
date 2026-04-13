# 📅 Planejador Semanal — Template Notion

> **Nome para venda:** Planejador Semanal Completo | Notion Template
> **Preço sugerido:** R$9,90 - R$12,90
> **Público-alvo:** Qualquer pessoa que quer organizar sua rotina

---

## 🎨 VISUAL DO TEMPLATE

- **Capa:** Imagem clean com tons de azul claro + branco (calma, organização, clareza)
- **Ícone da página:** 📅
- **Estilo:** Ultra clean e minimalista

---

## 📄 PÁGINA PRINCIPAL — "Minha Semana"

### Texto de boas-vindas:

```
📅 Planejador Semanal

Uma semana bem planejada é uma semana produtiva.
Organize suas tarefas, compromissos e metas semanais 
em um único lugar.

📌 Como usar:
1. Todo domingo (ou segunda de manhã), planeje sua semana
2. Adicione tarefas e compromissos nos dias certos
3. Marque como feito ao longo da semana
4. No fim da semana, revise o que funcionou

Simplifique sua vida. Uma semana de cada vez. ✨
```

---

## 📊 DATABASE 1: "Tarefas da Semana"

### Propriedades:

| Propriedade | Tipo | Opções |
|---|---|---|
| ✏️ Tarefa | Title | O que precisa fazer |
| 📅 Dia | Select | Ver opções abaixo |
| ⏰ Horário | Text | Ex: "09:00" ou "Manhã" |
| 📂 Área | Select | Ver opções abaixo |
| 🎯 Prioridade | Select | `🔴 Urgente` / `🟡 Importante` / `🟢 Normal` / `⚪ Baixa` |
| ✅ Status | Select | `⬜ A fazer` / `📌 Fazendo` / `✅ Feito` / `⏭️ Adiado` |
| ⏱️ Duração Est. | Select | `⚡ 15min` / `🕐 30min` / `🕐 1h` / `🕑 2h` / `🕒 3h+` |
| 📝 Notas | Text | Detalhes extras |

### Opções de DIA:

```
🟡 Segunda-feira
🟡 Terça-feira
🟡 Quarta-feira
🟡 Quinta-feira
🟡 Sexta-feira
🔵 Sábado
🔵 Domingo
```

### Opções de ÁREA:

```
💼 Trabalho
📚 Estudos
🏠 Casa
💪 Saúde
👥 Social
💰 Finanças
🎨 Pessoal
📦 Compras
```

### Dados de exemplo:

| Tarefa | Dia | Horário | Área | Prioridade | Status |
|---|---|---|---|---|---|
| Reunião com equipe | 🟡 Segunda | 10:00 | 💼 Trabalho | 🔴 Urgente | ✅ Feito |
| Ir ao mercado | 🟡 Segunda | Tarde | 📦 Compras | 🟢 Normal | ✅ Feito |
| Entregar relatório | 🟡 Terça | 14:00 | 💼 Trabalho | 🔴 Urgente | 📌 Fazendo |
| Estudar para prova | 🟡 Terça | 19:00 | 📚 Estudos | 🟡 Importante | ⬜ A fazer |
| Academia | 🟡 Quarta | 07:00 | 💪 Saúde | 🟡 Importante | ⬜ A fazer |
| Consulta dentista | 🟡 Quarta | 15:00 | 💪 Saúde | 🔴 Urgente | ⬜ A fazer |
| Pagar contas | 🟡 Quinta | Manhã | 💰 Finanças | 🔴 Urgente | ⬜ A fazer |
| Projeto freelance | 🟡 Sexta | 09:00 | 💼 Trabalho | 🟡 Importante | ⬜ A fazer |
| Faxina casa | 🔵 Sábado | Manhã | 🏠 Casa | 🟢 Normal | ⬜ A fazer |
| Almoço com amigos | 🔵 Sábado | 12:00 | 👥 Social | 🟢 Normal | ⬜ A fazer |
| Planejar próxima semana | 🔵 Domingo | 20:00 | 🎨 Pessoal | 🟡 Importante | ⬜ A fazer |

---

## 📊 DATABASE 2: "Metas da Semana"

### Propriedades:

| Propriedade | Tipo | Opções |
|---|---|---|
| 🎯 Meta | Title | Ex: "Terminar curso online" |
| 📂 Área | Select | Mesmas opções da DB Tarefas |
| 📌 Status | Select | `⬜ Pendente` / `📌 Em progresso` / `✅ Concluída` / `❌ Não alcançada` |
| 📊 Progresso | Number | Percentual (0-100%) |
| 📝 Resultado | Text | O que aconteceu com essa meta |

### Dados de exemplo:

| Meta | Área | Status | Progresso |
|---|---|---|---|
| Entregar projeto do cliente | 💼 Trabalho | 📌 Em progresso | 70% |
| Estudar 10 horas | 📚 Estudos | ⬜ Pendente | 30% |
| Ir à academia 3x | 💪 Saúde | ⬜ Pendente | 33% |
| Ler 50 páginas | 🎨 Pessoal | 📌 Em progresso | 60% |
| Não gastar além do limite | 💰 Finanças | ✅ Concluída | 100% |

---

## 📊 DATABASE 3: "Notas Rápidas"

### Propriedades:

| Propriedade | Tipo | Opções |
|---|---|---|
| 📝 Nota | Title | Anotação rápida |
| 📂 Tipo | Select | `💡 Ideia` / `📌 Lembrete` / `📞 Contato` / `🔗 Link` / `📝 Geral` |
| 📅 Data | Date | Quando anotou |
| ⭐ Importante? | Checkbox | Marcar se for prioridade |

### Dados de exemplo:

| Nota | Tipo | Importante? |
|---|---|---|
| Ligar pro encanador - 11 99999-0000 | 📞 Contato | ✅ |
| Ideia: criar canal no YouTube | 💡 Ideia | ❌ |
| Senha WiFi escritório: abc123 | 📝 Geral | ❌ |
| Aniversário da mãe dia 25 | 📌 Lembrete | ✅ |

---

## 👁️ VIEWS

### Database "Tarefas da Semana":
1. **"📊 Kanban por Dia"** — Board, agrupar por Dia ⭐ (principal)
2. **"📋 Lista Completa"** — Table, ordenar por Dia + Prioridade
3. **"🔴 Urgentes"** — Table, filtro: Prioridade = Urgente
4. **"✅ Feitas"** — Table, filtro: Status = Feito
5. **"📊 Por Área"** — Board, agrupar por Área

### Database "Metas da Semana":
1. **"🎯 Minhas Metas"** — Gallery, mostra tudo
2. **"📋 Tabela"** — Table

### Database "Notas Rápidas":
1. **"📝 Todas"** — Table
2. **"⭐ Importantes"** — Table, filtro: Importante = True

---

## 🧩 LAYOUT DA PÁGINA PRINCIPAL

```
┌──────────────────────────────────────────────┐
│  📅 Planejador Semanal                       │
│  [Texto de boas-vindas]                      │
├──────────────────┬───────────────────────────┤
│                  │                           │
│  🎯 Metas da    │  📝 Notas Rápidas         │
│  Semana          │  (Table: últimas notas    │
│  (Gallery view)  │   + botão de adicionar)   │
│                  │                           │
├──────────────────┴───────────────────────────┤
│                                              │
│  📊 Minha Semana                             │
│  (Board/Kanban agrupado por Dia)             │
│                                              │
│  SEG  |  TER  |  QUA  |  QUI  |  SEX  | SAB │
│  ───  |  ───  |  ───  |  ───  |  ───  | ──  │
│  Task |  Task |  Task |  Task |  Task | Task │
│  Task |  Task |       |  Task |       |      │
│       |       |       |       |       |      │
│                                              │
├──────────────────────────────────────────────┤
│                                              │
│  📊 Resumo da Semana                         │
│  Callout: Total de tarefas | Feitas | %      │
│                                              │
└──────────────────────────────────────────────┘
```

---

## 📑 TEMPLATE DE TAREFA (Page template dentro da database)

Quando clicar em uma tarefa, a página interna mostra:

```
✏️ [Nome da Tarefa]

📋 Detalhes
━━━━━━━━━━━━━━━━
📅 Quando: [propriedade Dia]
⏰ Horário: [propriedade Horário]  
🎯 Prioridade: [propriedade Prioridade]
📂 Área: [propriedade Área]

📝 O que preciso fazer:
• 
• 
• 

✅ Subtarefas:
- [ ] 
- [ ] 
- [ ] 

📝 Anotações:

```

---

## 📑 PÁGINA EXTRA: "Template de Planejamento Semanal"

Crie como sub-página para o usuário duplicar todo domingo:

```
📅 Planejamento da Semana (__/__/2026)

🔙 Revisão da Semana Anterior:
• O que funcionou bem?
• O que não funcionou?
• O que vou fazer diferente?

🎯 Top 3 Prioridades desta Semana:
1. 
2. 
3. 

📋 Compromissos Fixos:
• Segunda: 
• Terça: 
• Quarta: 
• Quinta: 
• Sexta: 
• Sábado: 
• Domingo: 

💡 Algo que quero experimentar:


📝 Notas para a semana:

```

---

## ✅ CHECKLIST DE MONTAGEM NO NOTION

- [ ] Criar página principal "📅 Planejador Semanal"
- [ ] Adicionar capa (azul claro/minimalista) e ícone 📅
- [ ] Escrever texto de boas-vindas
- [ ] Criar database "Tarefas da Semana" (8 propriedades + 5 views)
- [ ] Criar database "Metas da Semana" (5 propriedades + 2 views)
- [ ] Criar database "Notas Rápidas" (4 propriedades + 2 views)
- [ ] Configurar a Board/Kanban por dia como view principal
- [ ] Montar layout com colunas (Metas + Notas)
- [ ] Preencher dados de exemplo completos
- [ ] Criar template de tarefa (page template)
- [ ] Criar subpágina "Template de Planejamento Semanal"
- [ ] Testar todas as views
- [ ] Publicar e ativar "Allow duplicate as template"
