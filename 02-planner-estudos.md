# 📚 Planner de Estudos Completo — Template Notion

> **Nome para venda:** Planner de Estudos | Notion Template
> **Preço sugerido:** R$14,90 - R$19,90
> **Público-alvo:** Vestibulandos, concurseiros, universitários

---

## 🎨 VISUAL DO TEMPLATE

- **Capa:** Imagem clean com tons de azul marinho + branco (remete a foco e estudo)
- **Ícone da página:** 📚
- **Estilo:** Minimalista e organizado, sem poluição visual

---

## 📄 PÁGINA PRINCIPAL — "Central de Estudos"

### Texto de boas-vindas (copie direto):

```
📚 Minha Central de Estudos

Organize. Estude. Conquiste.

Seu espaço completo para gerenciar matérias, cronogramas,
revisões e acompanhar seu progresso rumo à aprovação.

📌 Como usar:
1. Cadastre suas matérias e tópicos
2. Planeje sua semana na aba "Cronograma"
3. Registre sessões de estudo para acompanhar seu progresso
4. Use o sistema de revisão espaçada para fixar o conteúdo

Bons estudos! 🎯
```

---

## 📊 DATABASE 1: "Matérias"

### Propriedades:

| Propriedade | Tipo no Notion | Opções/Config |
|---|---|---|
| 📖 Matéria | Title | Ex: "Matemática", "Português" |
| 🎨 Cor | Select | Para organização visual |
| 📊 Peso/Importância | Select | `🔴 Alta` / `🟡 Média` / `🟢 Baixa` |
| 📈 Progresso | Number | Percentual (0-100%) com barra de progresso |
| 📝 Notas | Text | Anotações gerais sobre a matéria |
| 🔗 Tópicos | Relation | Relacionar com database "Tópicos" |

### Dados de exemplo:

| Matéria | Peso | Progresso |
|---|---|---|
| 📐 Matemática | 🔴 Alta | 35% |
| 📝 Português | 🔴 Alta | 50% |
| 🌍 Geografia | 🟡 Média | 20% |
| 🔬 Física | 🔴 Alta | 15% |
| 📜 História | 🟡 Média | 40% |
| 🧬 Biologia | 🟡 Média | 30% |
| 🧪 Química | 🔴 Alta | 25% |
| 🗣️ Inglês | 🟢 Baixa | 60% |

---

## 📊 DATABASE 2: "Tópicos"

### Propriedades:

| Propriedade | Tipo | Opções |
|---|---|---|
| 📌 Tópico | Title | Ex: "Equação 2º grau", "Concordância verbal" |
| 📖 Matéria | Relation | Relacionar com database "Matérias" |
| 📌 Status | Select | Ver opções abaixo |
| 🎯 Dificuldade | Select | `🟢 Fácil` / `🟡 Médio` / `🔴 Difícil` |
| 📅 Última Revisão | Date | Data da última vez que revisou |
| 📅 Próxima Revisão | Date | Quando precisa revisar de novo |
| 📝 Resumo | Text | Resumo rápido do tópico |
| 🔗 Link do Material | URL | Link para vídeo aula, PDF, etc. |

### Opções de STATUS:

```
⬜ Não estudado
📖 Estudando
✅ Estudado
🔄 Precisa revisar
🏆 Dominado
```

### Dados de exemplo:

| Tópico | Matéria | Status | Dificuldade |
|---|---|---|---|
| Equação 2º grau | Matemática | ✅ Estudado | 🟡 Médio |
| Progressão Aritmética | Matemática | 📖 Estudando | 🟡 Médio |
| Concordância verbal | Português | 🏆 Dominado | 🟢 Fácil |
| Regência verbal | Português | 🔄 Precisa revisar | 🔴 Difícil |
| Cinemática | Física | ⬜ Não estudado | 🔴 Difícil |
| Termodinâmica | Física | ⬜ Não estudado | 🔴 Difícil |
| Revolução Francesa | História | ✅ Estudado | 🟡 Médio |
| Genética | Biologia | 📖 Estudando | 🔴 Difícil |

---

## 📊 DATABASE 3: "Sessões de Estudo"

### Propriedades:

| Propriedade | Tipo | Opções |
|---|---|---|
| 📝 O que estudei | Title | Descrição livre |
| 📖 Matéria | Relation | Relacionar com "Matérias" |
| 📅 Data | Date | Quando estudou |
| ⏱️ Tempo (minutos) | Number | Duração em minutos |
| 📊 Rendimento | Select | `😴 Baixo` / `😐 Médio` / `🔥 Alto` / `🚀 Excelente` |
| 📂 Tipo | Select | Ver opções abaixo |
| 📝 Anotações | Text | O que aprendeu, dúvidas |

### Opções de TIPO:

```
📖 Teoria (leitura/vídeo)
✏️ Exercícios
📝 Revisão
🧪 Simulado
📄 Resumo/Fichamento
🎧 Podcast/Áudio
```

### Dados de exemplo:

| O que estudei | Matéria | Tempo | Rendimento | Tipo |
|---|---|---|---|---|
| PA e PG - exercícios | Matemática | 90 min | 🔥 Alto | ✏️ Exercícios |
| Revolução Industrial | História | 45 min | 😐 Médio | 📖 Teoria |
| Simulado ENEM 2024 | — | 300 min | 🔥 Alto | 🧪 Simulado |
| Genética - Mendel | Biologia | 60 min | 🚀 Excelente | 📖 Teoria |

---

## 📊 DATABASE 4: "Cronograma Semanal"

### Propriedades:

| Propriedade | Tipo | Opções |
|---|---|---|
| 📝 Atividade | Title | O que vai estudar |
| 📖 Matéria | Relation | Relacionar com "Matérias" |
| 📅 Dia da Semana | Select | `🟡 Segunda` / `🟡 Terça` / `🟡 Quarta` / `🟡 Quinta` / `🟡 Sexta` / `🔵 Sábado` / `🔵 Domingo` |
| ⏰ Horário | Text | Ex: "08:00 - 10:00" |
| ⏱️ Duração | Number | Minutos |
| 📂 Tipo | Select | Mesmas opções da DB Sessões |
| ✅ Feito? | Checkbox | Marcar quando concluir |

### Dados de exemplo:

| Atividade | Matéria | Dia | Horário | Duração |
|---|---|---|---|---|
| Equações - exercícios | Matemática | 🟡 Segunda | 08:00 - 10:00 | 120 min |
| Interpretação de texto | Português | 🟡 Segunda | 10:30 - 12:00 | 90 min |
| Cinemática - teoria | Física | 🟡 Terça | 08:00 - 09:30 | 90 min |
| Revisão - flashcards | Várias | 🟡 Terça | 10:00 - 11:00 | 60 min |
| Brasil Colonial | História | 🟡 Quarta | 08:00 - 10:00 | 120 min |
| Genética + exercícios | Biologia | 🟡 Quinta | 08:00 - 10:00 | 120 min |
| Simulado semanal | — | 🔵 Sábado | 08:00 - 13:00 | 300 min |

---

## 👁️ VIEWS (Visualizações)

### Database "Tópicos":
1. **"📋 Todos os Tópicos"** — Table, ordenar por Matéria
2. **"🔄 Para Revisar"** — Table, filtro: Status = "Precisa revisar"
3. **"📊 Por Matéria"** — Board, agrupar por Matéria
4. **"🎯 Por Dificuldade"** — Board, agrupar por Dificuldade

### Database "Sessões de Estudo":
1. **"📅 Histórico"** — Table, ordenar por Data (desc)
2. **"📊 Por Matéria"** — Board, agrupar por Matéria
3. **"📅 Calendário"** — Calendar view

### Database "Cronograma":
1. **"📅 Semana Completa"** — Table, ordenar por Dia da Semana
2. **"📊 Por Dia"** — Board, agrupar por Dia da Semana
3. **"✅ Pendentes"** — Table, filtro: Feito = False

---

## 📊 DATABASE 5: "Flashcards" (Revisão Espaçada)

### Propriedades:

| Propriedade | Tipo | Opções |
|---|---|---|
| ❓ Pergunta | Title | A pergunta do flashcard |
| ✅ Resposta | Text | A resposta (toggle block p/ esconder) |
| 📖 Matéria | Relation | Relacionar com "Matérias" |
| 📌 Tópico | Relation | Relacionar com "Tópicos" |
| 🎯 Nível | Select | `🔴 Não sei` / `🟡 Quase` / `🟢 Sei` |
| 📅 Última Revisão | Date | Quando revisou pela última vez |
| 📅 Próxima Revisão | Formula | Baseada no nível (ver abaixo) |

### Lógica da Revisão Espaçada (fórmula simplificada):

```
Se Nível = "Não sei" → revisar em 1 dia
Se Nível = "Quase" → revisar em 3 dias
Se Nível = "Sei" → revisar em 7 dias
```

**Fórmula Notion para "Próxima Revisão":**
```
if(prop("Nível") == "🔴 Não sei", dateAdd(prop("Última Revisão"), 1, "days"), if(prop("Nível") == "🟡 Quase", dateAdd(prop("Última Revisão"), 3, "days"), dateAdd(prop("Última Revisão"), 7, "days")))
```

### Dados de exemplo:

| Pergunta | Resposta | Matéria | Nível |
|---|---|---|---|
| Fórmula de Bhaskara? | x = (-b ± √(b²-4ac)) / 2a | Matemática | 🟢 Sei |
| O que é Mitose? | Divisão celular que gera 2 células idênticas | Biologia | 🟡 Quase |
| Ano da Proclamação da República? | 1889 | História | 🟢 Sei |
| 3 leis de Newton? | Inércia, F=ma, Ação e reação | Física | 🔴 Não sei |

---

## 🧩 LAYOUT DA PÁGINA PRINCIPAL

```
┌──────────────────────────────────────────────┐
│  📚 Minha Central de Estudos                 │
│  [Texto de boas-vindas]                      │
├──────────────────┬───────────────────────────┤
│                  │                           │
│  📊 Meu Progresso│  📅 Cronograma de Hoje   │
│  (Gallery view   │  (Table filtrada          │
│   das Matérias)  │   pelo dia atual)         │
│                  │                           │
├──────────────────┴───────────────────────────┤
│                                              │
│  🔄 Tópicos Para Revisar                     │
│  (Table filtrada: Status = Precisa revisar)  │
│                                              │
├──────────────────────────────────────────────┤
│                                              │
│  📝 Sessões de Estudo Recentes               │
│  (Table: últimas 7 sessões)                  │
│                                              │
├──────────────────────────────────────────────┤
│                                              │
│  ❓ Flashcards para Revisar Hoje             │
│  (Table filtrada: Próxima Revisão ≤ hoje)    │
│                                              │
└──────────────────────────────────────────────┘
```

---

## 📑 PÁGINAS EXTRAS (subpáginas)

### 📖 "Guia de Estudos"

```
📖 Como Usar Este Planner

🎯 Método de Estudo Recomendado:

1. PLANEJE → Use o Cronograma Semanal para organizar sua semana
2. ESTUDE → Registre cada sessão na database "Sessões de Estudo"
3. REVISE → Use os Flashcards com revisão espaçada
4. ACOMPANHE → Veja seu progresso na página principal

💡 Dicas:
• Estude em blocos de 45-90 minutos (técnica Pomodoro)
• Intercale matérias diferentes no mesmo dia
• Revise os flashcards todo dia antes de dormir
• Faça pelo menos 1 simulado por semana
```

---

## ✅ CHECKLIST DE MONTAGEM NO NOTION

- [ ] Criar página principal "📚 Minha Central de Estudos"
- [ ] Adicionar capa (azul marinho/clean) e ícone 📚
- [ ] Escrever texto de boas-vindas
- [ ] Criar database "Matérias" (6 propriedades)
- [ ] Criar database "Tópicos" (8 propriedades + 4 views)
- [ ] Criar database "Sessões de Estudo" (7 propriedades + 3 views)
- [ ] Criar database "Cronograma Semanal" (7 propriedades + 3 views)
- [ ] Criar database "Flashcards" (7 propriedades + fórmula)
- [ ] Criar as relações entre databases
- [ ] Montar layout da página principal com colunas
- [ ] Preencher todos os dados de exemplo
- [ ] Criar subpágina "Guia de Estudos"
- [ ] Testar todas as views e fórmulas
- [ ] Publicar e ativar "Allow duplicate as template"
