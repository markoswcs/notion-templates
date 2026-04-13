# 💰 Controle Financeiro Pessoal — Template Notion

> **Nome para venda:** Controle Financeiro Pessoal | Notion Template
> **Preço sugerido:** R$14,90 - R$19,90
> **Público-alvo:** Jovens adultos, universitários, freelancers

---

## 🎨 VISUAL DO TEMPLATE

- **Capa:** Imagem minimalista com tons de verde escuro + dourado (remete a dinheiro/prosperidade)
- **Ícone da página:** 💰
- **Fonte sugerida:** Default do Notion (Serif para títulos fica elegante)

---

## 📄 PÁGINA PRINCIPAL — "Painel Financeiro"

### Texto de boas-vindas (copie direto):

```
💰 Meu Controle Financeiro

Bem-vindo ao seu painel financeiro pessoal!
Aqui você controla tudo: receitas, despesas, metas e assinaturas.

📌 Como usar:
1. Registre cada transação na tabela abaixo
2. Use as views pra visualizar por mês, categoria ou tipo
3. Acompanhe seu saldo e metas na seção de resumo

Feito com ❤️ para organizar suas finanças.
```

---

## 📊 DATABASE 1: "Transações"

### Propriedades (colunas):

| Propriedade | Tipo no Notion | Opções/Config |
|---|---|---|
| Nome | Title | Ex: "Almoço", "Salário", "Netflix" |
| 💲 Valor | Number | Formato: Real brasileiro (R$) |
| 📅 Data | Date | Data da transação |
| 📂 Categoria | Select | Ver lista abaixo |
| 🔄 Tipo | Select | `✅ Receita` / `❌ Despesa` |
| 💳 Forma de Pagamento | Select | Ver lista abaixo |
| 🏦 Conta | Select | Ver lista abaixo |
| 📝 Observação | Text | Campo livre |
| 🔁 Recorrente? | Checkbox | Marcar se for gasto fixo |

### Opções de CATEGORIA (Select):

```
🍔 Alimentação
🏠 Moradia
🚗 Transporte
👕 Roupas
🎓 Educação
💊 Saúde
🎮 Entretenimento
📱 Assinaturas
🛒 Compras
💼 Trabalho
🎁 Presentes
📦 Outros
```

### Opções de FORMA DE PAGAMENTO (Select):

```
💳 Cartão de Crédito
💳 Cartão de Débito
📱 PIX
🏦 Transferência
💵 Dinheiro
📄 Boleto
```

### Opções de CONTA (Select):

```
🟧 Nubank
🔵 Inter
⬛ C6 Bank
🟢 PicPay
🏦 Itaú
🏦 Bradesco
🏦 Banco do Brasil
🏦 Caixa
💵 Carteira
```

---

## 👁️ VIEWS (Visualizações) da Database "Transações"

### View 1: "📋 Todas as Transações" (Table)
- **Tipo:** Table
- **Ordenar por:** Data (Descending — mais recente primeiro)
- **Mostrar:** Todas as propriedades

### View 2: "📅 Calendário" (Calendar)
- **Tipo:** Calendar
- **Propriedade de data:** 📅 Data
- **Bom para:** Ver gastos distribuídos no mês

### View 3: "📊 Por Categoria" (Board/Kanban)
- **Tipo:** Board
- **Agrupar por:** 📂 Categoria
- **Bom para:** Ver onde está gastando mais

### View 4: "✅ Receitas vs ❌ Despesas" (Board/Kanban)
- **Tipo:** Board
- **Agrupar por:** 🔄 Tipo
- **Bom para:** Comparar entradas e saídas

### View 5: "📱 Gastos por Conta" (Board/Kanban)
- **Tipo:** Board
- **Agrupar por:** 🏦 Conta
- **Bom para:** Ver saldo por banco

---

## 📊 DATABASE 2: "Metas Financeiras"

### Propriedades:

| Propriedade | Tipo | Opções |
|---|---|---|
| 🎯 Meta | Title | Ex: "Reserva de emergência" |
| 💲 Valor Alvo | Number | R$ |
| 💲 Valor Atual | Number | R$ |
| 📊 Progresso | Formula | `round(prop("Valor Atual") / prop("Valor Alvo") * 100)` |
| 📅 Prazo | Date | Data limite |
| 📌 Status | Select | `🔴 Não iniciada` / `🟡 Em andamento` / `🟢 Concluída` |
| 📂 Categoria | Select | `🏖️ Viagem` / `📱 Eletrônico` / `🏠 Casa` / `🎓 Curso` / `🚗 Veículo` / `💰 Reserva` |

### View: "🎯 Minhas Metas" (Gallery)
- **Tipo:** Gallery
- **Preview:** Nenhum (mostra propriedades)
- **Mostrar:** Meta, Progresso, Status, Prazo

---

## 📊 DATABASE 3: "Assinaturas"

### Propriedades:

| Propriedade | Tipo | Opções |
|---|---|---|
| 📱 Serviço | Title | Ex: "Netflix", "Spotify" |
| 💲 Valor Mensal | Number | R$ |
| 📅 Dia de Cobrança | Number | Dia do mês (1-31) |
| 📂 Categoria | Select | `🎬 Streaming` / `🎵 Música` / `☁️ Nuvem` / `📱 Apps` / `🎮 Games` / `📦 Outros` |
| 📌 Status | Select | `✅ Ativa` / `⏸️ Pausada` / `❌ Cancelada` |

### View: "📱 Minhas Assinaturas" (Table)
- **Filtro:** Status = ✅ Ativa
- **Ordenar por:** Valor Mensal (Descending)

---

## 🧩 LAYOUT DA PÁGINA PRINCIPAL

Organize assim (usando colunas do Notion):

```
┌──────────────────────────────────────────────┐
│  💰 Meu Controle Financeiro                  │
│  [Texto de boas-vindas]                      │
├──────────────────┬───────────────────────────┤
│                  │                           │
│  📌 Resumo       │  🎯 Metas                │
│  Callout boxes:  │  (Gallery view da DB      │
│  • Total Receitas│   Metas Financeiras)      │
│  • Total Despesas│                           │
│  • Saldo         │                           │
│                  │                           │
├──────────────────┴───────────────────────────┤
│                                              │
│  📊 Transações do Mês                        │
│  (Table view com filtro: mês atual)          │
│                                              │
├──────────────────────────────────────────────┤
│                                              │
│  📱 Assinaturas Ativas                       │
│  (Table view filtrada)                       │
│                                              │
└──────────────────────────────────────────────┘
```

---

## 📌 CALLOUT BOXES — Resumo (topo da página)

Crie 3 callout blocks lado a lado:

**Callout 1:**
```
✅ Total Receitas
R$ ___
(atualize manualmente ou use rollup)
```

**Callout 2:**
```
❌ Total Despesas
R$ ___
```

**Callout 3:**
```
💰 Saldo
R$ ___
```

> **Cor dos callouts:** Verde para receitas, Vermelho para despesas, Azul para saldo

---

## 🎯 DADOS DE EXEMPLO (já deixe preenchidos no template)

### Transações exemplo:

| Nome | Valor | Data | Categoria | Tipo | Pagamento |
|---|---|---|---|---|---|
| Salário | R$ 3.500 | 05/01 | 💼 Trabalho | ✅ Receita | 🏦 Transferência |
| Aluguel | R$ 1.200 | 10/01 | 🏠 Moradia | ❌ Despesa | 📄 Boleto |
| Mercado | R$ 450 | 12/01 | 🍔 Alimentação | ❌ Despesa | 💳 Cartão Débito |
| Netflix | R$ 39,90 | 15/01 | 📱 Assinaturas | ❌ Despesa | 💳 Cartão Crédito |
| Uber | R$ 25 | 18/01 | 🚗 Transporte | ❌ Despesa | 📱 PIX |
| Freelance | R$ 800 | 20/01 | 💼 Trabalho | ✅ Receita | 📱 PIX |
| Academia | R$ 89,90 | 05/01 | 💊 Saúde | ❌ Despesa | 💳 Cartão Crédito |

### Metas exemplo:

| Meta | Valor Alvo | Valor Atual | Status |
|---|---|---|---|
| Reserva de Emergência | R$ 10.000 | R$ 3.200 | 🟡 Em andamento |
| Notebook Novo | R$ 4.500 | R$ 1.800 | 🟡 Em andamento |
| Viagem Fim de Ano | R$ 3.000 | R$ 0 | 🔴 Não iniciada |

### Assinaturas exemplo:

| Serviço | Valor | Dia | Categoria | Status |
|---|---|---|---|---|
| Netflix | R$ 39,90 | 15 | 🎬 Streaming | ✅ Ativa |
| Spotify | R$ 21,90 | 10 | 🎵 Música | ✅ Ativa |
| iCloud | R$ 3,50 | 01 | ☁️ Nuvem | ✅ Ativa |
| Xbox Game Pass | R$ 44,90 | 20 | 🎮 Games | ✅ Ativa |

---

## ✅ CHECKLIST DE MONTAGEM NO NOTION

- [ ] Criar página principal "💰 Meu Controle Financeiro"
- [ ] Adicionar capa e ícone
- [ ] Escrever texto de boas-vindas
- [ ] Criar database "Transações" com todas as propriedades
- [ ] Configurar as 5 views
- [ ] Criar database "Metas Financeiras" com propriedades e fórmula
- [ ] Criar database "Assinaturas"
- [ ] Montar layout com colunas (Resumo + Metas)
- [ ] Adicionar callout boxes de resumo
- [ ] Preencher dados de exemplo
- [ ] Testar todas as views
- [ ] Publicar e ativar "Allow duplicate as template"
