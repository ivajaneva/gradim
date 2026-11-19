#!/usr/bin/env python3
"""Gradim mockupi – en vir, dve jezikovni različici (mk / sl).
Uporaba: python3 gen.py  -> out/mk.html, out/sl.html
"""
import os, sys

LANG = "mk"
def L(mk, sl):
    return mk if LANG == "mk" else sl

# ---------------------------------------------------------------- ikone (SVG)
def ico(name, c="currentColor", s=22):
    p = {
     "home": '<path d="M3 11l9-7 9 7v9a1 1 0 0 1-1 1h-5v-6h-6v6H4a1 1 0 0 1-1-1z"/>',
     "cal": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
     "warn": '<path d="M12 3l10 18H2z"/><path d="M12 10v5M12 18h.01"/>',
     "box": '<path d="M12 2l9 5v10l-9 5-9-5V7z"/><path d="M3 7l9 5 9-5M12 12v10"/>',
     "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21c1-4 4-6 8-6s7 2 8 6"/>',
     "back": '<path d="M15 5l-7 7 7 7"/>',
     "plus": '<path d="M12 5v14M5 12h14"/>',
     "dots": '<circle cx="5" cy="12" r="1.3"/><circle cx="12" cy="12" r="1.3"/><circle cx="19" cy="12" r="1.3"/>',
     "search": '<circle cx="11" cy="11" r="6"/><path d="M20 20l-4.5-4.5"/>',
     "phone": '<path d="M5 3h4l2 5-2.5 1.5a11 11 0 0 0 6 6L16 13l5 2v4a2 2 0 0 1-2 2A17 17 0 0 1 3 5a2 2 0 0 1 2-2z"/>',
     "check": '<path d="M5 12l5 5 9-10"/>',
     "chev": '<path d="M9 5l7 7-7 7"/>',
     "cam": '<path d="M4 7h4l2-3h4l2 3h4v12H4z"/><circle cx="12" cy="13" r="3.5"/>',
     "pen": '<path d="M4 20l4-1 11-11-3-3L5 16z"/>',
     "pin": '<path d="M12 21s-7-6-7-12a7 7 0 0 1 14 0c0 6-7 12-7 12z"/><circle cx="12" cy="9" r="2.5"/>',
     "undo": '<path d="M9 7L4 12l5 5"/><path d="M4 12h11a5 5 0 0 1 0 10h-2"/>',
     "chat": '<path d="M4 5h16v11H9l-5 4z"/>',
    }[name]
    fill = "none"
    return (f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="{fill}" stroke="{c}" '
            f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{p}</svg>')

def viber(s=24):
    return (f'<span class="vb" style="width:{s}px;height:{s}px">'
            f'<svg width="{s-8}" height="{s-8}" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.2" '
            f'stroke-linecap="round" stroke-linejoin="round"><path d="M12 3c5 0 8 3 8 8s-3 8-8 8c-1 0-2 0-3-.4L5 20l1-3.5C4.5 15 4 13 4 11c0-5 3-8 8-8z"/>'
            f'<path d="M9.5 8.5c0 3 3 6 6 6"/></svg></span>')

def callbtn():
    return f'<span class="cb">{ico("phone","#16a34a",20)}</span>'

# ---------------------------------------------------------------- gradniki
def statusbar(dark=False):
    c = "#fff" if dark else "#111"
    return (f'<div class="sb" style="color:{c}"><span>9:41</span><span class="island"></span>'
            f'<span class="sbr"><svg width="20" height="12" viewBox="0 0 20 12"><g fill="{c}">'
            f'<rect x="0" y="8" width="3" height="4" rx="1"/><rect x="5" y="5.5" width="3" height="6.5" rx="1"/>'
            f'<rect x="10" y="3" width="3" height="9" rx="1"/><rect x="15" y="0" width="3" height="12" rx="1"/></g></svg>'
            f'<svg width="28" height="13" viewBox="0 0 28 13"><rect x=".5" y=".5" width="24" height="12" rx="3.5" fill="none" stroke="{c}" opacity=".5"/>'
            f'<rect x="2.5" y="2.5" width="20" height="8" rx="2" fill="{c}"/><rect x="25.5" y="4" width="2" height="5" rx="1" fill="{c}" opacity=".5"/></svg></span></div>')

def nav(active):
    items = [("home", L("Проекти", "Projekti")), ("cal", L("Календар", "Koledar")),
             ("warn", L("Грешки", "Napake")), ("box", L("Материјал", "Material")),
             ("user", L("Изведувачи", "Izvajalci"))]
    out = '<div class="nav">'
    for i, (ic, lab) in enumerate(items):
        on = i == active
        col = "#f26a1b" if on else "#8a8f98"
        out += f'<div class="ni{" on" if on else ""}">{ico(ic, col, 24)}<span>{lab}</span></div>'
    return out + "</div>"

def head(title, sub=None, back=True, right=None):
    b = f'<span class="rb">{ico("back","#111",20)}</span>' if back else ""
    r = right or ""
    s = f'<div class="hs">{sub}</div>' if sub else ""
    return f'<div class="hd">{b}<div class="ht"><div class="htt">{title}</div>{s}</div>{r}</div>'

def plusbtn(): return f'<span class="pb">{ico("plus","#fff",22)}</span>'
def roundbtn(n): return f'<span class="rb">{ico(n,"#111",20)}</span>'

def field(label, value, cls="", extra=""):
    return f'<div class="fld {cls}"><div class="fl">{label}</div><div class="fv">{value}</div>{extra}</div>'

def chip(t, on=False, cls=""):
    return f'<span class="chip{" on" if on else ""} {cls}">{t}</span>'

def badge(t, kind):
    return f'<span class="bdg {kind}">{t}</span>'

def bar(pct, col="#f26a1b", h=8, mark=None):
    m = f'<span class="mk" style="left:{mark}%"></span>' if mark is not None else ""
    return f'<div class="bar" style="height:{h}px"><span style="width:{pct}%;background:{col}"></span>{m}</div>'

def avatar(t, col, s=40):
    return f'<span class="av" style="background:{col};width:{s}px;height:{s}px;font-size:{s*0.38:.0f}px">{t}</span>'

def btn(t, kind="pri", cls=""):
    return f'<div class="btn {kind} {cls}">{t}</div>'

def sec(t): return f'<div class="sec">{t}</div>'

def tiles(h, cls=""):
    return f'<div class="tiles {cls}" style="height:{h}px"></div>'

def phone(content, dark_top=False, bg="#f3f4f6"):
    return (f'<div class="phone"><div class="scr" style="background:{bg}">'
            f'{statusbar(dark_top)}{content}</div></div>')

# ---------------------------------------------------------------- zasloni
def s01():
    st = lambda n, t, c, bg: (f'<div class="st" style="background:{bg}"><b style="color:{c}">{n}</b>'
                              f'<span>{t}</span></div>')
    def proj(img, name, loc, b, pct, col, phase, eng):
        return (f'<div class="card pj"><div class="pjr"><span class="pji" style="background:{img}"></span>'
                f'<div class="pjt"><b>{name}</b><span>{loc}</span></div>{b}</div>'
                f'<div class="pjb">{bar(pct, col)}<b>{pct}%</b></div>'
                f'<div class="pjf"><span>{phase}</span><span>👷 {eng}</span></div></div>')
    top = (f'<div class="dtop"><div class="dd">{L("Сабота, 7 ноември", "Sobota, 7. november")}</div>'
           f'<div class="dh">{L("Добро утро, Марко", "Dobro jutro, Marko")}</div><div class="sts">'
           + st("3", L("активни проекти", "aktivni projekti"), "#fff", "#2c3340")
           + st("15", L("отворени грешки", "odprte napake"), "#ff8a7a", "#2c3340")
           + st("2", L("барања те чекаат", "zahtevka te čakata"), "#ffb067", "#5a3a28")
           + '</div></div>')
    body = (sec(L("ПРОЕКТИ", "PROJEKTI"))
        + proj("linear-gradient(135deg,#d9cbb6,#a8957a)", L("Станбена зграда Лиман 4", "Stanovanjska stavba Liman 4"),
               L("Нови Сад · П+4 · 24 стана", "Novi Sad · P+4 · 24 stanovanj"), badge(L("Доцни 4 д", "Zamuja 4 d"), "red"),
               62, "#f26a1b", L("Фаза: Керамика · Фасада", "Faza: Keramika · Fasada"), L("2 инженери", "2 inženirja"))
        + proj("linear-gradient(135deg,#9aa3b0,#6b7482)", L("Семејна куќа Златибор", "Družinska hiša Zlatibor"),
               L("Чајетина · П+1+Пк", "Čajetina · P+1+M"), badge(L("Според план", "Po planu"), "green"),
               35, "#16a34a", L("Фаза: Покрив", "Faza: Streha"), L("1 инженер", "1 inženir"))
        + proj("repeating-linear-gradient(90deg,#c98f5a 0 12px,#d9a06b 12px 24px)", L("Адаптација на деловен простор", "Prenova poslovnega prostora"),
               L("Белград · 420 m²", "Beograd · 420 m²"), badge(L("Според план", "Po planu"), "green"),
               88, "#16a34a", L("Фаза: Ламперија · завршни", "Faza: Opaž · zaključna dela"), L("1 инженер", "1 inženir"))
        + f'<div class="fab">{ico("plus","#fff",18)} {L("Нов проект", "Nov projekt")}</div>')
    return phone(top + f'<div class="body">{body}</div>' + nav(0), dark_top=True, bg="#f3f4f6")

def s02():
    team = [("MJ", "#1f2937", L("Марко Јовиќ", "Marko Jović"), L("Директор на фирмата", "Direktor podjetja"), badge(L("Директор", "Direktor"), "gray")),
            ("AC", "#2563eb", L("Ана Станковиќ", "Ana Stanković"), L("Инженер · +381 64 123 4567", "Inženirka · +381 64 123 4567"), badge(L("Главен", "Glavna"), "blue")),
            ("НП" if LANG == "mk" else "NP", "#7c3aed", L("Никола Периќ", "Nikola Perić"), L("Инженер · +381 63 555 0101", "Inženir · +381 63 555 0101"), badge(L("Инженер", "Inženir"), "gray"))]
    rows = "".join(f'<div class="row">{avatar(a, c)}<div class="rt"><b>{n}</b><span>{d}</span></div>{b}</div>' for a, c, n, d, b in team)
    rows += f'<div class="row add"><span class="addc">{ico("plus","#f26a1b",20)}</span><b>{L("Додај инженер од фирмата", "Dodaj inženirja iz podjetja")}</b></div>'
    body = (field(L("Име на проектот", "Ime projekta"), L("Станбена зграда Лиман 4", "Stanovanjska stavba Liman 4"))
        + field(L("Адреса", "Naslov"), L("Булевар деспота Стефана 12, Нови Сад", "Bulevar despota Stefana 12, Novi Sad"))
        + '<div class="g2">' + field(L("Почеток", "Začetek"), "01.03.2026") + field(L("Рок за завршување", "Rok za dokončanje"), "30.04.2027") + "</div>"
        + sec(L("ТИП НА ПРОЕКТ", "TIP PROJEKTA"))
        + '<div class="chips">' + chip(L("Станбена зграда", "Stanovanjska stavba"), True) + chip(L("Куќа", "Hiša"))
        + chip(L("Адаптација на стан", "Prenova stanovanja")) + chip(L("Деловен простор", "Poslovni prostor"))
        + "</div>"
        + f'<div class="note">{L("Проектот добива 20 стандардни фази – инженерот може да исклучи фаза или да додаде нова. Во чекор 2 се внесуваат катовите и становите.", "Projekt dobi 20 privzetih faz – inženir lahko fazo izklopi ali doda novo. V koraku 2 se vnesejo nadstropja in stanovanja.")}</div>'
        + sec(L("ТИМ НА ПРОЕКТОТ", "EKIPA PROJEKTA"))
        + f'<div class="card list">{rows}</div>'
        + btn(L("Креирај проект", "Ustvari projekt")))
    return phone(head(L("Нов проект", "Nov projekt"), L("Чекор 1 од 2 · Основно и тим", "Korak 1 od 2 · Osnovno in ekipa")) + f'<div class="body">{body}</div>')

def s03():
    ring = ('<div class="ring"><svg width="140" height="140" viewBox="0 0 140 140"><circle cx="70" cy="70" r="58" fill="none" stroke="#e5e7eb" stroke-width="14"/>'
            '<circle cx="70" cy="70" r="58" fill="none" stroke="#f26a1b" stroke-width="14" stroke-dasharray="226 365" stroke-linecap="butt" transform="rotate(-90 70 70)"/></svg>'
            f'<div class="rc"><b>62%</b><span>{L("завршено", "dokončano")}</span></div></div>')
    kv = lambda k, v: f'<div class="kv"><span>{k}</span><b>{v}</b></div>'
    stats = (f'<div class="rs">{kv(L("Завршени задачи", "Dokončane naloge"), "87 / 140")}{kv(L("Во тек", "V teku"), "21")}'
             f'{kv(L("Не е почнато", "Ni začeto"), "32")}{badge(L("6 задачи доцнат", "6 nalog zamuja"), "red")}</div>')
    qa = [("⚠️", L("Пријави грешка", "Prijavi napako")), ("📦", L("Побарај материјал", "Zahtevaj material")),
          ("📊", L("Преглед на материјал", "Pregled materiala")), ("🗓️", L("Нов термин", "Nov termin"))]
    q = '<div class="qa">' + "".join(f'<div class="qai"><span>{e}</span><b>{t}</b></div>' for e, t in qa) + "</div>"
    fin = (f'<div class="card"><div class="ct">{L("Финансии на проектот", "Finance projekta")}</div>'
           + kv(L("Договорено со изведувачи", "Dogovorjeno z izvajalci"), "38,6 " + L("мил.", "mio.") + " RSD")
           + kv(L("Платено за завршени задачи", "Plačano za dokončane naloge"), "24,1 " + L("мил.", "mio."))
           + kv(L("Материјал (потрошено)", "Material (porabljeno)"), "18,4 " + L("мил.", "mio."))
           + bar(62) + "</div>")
    op = lambda c, n, t: f'<div class="op"><i style="background:{c}"></i><div><b>{n}</b><span>{t}</span></div></div>'
    opened = (sec(L("ОТВОРЕНО", "ODPRTO")) + '<div class="ops">' + op("#ef4444", "12", L("грешки", "napak"))
              + op("#f59e0b", "1", L("барање", "zahtevek")) + op("#3b82f6", "3", L("термини денес", "termini danes")) + "</div>")
    body = f'<div class="card rr">{ring}{stats}</div>' + q + fin + opened
    return phone(head(L("Лиман 4", "Liman 4"), L("Станбена зграда · Нови Сад", "Stanovanjska stavba · Novi Sad"), right=roundbtn("dots"))
                 + f'<div class="body">{body}</div>' + nav(0))

def taskrow(state, name, who, price):
    dot = {"done": '<i class="dt done"></i>', "prog": '<i class="dt prog"></i>', "todo": '<i class="dt todo"></i>'}[state]
    return f'<div class="tr">{dot}<div class="rt"><b>{name}</b><span>{who}</span></div><b class="pr">{price}</b></div>'

def s04():
    def phase(name, done, tot, pct, rows):
        return (f'<div class="card ph"><div class="phh"><b>{name}</b><span>{done}/{tot}</span></div>{bar(pct)}{rows}</div>')
    body = (f'<div class="seg"><span class="on">{L("По фаза", "Po fazi")}</span><span>{L("По стан", "Po stanovanju")}</span><span>{L("По изведувач", "Po izvajalcu")}</span></div>'
        + phase(L("Инсталации", "Inštalacije"), 34, 40, 85,
                taskrow("done", L("Стан 9 · Разводна табла", "Stan 9 · Razdelilna omarica"), L("Волт ДОО · шеф: Драган", "Volt d.o.o. · vodja: Dragan"), "85.000")
                + taskrow("prog", L("Стан 12 · Водовод бања", "Stan 12 · Vodovod kopalnica"), L("Термо инстал", "Termo instal"), "120.000"))
        + phase(L("Керамика", "Keramika"), 9, 24, 38,
                taskrow("prog", L("Стан 12 · Бања – плочки", "Stan 12 · Kopalnica – ploščice"), L("Јован Петровиќ", "Jovan Petrović"), "96.000")
                + taskrow("todo", L("Стан 11 · Бања – плочки", "Stan 11 · Kopalnica – ploščice"), L("Јован Петровиќ", "Jovan Petrović"), "96.000"))
        + phase(L("Мебел и завршни", "Pohištvo in zaključna dela"), 0, 18, 0,
                taskrow("todo", L("Стан 12 · Спална – монтажа на плакар", "Stan 12 · Spalnica – montaža omare"), L("Столарија Ковач", "Mizarstvo Kovač"), "140.000"))
        + f'<div class="cap">{L("20 стандардни фази – инженерот може да исклучи фаза или да додаде нова.", "20 privzetih faz – inženir lahko fazo izklopi ali doda novo.")}</div>')
    return phone(head(L("План на работи", "Plan del"), L("Лиман 4 · 140 задачи", "Liman 4 · 140 nalog"), right=plusbtn())
                 + f'<div class="body">{body}</div>' + nav(0))

def s05():
    apts = "".join(chip(x, x == "12", "circ sq") for x in ["9", "10", "11", "12", "13", "14"])
    body = (field(L("Фаза", "Faza"), L("Керамика", "Keramika"))
        + field(L("Што се работи (глагол + предмет)", "Kaj se dela (glagol + predmet)"), L("Поставување ѕидни и подни плочки", "Polaganje stenskih in talnih ploščic"))
        + f'<div class="sl">{L("Обем", "Obseg")}</div><div class="seg s3"><span>{L("Цела зграда", "Cela stavba")}</span><span>{L("Кат", "Nadstropje")}</span><span class="on">{L("Станови", "Stanovanja")}</span></div>'
        + f'<div class="sl">{L("Станови · 3. кат", "Stanovanja · 3. nadstropje")}</div><div class="chips">' + apts + "</div>"
        + f'<div class="sl">{L("Простор", "Prostor")}</div><div class="chips">' + chip(L("Сите", "Vsi")) + chip(L("Бања", "Kopalnica"), True) + chip(L("Кујна", "Kuhinja")) + chip(L("Дневна", "Dnevna")) + chip(L("Спална", "Spalnica")) + "</div>"
        + f'<div class="hint"><span>{L("Насловот се прави сам:", "Naslov se sestavi sam:")}</span><b>{L("Стан 12 · Бања – Поставување плочки", "Stan 12 · Kopalnica – Polaganje ploščic")}</b>'
          f'<em>{L("„Цела зграда + Бања“ = сите бањи во зградата", "»Cela stavba + Kopalnica« = vse kopalnice v stavbi")}</em></div>'
        + field(L("Изведувач", "Izvajalec"), L("Јован Петровиќ · керамичар", "Jovan Petrović · keramičar"), extra=avatar(L("ЈП", "JP"), "#0ea5e9", 34))
        + '<div class="g2">' + field(L("Договорена цена", "Dogovorjena cena"), "<b>96.000 RSD</b>") + field(L("Рок", "Rok"), "14.11.2026") + "</div>"
        + btn(L("Зачувај задача", "Shrani nalogo")))
    return phone(head(L("Нова задача", "Nova naloga"), L("Лиман 4", "Liman 4")) + f'<div class="body b5">{body}</div>')

def s06():
    top = (f'<div class="card"><div class="rowb">{badge(L("Во тек", "V teku"), "orange")}<span class="muted">{L("Рок", "Rok")}: 14.11.2026</span></div>'
           f'<div class="row nob">{avatar(L("ЈП", "JP"), "#0ea5e9")}<div class="rt"><b>{L("Јован Петровиќ", "Jovan Petrović")}</b>'
           f'<span>{L("Керамичар · 2 отворени грешки", "Keramičar · 2 odprti napaki")}</span></div>{viber()}{callbtn()}</div></div>')
    price = (f'<div class="card"><div class="rowb"><span class="fl">{L("Договорена цена", "Dogovorjena cena")}</span>{badge(L("Работа + превоз", "Delo + prevoz"), "gray")}</div>'
             f'<div class="big">96.000 RSD</div><div class="rowb muted"><span>{L("Платен аванс", "Plačan avans")}: 30.000</span><span>{L("Останува", "Ostane")}: 66.000</span></div></div>')
    mat = (sec(L("МАТЕРИЈАЛ ЗА ОВАА ЗАДАЧА", "MATERIAL ZA TO NALOGO"))
           + f'<div class="card list"><div class="row"><div class="rt"><b class="n">{L("Плочки 30×60 сива мат", "Ploščice 30×60 siva mat")}</b></div><b>22 m²</b>{badge(L("фали 4", "manjka 4"), "red")}</div>'
           f'<div class="row"><div class="rt"><b class="n">{L("Лепак C2TE", "Lepilo C2TE")}</b></div><b>6 {L("вр.", "vr.")}</b>{badge("ok", "green")}</div></div>')
    ph = (sec(L("ФОТОГРАФИИ (3)", "FOTOGRAFIJE (3)")) + '<div class="phs"><span class="ph1 gray"></span><span class="ph1 tl"></span><span class="ph1 tl lt"></span>'
          f'<span class="ph1 addp">{ico("plus","#9ca3af",26)}</span></div>')
    btns = (f'<div class="g2 w12">{btn("⚠ " + L("Грешка", "Napaka"), "outline-red")}{btn(ico("check","#fff",18) + " " + L("Означи завршено", "Označi dokončano"), "green")}</div>')
    return phone(head(L("Стан 12 · Бања", "Stan 12 · Kopalnica"), L("Поставување плочки · Керамика", "Polaganje ploščic · Keramika"))
                 + f'<div class="body">{top}{price}{mat}{ph}{btns}</div>' + nav(0))

def s07():
    body = (f'<div class="sl">{L("Фотографија од завршената работа (опционално)", "Fotografija opravljenega dela (neobvezno)")}</div>'
        + f'<div class="photo">{tiles(240)}<span class="geo">📍 {L("Лиман 4", "Liman 4")} · 7.11. 15:42</span></div>'
        + f'<div class="phs3"><span class="ph1 tl lt"></span><span class="ph1 tl dk"></span><span class="ph1 addp">📷</span></div>'
        + f'<div class="card"><b class="q">{L("Работата е направена како што треба?", "Je delo opravljeno pravilno?")}</b>'
          f'<span class="muted sm">{L("Ако не – пријави грешка наместо затворање", "Če ne – namesto zaključka prijavi napako")}</span>'
          f'<div class="g2">{btn(L("Да, сè е OK", "Da, vse je v redu"), "green sm")}{btn(L("Има забелешки", "Imam pripombe"), "outline sm")}</div></div>'
        + f'<div class="card"><div class="kv"><span>{L("За исплата на изведувачот", "Za izplačilo izvajalcu")}</span><b class="lg">66.000 RSD</b></div>'
          f'<div class="kv"><span>{L("Потрошен материјал", "Porabljen material")}</span><b class="lg">{L("22 m² плочки, 6 вр. лепак", "22 m² ploščic, 6 vr. lepila")}</b></div></div>'
        + field(L("Забелешка (опционално)", "Opomba (neobvezno)"), L("Силиконот околу кадата е направен дополнително.", "Silikon okoli kadi je bil narejen dodatno."))
        + btn(ico("check", "#fff", 18) + " " + L("Завршено", "Dokončano"), "green"))
    return phone(head(L("Заврши задача", "Zaključi nalogo"), L("Стан 12 · Бања – Поставување плочки", "Stan 12 · Kopalnica – Polaganje ploščic")) + f'<div class="body">{body}</div>')

def s08():
    days = L(["П", "В", "С", "Ч", "П", "С", "Н"], ["P", "T", "S", "Č", "P", "S", "N"])
    dots = [1, 1, 0, 1, 0, 1, 0]
    wk = '<div class="card wk">' + "".join(
        f'<div class="dy{" on" if i == 0 else ""}"><span>{d}</span><b>{9+i}</b>{"<i></i>" if dots[i] else ""}</div>'
        for i, d in enumerate(days)) + "</div>"
    def ev(t, col, title, sub, b):
        return (f'<div class="ev"><span class="evt">{t}</span><div class="evc" style="border-left-color:{col}">'
                f'<div class="rt"><b>{title}</b><span>{sub}</span></div>{b}</div></div>')
    body = (wk + sec(L("ПОНЕДЕЛНИК, 9 НОЕ", "PONEDELJEK, 9. NOV."))
        + ev("07:00", "#0ea5e9", L("Јован Петровиќ – керамика", "Jovan Petrović – keramika"), L("Стан 12 · Бања · договорено по телефон", "Stan 12 · Kopalnica · dogovorjeno po telefonu"), badge(L("Дојде ✓", "Prišel ✓"), "green"))
        + ev("08:00", "#eab308", L("Волт ДОО – 3 работници", "Volt d.o.o. – 3 delavci"), L("Стан 9 · Разводна табла · шеф Драган", "Stan 9 · Razdelilna omarica · vodja Dragan"), badge(L("Не дојде", "Ni prišel"), "red"))
        + ev("10:30", "#7c3aed", L("Испорака: плочки 30×60", "Dobava: ploščice 30×60"), L("Керамика Центар · барање MT-142", "Keramika Center · zahtevek MT-142"), badge(L("Достава", "Dobava"), "blue"))
        + ev("13:00", "#16a34a", L("Столарија Ковач – мерење", "Mizarstvo Kovač – meritev"), L("Станови 11 и 12 · плакари", "Stanovanji 11 in 12 · omare"), badge(L("Закажано", "Dogovorjeno"), "gray"))
        + sec(L("ТРЕБА ДА СЕ ЗАКАЖЕ", "TREBA DOGOVORITI"))
        + f'<div class="card warmc"><div class="rt"><b>{L("Фасадери – демит, север", "Fasaderji – demit, sever")}</b>'
          f'<span>{L("Малтер 4. кат речиси готов · нема термин", "Omet 4. nadstr. skoraj končan · ni termina")}</span></div>'
          f'<span class="callo">{ico("phone","#fff",15)} {L("Јави се", "Pokliči")}</span></div>')
    return phone(head(L("Календар на градилиштето", "Koledar gradbišča"), L("Ноември 2026 · Лиман 4", "November 2026 · Liman 4"), back=False, right=plusbtn())
                 + f'<div class="body">{body}</div>' + nav(1))

def s09():
    body = (field(L("Кој доаѓа", "Kdo pride"), L("Волт ДОО · шеф на екипа Драган", "Volt d.o.o. · vodja ekipe Dragan"), extra=avatar("VT" if LANG == "sl" else "ВТ", "#eab308", 38))
        + field(L("За задача", "Za nalogo"), L("Стан 9 · Разводна табла – Поврзување", "Stan 9 · Razdelilna omarica – Priklop"))
        + '<div class="g2">' + field(L("Датум", "Datum"), L("Вторник, 10.11.", "Torek, 10. 11.")) + field(L("Време", "Ura"), "07:30") + "</div>"
        + f'<div class="sl">{L("Колку луѓе", "Število oseb")}</div><div class="chips">' + chip("1", cls="circ") + chip("2", cls="circ") + chip("3", True, "circ") + chip("4+", cls="circ") + "</div>"
        + f'<div class="sl">{L("Како е договорено", "Kako je dogovorjeno")}</div><div class="chips">'
        + chip("📞 " + L("По телефон", "Po telefonu"), True) + chip("💬 Viber") + chip(L("Во живо", "V živo")) + "</div>"
        + field(L("Забелешка", "Opomba"), L("Во понеделник не дојдоа – рече дека сигурно доаѓаат во вторник наутро.", "V ponedeljek niso prišli – rekel je, da zagotovo pridejo v torek zjutraj."))
        + f'<div class="card tg"><div class="rt"><b>{L("Потсети ме", "Opomni me")}</b><span>{L("Вечерта пред тоа – да го повикам и проверам", "Večer prej – da ga pokličem in preverim")}</span></div><span class="tgl"><i></i></span></div>'
        + btn(L("Зачувај термин", "Shrani termin")))
    return phone(head(L("Нов термин за доаѓање", "Nov termin prihoda"), L("Лиман 4", "Liman 4")) + f'<div class="body">{body}</div>')

def s10():
    img = (f'<div class="photo">{tiles(178)}<span class="circle" style="left:180px;top:52px"></span>'
           f'<span class="tag" style="left:266px;top:40px">{L("фуга 5 mm", "fuga 5 mm")}</span>'
           f'<span class="geo r">✎ {L("Означи на сликата", "Označi na sliki")}</span></div>')
    body = (img + field(L("Задача / локација", "Naloga / lokacija"), L("Стан 12 · Бања – Поставување плочки", "Stan 12 · Kopalnica – Polaganje ploščic"))
        + field(L("Кој е одговорен (од задачата)", "Kdo je odgovoren (iz naloge)"), L("Јован Петровиќ · керамичар", "Jovan Petrović · keramičar"), extra='<span class="muted tel">064 222 3344</span>')
        + f'<div class="sl">{L("Сериозност", "Resnost")}</div><div class="chips">' + chip(L("Ниска", "Nizka")) + chip(L("Средна", "Srednja"), True, "or")
        + chip(L("Висока", "Visoka")) + chip(L("Критична", "Kritična")) + "</div>"
        + field(L("Опис и како треба да изгледа кога ќе се реши", "Opis in kako mora izgledati po popravku"),
                L("Плочките не се во рамнина, фуги 2–5 mm. Да се отстрани долниот ред и повторно да се постави, фуга 3 mm.", "Ploščice niso v ravnini, fuge 2–5 mm. Odstraniti spodnjo vrsto in jo ponovno položiti, fuga 3 mm."))
        + field(L("Рок за поправка", "Rok za popravilo"), "13.11.2026")
        + btn(viber(22) + " " + L("Зачувај и прати на Viber", "Shrani in pošlji na Viber"), "viber")
        + btn(L("Само зачувај", "Samo shrani"), "outline"))
    return phone(head(L("Нова грешка", "Nova napaka"), L("Лиман 4", "Liman 4")) + f'<div class="body">{body}</div>')

def s11():
    hdr = (f'<div class="vh"><span>{ico("back","#fff",20)}</span>{avatar("AC" if LANG=="sl" else "АС", "#2563eb", 38)}'
           f'<div class="rt"><b>{L("Ана Станковиќ", "Ana Stanković")}</b><span>Viber · {L("онлајн", "na spletu")}</span></div></div>')
    msg = (f'<div class="day">{L("Денес", "Danes")}</div><div class="bub">'
           f'<div class="photo in">{tiles(176)}<span class="circle" style="left:140px;top:48px"></span></div>'
           f'<div class="bt">⚠️ <b>{L("Грешка", "Napaka")} GR-031</b> – {L("Лиман 4", "Liman 4")}<br>📍 {L("Стан 12 · Бања", "Stan 12 · Kopalnica")}<br>'
           f'{L("Плочките не се во рамнина, фуги 2–5 mm. Да се отстрани долниот ред и повторно да се постави, фуга 3 mm.", "Ploščice niso v ravnini, fuge 2–5 mm. Odstraniti spodnjo vrsto in jo ponovno položiti, fuga 3 mm.")}<br>'
           f'⏰ {L("Рок", "Rok")}: <b>13.11.</b><div class="sent">{L("Испратено од апликацијата Gradim", "Poslano iz aplikacije Gradim")}</div></div></div>'
           f'<div class="tm r">15:58 ✓✓</div>'
           f'<div class="bub2">{L("Видов, доаѓам во вторник да поправам.", "Videl, pridem v torek popravit.")}</div><div class="tm">16:20</div>'
           f'<div class="card how"><b>{L("Како работи:", "Kako deluje:")}</b> {L("апликацијата го отвора Viber со веќе подготвена слика и текст, инженерот само притиска „Испрати“. Мајсторот не инсталира ништо – пораката доаѓа од личност што ја познава.", "aplikacija odpre Viber z že pripravljeno sliko in besedilom, inženir pritisne samo »Pošlji«. Mojster ne namesti ničesar – sporočilo prejme od osebe, ki jo pozna.")}</div>')
    return phone(hdr + f'<div class="body vbody">{msg}</div>', dark_top=True, bg="#e9e5f7")

def s12():
    def de(code, b, title, loc, who, ago, img, warn=False):
        return (f'<div class="card de"><span class="dei {img}"></span><div class="rt"><div class="rowb"><span class="code">{code}</span>{b}</div>'
                f'<b>{title}</b><span>{loc}</span><div class="rowb"><span>👷 {who}</span><span class="{"red" if warn else ""}">{"⚠ " if warn else ""}{ago}</span></div></div></div>')
    flt = ('<div class="chips nowrap">' + chip(L("Сите 12", "Vse 12"), True)
           + chip('<i class="cd" style="background:#ef4444"></i>' + L("Отворени 5", "Odprte 5"))
           + chip('<i class="cd" style="background:#7c3aed"></i>' + L("Јавени 4", "Sporočene 4"))
           + chip('<i class="cd" style="background:#f59e0b"></i>' + L("Во поправка 3", "V popravilu 3")) + "</div>")
    body = (flt
        + de("GR-031", badge(L("Јавено преку Viber", "Poslano prek Viberja"), "purple"), L("Нерамни плочки, фуги 2–5 mm", "Neravne ploščice, fuge 2–5 mm"), L("Стан 12 · Бања", "Stan 12 · Kopalnica"), L("Јован Петровиќ", "Jovan Petrović"), L("пред 2 ч", "pred 2 h"), "tl")
        + de("GR-029", badge(L("Во поправка", "V popravilu"), "orange"), L("Штекер надвор од оската, 4 cm", "Vtičnica izven osi, 4 cm"), L("Стан 9 · Дневна соба", "Stan 9 · Dnevna soba"), L("Волт ДОО", "Volt d.o.o."), L("3 дена", "3 dni"), "bg")
        + de("GR-027", badge(L("Отворено", "Odprto"), "red"), L("Пукнатина во малтерот околу прозорецот", "Razpoka v ometu okoli okna"), L("Стан 7 · Спална", "Stan 7 · Spalnica"), L("Малтер тим Ж.", "Omet tim Ž."), L("5 дена", "5 dni"), "bg")
        + de("GR-024", badge(L("Критично", "Kritično"), "red"), L("Протекува спој на одводот", "Pušča spoj odtoka"), L("Стан 4 · Кујна", "Stan 4 · Kuhinja"), L("Термо инстал", "Termo instal"), L("8 дена", "8 dni"), "gr", True)
        + f'<div class="card rowb"><div class="rt"><span>{L("Најмногу грешки (30 дена)", "Največ napak (30 dni)")}</span><b>{L("Волт ДОО – 5 · Малтер тим – 4", "Volt d.o.o. – 5 · Omet tim – 4")}</b></div>{ico("chev","#f26a1b",20)}</div>')
    return phone(head(L("Грешки", "Napake"), L("Лиман 4 · 12 активни", "Liman 4 · 12 aktivnih"), back=False, right=roundbtn("search"))
                 + f'<div class="body">{body}</div>' + nav(2))

def s13():
    steps = [L("Отворено", "Odprto"), L("Јавено", "Sporočeno"), L("Во поправка", "V popravilu"), L("Решено", "Rešeno")]
    cols = ["#16a34a", "#16a34a", "#f26a1b", "#d1d5db"]
    tl = '<div class="steps">' + "".join(f'<div><i style="background:{c}"></i><span class="{"muted" if i==3 else ""}">{s}</span></div>' for i, (s, c) in enumerate(zip(steps, cols))) + "</div>"
    hist = [("⚠️", L("Ана пријави грешка", "Ana je prijavila napako"), L("7 ное 15:58", "7. nov. 15:58")),
            ("💬", L("Испратено на Јован на Viber", "Poslano Jovanu na Viber"), L("7 ное 15:58", "7. nov. 15:58")),
            ("📝", L("„Рече дека доаѓа во вторник“ – белешка", "»Pravi, da pride v torek« – opomba"), L("8 ное 08:10", "8. nov. 08:10")),
            ("🗓️", L("Термин: вторник 10.11. во 07:00", "Termin: torek 10. 11. ob 07:00"), L("8 ное 08:11", "8. nov. 08:11"))]
    h = '<div class="card list">' + "".join(f'<div class="row hi"><span class="hic">{e}</span><div class="rt"><b class="n">{t}</b><span>{d}</span></div></div>' for e, t, d in hist) + "</div>"
    body = (f'<div class="photo">{tiles(140)}<span class="circle" style="left:176px;top:34px"></span></div>'
        + f'<div class="card"><div class="rowb"><span>{badge(L("Во поправка", "V popravilu"), "orange")} {badge(L("Средна", "Srednja"), "peach")}</span><span class="muted">{L("Рок", "Rok")} 13.11.</span></div>{tl}</div>'
        + f'<div class="card row nob">{avatar(L("ЈП", "JP"), "#0ea5e9")}<div class="rt"><b>{L("Јован Петровиќ", "Jovan Petrović")}</b><span>{L("Одговорен · керамичар", "Odgovoren · keramičar")}</span></div>{viber()}{callbtn()}</div>'
        + sec(L("ИСТОРИЈА (ВНЕСУВА ИНЖЕНЕРОТ)", "ZGODOVINA (VNAŠA INŽENIR)")) + h
        + f'<div class="g2 w12">{btn("📷 " + L("Слика", "Slika"), "outline")}{btn(ico("check","#fff",18) + " " + L("Означи решено", "Označi rešeno"), "green")}</div>'
        + f'<div class="cap">{L("Сликата од поправката е опционална.", "Fotografija popravila je neobvezna.")}</div>')
    return phone(head("GR-031", L("Нерамни плочки · Стан 12", "Neravne ploščice · Stan 12")) + f'<div class="body">{body}</div>')

def s14():
    tot = lambda t, v, cls="": f'<div class="tot {cls}"><span>{t}</span><b>{v}</b></div>'
    def it(name, b, o, d, p, amt):
        return (f'<div class="it"><div class="rowb"><b>{name}</b>{b}</div><div class="itn">'
                f'<span>{L("Нарачано", "Naročeno")} <b>{o}</b></span><span>{L("Докупено", "Dokupljeno")} <b>{d}</b></span>'
                f'<span>{L("Потрошено", "Porabljeno")} <b>{p}</b></span><b class="amt">{amt}</b></div></div>')
    body = ('<div class="tots">' + tot(L("Вкупно купено", "Skupaj kupljeno"), "19,2 " + L("мил.", "mio."))
        + tot(L("Потрошено", "Porabljeno"), "18,4 " + L("мил.", "mio.")) + tot(L("Вишокот вреди", "Vrednost viška"), "35.300", "gr") + "</div>"
        + '<div class="chips nowrap">' + chip(L("Сите", "Vse"), True) + chip(L("Керамика", "Keramika")) + chip(L("Инсталации", "Inštalacije")) + chip(L("Малтер", "Omet")) + "</div>"
        + '<div class="card its">'
        + it(L("Плочки 30×60 сива мат (m²)", "Ploščice 30×60 siva mat (m²)"), badge(L("Останато 7 m²", "Ostalo 7 m²"), "green"), 100, 25, 118, "212.500")
        + it(L("Лепак C2TE (вреќа)", "Lepilo C2TE (vreča)"), badge(L("Останато 26 вр.", "Ostalo 26 vr."), "green"), 90, 0, 64, "81.000")
        + it(L("Кабел PP-Y 3×2,5 (m)", "Kabel PP-Y 3×2,5 (m)"), badge(L("Потрошено", "Porabljeno"), "gray"), 2000, 300, 2300, "391.000")
        + it(L("Хидроизолација 2K (парче)", "Hidroizolacija 2K (kos)"), badge(L("Фали", "Manjka"), "red"), 30, 0, 30, "96.000")
        + f'<div class="cap l">{L("Колони: количина · износ во RSD", "Stolpci: količina · znesek v RSD")}</div></div>'
        + f'<div class="g2">{btn(L("Фали материјал", "Manjka material"), "outline-red")}{btn("+ " + L("Внеси купување", "Vnesi nakup"))}</div>')
    return phone(head(L("Материјал", "Material"), L("Лиман 4 · сите количини", "Liman 4 · vse količine"), back=False, right=roundbtn("search"))
                 + f'<div class="body">{body}</div>' + nav(3))

def s15():
    col = lambda t, v, c="#111": f'<div class="c3"><span>{t}</span><b style="color:{c}">{v}</b><span>m²</span></div>'
    top = (f'<div class="card"><div class="g3">{col(L("Купено", "Kupljeno"), 125)}{col(L("Потрошено", "Porabljeno"), 118)}{col(L("Останато", "Ostalo"), 7, "#16a34a")}</div>{bar(94, "#16a34a")}</div>')
    hist = [("🛒", L("Нарачано – почетна нарачка", "Naročeno – začetno naročilo"), "+100", "170.000", ""),
            ("⚠️", L("Јован јави дека фали (стан 12)", "Jovan sporoči, da manjka (stan 12)"), "—", "", ""),
            ("🛒", L("Докупено – барање MT-142", "Dokupljeno – zahtevek MT-142"), "+25", "42.500", ""),
            ("🧱", L("Потрошено – 6 керамички задачи", "Porabljeno – 6 keramičnih nalog"), "−118", "", "red")]
    h = '<div class="card list">' + "".join(f'<div class="row hi"><span class="hic">{e}</span><div class="rt"><b class="n">{t}</b></div><b class="{c} q2">{q}</b><span class="muted pr2">{p}</span></div>' for e, t, q, p, c in hist) + "</div>"
    surplus = (f'<div class="card grc"><b>{L("Вишок: 7 m² (3 неотворени кутии)", "Višek: 7 m² (3 neodprte škatle)")}</b>'
               f'<div class="kv"><span>{L("Добавувачот прима враќање", "Dobavitelj sprejme vračilo")}</span><b class="green">{L("Да, до 30 дена", "Da, do 30 dni")}</b></div>'
               f'<div class="kv"><span>{L("Враќање пари", "Vračilo denarja")}</span><b class="lg">11.900 RSD</b></div></div>')
    btns = f'<div class="g2">{btn(L("Задржи како резерва", "Obdrži kot rezervo"), "outline")}{btn(ico("undo","#fff",18) + " " + L("Врати на добавувачот", "Vrni dobavitelju"), "green")}</div>'
    return phone(head(L("Плочки 30×60 сива мат", "Ploščice 30×60 siva mat"), L("Керамика · 1.700 RSD/m²", "Keramika · 1.700 RSD/m²"))
                 + f'<div class="body">{top}{sec(L("ИСТОРИЈА", "ZGODOVINA"))}{h}{surplus}{btns}</div>')

def s16():
    top = (f'<div class="card"><div class="rowb"><span>{badge(L("Чека одобрување", "Čaka odobritev"), "yellow")} {badge(L("Итно", "Nujno"), "red")}</span><span class="muted">{L("пред 25 мин", "pred 25 min")}</span></div>'
           f'<div class="big2">{L("Плочки 30×60 сива мат", "Ploščice 30×60 siva mat")}</div><span class="muted">{L("25 m² · иста серија (лот) како првата испорака", "25 m² · ista serija (lot) kot prva dobava")}</span>'
           f'<div class="g2">{field(L("Потребно до", "Potrebno do"), "<b>10.11. 10:30</b>", "gbox")}{field(L("Проценка", "Ocena cene"), "<b>42.500 RSD</b>", "gbox")}</div></div>')
    kv = lambda k, v: f'<div class="row kvr"><span class="muted">{k}</span><b>{v}</b></div>'
    det = ('<div class="card list">' + kv(L("Бара", "Zahteva"), avatar("AC" if LANG=="sl" else "АС", "#2563eb", 36) + " " + L("Ана Станковиќ", "Ana Stanković"))
           + kv(L("Причина", "Razlog"), L("Мајсторот јави дека фали", "Mojster sporoči, da manjka")) + kv(L("За задача", "Za nalogo"), L("Стан 12 · Бања", "Stan 12 · Kopalnica"))
           + kv(L("Добавувач", "Dobavitelj"), L("Керамика Центар НС", "Keramika Center NS")) + "</div>")
    flow = (sec(L("ТЕК НА БАРАЊЕТО", "POTEK ZAHTEVKA")) + '<div class="flow">' + badge(L("Креирано", "Ustvarjen"), "green") + "›" + badge(L("Одобрување", "Odobritev"), "yellow")
            + "›" + badge(L("Купено", "Kupljeno"), "gray") + "›" + badge(L("Внесено во залиха", "V zalogi"), "gray") + "</div>"
            + f'<div class="cap l">{L("Кога ќе пристигне, инженерот ја внесува вистинската количина и цена – автоматски се додава во „Докупено“.", "Ko material prispe, inženir vnese dejansko količino in ceno – samodejno se doda v »Dokupljeno«.")}</div>')
    btns = f'<div class="g2 w12">{btn(L("Одбиј", "Zavrni"), "outline")}{btn(ico("check","#fff",18) + " " + L("Одобри", "Odobri"), "green")}</div>'
    return phone(head(L("Барање MT-142", "Zahtevek MT-142"), L("Барање за материјал · Лиман 4", "Zahtevek za material · Liman 4")) + f'<div class="body">{top}{det}{flow}{btns}</div>')

def s17():
    def c(a, col, n, d, s, err):
        e = f' · <span class="red">{err}</span>' if err else ""
        return f'<div class="card row nob">{avatar(a, col, 44)}<div class="rt"><b>{n}</b><span>{d}</span><span>{s}{e}</span></div>{viber()}{callbtn()}</div>'
    body = (f'<div class="srch">{ico("search","#9ca3af",18)} {L("Барај по име или занает…", "Išči po imenu ali obrti …")}</div>'
        + '<div class="chips nowrap">' + chip(L("Сите", "Vsi"), True) + chip(L("Керамичари", "Keramičarji")) + chip(L("Струја", "Elektrika")) + chip(L("Вода", "Voda")) + chip(L("Столари", "Mizarji")) + "</div>"
        + c(L("ЈП", "JP"), "#0ea5e9", L("Јован Петровиќ", "Jovan Petrović"), L("Керамичар", "Keramičar"), L("8 задачи", "8 nalog"), L("2 отворени грешки", "2 odprti napaki"))
        + c(L("ВТ", "VT"), "#eab308", L("Волт ДОО", "Volt d.o.o."), L("Електроинсталации · шеф: Драган М.", "Elektroinštalacije · vodja: Dragan M."), L("14 задачи", "14 nalog"), L("5 грешки", "5 napak"))
        + c(L("СК", "MK"), "#16a34a", L("Столарија Ковач", "Mizarstvo Kovač"), L("Мебел по мерка · шеф: Милош К.", "Pohištvo po meri · vodja: Miloš K."), L("6 задачи · без грешки", "6 nalog · brez napak"), "")
        + c(L("МЖ", "OŽ"), "#7c3aed", L("Малтер тим Ж.", "Omet tim Ž."), L("Малтер и естрих · шеф: Живко", "Omet in estrih · vodja: Živko"), L("11 задачи", "11 nalog"), L("4 грешки", "4 napake"))
        + f'<div class="cap">{L("Изведувачите немаат профил – само контакт.<br>За секого: телефон, Viber, шеф на екипа, историја.", "Izvajalci nimajo profila – samo kontakt.<br>Za vsakega: telefon, Viber, vodja ekipe, zgodovina.")}</div>')
    return phone(head(L("Изведувачи", "Izvajalci"), L("Контакти на фирмата · 23", "Kontakti podjetja · 23"), back=False, right=plusbtn())
                 + f'<div class="body">{body}</div>' + nav(4))

def s18():
    k = lambda t, v, d: f'<div class="card kpi"><span>{t}</span><b>{v}</b><em>{d}</em></div>'
    kpis = ('<div class="g2">' + k(L("Рокот е испочитуван", "Spoštovani roki"), "71%", "▲ " + L("6% во однос на минатиот месец", "6 % glede na prejšnji mesec"))
            + k(L("Просечно решавање грешка", "Povprečno reševanje napake"), L("3,4 д", "3,4 d"), "▼ " + L("1,1 д", "1,1 d")) + "</div>")
    def pr(n, pct, mark, col, d):
        return f'<div class="pvr"><span>{n}</span><div class="rowb">{bar(pct, col, 8, mark)}<b style="color:{col}">{d}</b></div></div>'
    plan = (f'<div class="card"><div class="ct">{L("План наспроти реално по проект", "Plan proti dejanskemu po projektih")}</div>'
            + pr(L("Лиман 4", "Liman 4"), 62, 68, "#f26a1b", "−6%") + pr(L("Куќа Златибор", "Hiša Zlatibor"), 35, 33, "#16a34a", "+2%")
            + pr(L("Адаптација БГ", "Prenova BG"), 88, 87, "#16a34a", "+1%")
            + f'<div class="cap l">▍ {L("линија = планирано до денес", "črta = načrtovano do danes")}</div></div>')
    errs = [(L("Волт ДОО", "Volt d.o.o."), 5, "#ef4444"), (L("Малтер тим Ж.", "Omet tim Ž."), 4, "#f59e0b"), (L("Термо инстал", "Termo instal"), 3, "#f59e0b"),
            (L("Ј. Петровиќ", "J. Petrović"), 2, "#9ca3af"), (L("PVC Прозор", "PVC Okno"), 1, "#9ca3af")]
    eb = (f'<div class="card"><div class="ct">{L("Грешки по изведувач", "Napake po izvajalcu")}</div>'
          + "".join(f'<div class="hb"><span>{n}</span><div class="hbb"><i style="width:{v*20}%;background:{c}"></i></div><b>{v}</b></div>' for n, v, c in errs) + "</div>")
    donut = ('<svg width="58" height="58" viewBox="0 0 58 58"><circle cx="29" cy="29" r="23" fill="none" stroke="#e5e7eb" stroke-width="7"/>'
             '<circle cx="29" cy="29" r="23" fill="none" stroke="#f26a1b" stroke-width="7" stroke-dasharray="111 145" transform="rotate(-90 29 29)"/>'
             '<text x="29" y="33" text-anchor="middle" font-size="11" font-weight="700" fill="#111">77%</text></svg>')
    mat = (f'<div class="card rowb"><div class="rt"><span>{L("Материјал – потрошено / буџет", "Material – porabljeno / proračun")}</span><b>18,4 / 24,0 {L("мил.", "mio.")} RSD</b></div>{donut}</div>')
    return phone(head(L("Преглед на фирмата", "Pregled podjetja"), L("Сите проекти · последни 30 дена", "Vsi projekti · zadnjih 30 dni"), back=False)
                 + f'<div class="body">{kpis}{plan}{eb}{mat}</div>' + nav(0))

def s19():
    pick = (f'<div class="card pick"><span class="pki">📇</span><div class="rt"><b>{L("Избери од контакти", "Izberi iz kontaktov")}</b>'
            f'<span>{L("Името и бројот се пополнуваат сами", "Ime in telefon se izpolnita sama")}</span></div>{ico("chev","#f26a1b",20)}</div>')
    body = (pick
        + f'<div class="orl"><span>{L("или внеси рачно", "ali vnesi ročno")}</span></div>'
        + field(L("Име / фирма", "Ime / podjetje"), L("Јован Петровиќ", "Jovan Petrović"), extra=badge(L("од контакти", "iz kontaktov"), "green"))
        + field(L("Телефон (и Viber)", "Telefon (in Viber)"), "+381 64 222 3344", extra=badge(L("од контакти", "iz kontaktov"), "green"))
        + f'<div class="sl">{L("Занает", "Obrt")}</div><div class="chips">' + chip(L("Керамичар", "Keramičar"), True) + chip(L("Струја", "Elektrika"))
        + chip(L("Вода", "Voda")) + chip(L("Столар", "Mizar")) + chip(L("Малтер", "Omet")) + chip("+ " + L("Друго", "Drugo"), cls="dash") + "</div>"
        + field(L("Шеф на екипа (ако има)", "Vodja ekipe (če obstaja)"), f'<span class="muted">{L("– работи сам", "– dela sam")}</span>')
        + field(L("Забелешка", "Opomba"), L("Работи и викенд. Препорачан од Марко.", "Dela tudi ob vikendih. Priporočil ga je Marko."))
        + f'<div class="card info">ℹ️ {L("Апликацијата го добива само избраниот контакт – не го чита целиот именик на телефонот.", "Aplikacija dobi samo izbrani kontakt – celotnega imenika na telefonu ne bere.")}</div>'
        + btn(L("Зачувај изведувач", "Shrani izvajalca")))
    return phone(head(L("Нов изведувач", "Nov izvajalec"), L("Контакти на фирмата", "Kontakti podjetja")) + f'<div class="body">{body}</div>')

SCREENS = [("01-direktor-projekti", s01), ("02-nov-projekt", s02), ("03-pregled-projekta", s03), ("04-plan-del-naloge", s04),
           ("05-nova-naloga", s05), ("06-podrobnosti-naloge", s06), ("07-zakljucek-naloge", s07), ("08-koledar", s08),
           ("09-nov-termin", s09), ("10-prijava-napake", s10), ("11-viber-sporocilo", s11), ("12-seznam-napak", s12),
           ("13-podrobnosti-napake", s13), ("14-pregled-materiala", s14), ("15-material-vracilo", s15),
           ("16-zahtevek-material", s16), ("17-izvajalci", s17), ("18-pregled-podjetja", s18), ("19-nov-izvajalec", s19)]

def build(lang):
    global LANG
    LANG = lang
    css = open(os.path.join(os.path.dirname(__file__), "style.css"), encoding="utf-8").read()
    parts = [f'<div class="wrap" id="ekran-{n}">{f()}</div>' for n, f in SCREENS]
    return f'<!DOCTYPE html><html lang="{lang}"><head><meta charset="utf-8"><style>{css}</style></head><body>{"".join(parts)}</body></html>'

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
    os.makedirs(out, exist_ok=True)
    for lg in ("mk", "sl"):
        open(os.path.join(out, f"{lg}.html"), "w", encoding="utf-8").write(build(lg))
    print("ok")
