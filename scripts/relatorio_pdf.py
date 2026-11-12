#!/usr/bin/env python3
"""Gera o PDF one page (A4) do relatório executivo do nao-reinventar-roda.

Uso:
    python3 relatorio_pdf.py <05-relatorio.json> <saida.pdf> [--png <previa.png>]

Entrada: o JSON de conteúdo descrito em referencia/modelos.md (seção 05-relatorio.json).
Dependência: reportlab. Para a prévia em PNG, pymupdf (opcional).
O texto aceita as marcas <b> e <i> do reportlab; escape &, < e > do resto.
"""
import json
import math
import sys

try:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import mm
    from reportlab.platypus import (BaseDocTemplate, Flowable, Frame, PageTemplate,
                                    Paragraph, Spacer, Table, TableStyle)
except ImportError:
    sys.exit("Falta a biblioteca reportlab. Instale com: python3 -m pip install reportlab")

FG = colors.HexColor("#15181d")
MU = colors.HexColor("#5d6572")
LN = colors.HexColor("#dfe3e8")
TI = colors.HexColor("#f6f7f9")
STOPS = [(0, colors.HexColor("#2f6fd6")), (.4, colors.HexColor("#5aa4c9")),
         (.7, colors.HexColor("#e0a326")), (1, colors.HexColor("#d2462f"))]


def style(name, **kw):
    base = dict(fontName="Helvetica", fontSize=8.6, leading=11.2, textColor=FG)
    base.update(kw)
    return ParagraphStyle(name, **base)


def build(data, out):
    accent = colors.HexColor(data.get("cor_veredito", "#c23b28"))
    body = style("b")
    small = style("s", fontSize=7.6, leading=9.6)
    muted = style("m", fontSize=7.4, leading=9.4, textColor=MU)
    h2 = style("h2", fontName="Helvetica-Bold", fontSize=7.4, leading=9, textColor=MU)
    h1 = style("h1", fontName="Helvetica-Bold", fontSize=17, leading=20.5)
    big = style("big", fontName="Helvetica-Bold", fontSize=14, leading=16, textColor=accent)
    rtitle = style("rt", fontName="Helvetica-Bold", fontSize=9.4, leading=11.5)
    rlabel = style("rn", fontName="Helvetica-Bold", fontSize=6.8, leading=8.5, textColor=accent)
    th = style("th", fontName="Helvetica-Bold", fontSize=6.8, textColor=MU)
    foot = style("f", fontSize=6.6, leading=8.6, textColor=MU)

    def P(text, st=body):
        return Paragraph(text, st)

    def H(text):
        return P(text.upper(), h2)

    def ref(r):
        return f' <font size="6.2" color="#5d6572">{r}</font>' if r else ""

    class Gauge(Flowable):
        def __init__(self, w, h, needles):
            super().__init__()
            self.w, self.h, self.needles = w, h, needles

        def wrap(self, *a):
            return self.w, self.h

        def draw(self):
            c = self.canv
            cx, cy = self.w / 2, 14
            r = min(self.w / 2 - 12, self.h - 24)

            def col(t):
                for (a, ca), (b, cb) in zip(STOPS, STOPS[1:]):
                    if t <= b:
                        f = (t - a) / (b - a)
                        return colors.Color(ca.red + (cb.red - ca.red) * f,
                                            ca.green + (cb.green - ca.green) * f,
                                            ca.blue + (cb.blue - ca.blue) * f)
                return STOPS[-1][1]

            c.setLineWidth(11)
            n = 60
            for i in range(n):
                a0, a1 = 180 - 180 * i / n, 180 - 180 * (i + 1) / n
                c.setStrokeColor(col(i / n))
                p = c.beginPath()
                p.arc(cx - r, cy - r, cx + r, cy + r, startAng=a1, extent=a0 - a1 + 0.6)
                c.drawPath(p, stroke=1, fill=0)

            # secundárias primeiro, principal por cima
            order = sorted(self.needles, key=lambda x: bool(x.get("principal")))
            used = []
            for nd in order:
                t = max(0, min(100, float(nd["t"])))
                main = bool(nd.get("principal"))
                th_ = math.radians(180 - 1.8 * t)
                L = r * (0.88 if main else 0.78)
                colr = FG if main else MU
                c.setStrokeColor(colr)
                c.setLineWidth(2.8 if main else 2)
                c.setLineCap(1)
                c.line(cx, cy, cx + L * math.cos(th_), cy + L * math.sin(th_))
                label = f'{nd["letra"]} · {int(round(t))}'
                c.setFillColor(colr)
                c.setFont("Helvetica-Bold", 7.5)
                if t < 25:
                    # agulha quase deitada: rótulo embaixo dela, rente à base
                    x, y = cx - r * 0.70, cy + 3
                elif t > 75:
                    x, y = cx + r * 0.40, cy + 3
                else:
                    rr = r * (0.62 if main else 0.48)
                    x, y = cx + rr * math.cos(th_) + 5, cy + rr * math.sin(th_)
                for ux, uy in used:  # evita rótulos sobrepostos
                    if abs(ux - x) < 30 and abs(uy - y) < 9:
                        y -= 11
                used.append((x, y))
                c.drawString(x, y, label)
            c.setFillColor(FG)
            c.circle(cx, cy, 4, fill=1, stroke=0)
            c.setFillColor(MU)
            c.setFont("Helvetica", 6.5)
            c.drawString(cx - r - 4, cy - 11, "0 · já existe")
            c.drawRightString(cx + r + 4, cy - 11, "lacuna aberta · 100")

    W, Hh = A4
    M = 12 * mm
    CW = W - 2 * M
    doc = BaseDocTemplate(out, pagesize=A4, leftMargin=M, rightMargin=M, topMargin=M, bottomMargin=M,
                          title=data.get("titulo_curto", "Relatório"), author=data.get("autor", ""))
    doc.addPageTemplates([PageTemplate(frames=[Frame(M, M, CW, Hh - 2 * M, 0, 0, 0, 0)])])

    st = []
    meta = data["meta"].upper()
    if data.get("previa"):
        meta += "  ·  PRÉVIA · SEM VEREDITO FORMAL"
    st += [P(meta, muted), Spacer(1, 3), P(data["titulo"], h1), Spacer(1, 8)]

    left = [H("A ideia"), Spacer(1, 2), P(data["ideia"], style("i", fontSize=9.6, leading=13)),
            Spacer(1, 7), H("Pesquisa realizada"), Spacer(1, 2), P(data["pesquisa"])]
    gw = CW * 0.40 - 16
    right = [H("Veredito"), Spacer(1, 2), P(data["veredito"], big), Spacer(1, 2),
             Gauge(gw, 92, data["agulhas"]), Spacer(1, 3), P(data["nota_medidor"], small)]
    top = Table([[left, right]], colWidths=[CW * 0.60 - 6, CW * 0.40 + 6])
    top.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (0, 0), 0),
        ("RIGHTPADDING", (0, 0), (0, 0), 12), ("BOX", (1, 0), (1, 0), 1.4, accent),
        ("LEFTPADDING", (1, 0), (1, 0), 9), ("RIGHTPADDING", (1, 0), (1, 0), 9),
        ("TOPPADDING", (1, 0), (1, 0), 8), ("BOTTOMPADDING", (1, 0), (1, 0), 8)]))
    st += [top, Spacer(1, 10), H(data.get("motivos_titulo", "Por que não é viável")), Spacer(1, 4)]

    cells = [[P(m["rotulo"].upper(), rlabel), Spacer(1, 2), P(m["titulo"], rtitle), Spacer(1, 3),
              P(m["texto"] + ref(m.get("ref")), small)] for m in data["motivos"][:3]]
    t = Table([cells], colWidths=[(CW - 12) / 3] * len(cells))
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"), ("BACKGROUND", (0, 0), (-1, -1), TI),
        ("INNERGRID", (0, 0), (-1, -1), 6, colors.white),
        ("LEFTPADDING", (0, 0), (-1, -1), 8), ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 8), ("BOTTOMPADDING", (0, 0), (-1, -1), 8)]))
    st += [t, Spacer(1, 10)]

    lw = CW * 0.54
    rows = [[P("EMPRESA", th), P("O QUE ENTREGA", th), P("MODELO", th)]]
    rows += [[P(f'<b>{m["empresa"]}</b>', small), P(m["entrega"] + ref(m.get("ref")), small),
              P(m["modelo"], muted)] for m in data["mercado"][:10]]
    mt = Table(rows, colWidths=[lw * 0.27, lw * 0.47, lw * 0.26])
    mt.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"), ("LINEABOVE", (0, 1), (-1, -1), 0.5, LN),
        ("LEFTPADDING", (0, 0), (-1, -1), 3), ("RIGHTPADDING", (0, 0), (-1, -1), 3),
        ("TOPPADDING", (0, 0), (-1, -1), 2.6), ("BOTTOMPADDING", (0, 0), (-1, -1), 2.6)]))

    rw = CW - lw - 14
    ev = data.get("casos") or [{"ano": "", "texto": "Nenhum caso com data encontrado."}]
    et = Table([[P(e["ano"], muted), P(e["texto"] + ref(e.get("ref")), small)] for e in ev],
               colWidths=[26, rw - 26])
    et.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"), ("LINEABOVE", (0, 1), (-1, -1), 0.5, LN),
        ("LEFTPADDING", (0, 0), (-1, -1), 2), ("TOPPADDING", (0, 0), (-1, -1), 2.4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2.4)]))
    who = [P(f'• <b>{q["quem"]}:</b> {q["texto"]}' + ref(q.get("ref")), small)
           for q in data.get("quem_usa", [])] or [P("Não encontrado nas buscas.", small)]
    if data.get("leitura_casos"):
        who += [Spacer(1, 2), P(data["leitura_casos"], muted)]
    two = Table([[[H("Mercado: quem já faz"), Spacer(1, 3), mt],
                  [H("Casos: o que acontece com quem entra"), Spacer(1, 3), et, Spacer(1, 7),
                   H("Quem usa e como resolve hoje"), Spacer(1, 3)] + who]],
                colWidths=[lw + 14, rw])
    two.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (0, 0), 14), ("RIGHTPADDING", (1, 0), (1, 0), 0)]))
    st += [two, Spacer(1, 10)]

    rc = data["recomendacao"][:3]
    rt2 = Table([[[P(x["titulo"], rtitle), Spacer(1, 2), P(x["texto"], small)] for x in rc]],
                colWidths=[CW / len(rc)] * len(rc))
    rt2.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"), ("LINEABOVE", (0, 0), (-1, 0), 1.6, FG),
        ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 7)]))
    st += [rt2, Spacer(1, 9)]

    ft = Table([[P(data["rodape"], foot)]], colWidths=[CW])
    ft.setStyle(TableStyle([("LINEABOVE", (0, 0), (-1, 0), 0.5, LN),
                            ("LEFTPADDING", (0, 0), (-1, -1), 0), ("TOPPADDING", (0, 0), (-1, -1), 5)]))
    st.append(ft)
    doc.build(st)


def main():
    args = sys.argv[1:]
    if len(args) < 2:
        sys.exit(__doc__)
    src, out = args[0], args[1]
    with open(src, encoding="utf-8") as fh:
        data = json.load(fh)
    build(data, out)
    pages = None
    if "--png" in args:
        try:
            import pymupdf
            d = pymupdf.open(out)
            pages = d.page_count
            d[0].get_pixmap(dpi=110).save(args[args.index("--png") + 1])
        except ImportError:
            print("pymupdf ausente: prévia PNG não gerada")
    print(f"PDF gravado: {out}" + (f" ({pages} página(s))" if pages else ""))
    if pages and pages > 1:
        print("AVISO: passou de uma página. Encurte textos ou reduza linhas de mercado e casos.")


if __name__ == "__main__":
    main()
