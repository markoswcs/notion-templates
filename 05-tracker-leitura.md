# 📖 Tracker de Leitura — Template Notion

> **Nome para venda:** Minha Estante Virtual | Notion Template
> **Preço sugerido:** R$9,90 - R$14,90
> **Público-alvo:** Leitores, BookTok, BookTube, clubes de leitura

---

## 🎨 VISUAL DO TEMPLATE

- **Capa:** Imagem de livros/biblioteca com tons quentes (bege, marrom, creme)
- **Ícone da página:** 📖
- **Estilo:** Aconchegante e elegante, estilo "café literário"

---

## 📄 PÁGINA PRINCIPAL — "Minha Estante"

### Texto de boas-vindas:

```
📖 Minha Estante Virtual

Seu cantinho de leitura dentro do Notion.
Organize seus livros, acompanhe seu progresso e 
descubra padrões nas suas leituras.

📌 Como usar:
1. Adicione livros à sua estante (lidos, lendo e quero ler)
2. Registre notas e frases marcantes
3. Defina sua meta anual de leitura
4. Acompanhe suas estatísticas

Boa leitura! ☕
```

---

## 📊 DATABASE 1: "Meus Livros"

### Propriedades:

| Propriedade | Tipo | Opções |
|---|---|---|
| 📖 Título | Title | Nome do livro |
| ✍️ Autor(a) | Text | Nome do autor |
| 📂 Gênero | Multi-select | Ver opções abaixo |
| 📌 Status | Select | Ver opções abaixo |
| ⭐ Nota | Select | `⭐` / `⭐⭐` / `⭐⭐⭐` / `⭐⭐⭐⭐` / `⭐⭐⭐⭐⭐` |
| 📄 Páginas Total | Number | Total de páginas do livro |
| 📄 Página Atual | Number | Em que página está |
| 📊 Progresso | Formula | `round(prop("Página Atual") / prop("Páginas Total") * 100)` |
| 📅 Início | Date | Quando começou a ler |
| 📅 Fim | Date | Quando terminou |
| 📂 Formato | Select | `📕 Físico` / `📱 Kindle/Digital` / `🎧 Audiobook` |
| 🏷️ Tags | Multi-select | `❤️ Favorito` / `🎁 Presente` / `📚 Releitura` / `🇧🇷 Nacional` / `🌍 Traduzido` |
| 🔗 Link | URL | Link para compra ou Goodreads |
| 📝 Resenha | Text | Sua opinião sobre o livro |

### Opções de STATUS:

```
📚 Quero ler
📖 Lendo
✅ Lido
⏸️ Pausado
❌ Abandonado
```

### Opções de GÊNERO (Multi-select):

```
📖 Romance
🔎 Suspense/Thriller
⚔️ Fantasia
🚀 Ficção Científica
📚 Não-ficção
💼 Negócios
🧠 Desenvolvimento Pessoal
📜 Biografia
💕 Romance (amor)
😂 Humor
📰 Jornalismo
🎨 Arte & Design
💊 Saúde & Bem-estar
📖 Clássico
🧒 Juvenil/YA
```

### Dados de exemplo:

| Título | Autor | Gênero | Status | Nota | Páginas | Formato |
|---|---|---|---|---|---|---|
| Hábitos Atômicos | James Clear | 🧠 Desenv. Pessoal | ✅ Lido | ⭐⭐⭐⭐⭐ | 320 | 📕 Físico |
| O Poder do Hábito | Charles Duhigg | 🧠 Desenv. Pessoal | ✅ Lido | ⭐⭐⭐⭐ | 408 | 📱 Kindle |
| Pai Rico Pai Pobre | Robert Kiyosaki | 💼 Negócios | ✅ Lido | ⭐⭐⭐ | 336 | 📕 Físico |
| A Sutil Arte de Ligar o F*da-se | Mark Manson | 🧠 Desenv. Pessoal | 📖 Lendo | — | 224 | 📱 Kindle |
| Duna | Frank Herbert | 🚀 Ficção Científica | 📖 Lendo | — | 680 | 📕 Físico |
| 1984 | George Orwell | 📖 Clássico | 📚 Quero ler | — | 328 | — |
| O Hobbit | J.R.R. Tolkien | ⚔️ Fantasia | 📚 Quero ler | — | 336 | — |
| Sapiens | Yuval Harari | 📚 Não-ficção | ✅ Lido | ⭐⭐⭐⭐⭐ | 464 | 🎧 Audiobook |
| Dom Casmurro | Machado de Assis | 📖 Clássico | ✅ Lido | ⭐⭐⭐⭐ | 208 | 📕 Físico |
| Admirável Mundo Novo | Aldous Huxley | 📖 Clássico | 📚 Quero ler | — | 312 | — |

---

## 👁️ VIEWS da Database "Meus Livros"

### View 1: "📚 Estante" (Gallery) ⭐ PRINCIPAL
- **Tipo:** Gallery
- **Card preview:** Nenhum (ou imagem de capa se adicionar)
- **Mostrar:** Título, Autor, Status, Nota
- **Agrupar por:** Nada (mostra todos)
- **Ordenar por:** Status

### View 2: "📌 Por Status" (Board/Kanban)
- **Tipo:** Board
- **Agrupar por:** Status
- **Colunas:** Quero ler | Lendo | Lido | Pausado | Abandonado

### View 3: "📖 Lendo Agora" (Table)
- **Filtro:** Status = "📖 Lendo"
- **Mostrar:** Título, Autor, Página Atual, Páginas Total, Progresso

### View 4: "⭐ Favoritos" (Gallery)
- **Filtro:** Nota = ⭐⭐⭐⭐⭐
- **Ordenar por:** Fim (desc)

### View 5: "📊 Por Gênero" (Board)
- **Agrupar por:** Gênero

### View 6: "📅 Linha do Tempo" (Timeline)
- **Propriedade:** Início → Fim
- **Bom para:** Ver quando leu cada livro

---

## 📊 DATABASE 2: "Frases & Anotações"

### Propriedades:

| Propriedade | Tipo | Opções |
|---|---|---|
| 💬 Frase/Trecho | Title | A frase ou anotação |
| 📖 Livro | Relation | Relacionar com "Meus Livros" |
| 📄 Página | Number | Número da página |
| 📂 Tipo | Select | `💬 Citação` / `💡 Insight` / `📝 Anotação` / `❓ Dúvida` |
| ⭐ Destaque? | Checkbox | Marcar se for especial |

### Dados de exemplo:

| Frase/Trecho | Livro | Página | Tipo |
|---|---|---|---|
| "Você não sobe ao nível das suas metas, cai ao nível dos seus sistemas." | Hábitos Atômicos | 28 | 💬 Citação |
| "Toda ação é um voto para o tipo de pessoa que você quer se tornar." | Hábitos Atômicos | 39 | 💬 Citação |
| Aplicar a regra dos 2 minutos na minha rotina | Hábitos Atômicos | 162 | 💡 Insight |
| "Conhecimento é poder." | Sapiens | 285 | 💬 Citação |

---

## 📊 DATABASE 3: "Meta de Leitura Anual"

### Propriedades:

| Propriedade | Tipo | Opções |
|---|---|---|
| 📅 Ano | Title | Ex: "2026" |
| 🎯 Meta | Number | Quantos livros quer ler |
| 📖 Lidos | Rollup | Conta livros com Status = Lido e Fim no ano |
| 📊 Progresso | Formula | `round(prop("Lidos") / prop("Meta") * 100)` |
| 📝 Reflexão | Text | Como foi o ano de leituras |

### Dados de exemplo:

| Ano | Meta | Lidos | Progresso |
|---|---|---|---|
| 2026 | 24 livros | 4 | 17% |
| 2025 | 12 livros | 15 | 125% 🎉 |

---

## 📊 DATABASE 4: "Wishlist / Lista de Desejos"

### Propriedades:

| Propriedade | Tipo | Opções |
|---|---|---|
| 📖 Título | Title | Nome do livro |
| ✍️ Autor | Text | Autor |
| 💰 Preço Estimado | Number | R$ |
| 📂 Onde comprar | Select | `🛒 Amazon` / `📦 Estante Virtual` / `🏪 Livraria` / `📱 Kindle` |
| 🎯 Prioridade | Select | `🔴 Quero muito` / `🟡 Interessante` / `🟢 Talvez` |
| 👤 Quem indicou | Text | Nome de quem indicou |
| 🔗 Link | URL | Link para compra |

### Dados de exemplo:

| Título | Autor | Preço | Onde | Prioridade |
|---|---|---|---|---|
| A Coragem de Ser Imperfeito | Brené Brown | R$ 39 | 🛒 Amazon | 🔴 Quero muito |
| Thinking Fast and Slow | Daniel Kahneman | R$ 55 | 📱 Kindle | 🟡 Interessante |
| As Crônicas de Nárnia (Box) | C.S. Lewis | R$ 89 | 🛒 Amazon | 🟢 Talvez |

---

## 🧩 LAYOUT DA PÁGINA PRINCIPAL

```
┌──────────────────────────────────────────────┐
│  📖 Minha Estante Virtual                    │
│  [Texto de boas-vindas]                      │
├──────────────────┬───────────────────────────┤
│                  │                           │
│  📊 Meta 2026    │  📖 Lendo Agora          │
│  Callout:        │  (Table filtrada:        │
│  "4 de 24 livros"│   Status = Lendo)        │
│  [barra visual]  │                           │
│                  │                           │
├──────────────────┴───────────────────────────┤
│                                              │
│  📚 Minha Estante                            │
│  (Gallery view — todos os livros)            │
│                                              │
├──────────────────────────────────────────────┤
│                                              │
│  💬 Frases & Anotações Favoritas             │
│  (Table filtrada: Destaque = True)           │
│                                              │
├──────────────────────────────────────────────┤
│                                              │
│  🛒 Wishlist — Próximas Leituras             │
│  (Table da Wishlist)                         │
│                                              │
└──────────────────────────────────────────────┘
```

---

## 📌 CALLOUT BOXES — Resumo

**Callout 1 (grande):**
```
📊 Meta de Leitura 2026
📖 4 de 24 livros lidos
████░░░░░░░░░░░░ 17%

Próximo marco: 6 livros (25%) 🎯
```

**Callout 2:**
```
📖 Lendo agora:
• Duna — 45%
• A Sutil Arte... — 30%
```

> **Cores:** Bege/marrom para meta, Azul para lendo

---

## 📑 PÁGINA EXTRA: "Desafios de Leitura"

```
🏆 Desafios de Leitura 2026

Complete estes desafios para ampliar seus horizontes literários!

🎯 Desafio Principal: Ler 24 livros no ano (2 por mês)

📋 Desafio de Diversidade:
- [ ] 📖 Um livro de autor brasileiro
- [ ] 🌍 Um livro traduzido de outro idioma
- [ ] 📜 Um clássico da literatura
- [ ] 🧠 Um livro de não-ficção
- [ ] 🚀 Um livro de ficção científica
- [ ] 📕 Um livro com menos de 150 páginas
- [ ] 📚 Um livro com mais de 500 páginas
- [ ] 🎧 Um audiobook
- [ ] 👤 Um livro indicado por amigo
- [ ] 🏆 Um livro premiado (Nobel, Pulitzer, etc.)
- [ ] ❤️ Reler um livro favorito
- [ ] 🆕 Um autor que nunca leu

Quantos você vai completar? 🏅
```

---

## ✅ CHECKLIST DE MONTAGEM NO NOTION

- [ ] Criar página principal "📖 Minha Estante Virtual"
- [ ] Adicionar capa (tons quentes/bege) e ícone 📖
- [ ] Escrever texto de boas-vindas
- [ ] Criar database "Meus Livros" (14 propriedades + fórmula + 6 views)
- [ ] Criar database "Frases & Anotações" (5 propriedades + relação)
- [ ] Criar database "Meta de Leitura Anual" (5 propriedades)
- [ ] Criar database "Wishlist" (7 propriedades)
- [ ] Configurar relações entre databases
- [ ] Montar layout com colunas (Meta + Lendo)
- [ ] Adicionar callout boxes de resumo
- [ ] Preencher TODOS os dados de exemplo
- [ ] Criar subpágina "Desafios de Leitura"
- [ ] Testar fórmula de progresso
- [ ] Testar todas as views
- [ ] Publicar e ativar "Allow duplicate as template"
