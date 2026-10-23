"""Render original illustrative profile artwork with Pillow.

Requires Segoe UI and Consolas; set PROFILE_FONT_DIR on other systems.
Graphics are illustrations, not screenshots or operational dashboards.
"""
from pathlib import Path
import os
from PIL import Image, ImageDraw, ImageFont
OUT = Path(__file__).resolve().parents[1] / 'assets'
OUT.mkdir(exist_ok=True)
FONTS = Path(os.environ.get('PROFILE_FONT_DIR', 'C:/Windows/Fonts'))
BG, WHITE, MUTED, LINE = '#101D2B', '#F3F0E7', '#A9BAC9', '#2B4155'
MINT, BLUE, GOLD = '#78DFC1', '#87BCF6', '#EDC37E'

def font(size, bold=False, mono=False):
    name = 'consola.ttf' if mono else 'segoeuib.ttf' if bold else 'segoeui.ttf'
    return ImageFont.truetype(str(FONTS / name), size)

def canvas(w, h):
    im = Image.new('RGB', (w,h), BG)
    d = ImageDraw.Draw(im)
    for x in range(w//2,w,40):
        for y in range(25,h,40):
            d.ellipse((x,y,x+2,y+2), fill='#293C4D')
    return im,d

def box(d, xy, text, accent):
    d.rounded_rectangle(xy,14,fill='#172A3A',outline=LINE,width=2)
    x,y,r,b=xy
    d.ellipse((x+20,y+26,x+30,y+36),fill=accent)
    d.text((x+48,y+17),text,font=font(24,mono=True),fill=WHITE)

im,d=canvas(1600,450)
d.rounded_rectangle((1,1,1598,448),22,outline=LINE,width=2)
d.line((64,65,115,65),fill=MINT,width=5)
d.text((133,45),'DREW109 / ENGINEERING PORTFOLIO',font=font(23,mono=True),fill=MUTED)
d.text((60,111),'Drew Webster',font=font(100,bold=True),fill=WHITE)
d.text((66,244),'Cybersecurity. Cloud. Software.',font=font(38),fill=MINT)
d.text((66,363),'BUILD WITH CURIOSITY. VERIFY WITH EVIDENCE.',font=font(22,mono=True),fill=MUTED)
d.line([(1020,110),(1100,110),(1100,213),(1190,213)],fill=MINT,width=3)
d.line([(1020,340),(1100,340),(1100,246),(1190,246)],fill=BLUE,width=3)
d.line([(1360,243),(1455,243),(1455,344)],fill=GOLD,width=3)
box(d,(1160,77,1490,143),'IDENTITY',MINT)
box(d,(1190,196,1520,262),'SIGNALS',BLUE)
box(d,(1130,315,1460,381),'SYSTEMS',GOLD)
d.ellipse((1090,219,1110,239),fill=WHITE)
d.ellipse((1008,99,1030,121),fill=BG,outline=MINT,width=3)
d.ellipse((1008,329,1030,351),fill=BG,outline=BLUE,width=3)
im.save(OUT/'header.png',optimize=True)

im,d=canvas(800,360)
d.rounded_rectangle((1,1,798,358),20,outline=LINE,width=2)
d.line((40,43,80,43),fill=MINT,width=4)
d.text((98,27),'DREW109',font=font(22,mono=True),fill=MUTED)
d.text((34,87),'Drew Webster',font=font(74,bold=True),fill=WHITE)
d.text((40,193),'Cybersecurity. Cloud. Software.',font=font(34),fill=MINT)
d.text((40,280),'BUILD. TEST. DOCUMENT.',font=font(24,mono=True),fill=MUTED)
im.save(OUT/'header-mobile.png',optimize=True)

cards=[('cloud','01 / CLOUD SECURITY','Identity & access',MINT),
       ('detection','02 / DEFENSIVE SECURITY','Detection & triage',BLUE),
       ('appsec','03 / APPLICATION SECURITY','Test. Explain. Fix.',GOLD),
       ('portfolio','04 / SOFTWARE & AUTOMATION','More of my work','#B9ACF0')]
for key,label,title,accent in cards:
    im,d=canvas(800,235)
    d.rectangle((0,0,7,234),fill=accent)
    d.text((35,30),label,font=font(22,mono=True),fill=accent)
    d.text((32,88),title,font=font(43,bold=True),fill=WHITE)
    d.line((36,188,290,188),fill=LINE,width=2)
    if key=='cloud':
        for x,y in [(610,78),(700,120),(610,168)]:
            d.line((x,y,655,122),fill=accent,width=3)
            d.rounded_rectangle((x-18,y-18,x+18,y+18),7,fill=BG,outline=accent,width=2)
        d.rounded_rectangle((638,105,672,139),7,fill=accent)
    elif key=='detection':
        d.line([(568,157),(592,157),(611,103),(638,177),(668,76),(691,137),(738,137)],fill=accent,width=4)
        d.line((560,188,750,188),fill=LINE,width=2)
    elif key=='appsec':
        d.line([(611,80),(573,126),(611,172)],fill=accent,width=4)
        d.line([(698,80),(736,126),(698,172)],fill=accent,width=4)
        d.line([(640,130),(652,145),(681,108)],fill=accent,width=5)
    else:
        for x,y in [(570,85),(630,112),(690,139)]:
            d.rounded_rectangle((x,y,x+61,y+50),7,fill=BG,outline=accent,width=2)
    im.save(OUT/(key+'.png'),optimize=True)
for p in sorted(OUT.glob('*.png')):
    print(f'{p.name}: {p.stat().st_size:,} bytes')
