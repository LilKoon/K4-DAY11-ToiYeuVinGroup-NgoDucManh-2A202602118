"""Render static rectangle evidence from QA SVG; never execute the HTML."""
from pathlib import Path
import re
import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw, ImageFont

base = Path(__file__).resolve().parents[2]
source = base / 'submission/r2_qa/qa_overlay.html'
out = base / 'submission/screenshots'
out.mkdir(exist_ok=True)
font = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 20)
small = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 17)
targets = {'adasind_014670.jpg': ('L6',), 'adasind_032280.jpg': ('L6','L7'), 'adasind_034080.jpg': ('L1','L7')}
notes = {
    'adasind_014670.jpg': 'QA: kiểm tra Bus L6 bị cắt ở mép trái; đối chiếu truncated theo R05.',
    'adasind_032280.jpg': 'QA: kiểm tra Car L6 bị Pedestrian L7 che; đối chiếu box/occluded theo R02/R05.',
    'adasind_034080.jpg': 'QA: kiểm tra Car L1 mép trái và Pedestrian L7 mép phải theo R05.'
}
for name, block in re.findall(r'<h2>([^<]+)</h2>\s*(<svg.*?</svg>)', source.read_text(encoding='utf-8'), re.S):
    root = ET.fromstring(block)
    image = Image.open(base/'assets/images'/name).convert('RGB')
    draw = ImageDraw.Draw(image)
    rects, labels = root.findall('rect'), root.findall('text')
    assert len(rects) == len(labels)
    for rect,label in zip(rects,labels):
        a=rect.attrib; x,y,w,h=(float(a[k]) for k in ('x','y','width','height'))
        text=label.text or ''
        focus=text.split()[0] in targets[name]
        color='#ffd400' if focus else '#00e5ff'
        draw.rectangle((x,y,x+w,y+h),outline=color,width=5 if focus else 3)
        tw=draw.textbbox((0,0),text,font=font)[2]
        tx=max(0,min(x,image.width-tw-8)); ty=max(0,y-26)
        draw.rectangle((tx,ty,tx+tw+8,ty+25),fill='#101820')
        draw.text((tx+4,ty+1),text,font=font,fill=color)
    # Keep full horizontal image boundaries, crop only empty sky and foreground.
    detail=image.crop((0,760,1080,1390))
    canvas=Image.new('RGB',(1080,760),'#ffffff')
    d=ImageDraw.Draw(canvas)
    d.text((16,12),'QA B1-mid | '+name,font=font,fill='#10243a')
    d.text((16,44),notes[name],font=small,fill='#10243a')
    d.text((16,72),'Vàng: đối tượng cần soát. Nhận xét QA chưa phải kết luận lỗi đã xác nhận.',font=small,fill='#10243a')
    canvas.paste(detail,(0,102))
    d.text((16,738),'Dựng tĩnh từ qa_overlay.html; crop y=760..1390; không phải screenshot CVAT.',font=small,fill='#334155')
    path=out/('qa_B1-mid_'+name.replace('.jpg','.png'))
    canvas.save(path)
    print(path)
