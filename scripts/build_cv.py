"""Rebuild the website CV from the author profile and supplied academic CV.

Dependencies: reportlab, PyYAML. Run from any working directory.
The user-supplied source PDF is never modified.
"""
from pathlib import Path
from html import escape
import re
import yaml
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_RIGHT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'static/uploads/resume.pdf'
author = yaml.safe_load((ROOT / 'content/authors/admin/_index.md').read_text(encoding='utf-8').split('---', 2)[1])
INK = colors.HexColor('#142F3E')
BLUE = colors.HexColor('#22627C')
MUTED = colors.HexColor('#50636E')
BODY = ParagraphStyle('body', fontName='Helvetica', fontSize=10, leading=14, textColor=INK, spaceAfter=7)
SMALL = ParagraphStyle('small', parent=BODY, fontSize=9, leading=12.5, textColor=MUTED, spaceAfter=5)
TITLE = ParagraphStyle('name', parent=BODY, fontName='Helvetica-Bold', fontSize=29, leading=34, spaceAfter=7)
HEADING = ParagraphStyle('heading', parent=BODY, fontName='Helvetica-Bold', fontSize=13, leading=17, textColor=BLUE, spaceBefore=17, spaceAfter=9)
SUB = ParagraphStyle('sub', parent=BODY, fontName='Helvetica-Bold', fontSize=10, leading=14, spaceBefore=8, spaceAfter=5)
RIGHT = ParagraphStyle('right', parent=SMALL, alignment=TA_RIGHT)
story = []

def clean(text):
    return escape(str(text).replace('–', '-').replace('—', '-').replace('’', "'"))

def para(text, style=BODY):
    return Paragraph(clean(text), style)

def heading(text):
    story.append(para(text, HEADING))

def entry(title, institution, period, details=()):
    available = A4[0] - 2 * 52 - 12
    table = Table([[para(title, SUB), para(period, RIGHT)]], colWidths=[available - 146, 146])
    table.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP'), ('LEFTPADDING',(0,0),(-1,-1),0), ('RIGHTPADDING',(0,0),(-1,-1),0), ('TOPPADDING',(0,0),(-1,-1),0), ('BOTTOMPADDING',(0,0),(-1,-1),0)]))
    elements = [table, para(institution)] + [para(detail, SMALL) for detail in details]
    story.append(KeepTogether(elements))
    story.append(Spacer(1, 5))

def date_year(value):
    return str(value)[:4]

def month_year(value):
    from datetime import date
    if not value:
        return 'Present'
    if not isinstance(value, date):
        value = date.fromisoformat(str(value))
    return value.strftime('%b %Y')

story += [para(author['title'], TITLE), para('Multisensory integration and immersive virtual reality', SUB), para(f"{author['location']}  |  {author['email']}  |  ORCID: 0009-0008-8104-8802", SMALL)]
heading('Education')
for item in author['education']:
    period = f"{date_year(item['date_start'])} - {date_year(item['date_end']) if item['date_end'] else 'Present'}"
    details = []
    if item.get('supervisor'):
        details.append('Supervisor: ' + item['supervisor'])
    if item.get('summary'):
        details += [part.strip() for part in item['summary'].strip().split('\n\n')]
    entry(item['degree'], item['institution'], period, details)

heading('Publications')
story.append(para('Published and in press', SUB))
for text in [
    'Xu, A., De Bruyne, J., Gherri, E., Marichal, T., & Talsma, D. (in press). Toward a comprehensive view of peripersonal space: From upper-limb foundations to lower-limb frontiers. Psychonomic Bulletin & Review.',
    'Gherri, E., Xu, A., Ambron, E., & Sedda, A. (2022). Peripersonal space around the upper and the lower limbs. Experimental Brain Research, 240(7-8), 2039-2050. DOI: 10.1007/s00221-022-06387-7.',
]: story.append(para(text))
story.append(para('In revision', SUB))
story.append(para('Xu, A., Gherri, E., De Bruyne, J., & Talsma, D. Effector-specific organisation of peripersonal space for the foot and hand: A virtual reality experiment.'))
story.append(para('In preparation', SUB))
for text in [
    'Xu, A., De Bruyne, J., & Talsma, D. Peripersonal space, interpersonal space, and reachability: Are they different, or is it just a matter of scale?',
    'Xu, A., et al. Tool-use-related plasticity of peripersonal space around the hand in immersive virtual reality.',
    'Foot motor preparation: An ERP-based investigation. Author order to be determined.',
]: story.append(para(text))

story.append(PageBreak())
story.append(para(author['title'], TITLE))
story.append(para('Academic CV / Experience and skills', SMALL))
heading('Professional experience')
for item in author['work']:
    if item['position'] == 'PhD Fellow':
        continue
    period = item.get('period') or f"{month_year(item['date_start'])} - {month_year(item.get('date_end'))}"
    summary = item.get('summary', '').strip()
    details = [re.sub(r'^-\s*', '', line.strip()) for line in summary.splitlines() if line.strip()]
    entry(item['position'], item['company_name'], period, details)
heading('Teaching experience')
for item in author['teaching']:
    entry(item['position'], item['institution'], item['period'], ['Course: ' + item['course']])
heading('Methods and technical skills')
story.append(para('Methods: immersive VR, behavioral experiments, EEG/ERP.'))
story.append(para('Programming and tools: ' + ', '.join(item['name'] for item in author['skills'][0]['items']) + '.'))
story.append(para('Languages: ' + ', '.join(item['name'] for item in author['languages']) + '.'))
heading('Awards and funding')
for item in author['awards']:
    story.append(para(item['title'] + ' - ' + item['awarder']))
    story.append(para(item['summary'], SMALL))
heading('Outside research')
story.append(para(author['skills'][1]['summary']))
if author.get('cats'):
    story.append(para('I also share my home with two Oriental Shorthair cats.'))
heading('References')
for title, text in [
    ('Prof. Durk Talsma - PhD Supervisor', 'Associate Professor, Department of General and Applied Psychology, Ghent University. durk.talsma@ugent.be'),
    ('Prof. Elena Gherri - MSc Supervisor', 'Associate Professor, Department of Philosophy, University of Bologna. elena.gherri@unibo.it'),
]:
    story.append(KeepTogether([para(title, SUB), para(text, SMALL)]))

def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(MUTED)
    canvas.drawString(52, 28, 'Aolong Xu | Academic CV | Updated November 2026')
    canvas.drawRightString(A4[0]-52, 28, str(doc.page))
    canvas.restoreState()

document = SimpleDocTemplate(str(OUTPUT), pagesize=A4, leftMargin=52, rightMargin=52, topMargin=42, bottomMargin=48, title='Aolong Xu - Academic CV', author=author['title'], allowSplitting=True)
document.build(story, onFirstPage=footer, onLaterPages=footer)
print('Updated website CV:', OUTPUT)
