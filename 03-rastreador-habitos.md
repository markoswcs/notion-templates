# ✅ Rastreador de Hábitos — Template Notion

> **Nome para venda:** Rastreador de Hábitos Diários | Notion Template
> **Preço sugerido:** R$9,90 - R$14,90
> **Público-alvo:** Pessoas focadas em desenvolvimento pessoal, rotina, saúde

---

## 🎨 VISUAL DO TEMPLATE

- **Capa:** Imagem motivacional com tons de laranja/coral (energia, ação, disciplina)
- **Ícone da página:** ✅
- **Estilo:** Vibrante mas limpo, com uso de emojis coloridos

---

## 📄 PÁGINA PRINCIPAL — "Meus Hábitos"

### Texto de boas-vindas:

```
✅ Rastreador de Hábitos

"Somos o que fazemos repetidamente. 
Excelência não é um ato, mas um hábito." — Aristóteles

Aqui você acompanha seus hábitos diários e transforma
pequenas ações em grandes resultados.

📌 Como usar:
1. Defina seus hábitos na lista abaixo
2. Marque cada hábito completado no dia
3. Acompanhe sua sequência e consistência
4. Revise semanalmente e ajuste conforme necessário

Vamos construir a melhor versão de você! 🚀
```

---

## 📊 DATABASE 1: "Hábitos"

### Propriedades:

| Propriedade | Tipo | Opções |
|---|---|---|
| 🎯 Hábito | Title | Nome do hábito |
| 📂 Categoria | Select | Ver opções abaixo |
| ⏰ Momento do Dia | Select | `🌅 Manhã` / `☀️ Tarde` / `🌙 Noite` / `🔄 Qualquer hora` |
| 🎯 Meta | Text | Ex: "30 min", "2 litros", "10 páginas" |
| 📊 Frequência | Select | `📅 Diário` / `📆 Seg-Sex` / `📆 3x Semana` / `📆 Semanal` |
| 🔥 Sequência Atual | Number | Dias seguidos que completou |
| 🏆 Melhor Sequência | Number | Recorde de dias seguidos |
| 📌 Status | Select | `✅  Ativo` / `⏸️ Pausado` / `❌ Abandonado` |
| 📝 Motivação | Text | Por que esse hábito é importante pra você |

### Opções de CATEGORIA:

```
💪 Saúde & Fitness
🧠 Mente & Aprendizado
💰 Finanças
🧘 Bem-estar & Mindfulness
📖 Leitura
💼 Carreira & Produtividade
❤️ Relacionamentos
🎨 Hobbies & Criatividade
```

### Dados de exemplo:

| Hábito | Categoria | Momento | Meta | Frequência |
|---|---|---|---|---|
| 💧 Beber 2L de água | 💪 Saúde | 🔄 Qualquer hora | 2 litros | 📅 Diário |
| 🏃 Exercício físico | 💪 Saúde | 🌅 Manhã | 30 minutos | 📆 Seg-Sex |
| 📖 Ler livro | 📖 Leitura | 🌙 Noite | 20 páginas | 📅 Diário |
| 🧘 Meditar | 🧘 Bem-estar | 🌅 Manhã | 10 minutos | 📅 Diário |
| 📝 Journaling | 🧠 Mente | 🌙 Noite | 1 entrada | 📅 Diário |
| 💰 Registrar gastos | 💰 Finanças | 🌙 Noite | Anotar tudo | 📅 Diário |
| 🚫 Sem redes sociais | 🧠 Mente | 🔄 Qualquer hora | Até 30 min/dia | 📆 Seg-Sex |
| 🎸 Praticar violão | 🎨 Hobbies | ☀️ Tarde | 15 minutos | 📆 3x Semana |

---

## 📊 DATABASE 2: "Registro Diário"

### Propriedades:

| Propriedade | Tipo | Opções |
|---|---|---|
| 📅 Data | Title | Data do dia (formato: 10/04/2026) |
| 💧 Água 2L | Checkbox | ☑️ |
| 🏃 Exercício | Checkbox | ☑️ |
| 📖 Leitura | Checkbox | ☑️ |
| 🧘 Meditação | Checkbox | ☑️ |
| 📝 Journaling | Checkbox | ☑️ |
| 💰 Registrar gastos | Checkbox | ☑️ |
| 🚫 Redes sociais | Checkbox | ☑️ |
| 🎸 Violão | Checkbox | ☑️ |
| 📊 Total do Dia | Formula | Ver fórmula abaixo |
| 🌟 Nota do Dia | Select | `😔 Ruim` / `😐 Ok` / `😊 Bom` / `🔥 Excelente` |
| 📝 Reflexão | Text | Como foi o dia |

### Fórmula do "Total do Dia":

```
(toNumber(prop("💧 Água 2L")) + toNumber(prop("🏃 Exercício")) + toNumber(prop("📖 Leitura")) + toNumber(prop("🧘 Meditação")) + toNumber(prop("📝 Journaling")) + toNumber(prop("💰 Registrar gastos")) + toNumber(prop("🚫 Redes sociais")) + toNumber(prop("🎸 Violão"))) / 8 * 100
```

> Resultado: mostra a % de hábitos completados no dia (ex: 75%)

### Dados de exemplo (1 semana):

| Data | 💧 | 🏃 | 📖 | 🧘 | 📝 | 💰 | 🚫 | 🎸 | Total | Nota |
|---|---|---|---|---|---|---|---|---|---|---|
| 07/04/2026 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | 87% | 🔥 |
| 08/04/2026 | ✅ | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | 75% | 😊 |
| 09/04/2026 | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ | 50% | 😐 |
| 10/04/2026 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | 87% | 🔥 |

---

## 📊 DATABASE 3: "Revisão Semanal"

### Propriedades:

| Propriedade | Tipo | Opções |
|---|---|---|
| 📅 Semana | Title | Ex: "Semana 01 - Jan/2026" |
| 📅 Período | Date | Range: início e fim da semana |
| 🏆 Melhor hábito | Text | Qual hábito você mais manteve |
| 😓 Hábito mais difícil | Text | Qual hábito você mais falhou |
| 📊 Consistência geral | Select | `🔴 Ruim (<40%)` / `🟡 Regular (40-70%)` / `🟢 Bom (70-90%)` / `🏆 Excelente (90%+)` |
| 🎯 Meta da próxima semana | Text | O que quer melhorar |
| 📝 Reflexão | Text | Como foi a semana |

### Dados de exemplo:

| Semana | Melhor hábito | Mais difícil | Consistência |
|---|---|---|---|
| Semana 14 - Abr/2026 | 💧 Água | 🧘 Meditação | 🟢 Bom (75%) |
| Semana 13 - Mar/2026 | 📖 Leitura | 🏃 Exercício | 🟡 Regular (60%) |

---

## 👁️ VIEWS

### Database "Hábitos":
1. **"📋 Meus Hábitos"** — Table, filtro: Status = Ativo
2. **"📊 Por Categoria"** — Board, agrupar por Categoria
3. **"⏰ Por Momento do Dia"** — Board, agrupar por Momento do Dia

### Database "Registro Diário":
1. **"📅 Este Mês"** — Table, filtro: Data = mês atual, ordenar por Data (desc)
2. **"📅 Calendário"** — Calendar
3. **"📊 Gallery"** — Gallery, mostra Total + Nota

### Database "Revisão Semanal":
1. **"📅 Todas as Semanas"** — Table, ordenar por Data (desc)

---

## 🧩 LAYOUT DA PÁGINA PRINCIPAL

```
┌──────────────────────────────────────────────┐
│  ✅ Rastreador de Hábitos                    │
│  [Texto motivacional]                        │
├──────────────────┬───────────────────────────┤
│                  │                           │
│  🔥 Resumo       │  📅 Registro de Hoje     │
│  Callout boxes:  │  (inline database         │
│  • Dias seguidos │   com 1 linha = hoje)     │
│  • % da semana   │                           │
│                  │                           │
├──────────────────┴───────────────────────────┤
│                                              │
│  📋 Meus Hábitos Ativos                      │
│  (Table view filtrada: ativos)               │
│                                              │
├──────────────────────────────────────────────┤
│                                              │
│  📊 Registro do Mês                          │
│  (Calendar view do Registro Diário)          │
│                                              │
├──────────────────────────────────────────────┤
│                                              │
│  📝 Revisão Semanal                          │
│  (Table: últimas 4 semanas)                  │
│                                              │
└──────────────────────────────────────────────┘
```

---

## 📌 CALLOUT BOXES — Resumo (topo)

**Callout 1:** 
```
🔥 Sequência Atual
___ dias seguidos
(atualize manualmente)
```

**Callout 2:**
```
📊 Consistência da Semana
___% dos hábitos feitos
```

**Callout 3:**
```
🏆 Recorde
___ dias seguidos
```

> **Cores:** Laranja para sequência, Azul para %, Dourado para recorde

---

## 📑 PÁGINA EXTRA: "Guia de Hábitos"

```
🧠 Como Construir Hábitos que Duram

📌 Regras de Ouro:

1. COMECE PEQUENO
   → Não tente fazer 10 hábitos novos de uma vez
   → Comece com 3-4 e vá adicionando

2. NÃO QUEBRE A CORRENTE
   → Marque todo dia, mesmo que parcialmente
   → 2 dias seguidos sem fazer = reinicia a sequência

3. HORÁRIO FIXO
   → Vincule cada hábito a um momento do dia
   → Ex: Meditar sempre ao acordar

4. REVISE TODA SEMANA
   → Use a Revisão Semanal todo domingo
   → Ajuste hábitos que não estão funcionando

5. CELEBRE PEQUENAS VITÓRIAS
   → Completou 7 dias seguidos? Comemore!
   → Completou 30 dias? Recompense-se!

💡 Baseado no livro "Hábitos Atômicos" de James Clear
```

---

## ✅ CHECKLIST DE MONTAGEM NO NOTION

- [ ] Criar página principal "✅ Rastreador de Hábitos"
- [ ] Adicionar capa (tons de laranja/coral) e ícone ✅
- [ ] Escrever texto de boas-vindas com citação
- [ ] Criar database "Hábitos" (9 propriedades + 3 views)
- [ ] Criar database "Registro Diário" (12 propriedades + fórmula + 3 views)
- [ ] Criar database "Revisão Semanal" (7 propriedades)
- [ ] Montar layout com colunas (Resumo + Registro de Hoje)
- [ ] Adicionar callout boxes de resumo
- [ ] Preencher dados de exemplo (hábitos + 1 semana de registros)
- [ ] Criar subpágina "Guia de Hábitos"
- [ ] Testar fórmula do Total do Dia
- [ ] Publicar e ativar "Allow duplicate as template"
