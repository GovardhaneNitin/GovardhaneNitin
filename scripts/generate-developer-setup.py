# Generates images/developer-setup.svg: an animated intro banner (welcome + coding desk scene),
# themed after https://nitingovardhane.com. Run from the repo root:
#   python3 scripts/generate-developer-setup.py
import random
from html import escape

random.seed(7)
W, H = 1000, 830
OY = 270  # the desk scene sits below the hero text
out, css = [], []
A = out.append

# Portfolio design tokens (dark theme).
BG, FG, FG2, FG3 = "#0a0a0b", "#f4f4f5", "#a8a8b0", "#82828c"
LINE, ACCENT, ACCENT2, SUCCESS = "#26262a", "#ff804a", "#ffb380", "#34d399"
SANS = "Geist, Inter, 'Segoe UI', Helvetica, Arial, sans-serif"
SERIF = "'Instrument Serif', Georgia, 'Times New Roman', serif"
MONO = "'Geist Mono', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"


def rect(x, y, w, h, fill, rx=0, extra=""):
    A(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" {extra}/>')


def monogram(x, y, s, bg=FG, fg=BG):
    """The portfolio's "NG" logo: a rounded square with an accent dot."""
    rect(x, y, s, s, bg, rx=round(s * 0.28, 1))
    A(f'<text x="{x + s / 2:.1f}" y="{y + s * 0.66:.1f}" font-family="{SANS}" font-size="{s * 0.4:.1f}" '
      f'font-weight="700" letter-spacing="-0.5" fill="{fg}" text-anchor="middle">NG</text>')
    A(f'<circle cx="{x + s * 0.8:.1f}" cy="{y + s * 0.8:.1f}" r="{s * 0.06:.1f}" fill="{ACCENT}"/>')


# ---------- editor typing schedule (right monitor) ----------
CW, FS, LH = 5.4, 9, 10.6
CHAR_T, LINE_PAUSE, HOLD = 0.045, 0.35, 3.5
COL = dict(kw="#569cd6", kw2="#c586c0", var="#9cdcfe", prop="#9cdcfe", str="#ce9178",
           fn="#dcdcaa", p="#d4d4d4", type="#4ec9b0", com="#6a9955")
CODE = [
    (0, [("kw", "const "), ("var", "nitin"), ("p", ": "), ("type", "Engineer"), ("p", " = {")]),
    (1, [("prop", "role"), ("p", ": "), ("str", '"Full-Stack Product Engineer"'), ("p", ",")]),
    (1, [("prop", "focus"), ("p", ": "), ("str", '"Web apps & AI products"'), ("p", ",")]),
    (1, [("prop", "coffee"), ("p", ": "), ("kw", "Infinity"), ("p", ",")]),
    (1, [("prop", "stack"), ("p", ": ["), ("str", '"React"'), ("p", ", "), ("str", '"Next.js"'), ("p", ", "),
         ("str", '"Supabase"'), ("p", "],")]),
    (1, [("prop", "site"), ("p", ": "), ("str", '"nitingovardhane.com"'), ("p", ",")]),
    (0, [("p", "};")]),
    (0, []),
    (0, [("com", "// software that keeps working after it ships")]),
    (0, [("kw", "async "), ("kw", "function "), ("fn", "ship"), ("p", "("), ("var", "idea"), ("p", ": "),
         ("type", "Idea"), ("p", ") {")]),
    (1, [("kw2", "await "), ("fn", "test"), ("p", "("), ("var", "idea"), ("p", "); "), ("kw2", "await "),
         ("fn", "review"), ("p", "("), ("var", "idea"), ("p", ");")]),
    (1, [("kw2", "return "), ("fn", "deploy"), ("p", "("), ("var", "idea"), ("p", ")."), ("fn", "then"),
         ("p", "("), ("fn", "monitor"), ("p", ");")]),
    (0, [("p", "}")]),
]
EX, EY = 676, 222
t = 0.6
sched = []
for ind, toks in CODE:
    n = sum(len(s) for _, s in toks)
    s = t
    t += n * CHAR_T
    sched.append((s, t, n))
    t += LINE_PAUSE
T = t + HOLD
pct = lambda x: f"{x / T * 100:.3f}%"

# ---------- header / defs ----------
A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="title desc">')
A("<title id=\"title\">Welcome to my GitHub. Hi, I'm Nitin Govardhane, a full-stack engineer.</title>")
A('<desc id="desc">Animated banner: an intro in the style of nitingovardhane.com above a scene of Nitin in a hoodie '
  'typing code on a multi-monitor desk at night while it rains outside, with a cat asleep on the PC and an owl perched on the window.</desc>')
A('<defs>')
A(f'''<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#080e1a"/><stop offset="0.3" stop-color="#0e1829"/><stop offset="0.7" stop-color="#16243a"/><stop offset="1" stop-color="#1d2d44"/></linearGradient>
<linearGradient id="fog" x1="0" y1="0" x2="0" y2="1"><stop offset="0.4" stop-color="#8fb4e0" stop-opacity="0"/><stop offset="1" stop-color="#8fb4e0" stop-opacity="0.16"/></linearGradient>
<radialGradient id="moonGlow" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#dbe7ff" stop-opacity="0.3"/><stop offset="0.35" stop-color="#9fbcf0" stop-opacity="0.1"/><stop offset="1" stop-color="#9fbcf0" stop-opacity="0"/></radialGradient>
<filter id="heroText" x="-5%" y="-30%" width="110%" height="160%"><feDropShadow dx="0" dy="2" stdDeviation="5" flood-color="#050912" flood-opacity=".85"/></filter>
<linearGradient id="heroShade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#060a13" stop-opacity="0.5"/><stop offset="0.75" stop-color="#060a13" stop-opacity="0.18"/><stop offset="1" stop-color="#060a13" stop-opacity="0"/></linearGradient>
<linearGradient id="rainFade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity="0.25"/><stop offset="0.35" stop-color="#fff" stop-opacity="1"/></linearGradient>
<mask id="rainMask" maskUnits="userSpaceOnUse" x="0" y="0" width="{W}" height="{H}"><rect width="{W}" height="{H}" fill="url(#rainFade)"/></mask>
<linearGradient id="hoodie" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#b3b9c3"/><stop offset="0.5" stop-color="#868c97"/><stop offset="1" stop-color="#50555e"/></linearGradient>
<radialGradient id="hood" cx="0.42" cy="0.3" r="0.75"><stop offset="0" stop-color="#c4c9d1"/><stop offset="0.55" stop-color="#959ba6"/><stop offset="1" stop-color="#5f6570"/></radialGradient>
<linearGradient id="shade" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{ACCENT}" stop-opacity="0.12"/><stop offset="0.2" stop-color="#05070c" stop-opacity="0.35"/><stop offset="0.5" stop-color="#05070c" stop-opacity="0.08"/><stop offset="0.75" stop-color="#6fa8ff" stop-opacity="0"/><stop offset="1" stop-color="#6fa8ff" stop-opacity="0.18"/></linearGradient>
<linearGradient id="sleeveL" x1="1" y1="0" x2="0" y2="0"><stop offset="0" stop-color="#7a808b"/><stop offset="1" stop-color="#7d7570"/></linearGradient>
<linearGradient id="sleeveR" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#868c97"/><stop offset="1" stop-color="#aab6cc"/></linearGradient>
<linearGradient id="desk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#b7a68c"/><stop offset="1" stop-color="#8d7d66"/></linearGradient>
<radialGradient id="glow" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#7fb2ff" stop-opacity="0.45"/><stop offset="1" stop-color="#7fb2ff" stop-opacity="0"/></radialGradient>
<radialGradient id="warmGlow" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="{ACCENT}" stop-opacity="0.35"/><stop offset="1" stop-color="{ACCENT}" stop-opacity="0"/></radialGradient>
<radialGradient id="vignette" cx="0.5" cy="0.6" r="0.8"><stop offset="0.6" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.6"/></radialGradient>
<linearGradient id="lampLight" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{ACCENT2}" stop-opacity="0.4"/><stop offset="1" stop-color="{ACCENT2}" stop-opacity="0"/></linearGradient>
<linearGradient id="rgb" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ff3d71"/><stop offset="0.25" stop-color="#ffb13d"/><stop offset="0.5" stop-color="#3dff9e"/><stop offset="0.75" stop-color="#3db8ff"/><stop offset="1" stop-color="#b03dff"/></linearGradient>
<pattern id="mesh" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="6" height="6" fill="#15171b"/><path d="M0 0H6M0 0V6" stroke="#2a2e35" stroke-width="1"/></pattern>
<clipPath id="frame"><rect width="{W}" height="{H}" rx="18"/></clipPath>
<clipPath id="scrR"><rect x="647" y="192" width="296" height="181"/></clipPath>
<clipPath id="scrC"><rect x="306" y="198" width="308" height="166"/></clipPath>
<clipPath id="scrL"><rect x="79" y="296" width="148" height="92"/></clipPath>
<clipPath id="scrT"><rect x="0" y="0" width="104" height="58"/></clipPath>''')

EYEBROW = "> welcome to my github"
EB_X, EB_Y, EB_CW = 56, 112, 8.4
A(f'<clipPath id="typeClip"><rect class="typeReveal" x="{EB_X}" y="{EB_Y - 16}" width="{len(EYEBROW) * EB_CW + 4:.1f}" height="22"/></clipPath>')
A('<linearGradient id="catFur" gradientUnits="userSpaceOnUse" x1="0" y1="-15" x2="0" y2="0"><stop offset="0" stop-color="#c8743a"/><stop offset=".45" stop-color="#e0965a"/><stop offset=".8" stop-color="#ebb27c"/><stop offset="1" stop-color="#f1cfa6"/></linearGradient>'
  '<filter id="catLine" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="0" stdDeviation=".4" flood-color="#1a0b04" flood-opacity=".75"/></filter>')
A('<filter id="soft" x="-50%" y="-200%" width="200%" height="500%"><feGaussianBlur stdDeviation="4"/></filter>'
  '<linearGradient id="velvet" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8b5cf6"/><stop offset=".5" stop-color="#6d28d9"/><stop offset="1" stop-color="#3b1780"/></linearGradient>')
A('</defs>')

# ---------- CSS ----------
css.append(f'''
.rain{{animation:rain .9s linear infinite}}
@keyframes rain{{from{{transform:translateY(-{H}px)}}to{{transform:translateY(0)}}}}
.win{{animation:flick 6s ease-in-out infinite}}
@keyframes flick{{0%,100%{{opacity:.85}}45%{{opacity:.25}}55%{{opacity:.9}}}}
.head{{transform-box:fill-box;transform-origin:50% 100%;animation:bob 5s ease-in-out infinite}}
@keyframes bob{{0%,100%{{transform:rotate(0deg)}}30%{{transform:rotate(-1.6deg) translateY(1px)}}65%{{transform:rotate(1.2deg) translateY(.5px)}}}}
.armL{{animation:typeL .32s ease-in-out infinite alternate}}
.armR{{animation:typeR .27s ease-in-out infinite alternate}}
@keyframes typeL{{from{{transform:translateY(0)}}to{{transform:translateY(2px)}}}}
@keyframes typeR{{from{{transform:translateY(1.5px)}}to{{transform:translateY(0)}}}}
.body{{transform-box:fill-box;transform-origin:50% 100%;animation:breathe 4s ease-in-out infinite}}
@keyframes breathe{{0%,100%{{transform:scale(1)}}50%{{transform:scale(1.008,1.012)}}}}
.blink{{animation:blink 1s steps(1) infinite}}
@keyframes blink{{50%{{opacity:0}}}}
.scrollC{{animation:scrollC 16s linear infinite}}
@keyframes scrollC{{from{{transform:translateY(0)}}to{{transform:translateY(-240px)}}}}
.term{{animation:term 12s steps(12) infinite}}
@keyframes term{{from{{transform:translateY(0)}}to{{transform:translateY(-108px)}}}}
.screenGlow{{animation:sg 3s ease-in-out infinite}}
@keyframes sg{{0%,100%{{opacity:.75}}50%{{opacity:1}}}}
.rim{{animation:rim 2.2s ease-in-out infinite}}
@keyframes rim{{0%,100%{{opacity:.35}}50%{{opacity:.7}}}}
.fan{{transform-box:fill-box;transform-origin:50% 50%;animation:spin 1.2s linear infinite}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}
.rgb{{animation:hue 6s linear infinite}}
@keyframes hue{{to{{filter:hue-rotate(360deg)}}}}
.steam{{animation:steam 3.2s ease-out infinite;opacity:0}}
@keyframes steam{{0%{{opacity:0;transform:translateY(0)}}30%{{opacity:.5}}100%{{opacity:0;transform:translateY(-22px)}}}}
.bar{{transform-box:fill-box;transform-origin:bottom;animation:bar 2.4s ease-in-out infinite alternate}}
@keyframes bar{{from{{transform:scaleY(.35)}}to{{transform:scaleY(1)}}}}
.led{{animation:led 1.4s steps(1) infinite}}
@keyframes led{{50%{{opacity:.2}}}}
.enter{{animation:enter .8s cubic-bezier(.21,.47,.32,.98) both}}
@keyframes enter{{from{{opacity:0;transform:translateY(14px)}}to{{opacity:1;transform:none}}}}
.breathe{{transform-box:fill-box;transform-origin:50% 100%;animation:breathe2 11.4s ease-in-out infinite}}
@keyframes breathe2{{0%,33.3%,66.6%,100%{{transform:scale(1,1)}}16.6%,50%{{transform:scale(1.015,1.05)}}83%{{transform:scale(1.03,1.1)}}}}
.breatheHead{{animation:breatheHead 11.4s ease-in-out infinite}}
@keyframes breatheHead{{0%,33.3%,66.6%,100%{{transform:translateY(0)}}16.6%,50%{{transform:translateY(-.4px)}}83%{{transform:translate(.2px,-.8px)}}}}
.bubble{{transform-box:fill-box;transform-origin:20% 100%;animation:bubble 11.4s ease-in-out infinite}}
@keyframes bubble{{0%{{transform:scale(.5);opacity:.85}}16.6%{{transform:scale(.25)}}33.3%{{transform:scale(.7)}}50%{{transform:scale(.3)}}66.6%{{transform:scale(1)}}80%{{transform:scale(.4)}}91%{{transform:scale(1.25);opacity:.85}}92.5%{{transform:scale(1.6);opacity:0}}97%{{transform:scale(.1);opacity:0}}100%{{transform:scale(.5);opacity:.85}}}}
.pop{{transform-box:fill-box;transform-origin:50% 50%;animation:pop 11.4s ease-out infinite;opacity:0}}
@keyframes pop{{0%,91.5%{{opacity:0;transform:scale(.4)}}92.5%{{opacity:1}}96%,100%{{opacity:0;transform:scale(1.5)}}}}
.tailTip{{transform-box:view-box;transform-origin:8.6px -.1px;animation:tailTip 7s ease-in-out infinite}}
@keyframes tailTip{{0%,58%,100%{{transform:rotate(0)}}63%{{transform:rotate(-16deg)}}68%{{transform:rotate(4deg)}}73%{{transform:rotate(-10deg)}}79%{{transform:rotate(0)}}}}
.paw{{transform-box:fill-box;transform-origin:0% 50%;animation:paw 9s ease-in-out infinite}}
@keyframes paw{{0%,40%,52%,100%{{transform:translate(0,0)}}43%{{transform:translate(.6px,-.5px)}}46%{{transform:translate(0,0)}}49%{{transform:translate(.5px,-.4px)}}}}
.whisk{{transform-box:fill-box;transform-origin:0% 50%;animation:whisk 6.2s ease-in-out infinite}}
@keyframes whisk{{0%,70%,100%{{transform:rotate(0)}}73%{{transform:rotate(-9deg)}}76%{{transform:rotate(3deg)}}79%{{transform:rotate(0)}}}}
.rem{{transform-box:fill-box;transform-origin:50% 0%;animation:rem 5.3s ease-in-out infinite}}
@keyframes rem{{0%,30%,40%,100%{{transform:scaleY(1)}}32%,36%{{transform:scaleY(.55)}}34%,38%{{transform:scaleY(1.15)}}}}
.purr{{transform-box:fill-box;transform-origin:50% 50%;animation:purr 3.8s ease-out infinite;opacity:0}}
@keyframes purr{{0%{{opacity:0;transform:scale(.6)}}25%{{opacity:.55}}100%{{opacity:0;transform:scale(1.5)}}}}
.zz{{transform-box:fill-box;transform-origin:50% 50%;animation:zz 4.2s ease-out infinite;opacity:0}}
@keyframes zz{{0%{{opacity:0;transform:translate(0,0) scale(.6)}}20%{{opacity:.9}}100%{{opacity:0;transform:translate(-16px,-34px) scale(1.25)}}}}
.sparkle{{transform-box:fill-box;transform-origin:50% 50%;animation:sparkle 2.6s ease-in-out infinite;opacity:0}}
@keyframes sparkle{{0%,100%{{opacity:0;transform:scale(.3) rotate(0)}}50%{{opacity:1;transform:scale(1) rotate(45deg)}}}}
.tassel{{transform-box:fill-box;transform-origin:50% 0;animation:tassel 3s ease-in-out infinite alternate}}
@keyframes tassel{{from{{transform:rotate(-8deg)}}to{{transform:rotate(8deg)}}}}
.ear{{transform-box:fill-box;transform-origin:50% 100%;animation:ear 5.2s ease-in-out infinite}}
@keyframes ear{{0%,86%,100%{{transform:rotate(0)}}89%{{transform:rotate(-14deg)}}92%{{transform:rotate(6deg)}}}}
.owlHead{{transform-box:fill-box;transform-origin:50% 90%;animation:owlHead 9s ease-in-out infinite}}
@keyframes owlHead{{0%,40%,100%{{transform:rotate(0)}}46%,58%{{transform:rotate(-14deg)}}64%,72%{{transform:rotate(10deg)}}78%{{transform:rotate(0)}}}}
.lid{{transform-box:fill-box;transform-origin:50% 0;animation:lid 4.6s infinite}}
@keyframes lid{{0%,92%,100%{{transform:scaleY(0)}}95%{{transform:scaleY(1)}}}}
.pulse{{transform-box:fill-box;transform-origin:50% 50%;animation:pulse 2.4s ease-out infinite}}
@keyframes pulse{{0%{{transform:scale(1);opacity:.7}}80%,100%{{transform:scale(2.6);opacity:0}}}}
.typeReveal{{animation:reveal {len(EYEBROW) * 0.07:.2f}s steps({len(EYEBROW)},end) .5s both}}
@keyframes reveal{{from{{transform:translateX(-{len(EYEBROW) * EB_CW + 4:.1f}px)}}to{{transform:none}}}}
.caret{{animation:caret {len(EYEBROW) * 0.07:.2f}s steps({len(EYEBROW)},end) .5s both}}
@keyframes caret{{from{{transform:translateX(0)}}to{{transform:translateX({len(EYEBROW) * EB_CW:.1f}px)}}}}
''')

A('<g clip-path="url(#frame)">')

# ---------- sky, hero backdrop, city ----------
rect(0, 0, W, H, "url(#sky)")
# stars and a moon so the intro sits in the same night sky as the desk scene
stars = []
for _ in range(70):
    sx, sy, sr = random.uniform(10, 990), random.uniform(10, 300), random.uniform(0.5, 1.2)
    if random.random() < 0.3:
        A(f'<circle class="win" style="animation-delay:-{random.uniform(0, 6):.1f}s" cx="{sx:.0f}" cy="{sy:.0f}" r="{sr:.1f}" fill="#fff"/>')
    else:
        stars.append(f"M{sx:.0f} {sy:.0f}m-{sr:.1f} 0a{sr:.1f} {sr:.1f} 0 1 0 {2 * sr:.1f} 0a{sr:.1f} {sr:.1f} 0 1 0 -{2 * sr:.1f} 0")
A(f'<path d="{"".join(stars)}" fill="#fff" opacity=".45"/>')
A('<ellipse cx="850" cy="150" rx="190" ry="160" fill="url(#moonGlow)"/>')
A('<circle cx="850" cy="150" r="26" fill="#f2eee0"/>')
A('<circle cx="841" cy="143" r="5" fill="#ddd7c4" opacity=".7"/><circle cx="858" cy="160" r="3.6" fill="#ddd7c4" opacity=".6"/><circle cx="861" cy="139" r="2.4" fill="#ddd7c4" opacity=".6"/>')
BASE = 470 + OY
x = -10
while x < W:
    w = random.randint(40, 90); h = random.randint(140, 330)
    rect(x, BASE - h, w, h + 100, "#22324b", extra='opacity="0.7"')
    x += w + random.randint(-5, 12)
winpaths = {}
x = -20
while x < W:
    w = random.randint(70, 130); h = random.randint(220, 430)
    top = BASE - h
    rect(x, top, w, h + 100, "#141f31")
    for wy in range(int(top) + 10, BASE, 14):
        for wx in range(int(x) + 8, int(x + w) - 8, 12):
            r = random.random()
            if r < 0.22:
                col = random.choice(["#ffd88a", "#ffe9b8", "#9fd0ff"])
                if r < 0.06:
                    A(f'<rect x="{wx}" y="{wy}" width="5" height="6" fill="{col}" opacity="0.75" class="win" style="animation-delay:-{random.uniform(0, 6):.1f}s"/>')
                else:
                    winpaths.setdefault(col, []).append(f"M{wx} {wy}h5v6h-5z")
    x += w + random.randint(4, 20)
for col, ps in winpaths.items():
    A(f'<path d="{"".join(ps)}" fill="{col}" opacity="0.75"/>')
rect(0, 0, W, H, "url(#fog)")
A(f'<g transform="translate(0 {OY})"><ellipse class="screenGlow" cx="620" cy="280" rx="420" ry="190" fill="url(#glow)"/></g>')
drops = []
for _ in range(190):
    dx, dy = random.uniform(0, W), random.uniform(0, H)
    drops.append(f'M{dx:.0f} {dy:.0f}l-2 {random.uniform(10, 22):.0f}')
d = "".join(drops)
A(f'<g mask="url(#rainMask)"><g class="rain" stroke="#a9c8ef" stroke-opacity="0.35" stroke-width="1"><path d="{d}"/><path transform="translate(0 {H})" d="{d}"/></g></g>')
# outer window frame around the hero glass
for fx in (0, 990):
    rect(fx - 6, 0, 12, H, "#262b33")
rect(0, 0, W, 8, "#262b33")

# ================= desk scene (scene coordinates, shifted down by OY) =================
A(f'<g transform="translate(0 {OY})">')
# transom + mullions
for fx in (245, 495, 745):
    rect(fx - 6, 0, 12, 560, "#262b33")
    rect(fx - 2, 0, 3, 560, "#323843")
rect(0, 0, W, 10, "#262b33")
rect(0, 3, W, 2, "#323843")
rect(0, 455, W, 8, "#262b33")

# ---------- lamp (warm, portfolio accent) ----------
A('<path d="M298 398 L262 262 L318 150" stroke="#0d0e11" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
A('<circle cx="262" cy="262" r="5" fill="#1a1c20"/>')
A('<path d="M330 154 L535 150 L560 330 L300 330 Z" fill="url(#lampLight)" opacity="0.45"/>')
A('<ellipse cx="430" cy="160" rx="150" ry="26" fill="url(#warmGlow)"/>')
A('<path d="M318 150 L540 146" stroke="#0d0e11" stroke-width="9" stroke-linecap="round"/>')
A(f'<path d="M326 154 L534 150" stroke="{ACCENT2}" stroke-width="2" stroke-linecap="round" opacity="0.9"/>')

# ---------- center monitor: nitingovardhane.com in a browser ----------
rect(453, 360, 16, 40, "#111317")
A('<ellipse cx="461" cy="401" rx="38" ry="4" fill="#0e0f12"/>')
rect(300, 180, 320, 190, "#0c0d10", rx=5)
rect(306, 186, 308, 178, BG)
rect(306, 186, 308, 12, "#121214")
for i, c in enumerate(["#ff5f57", "#febc2e", "#28c840"]):
    A(f'<circle cx="{313 + i * 7}" cy="192" r="2" fill="{c}"/>')
rect(334, 188.5, 120, 7, "#1b1b1e", rx=3.5)
A(f'<text x="339" y="194" font-family="{MONO}" font-size="5.5" fill="{FG2}">nitingovardhane.com</text>')


def site_block(y0):
    """One screen of the portfolio home page, abstracted."""
    monogram(314, y0 + 6, 8)
    for i, w in enumerate((18, 22, 16)):
        rect(520 + i * 28, y0 + 9, w, 3, FG3, rx=1.5)
    rect(588, y0 + 6, 20, 8, ACCENT, rx=4)
    rect(314, y0 + 26, 70, 9, "#121214", rx=4.5, extra=f'stroke="{LINE}" stroke-width="0.8"')
    A(f'<circle cx="320" cy="{y0 + 30.5}" r="2" fill="{SUCCESS}"/>')
    rect(326, y0 + 29.5, 50, 2.5, FG3, rx=1)
    rect(314, y0 + 44, 230, 11, FG, rx=2)
    rect(314, y0 + 60, 70, 11, FG, rx=2)
    rect(390, y0 + 60, 96, 11, ACCENT, rx=2)
    rect(492, y0 + 60, 60, 11, FG, rx=2)
    for i, w in enumerate((210, 190, 150)):
        rect(314, y0 + 82 + i * 7, w, 3.5, FG3, rx=1.5)
    rect(314, y0 + 108, 46, 11, FG, rx=5.5)
    rect(366, y0 + 108, 40, 11, "none", rx=5.5, extra=f'stroke="{LINE}"')
    for i in range(3):
        cx = 314 + i * 98
        rect(cx, y0 + 132, 92, 52, "#121214", rx=4, extra=f'stroke="{LINE}" stroke-width="0.8"')
        rect(cx + 6, y0 + 138, 80, 22, ["#1f2937", "#2a1a12", "#14231d"][i], rx=2)
        rect(cx + 6, y0 + 166, 50, 3.5, FG2, rx=1.5)
        rect(cx + 6, y0 + 173, 70, 3, FG3, rx=1.5)
    rect(314, y0 + 200, 120, 7, FG, rx=2)
    rect(440, y0 + 200, 60, 7, ACCENT, rx=2)
    for i, w in enumerate((180, 160)):
        rect(314, y0 + 214 + i * 7, w, 3, FG3, rx=1.5)


A('<g clip-path="url(#scrC)"><g class="scrollC">')
site_block(198)
site_block(438)
A('</g></g>')

# ---------- right monitor: live-typing editor ----------
rect(787, 378, 18, 22, "#111317")
A('<ellipse cx="796" cy="401" rx="42" ry="4" fill="#0e0f12"/>')
A('<ellipse class="screenGlow" cx="795" cy="282" rx="190" ry="130" fill="url(#glow)"/>')
rect(640, 185, 310, 195, "#0c0d10", rx=5)
A('<g clip-path="url(#scrR)">')
rect(647, 192, 296, 181, "#1e1e1e")
rect(647, 192, 296, 14, "#2d2d30")
for i, c in enumerate(["#ff5f57", "#febc2e", "#28c840"]):
    A(f'<circle cx="{656 + i * 9}" cy="199" r="2.6" fill="{c}"/>')
rect(690, 194, 70, 12, "#1e1e1e")
A(f'<rect x="690" y="194" width="70" height="1.2" fill="{ACCENT}"/>')
A('<text x="697" y="203" font-family="monospace" font-size="7" fill="#d4d4d4"><tspan fill="#3178c6">TS</tspan> nitin.ts</text>')
for i in range(len(CODE)):
    A(f'<text x="666" y="{EY + i * LH:.1f}" font-family="monospace" font-size="{FS - 1}" fill="#5a5a5a" text-anchor="end">{i + 1}</text>')
# Drawn bottom-up so each line's cover can extend upward without hiding the line above it.
for i, (ind, toks) in reversed(list(enumerate(CODE))):
    if not toks:
        continue
    n = sched[i][2]
    y = EY + i * LH
    x0 = EX + ind * 2 * CW
    spans = "".join(f'<tspan fill="{COL[k]}">{escape(s)}</tspan>' for k, s in toks)
    A(f'<text x="{x0:.1f}" y="{y:.1f}" font-family="Consolas,Menlo,monospace" font-size="{FS}" textLength="{n * CW:.1f}" lengthAdjust="spacingAndGlyphs" xml:space="preserve">{spans}</text>')
    s, e, _ = sched[i]
    A(f'<rect class="cv{i}" x="{x0:.1f}" y="{y - 9.6:.1f}" width="{n * CW + 2:.1f}" height="12.4" fill="#1e1e1e"/>')
    css.append(f'.cv{i}{{animation:cv{i} {T:.2f}s infinite}}'
               f'@keyframes cv{i}{{0%,{pct(s)}{{transform:translateX(0);animation-timing-function:steps({n},end)}}'
               f'{pct(e)},100%{{transform:translateX({n * CW:.1f}px)}}}}')
kf = []
for i, (ind, toks) in enumerate(CODE):
    s, e, n = sched[i]
    x0 = EX + ind * 2 * CW
    y = EY + i * LH - FS + 1
    if i == 0:
        kf.append(f'0%{{transform:translate({x0:.1f}px,{y:.1f}px);animation-timing-function:step-end}}')
    if n:
        kf.append(f'{pct(s)}{{transform:translate({x0:.1f}px,{y:.1f}px);animation-timing-function:steps({n},end)}}')
        kf.append(f'{pct(e)}{{transform:translate({x0 + n * CW:.1f}px,{y:.1f}px);animation-timing-function:step-end}}')
    else:
        kf.append(f'{pct(s)}{{transform:translate({x0:.1f}px,{y:.1f}px);animation-timing-function:step-end}}')
kf.append(f'100%{{transform:translate({x0 + n * CW:.1f}px,{y:.1f}px)}}')
css.append(f'.cur{{animation:cur {T:.2f}s infinite}}@keyframes cur{{{"".join(kf)}}}')
A(f'<g class="cur"><rect class="blink" x="0" y="0" width="1.4" height="{FS + 1}" fill="#aeafad"/></g>')
rect(647, 364, 296, 9, ACCENT)
A(f'<text x="652" y="371" font-family="monospace" font-size="6.5" fill="{BG}">⎇ main  ✓ CI passing</text>')
A(f'<text x="938" y="371" font-family="monospace" font-size="6.5" fill="{BG}" text-anchor="end">TypeScript</text>')
A('</g>')

# ---------- desk ----------
A('<polygon points="18,400 982,400 992,414 8,414" fill="url(#desk)"/>')
rect(8, 414, 984, 8, "#6d5f4c")
rect(78, 422, 18, 140, "#121315")
rect(904, 422, 18, 140, "#121315")
rect(78, 440, 844, 6, "#121315")

# ---------- laptop: terminal ----------
A('<ellipse class="screenGlow" cx="153" cy="340" rx="110" ry="70" fill="url(#glow)" opacity=".7"/>')
A('<polygon points="72,290 234,290 236,394 70,394" fill="#16181c"/>')
rect(79, 296, 148, 92, "#0d1117")
TERM = [
    ("#7ee787", "~/projects $ npm run test:e2e"),
    ("#8b949e", "Running 128 tests using 8 workers"),
    ("#7ee787", "  ✓ 128 passed (41.2s)"),
    ("#c9d1d9", "$ npm run typecheck"),
    ("#7ee787", "  ✓ no type errors"),
    ("#c9d1d9", '$ git commit -m "feat: custom roles"'),
    ("#c9d1d9", "$ git push origin main"),
    ("#79c0ff", "  ▲ CI green · deploying…"),
    ("#7ee787", "  ✔ Deployed to production"),
    ("#c9d1d9", "$ sentry issues --new"),
    ("#7ee787", "  0 new issues"),
    (ACCENT2, '$ echo "keeps working ✨"'),
]
A('<g clip-path="url(#scrL)"><g class="term">')
for rep in range(2):
    for i, (c, s) in enumerate(TERM):
        A(f'<text x="84" y="{306 + (rep * len(TERM) + i) * 9}" font-family="monospace" font-size="6.2" fill="{c}" xml:space="preserve">{escape(s)}</text>')
A('</g></g>')
A('<polygon points="62,394 244,394 256,406 50,406" fill="#9ea3ab"/>')
A('<polygon points="62,394 244,394 246,397 60,397" fill="#c3c7cd"/>')

# ---------- coffee mug ----------
rect(262, 380, 20, 22, "#e8e2d6", rx=3)
A('<path d="M282 385 q8 0 8 7 q0 7 -8 7" stroke="#e8e2d6" stroke-width="3" fill="none"/>')
A(f'<text x="272" y="395" font-family="{SANS}" font-size="7" font-weight="700" fill="{BG}" text-anchor="middle">NG</text>')
A(f'<circle cx="278" cy="397" r="0.9" fill="{ACCENT}"/>')
for i, dx in enumerate((266, 272, 278)):
    A(f'<path class="steam" style="animation-delay:{i * 1.05:.2f}s" d="M{dx} 376 q-4 -6 0 -12 q4 -6 0 -12" stroke="#ffffff" stroke-width="1.6" fill="none" stroke-linecap="round"/>')

# ---------- tablet: contribution bars ----------
A('<g transform="translate(838 334) skewX(-10)">')
rect(0, 0, 110, 64, "#0c0d10", rx=4)
A('<g transform="translate(3 3)" clip-path="url(#scrT)">')
rect(0, 0, 104, 58, "#161b22")
A('<text x="5" y="9" font-family="sans-serif" font-size="6" fill="#8b949e">contributions</text>')
for i in range(10):
    h = random.randint(16, 40)
    A(f'<rect class="bar" style="animation-delay:-{random.uniform(0, 2.4):.2f}s" x="{6 + i * 9.5}" y="{54 - h}" width="6" height="{h}" rx="1" fill="#{random.choice(["39d353", "26a641", "006d32", "39d353"])}"/>')
A('</g></g>')

# ---------- keyboard + mouse ----------
A('<g class="rgb">')
A('<polygon points="335,398 610,398 616,406 329,406" fill="#101114"/>')
rect(331, 405, 284, 2, "url(#rgb)", extra='opacity="0.9"')
A('<ellipse cx="655" cy="402" rx="9" ry="4.5" fill="#101114"/>')
A('<ellipse cx="655" cy="405" rx="9" ry="1.4" fill="url(#rgb)"/>')
A('</g>')

# ---------- person ----------
TORSO = "M352 560 C346 500 340 440 346 380 C350 336 372 304 410 292 L530 292 C568 304 590 336 594 380 C600 440 594 500 588 560 Z"
HOOD = ("M470 146 C474 146 478 147 482 149 C516 158 538 188 538 226 C538 256 530 280 520 298 "
        "C496 310 444 310 420 298 C410 280 402 256 402 226 C402 190 424 160 458 149 C462 147 466 146 470 146 Z")
A('<g class="body">')
A(f'<path d="{TORSO}" fill="url(#hoodie)"/>')
A('<path d="M470 300 L470 560" stroke="#6c727d" stroke-opacity="0.35" stroke-width="2"/>')
A('<path d="M372 330 C400 380 405 470 395 560" stroke="#7b818c" stroke-opacity="0.35" stroke-width="10" fill="none"/>')
A('<path d="M568 330 C540 380 535 470 545 560" stroke="#7b818c" stroke-opacity="0.35" stroke-width="10" fill="none"/>')
monogram(457, 326, 26, bg=BG, fg=FG)  # back print
A(f'<path d="{TORSO}" fill="url(#shade)"/>')
A('<g class="armL"><path d="M362 318 C334 336 318 380 316 420 C315 446 326 462 344 462 C360 462 364 440 364 420 C364 390 372 360 380 340 Z" fill="url(#sleeveL)"/>'
  '<path d="M318 420 C320 446 330 458 344 460" stroke="#6c727d" stroke-width="2" fill="none" opacity=".5"/></g>')
A('<g class="armR"><path d="M578 318 C606 336 622 380 624 420 C625 446 614 462 596 462 C580 462 576 440 576 420 C576 390 568 360 560 340 Z" fill="url(#sleeveR)"/>'
  '<path d="M622 420 C620 446 610 458 596 460" stroke="#6c727d" stroke-width="2" fill="none" opacity=".5"/></g>')
A('<path class="rim" d="M560 300 C590 320 606 350 616 390" stroke="#8ec1ff" stroke-width="3" fill="none" stroke-linecap="round"/>')
A(f'<path class="rim" style="animation-delay:-1.1s" d="M380 300 C352 320 336 350 326 390" stroke="{ACCENT2}" stroke-width="2" fill="none" stroke-linecap="round" opacity=".6"/>')
A('</g>')
A('<g class="head">')
A('<path d="M424 286 C440 304 500 304 516 286 L530 300 C500 318 440 318 410 300 Z" fill="#8e949f"/>')
A(f'<path d="{HOOD}" fill="url(#hood)"/>')
A(f'<path d="{HOOD}" fill="url(#shade)"/>')
A('<path d="M470 150 C468 196 468 246 470 300" stroke="#7b818c" stroke-opacity="0.45" stroke-width="2" fill="none"/>')
A('<path d="M412 250 C424 278 442 294 470 300" stroke="#7b818c" stroke-opacity="0.3" stroke-width="6" fill="none"/>')
A('<path class="rim" d="M504 158 C528 176 538 200 537 230 C536 256 528 278 518 294" stroke="#8ec1ff" stroke-width="2.5" fill="none" stroke-linecap="round"/>')
A(f'<path class="rim" style="animation-delay:-1s" d="M440 158 C418 176 404 200 404 226" stroke="{ACCENT2}" stroke-width="1.8" fill="none" stroke-linecap="round" opacity=".7"/>')
A('</g>')

# ---------- chair ----------
A('<path d="M330 470 L382 470 M558 470 L610 470" stroke="#0c0d0f" stroke-width="9" stroke-linecap="round"/>')
rect(352, 470, 10, 90, "#0c0d0f")
rect(578, 470, 10, 90, "#0c0d0f")
A('<path d="M384 396 C384 382 396 376 410 376 L530 376 C544 376 556 382 556 396 L552 470 C548 486 548 500 556 520 L560 560 L380 560 L384 520 C392 500 392 486 388 470 Z" fill="url(#mesh)" stroke="#0a0b0d" stroke-width="5"/>')
A('<path d="M470 380 L470 560" stroke="#0a0b0d" stroke-width="3" opacity=".7"/>')
A('<path d="M392 470 C440 480 500 480 548 470" stroke="#0a0b0d" stroke-width="4" fill="none" opacity=".8"/>')

# ---------- PC tower ----------
rect(918, 452, 90, 120, "#0e0f12", rx=4)
rect(924, 458, 80, 108, "#14161a", rx=3)
A('<g class="rgb"><circle cx="962" cy="508" r="30" fill="none" stroke="url(#rgb)" stroke-width="3"/></g>')
A('<g class="fan" opacity="0.85"><circle cx="962" cy="508" r="27" fill="none"/>')
for k in range(7):
    A(f'<path transform="rotate({k * 360 / 7:.1f} 962 508)" d="M962 508 C968 496 976 488 986 486 C980 496 974 504 962 508 Z" fill="#3a4250"/>')
A('<circle cx="962" cy="508" r="6" fill="#1b1e24"/></g>')
A('<circle class="led" cx="932" cy="464" r="2" fill="#3dff9e"/>')

# ---------- cat asleep on the PC tower (curled up, head on its tail; bottom at y=0) ----------
FUR, STRIPE, CREAM = "url(#catFur)", "#9a4f22", "#f3dcbc"
GOLD = "#f5c84c"
# RGB glow spilling from the PC, then a velvet cushion with gold piping and tassels
A('<g class="rgb"><ellipse cx="956" cy="450" rx="46" ry="7" fill="url(#rgb)" opacity=".55" filter="url(#soft)"/></g>')
for tx in (922, 990):
    A(f'<g class="tassel" style="animation-delay:-{(tx - 922) / 40:.1f}s"><path d="M{tx} 449 v7" stroke="{GOLD}" stroke-width="1"/>'
      f'<path d="M{tx - 1.8} 456 h3.6 l.8 6 h-5.2 Z" fill="{GOLD}"/><circle cx="{tx}" cy="455.6" r="1.4" fill="#ffe08a"/></g>')
A(f'<rect x="920" y="443" width="72" height="10" rx="5" fill="url(#velvet)" stroke="{GOLD}" stroke-width="1"/>')
A('<path d="M926 445.4 C944 443.8 968 443.8 986 445.4" stroke="#c4a5ff" stroke-width="1" fill="none" opacity=".5" stroke-linecap="round"/>')
A(f'<path d="M{"".join(f"M{bx} 448.4a.9 .9 0 1 0 .1 0" for bx in (932, 944, 956, 968, 980))[1:]}" fill="#2e1065" opacity=".7"/>')
A('<g transform="translate(953 444) scale(1.7)"><g filter="url(#catLine)">')
A('<ellipse cx="0" cy="0.2" rx="20" ry="1.4" fill="#000" opacity=".4"/>')
A('<g class="breathe">')
A(f'<path d="M-19 -1 C-20.5 -8 -15 -14.5 -5 -15 C4 -15.4 11 -13 14.5 -9 C16.5 -6.5 16.5 -2 14 -0.6 C6 0.4 -12 0.4 -19 -1 Z" fill="{FUR}"/>')
A(f'<ellipse cx="-10.4" cy="-6.6" rx="8.4" ry="6.6" fill="{FUR}"/>')
A(f'<path d="M-17.4 -2.6 C-16.4 -9.6 -9.6 -12.6 -3.4 -10" stroke="{STRIPE}" stroke-width=".8" fill="none" opacity=".4"/>')
stripes = "".join(f"M{x} {y} q.9 2.4 .1 4.4" for x, y in ((-15.4, -11.2), (-11.8, -13.4), (-7.8, -14.6), (-3.8, -15), (0.2, -14.9), (4.2, -14.4), (8, -13.2)))
A(f'<path d="{stripes}" stroke="{STRIPE}" stroke-width="1" fill="none" stroke-linecap="round" opacity=".5"/>')
A('</g>')
A(f'<ellipse cx="12.6" cy="-0.9" rx="2.3" ry="1" fill="{CREAM}"/><g class="paw"><ellipse cx="16.4" cy="-1" rx="2.4" ry="1.1" fill="{CREAM}"/>'
  '<path d="M17.4 -0.4 v-.9 M18.4 -0.5 v-.8" stroke="#c9a27a" stroke-width=".3" stroke-linecap="round"/></g>')
# tail wrapped around the front
A(f'<path d="M-18.6 -2.4 C-16 1.2 -2 1.6 8.6 0.1" stroke="{FUR}" stroke-width="3" fill="none" stroke-linecap="round"/>')
A(f'<path d="M-12 0.2 l.4 -2.4 M-6 0.8 l.2 -2.6 M0 0.9 l0 -2.6 M5 0.6 l-.2 -2.4" stroke="{STRIPE}" stroke-width=".9" stroke-linecap="round" opacity=".6"/>')
A(f'<g class="tailTip"><path d="M8.4 0 C10.2 -0.2 11.6 -0.9 12.2 -2.2" stroke="{FUR}" stroke-width="3" fill="none" stroke-linecap="round"/>'
  f'<path d="M10.2 -0.4 C11.2 -0.8 11.9 -1.4 12.2 -2.2" stroke="{STRIPE}" stroke-width="3" fill="none" stroke-linecap="round"/></g>')
# head resting on the tail, eyes closed
A('<g class="breatheHead">')
A('<path d="M9 -11 L9.6 -16.4 L12.8 -12.6 Z" fill="#b8692f"/>')
A(f'<path class="ear" d="M13.6 -12.9 L17.6 -16.6 L18.6 -11.2 Z" fill="{FUR}"/>')
A('<path d="M14.8 -12.8 L17.2 -15 L17.7 -11.8 Z" fill="#d99a86"/>')
A(f'<path d="M7.4 -6 C7.4 -10.8 10.6 -13 14 -13 C17.6 -13 20.4 -10.6 20.8 -7.4 C21.2 -4.4 19.4 -1.8 16 -1.4 C12 -1 7.4 -2.2 7.4 -6 Z" fill="{FUR}"/>')
A(f'<path d="M12.4 -12.6 l.3 1.8 M14 -12.9 v1.9 M15.6 -12.6 l-.3 1.7 M10 -6.6 C11 -5.8 12.2 -5.6 13.2 -5.8" stroke="{STRIPE}" stroke-width=".55" fill="none" stroke-linecap="round" opacity=".8"/>')
A(f'<ellipse cx="18.4" cy="-4.6" rx="2.8" ry="2" fill="{CREAM}"/>')
A('<path class="rem" d="M14.6 -8.2 q1.5 1.2 3 0" stroke="#3a1d0b" stroke-width=".55" fill="none" stroke-linecap="round"/>')
A('<path d="M14.3 -8.5 l-.5 -.4 M17.9 -8.5 l.5 -.4" stroke="#3a1d0b" stroke-width=".35" stroke-linecap="round" opacity=".7"/>')
A('<path d="M20.4 -6.2 L21.2 -5.6 L20.5 -5 Z" fill="#b8706c"/>')
A('<path class="whisk" d="M19.4 -4.4 l4.4 .6 M19.4 -3.9 l4 1.4 M19.4 -4.9 l4.2 -.4" stroke="#fff" stroke-width=".22" opacity=".6" stroke-linecap="round"/>')
A('<g transform="translate(21 -6.2)"><g class="bubble">'
  '<circle cx="1.2" cy="-2.4" r="2.6" fill="#bfe3ff" fill-opacity=".28" stroke="#e8f6ff" stroke-width=".3"/>'
  '<path d="M0 -3.7 a1.6 1.6 0 0 1 1.5 -.6" stroke="#fff" stroke-width=".45" fill="none" stroke-linecap="round"/></g>'
  '<g class="pop" fill="none" stroke="#e8f6ff" stroke-width=".35" stroke-linecap="round">'
  '<path d="M1.2 -6 v-1 M3.8 -4.8 l.8 -.6 M4.4 -2 h1 M-1.4 -5 l-.7 -.6 M-2.2 -2.2 h-.9"/></g></g>')
A('<g transform="translate(12.4 -12.2) rotate(-18) scale(.85)">'
  '<path d="M-.4 .4 L-1.6 3.2 M.4 .4 L1.8 3" stroke="#e23d86" stroke-width=".9" stroke-linecap="round"/>'
  '<path d="M0 0 C-2.8 -2.6 -3.9 .6 -2.8 1.7 C-1.9 2.3 -.8 1 0 0 Z M0 0 C2.8 -2.6 3.9 .6 2.8 1.7 C1.9 2.3 .8 1 0 0 Z" fill="#ff5fa2"/>'
  '<path d="M-2.4 -.6 C-2 -1.2 -1.4 -1 -1 -.4 M2.4 -.6 C2 -1.2 1.4 -1 1 -.4" stroke="#ffc2dc" stroke-width=".45" fill="none" stroke-linecap="round"/>'
  '<circle r=".8" fill="#e23d86"/></g>')
A('</g>')
for i in range(2):
    A(f'<path class="purr" style="animation-delay:{i * 1.9:.1f}s" d="M-21.5 -9 q-1.6 2.6 0 5.2 M-23.2 -10 q-2.2 3.6 0 7.2" stroke="#ffd9a8" stroke-width=".4" fill="none" stroke-linecap="round"/>')
A('</g></g>')
for i, (sx, sy, sc) in enumerate(((913, 436, 1), (934, 413, .8), (996, 426, .7))):
    A(f'<g transform="translate({sx} {sy}) scale({sc})"><path class="sparkle" style="animation-delay:{i * 0.85:.2f}s" '
      f'd="M0 -3.4 L.8 -.8 L3.4 0 L.8 .8 L0 3.4 L-.8 .8 L-3.4 0 L-.8 -.8 Z" fill="#ffd76a"/></g>')
for i, fs in enumerate((10, 12.5, 15)):
    A(f'<text class="zz" style="animation-delay:{i * 1.4:.1f}s" x="{968 + i * 4}" y="424" font-family="{MONO}" font-size="{fs}" font-weight="700" '
      f'fill="#e6efff" stroke="#0b1220" stroke-width="1.2" paint-order="stroke">z</text>')
A('</g>')  # end scene

rect(0, 0, W, H, "url(#vignette)")
A(f'<rect width="{W}" height="{OY - 20}" fill="url(#heroShade)"/>')
A(f'<text x="24" y="{OY + 540}" font-family="{MONO}" font-size="13" fill="#c9d1d9" opacity=".85">~/nitin <tspan fill="{ACCENT}">$</tspan> git push --ship<tspan class="blink">_</tspan></text>')

# ---------- owl on the window corner ----------
OWL_X, OWL_Y = 948, OY + 1  # feet rest on the transom
OWL, OWL_DK, FACE, BELLY = "#7a5a3f", "#4e3826", "#ead6b4", "#cfae82"
A(f'<g transform="translate({OWL_X} {OWL_Y})">')
A(f'<path d="M-15 -4 C-20 -18 -17 -34 -9 -38 L9 -38 C17 -34 20 -18 15 -4 Q0 4 -15 -4 Z" fill="{OWL}"/>')
A(f'<path d="M-14 -24 C-20 -16 -18 -6 -11 -2 Z M14 -24 C20 -16 18 -6 11 -2 Z" fill="{OWL_DK}"/>')
A(f'<ellipse cx="0" cy="-15" rx="9.5" ry="11" fill="{BELLY}"/>')
A(f'<path d="M-5 -19 l2 2 l2 -2 M1 -19 l2 2 l2 -2 M-6 -13 l2 2 l2 -2 M0 -13 l2 2 l2 -2 M-3 -7 l2 2 l2 -2 M3 -7 l2 2 l2 -2" stroke="{OWL_DK}" stroke-width=".9" fill="none" opacity=".7"/>')
A(f'<path d="M-6 0 l-1.6 2.6 M-4.4 0 v3 M-2.8 0 l1.6 2.6 M2.8 0 l-1.6 2.6 M4.4 0 v3 M6 0 l1.6 2.6" stroke="{ACCENT2}" stroke-width="1.3" stroke-linecap="round"/>')
A('<g class="owlHead">')
A(f'<path d="M-16 -36 C-17 -48 -12 -56 0 -56 C12 -56 17 -48 16 -36 C14 -29 8 -27 0 -27 C-8 -27 -14 -29 -16 -36 Z" fill="{OWL}"/>')
A(f'<path d="M-14.5 -47 L-16.5 -60 L-6 -54 Z M14.5 -47 L16.5 -60 L6 -54 Z" fill="{OWL_DK}"/>')
A(f'<circle cx="-6.8" cy="-42" r="7.4" fill="{FACE}"/><circle cx="6.8" cy="-42" r="7.4" fill="{FACE}"/>')
for ex in (-6.8, 6.8):
    A(f'<circle cx="{ex}" cy="-42" r="4.6" fill="#ffb13d"/><circle cx="{ex}" cy="-42" r="2.4" fill="#111"/>'
      f'<circle cx="{ex + 1}" cy="-43.2" r=".8" fill="#fff"/>')
    A(f'<rect class="lid" x="{ex - 5}" y="-47" width="10" height="10" rx="5" fill="{OWL}"/>')
A(f'<path d="M-1.8 -38.5 L1.8 -38.5 L0 -34 Z" fill="#e0a040"/>')
A('<path d="M-12 -51.5 C-6 -55.2 6 -55.2 12 -51.5" stroke="#8ec1ff" stroke-width=".9" fill="none" opacity=".35"/>')
A('</g></g>')

# ================= hero (portfolio style, set in the night sky) =================
# status pill
A('<g class="enter">')
rect(50, 36, 200, 32, "#0f1a2c", rx=16, extra=f'stroke="#2c3d5a" fill-opacity="0.6"')
monogram(55, 41, 22)
A(f'<circle class="pulse" cx="92" cy="52" r="4" fill="{SUCCESS}"/>')
A(f'<circle cx="92" cy="52" r="4" fill="{SUCCESS}"/>')
A(f'<text x="104" y="56.5" font-family="{SANS}" font-size="13" font-weight="600" fill="{FG}" textLength="128" lengthAdjust="spacingAndGlyphs">Software Engineer</text>')
A('</g>')
A(f'<g class="enter"><text x="944" y="57" font-family="{MONO}" font-size="13" fill="{FG2}" text-anchor="end">'
  f'nitingovardhane.com <tspan fill="{ACCENT}">↗</tspan></text></g>')
# typed eyebrow
A(f'<text x="{EB_X}" y="{EB_Y}" font-family="{MONO}" font-size="14" font-weight="500" fill="{ACCENT}" '
  f'textLength="{len(EYEBROW) * EB_CW:.1f}" lengthAdjust="spacingAndGlyphs" clip-path="url(#typeClip)">{escape(EYEBROW)}</text>')
A(f'<g class="caret"><rect class="blink" x="{EB_X + 2}" y="{EB_Y - 13}" width="8" height="16" fill="{ACCENT}" opacity="0.85"/></g>')
# headline
A(f'<g class="enter" style="animation-delay:.25s" filter="url(#heroText)"><text x="54" y="170" font-family="{SANS}" font-size="52" font-weight="600" '
  f'letter-spacing="-2" fill="{FG}">Hi, I\'m Nitin Govardhane<tspan dx="14" font-size="44">👋</tspan></text></g>')
# tagline
A(f'<g class="enter" style="animation-delay:.45s" filter="url(#heroText)"><text x="56" y="210" font-family="{SANS}" font-size="21" fill="#c3cfe2">'
  f'Full-stack engineer. I build software that '
  f'<tspan font-family="{SERIF}" font-style="italic" font-size="25" fill="{ACCENT}">keeps working</tspan> after it ships.</text></g>')
# stack chips
A('<g class="enter" style="animation-delay:.65s">')
cx = 56
for name in ("TypeScript", "React", "Next.js", "Node.js", "PostgreSQL", "Supabase", "AI / LLMs"):
    tw = len(name) * 6.9
    rect(cx, 226, tw + 20, 24, "#0f1a2c", rx=12, extra=f'stroke="#2c3d5a" fill-opacity="0.6"')
    A(f'<text x="{cx + 10}" y="242" font-family="{MONO}" font-size="11.5" fill="#c3cfe2" textLength="{tw:.1f}" lengthAdjust="spacingAndGlyphs">{escape(name)}</text>')
    cx += tw + 28
A('</g>')
A('</g>')  # end frame clip
A('</svg>')

svg = out[0] + "\n<style>" + "".join(css) + "</style>\n" + "\n".join(out[1:])
open("images/developer-setup.svg", "w").write(svg)
print("cycle", round(T, 2), "s; bytes", len(svg))
