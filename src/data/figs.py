"""문항에 넣는 그림(SVG)과 표를 만드는 도우미.
선 색은 currentColor 를 써서 밝은 화면·어두운 화면 모두에서 보이게 한다."""

import math


def _num(v):
    return f"{v:.1f}".rstrip("0").rstrip(".")


def table(head, rows, caption=""):
    h = "".join(f"<th>{x}</th>" for x in head)
    r = "".join("<tr>" + "".join(f"<td>{x}</td>" for x in row) + "</tr>" for row in rows)
    cap = f"<caption>{caption}</caption>" if caption else ""
    return f"<div class='tblwrap'><table class='tbl'>{cap}<thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>"


class Plot:
    """좌표평면 그림. 수학 좌표(x, y)를 받아 SVG 좌표로 바꾼다."""

    def __init__(self, xmin, xmax, ymin, ymax, w=280, h=230, pad=22, axes=True, xlabel="x", ylabel="y", origin=True, equal=False):
        if equal:  # 가로·세로 눈금 간격을 같게(원이 찌그러지지 않게)
            h = round((ymax - ymin) / (xmax - xmin) * (w - 2 * pad) + 2 * pad)
        self.xmin, self.xmax, self.ymin, self.ymax = xmin, xmax, ymin, ymax
        self.w, self.h, self.pad = w, h, pad
        self.parts = []
        if axes:
            x0, y0 = self.X(max(min(0, xmax), xmin)), self.Y(max(min(0, ymax), ymin))
            self.parts.append(f"<line x1='{pad - 6}' y1='{_num(y0)}' x2='{w - pad + 8}' y2='{_num(y0)}' stroke='currentColor' stroke-width='1.2' marker-end='url(#ar)'/>")
            self.parts.append(f"<line x1='{_num(x0)}' y1='{h - pad + 6}' x2='{_num(x0)}' y2='{pad - 8}' stroke='currentColor' stroke-width='1.2' marker-end='url(#ar)'/>")
            self.text(xmax, 0, xlabel, dx=10, dy=4, raw=True)
            self.parts.append(f"<text x='{_num(x0 + 6)}' y='{pad - 6}' font-size='13' font-style='italic' fill='currentColor'>{ylabel}</text>")
            if origin and xmin <= 0 <= xmax and ymin <= 0 <= ymax:
                self.parts.append(f"<text x='{_num(x0 - 13)}' y='{_num(y0 + 14)}' font-size='12' fill='currentColor'>O</text>")

    def X(self, x):
        return self.pad + (x - self.xmin) / (self.xmax - self.xmin) * (self.w - 2 * self.pad)

    def Y(self, y):
        return self.h - self.pad - (y - self.ymin) / (self.ymax - self.ymin) * (self.h - 2 * self.pad)

    def curve(self, f, a=None, b=None, n=200, dash=False, width=2):
        a = self.xmin if a is None else a
        b = self.xmax if b is None else b
        pts, segs = [], []
        for i in range(n + 1):
            x = a + (b - a) * i / n
            try:
                y = f(x)
            except (ValueError, ZeroDivisionError):
                y = None
            if y is None or not (self.ymin - 1 <= y <= self.ymax + 1):
                if len(pts) > 1:
                    segs.append(pts)
                pts = []
                continue
            pts.append(f"{_num(self.X(x))},{_num(self.Y(y))}")
        if len(pts) > 1:
            segs.append(pts)
        d = " stroke-dasharray='5 4'" if dash else ""
        for s in segs:
            self.parts.append(f"<polyline points='{' '.join(s)}' fill='none' stroke='currentColor' stroke-width='{width}'{d}/>")
        return self

    def seg(self, x1, y1, x2, y2, dash=False, width=1.4):
        d = " stroke-dasharray='4 3'" if dash else ""
        self.parts.append(f"<line x1='{_num(self.X(x1))}' y1='{_num(self.Y(y1))}' x2='{_num(self.X(x2))}' y2='{_num(self.Y(y2))}' stroke='currentColor' stroke-width='{width}'{d}/>")
        return self

    def poly(self, pts, fill=False, width=1.6):
        p = " ".join(f"{_num(self.X(x))},{_num(self.Y(y))}" for x, y in pts)
        f = "fill='currentColor' fill-opacity='.15'" if fill else "fill='none'"
        self.parts.append(f"<polygon points='{p}' {f} stroke='currentColor' stroke-width='{width}'/>")
        return self

    def shade(self, f, g, a, b, n=80):
        top = [(a + (b - a) * i / n, f(a + (b - a) * i / n)) for i in range(n + 1)]
        bot = [(a + (b - a) * i / n, g(a + (b - a) * i / n)) for i in range(n, -1, -1)]
        p = " ".join(f"{_num(self.X(x))},{_num(self.Y(y))}" for x, y in top + bot)
        self.parts.append(f"<polygon points='{p}' fill='currentColor' fill-opacity='.18' stroke='none'/>")
        return self

    def dot(self, x, y, label="", dx=6, dy=-6, open_=False):
        fill = "none" if open_ else "currentColor"
        self.parts.append(f"<circle cx='{_num(self.X(x))}' cy='{_num(self.Y(y))}' r='3' fill='{fill}' stroke='currentColor' stroke-width='1.3'/>")
        if label:
            self.text(x, y, label, dx=dx, dy=dy)
        return self

    def text(self, x, y, s, dx=0, dy=0, size=13, raw=False, italic=False):
        X = (self.w - self.pad + 8) if raw else self.X(x)
        Y = self.Y(y)
        it = " font-style='italic'" if italic or raw else ""
        self.parts.append(f"<text x='{_num(X + dx)}' y='{_num(Y + dy)}' font-size='{size}' fill='currentColor'{it}>{s}</text>")
        return self

    def tick(self, x=None, y=None, label=None):
        if x is not None:
            X, Y = self.X(x), self.Y(0)
            self.parts.append(f"<line x1='{_num(X)}' y1='{_num(Y - 3)}' x2='{_num(X)}' y2='{_num(Y + 3)}' stroke='currentColor'/>")
            self.parts.append(f"<text x='{_num(X - 4)}' y='{_num(Y + 16)}' font-size='12' fill='currentColor'>{label if label is not None else _num(x)}</text>")
        if y is not None:
            X, Y = self.X(0), self.Y(y)
            self.parts.append(f"<line x1='{_num(X - 3)}' y1='{_num(Y)}' x2='{_num(X + 3)}' y2='{_num(Y)}' stroke='currentColor'/>")
            self.parts.append(f"<text x='{_num(X - 22)}' y='{_num(Y + 4)}' font-size='12' fill='currentColor'>{label if label is not None else _num(y)}</text>")
        return self

    def svg(self, caption=""):
        defs = ("<defs><marker id='ar' viewBox='0 0 10 10' refX='8' refY='5' markerWidth='7' markerHeight='7' orient='auto-start-reverse'>"
                "<path d='M0,0 L10,5 L0,10 z' fill='currentColor'/></marker></defs>")
        cap = f"<figcaption>{caption}</figcaption>" if caption else ""
        return (f"<figure class='fig'><svg viewBox='0 0 {self.w} {self.h}' width='{self.w}' height='{self.h}' role='img' "
                f"aria-label='{caption or '그림'}' font-family='inherit'>{defs}{''.join(self.parts)}</svg>{cap}</figure>")


def bars(labels, values, unit="", w=300, h=200, vmax=None, caption=""):
    """막대그래프."""
    vmax = vmax or max(values) * 1.15
    pad, n = 28, len(values)
    bw = (w - 2 * pad) / n
    out = [f"<line x1='{pad}' y1='{h - pad}' x2='{w - pad / 2}' y2='{h - pad}' stroke='currentColor'/>"]
    for i, (lab, v) in enumerate(zip(labels, values)):
        x = pad + i * bw + bw * 0.2
        bh = (h - 2 * pad) * v / vmax
        out.append(f"<rect x='{_num(x)}' y='{_num(h - pad - bh)}' width='{_num(bw * 0.6)}' height='{_num(bh)}' fill='currentColor' fill-opacity='.35' stroke='currentColor'/>")
        out.append(f"<text x='{_num(x + bw * 0.3)}' y='{_num(h - pad - bh - 4)}' font-size='12' text-anchor='middle' fill='currentColor'>{_num(v)}{unit}</text>")
        out.append(f"<text x='{_num(x + bw * 0.3)}' y='{h - pad + 15}' font-size='12' text-anchor='middle' fill='currentColor'>{lab}</text>")
    cap = f"<figcaption>{caption}</figcaption>" if caption else ""
    return f"<figure class='fig'><svg viewBox='0 0 {w} {h}' width='{w}' height='{h}' role='img' aria-label='{caption or '막대그래프'}'>{''.join(out)}</svg>{cap}</figure>"


def shape(points, edges, labels=None, extra=None, w=260, h=200, pad=24, caption="", fill=None):
    """도형 그림. points: {'A': (x, y)} (수학 좌표), edges: ['AB', ...], labels: {'A': (dx, dy)} 글자 위치 조정,
    extra: [('text', x, y, '5'), ('dash', 'AC'), ('right', 'B', 'A', 'C')]  ※ right = 꼭짓점 B의 직각 표시"""
    xs = [p[0] for p in points.values()]
    ys = [p[1] for p in points.values()]
    xmin, xmax, ymin, ymax = min(xs), max(xs), min(ys), max(ys)
    sc = min((w - 2 * pad) / ((xmax - xmin) or 1), (h - 2 * pad) / ((ymax - ymin) or 1))
    ox = (w - (xmax - xmin) * sc) / 2
    oy = (h - (ymax - ymin) * sc) / 2
    P = {k: (ox + (x - xmin) * sc, h - oy - (y - ymin) * sc) for k, (x, y) in points.items()}
    out = []
    if fill:
        p = " ".join(f"{_num(P[k][0])},{_num(P[k][1])}" for k in fill)
        out.append(f"<polygon points='{p}' fill='currentColor' fill-opacity='.15' stroke='none'/>")
    for e in edges:
        a, b = P[e[0]], P[e[1]]
        out.append(f"<line x1='{_num(a[0])}' y1='{_num(a[1])}' x2='{_num(b[0])}' y2='{_num(b[1])}' stroke='currentColor' stroke-width='1.6'/>")
    cx = sum(p[0] for p in P.values()) / len(P)
    cy = sum(p[1] for p in P.values()) / len(P)
    for k, (x, y) in P.items():
        dx, dy = (labels or {}).get(k, (None, None))
        if dx is None:
            vx, vy = x - cx, y - cy
            n = math.hypot(vx, vy) or 1
            dx, dy = vx / n * 12, vy / n * 12
        out.append(f"<text x='{_num(x + dx)}' y='{_num(y + dy + 4)}' font-size='14' text-anchor='middle' fill='currentColor'>{k}</text>")
    for ex in extra or []:
        if ex[0] == "text":
            _, x, y, s = ex
            X, Y = ox + (x - xmin) * sc, h - oy - (y - ymin) * sc
            out.append(f"<text x='{_num(X)}' y='{_num(Y)}' font-size='13' text-anchor='middle' fill='currentColor'>{s}</text>")
        elif ex[0] == "dash":
            a, b = P[ex[1][0]], P[ex[1][1]]
            out.append(f"<line x1='{_num(a[0])}' y1='{_num(a[1])}' x2='{_num(b[0])}' y2='{_num(b[1])}' stroke='currentColor' stroke-dasharray='4 3'/>")
        elif ex[0] == "right":
            v, a, b = P[ex[1]], P[ex[2]], P[ex[3]]
            def u(p):
                d = math.hypot(p[0] - v[0], p[1] - v[1]) or 1
                return ((p[0] - v[0]) / d * 10, (p[1] - v[1]) / d * 10)
            ua, ub = u(a), u(b)
            pts = [(v[0] + ua[0], v[1] + ua[1]), (v[0] + ua[0] + ub[0], v[1] + ua[1] + ub[1]), (v[0] + ub[0], v[1] + ub[1])]
            out.append("<polyline points='" + " ".join(f"{_num(x)},{_num(y)}" for x, y in pts) + "' fill='none' stroke='currentColor'/>")
        elif ex[0] == "circle":
            _, x, y, r = ex
            X, Y = ox + (x - xmin) * sc, h - oy - (y - ymin) * sc
            out.append(f"<circle cx='{_num(X)}' cy='{_num(Y)}' r='{_num(r * sc)}' fill='none' stroke='currentColor' stroke-width='1.6'/>")
    cap = f"<figcaption>{caption}</figcaption>" if caption else ""
    return f"<figure class='fig'><svg viewBox='0 0 {w} {h}' width='{w}' height='{h}' role='img' aria-label='{caption or '도형'}'>{''.join(out)}</svg>{cap}</figure>"
