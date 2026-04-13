"""
Gerador do PDF de Venda - Pack 10 Templates Notion
Design baseado nos criativos: fundo preto, texto branco, estilo clean.
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable
)
import os

# ── CORES (baseadas nos criativos) ─────────────────────
BG_BLACK = HexColor("#0A0A0A")
CARD_BG = HexColor("#141414")
CARD_BORDER = HexColor("#2A2A2A")
TEXT_WHITE = HexColor("#FFFFFF")
TEXT_LIGHT = HexColor("#E5E5E5")
TEXT_GRAY = HexColor("#999999")
TEXT_MUTED = HexColor("#666666")
ACCENT_BLUE = HexColor("#4A9EFF")
CHECK_GREEN = HexColor("#22C55E")

# ── PATHS ──────────────────────────────────────────────
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PDF = os.path.join(OUTPUT_DIR, "10-Templates-Notion-Organizar.pdf")
NOTION_LINK = (
    "https://vivacious-promise-9da.notion.site/"
    "10-Templates-para-se-Organizar-33ffc3bc379680a9b878fe845f20bb16?pvs=141"
)


# ── BACKGROUND CALLBACK ─────────────────────────────────
def draw_bg(canvas, doc):
    """Draws solid black background on every page, BEFORE content."""
    canvas.saveState()
    w, h = A4
    canvas.setFillColor(BG_BLACK)
    canvas.rect(0, 0, w, h, fill=1, stroke=0)
    canvas.restoreState()


# ── ESTILOS ────────────────────────────────────────────
def S(name, **kw):
    """Shortcut to create ParagraphStyle."""
    defaults = {"fontName": "Helvetica", "textColor": TEXT_WHITE}
    defaults.update(kw)
    return ParagraphStyle(name, **defaults)


STYLES = {
    # Pagina 1
    "badge": S("badge", fontName="Helvetica-Bold", fontSize=11, leading=14,
               textColor=TEXT_GRAY, alignment=TA_CENTER),
    "hero_title": S("hero_title", fontName="Helvetica-Bold", fontSize=36,
                     leading=42, alignment=TA_CENTER, spaceAfter=6),
    "hero_sub": S("hero_sub", fontName="Helvetica-Oblique", fontSize=16,
                   leading=22, textColor=TEXT_GRAY, alignment=TA_CENTER),
    "price_label": S("price_label", fontName="Helvetica-Oblique", fontSize=14,
                      leading=18, textColor=TEXT_GRAY, alignment=TA_CENTER),
    "price_note": S("price_note", fontName="Helvetica-Oblique", fontSize=11,
                     leading=15, textColor=TEXT_GRAY, alignment=TA_CENTER),

    # Pagina 2
    "section_title": S("section_title", fontName="Helvetica-Bold", fontSize=24,
                        leading=30, alignment=TA_CENTER, spaceAfter=10),
    "section_sub": S("section_sub", fontName="Helvetica-Oblique", fontSize=12,
                      leading=16, textColor=TEXT_GRAY, alignment=TA_CENTER),

    # Pagina 3
    "step_num": S("step_num", fontName="Helvetica-Bold", fontSize=32,
                   leading=36, textColor=TEXT_MUTED, alignment=TA_CENTER),
    "step_title": S("step_title", fontName="Helvetica-Bold", fontSize=14,
                     leading=18, alignment=TA_CENTER, spaceAfter=4),
    "step_desc": S("step_desc", fontName="Helvetica", fontSize=10,
                    leading=15, textColor=TEXT_GRAY, alignment=TA_CENTER),

    # Pagina 4
    "cta_title": S("cta_title", fontName="Helvetica-Bold", fontSize=26,
                    leading=32, alignment=TA_CENTER),
    "cta_sub": S("cta_sub", fontName="Helvetica", fontSize=12,
                  leading=17, textColor=TEXT_LIGHT, alignment=TA_CENTER),
    "link_label": S("link_label", fontName="Helvetica-Bold", fontSize=14,
                     leading=18, alignment=TA_CENTER),
    "link_url": S("link_url", fontName="Helvetica", fontSize=8,
                   leading=12, textColor=ACCENT_BLUE, alignment=TA_CENTER),
    "recap_item": S("recap_item", fontName="Helvetica", fontSize=11,
                     leading=18, textColor=TEXT_LIGHT, alignment=TA_CENTER),
    "footer": S("footer", fontName="Helvetica", fontSize=9,
                 leading=13, textColor=TEXT_MUTED, alignment=TA_CENTER),
    "thanks": S("thanks", fontName="Helvetica-Bold", fontSize=16,
                 leading=22, alignment=TA_CENTER),
}


# ── TEMPLATES DATA ─────────────────────────────────────
TEMPLATES = [
    ("Controle Financeiro Pessoal",
     "Gerencie receitas, despesas, metas de economia e assinaturas."),
    ("Planner de Estudos Completo",
     "Cronograma, flashcards, revisao espacada e progresso por materia."),
    ("Rastreador de Habitos",
     "Acompanhe habitos diarios, sequencias e revisoes semanais."),
    ("Planejador Semanal",
     "Kanban por dia, metas semanais, notas rapidas e planejamento."),
    ("Minha Estante Virtual",
     "Catalogue livros, progresso de leitura, wishlist e anotacoes."),
    ("Tracker de Treinos",
     "Registre exercicios, medidas corporais e acompanhe evolucao."),
    ("Planejador de Viagem",
     "Organize destinos, itinerarios, orcamentos e packing list."),
    ("Dashboard Freelancer",
     "Gerencie clientes, projetos, receitas e prazos."),
    ("Planejador de Refeicoes",
     "Cardapio semanal, lista de compras e receitas favoritas."),
    ("Diario Pessoal",
     "Reflexoes diarias, gratidao, humor e bem-estar emocional."),
]


def build_pdf():
    doc = SimpleDocTemplate(
        OUTPUT_PDF,
        pagesize=A4,
        topMargin=0,
        bottomMargin=15 * mm,
        leftMargin=22 * mm,
        rightMargin=22 * mm,
    )

    W = A4[0] - 44 * mm  # usable width
    story = []
    s = STYLES

    # ══════════════════════════════════════════════════
    # PAGINA 1 — HERO / CAPA
    # ══════════════════════════════════════════════════
    story.append(Spacer(1, 55 * mm))

    story.append(Paragraph("PACK COMPLETO", s["badge"]))
    story.append(Spacer(1, 12 * mm))

    story.append(Paragraph("10 Templates", s["hero_title"]))
    story.append(Paragraph("para se Organizar", s["hero_sub"]))
    story.append(Spacer(1, 25 * mm))

    # Bullets
    bullets = [
        "Acesso imediato",
        "Acesso vitalicio",
        "Nao precisa pagar mais nada",
    ]
    for i, b in enumerate(bullets):
        bullet_style = S(
            f"bullet_{i}",
            fontName="Helvetica-Bold",
            fontSize=14,
            leading=20,
            textColor=TEXT_WHITE,
            alignment=TA_CENTER,
        )
        story.append(Paragraph(
            f'<font color="#22C55E">&#10003;</font>  {b}',
            bullet_style
        ))
        story.append(Spacer(1, 3 * mm))

    story.append(Spacer(1, 20 * mm))

    # Preco
    story.append(Paragraph("POR APENAS", s["price_label"]))
    story.append(Spacer(1, 4 * mm))

    price_p = Paragraph(
        'R$ <font size="56"><b>17</b></font>,00',
        S("price_inner", fontName="Helvetica", fontSize=22, leading=60,
          textColor=TEXT_WHITE, alignment=TA_CENTER)
    )
    price_tbl = Table([[price_p]], colWidths=[120 * mm])
    price_tbl.setStyle(TableStyle([
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 12),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
        ("BOX", (0, 0), (-1, -1), 1, CARD_BORDER),
        ("ROUNDEDCORNERS", [12, 12, 12, 12]),
        ("BACKGROUND", (0, 0), (-1, -1), CARD_BG),
    ]))
    price_tbl.hAlign = "CENTER"
    story.append(price_tbl)
    story.append(Spacer(1, 8 * mm))

    story.append(Paragraph("so duplicar e usar", s["price_note"]))

    story.append(PageBreak())

    # ══════════════════════════════════════════════════
    # PAGINA 2 — LISTA DOS 10 TEMPLATES
    # ══════════════════════════════════════════════════
    story.append(Spacer(1, 18 * mm))

    story.append(Paragraph("O que voce recebe", s["section_title"]))
    story.append(Paragraph(
        "10 templates prontos para duplicar no Notion",
        s["section_sub"]
    ))
    story.append(Spacer(1, 10 * mm))

    tpl_rows = []
    for idx, (name, desc) in enumerate(TEMPLATES, 1):
        num_p = Paragraph(
            f"{idx:02d}.",
            S(f"n_{idx}", fontName="Helvetica-Bold", fontSize=12,
              leading=16, textColor=TEXT_MUTED)
        )
        name_p = Paragraph(
            name,
            S(f"nm_{idx}", fontName="Helvetica-Bold", fontSize=13,
              leading=17, textColor=TEXT_WHITE)
        )
        desc_p = Paragraph(
            desc,
            S(f"d_{idx}", fontName="Helvetica", fontSize=10,
              leading=14, textColor=TEXT_GRAY)
        )
        # Need to use a nested list for multi-paragraph cells
        cell_content = Table(
            [[name_p], [desc_p]],
            colWidths=[W - 28 * mm],
        )
        cell_content.setStyle(TableStyle([
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
        ]))
        tpl_rows.append([num_p, cell_content])

    tpl_tbl = Table(tpl_rows, colWidths=[14 * mm, W - 28 * mm])
    tpl_tbl.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING", (0, 0), (0, -1), 12),
        ("LEFTPADDING", (1, 0), (1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("BACKGROUND", (0, 0), (-1, -1), CARD_BG),
        ("BOX", (0, 0), (-1, -1), 0.5, CARD_BORDER),
        ("LINEBELOW", (0, 0), (-1, -2), 0.3, CARD_BORDER),
        ("ROUNDEDCORNERS", [10, 10, 10, 10]),
    ]))
    tpl_tbl.hAlign = "CENTER"
    story.append(tpl_tbl)

    story.append(PageBreak())

    # ══════════════════════════════════════════════════
    # PAGINA 3 — BENEFICIOS + COMO FUNCIONA
    # ══════════════════════════════════════════════════
    story.append(Spacer(1, 18 * mm))

    story.append(Paragraph("Por que esse pack?", s["section_title"]))
    story.append(Spacer(1, 8 * mm))

    benefits = [
        ("100% em Portugues",
         "Tudo adaptado para a realidade brasileira."),
        ("Dados de Exemplo",
         "Cada template vem preenchido para voce entender."),
        ("Pronto para Usar",
         "Duplique no seu Notion e comece agora."),
        ("Editavel",
         "Personalize cores, campos e layouts."),
        ("10 Areas da Vida",
         "Financas, estudos, habitos, treinos e mais."),
        ("Atualizacoes Gratis",
         "Novos templates sem custo adicional."),
    ]

    ben_rows = []
    for i in range(0, len(benefits), 2):
        left_t, left_d = benefits[i]
        right_t, right_d = benefits[i + 1] if i + 1 < len(benefits) else ("", "")

        def make_cell(title, desc, uid):
            if not title:
                return Paragraph("", s["footer"])
            t = Paragraph(
                f'<font color="#22C55E">&#10003;</font>  {title}',
                S(f"bt_{uid}", fontName="Helvetica-Bold", fontSize=12,
                  leading=16, textColor=TEXT_WHITE, spaceAfter=3)
            )
            d = Paragraph(
                desc,
                S(f"bd_{uid}", fontName="Helvetica", fontSize=10,
                  leading=14, textColor=TEXT_GRAY)
            )
            inner = Table([[t], [d]], colWidths=[(W - 10 * mm) / 2 - 4 * mm])
            inner.setStyle(TableStyle([
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]))
            return inner

        col_w = (W - 10 * mm) / 2
        ben_rows.append([
            make_cell(left_t, left_d, f"L{i}"),
            make_cell(right_t, right_d, f"R{i}"),
        ])

    col_w = (W - 10 * mm) / 2
    ben_tbl = Table(ben_rows, colWidths=[col_w, col_w])
    ben_tbl.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
    ]))
    story.append(ben_tbl)

    story.append(Spacer(1, 12 * mm))

    story.append(HRFlowable(
        width="60%", thickness=0.5, color=CARD_BORDER,
        spaceAfter=10, spaceBefore=5
    ))

    story.append(Spacer(1, 8 * mm))
    story.append(Paragraph("Como funciona", s["section_title"]))
    story.append(Spacer(1, 8 * mm))

    steps_data = [
        ("01", "Acesse o Link",
         "Clique no link que voce\nrecebeu nesta pagina."),
        ("02", "Duplique no Notion",
         "Clique em Duplicar e copie\ntudo para o seu Notion."),
        ("03", "Comece a Usar",
         "Edite, personalize e\norganize sua vida."),
    ]

    step_cells = []
    for num, title, desc in steps_data:
        num_p = Paragraph(num, s["step_num"])
        sp = Spacer(1, 2 * mm)
        title_p = Paragraph(title, s["step_title"])
        desc_p = Paragraph(desc, s["step_desc"])
        inner = Table(
            [[num_p], [sp], [title_p], [desc_p]],
            colWidths=[W / 3 - 6 * mm]
        )
        inner.setStyle(TableStyle([
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 2),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
        ]))
        step_cells.append(inner)

    step_tbl = Table([step_cells], colWidths=[W / 3] * 3)
    step_tbl.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("TOPPADDING", (0, 0), (-1, -1), 14),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 14),
        ("BACKGROUND", (0, 0), (-1, -1), CARD_BG),
        ("BOX", (0, 0), (-1, -1), 0.5, CARD_BORDER),
        ("LINEBEFORE", (1, 0), (1, 0), 0.3, CARD_BORDER),
        ("LINEBEFORE", (2, 0), (2, 0), 0.3, CARD_BORDER),
        ("ROUNDEDCORNERS", [10, 10, 10, 10]),
    ]))
    story.append(step_tbl)

    story.append(PageBreak())

    # ══════════════════════════════════════════════════
    # PAGINA 4 — CTA / LINK DE ACESSO
    # ══════════════════════════════════════════════════
    story.append(Spacer(1, 35 * mm))

    story.append(Paragraph(
        "Acesse seus 10 Templates:",
        s["cta_title"]
    ))
    story.append(Spacer(1, 6 * mm))
    story.append(Paragraph(
        'Clique no link abaixo ou copie e cole no navegador.',
        s["cta_sub"]
    ))
    story.append(Spacer(1, 2 * mm))
    story.append(Paragraph(
        'Depois clique em <b>"Duplicar"</b> no canto superior direito do Notion.',
        s["cta_sub"]
    ))
    story.append(Spacer(1, 12 * mm))

    # Link box
    link_label_p = Paragraph("ACESSAR TEMPLATES", s["link_label"])
    link_sp = Spacer(1, 3 * mm)
    link_url_p = Paragraph(
        f'<a href="{NOTION_LINK}" color="#4A9EFF">'
        f'{NOTION_LINK}</a>',
        s["link_url"]
    )
    link_inner = Table(
        [[link_label_p], [link_sp], [link_url_p]],
        colWidths=[W - 20 * mm]
    )
    link_inner.setStyle(TableStyle([
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))

    link_tbl = Table([[link_inner]], colWidths=[W - 16 * mm])
    link_tbl.setStyle(TableStyle([
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 16),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 16),
        ("LEFTPADDING", (0, 0), (-1, -1), 14),
        ("RIGHTPADDING", (0, 0), (-1, -1), 14),
        ("BOX", (0, 0), (-1, -1), 1, TEXT_WHITE),
        ("ROUNDEDCORNERS", [12, 12, 12, 12]),
        ("BACKGROUND", (0, 0), (-1, -1), CARD_BG),
    ]))
    link_tbl.hAlign = "CENTER"
    story.append(link_tbl)

    story.append(Spacer(1, 18 * mm))

    story.append(HRFlowable(
        width="40%", thickness=0.5, color=CARD_BORDER,
        spaceAfter=10, spaceBefore=5
    ))

    story.append(Spacer(1, 8 * mm))

    story.append(Paragraph(
        "<b>Recapitulando:</b>",
        S("recap_h", fontName="Helvetica-Bold", fontSize=14, leading=18,
          textColor=TEXT_WHITE, alignment=TA_CENTER)
    ))
    story.append(Spacer(1, 6 * mm))

    for idx, (name, _) in enumerate(TEMPLATES, 1):
        story.append(Paragraph(
            f'<font color="#22C55E">&#10003;</font>  {idx}. {name}',
            s["recap_item"]
        ))

    story.append(Spacer(1, 16 * mm))

    story.append(Paragraph("Obrigado pela compra!", s["thanks"]))
    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph(
        "Em caso de duvidas, entre em contato pelo mesmo canal de compra.",
        s["footer"]
    ))

    # ── BUILD with background callback ─────────────────
    doc.build(story, onFirstPage=draw_bg, onLaterPages=draw_bg)
    print("\n[OK] PDF gerado com sucesso!")
    print(f"Arquivo: {OUTPUT_PDF}\n")


if __name__ == "__main__":
    build_pdf()
