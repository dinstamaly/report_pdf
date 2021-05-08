from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle,Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import registerFont
from reportlab.pdfbase.ttfonts import TTFont
from para_style import get_cell_paragraph

name = 12345678

pdf = SimpleDocTemplate("simple_table_grid.pdf", pagesize=letter)
pdfmetrics.registerFont(TTFont('times', 'fonts/times.ttf'))
pdfmetrics.registerFont(TTFont('timesbd', 'fonts/timesbd.ttf'))
styles_heading = ParagraphStyle(name='Title', fontName="timesbd", fontSize=11, alignment=1)
styles_data = ParagraphStyle('small', fontName="times", fontSize=9, alignment=1)
elements = []
data = [
    ['№', 'Дата', 'Документ', 'Операции', '№', 'Сумма', ''],
    ['','','','','','Дебет ', 'Кредит'],
    ['', 'Сальдо на ', '', '', '', '', ''],
    ['1', 'каждый день месяца', 'Прием платежей ', 'Прием платежей за ', '№ ', '', ''],
    ['2', 'каждый день месяца', 'Платеж. поручение № ', 'Перечисленно ', '№ ', '', ''],
    ['','Обороты за период ','','','','',''],
    ['','Сальдо на конец ','','','','',''],
    ['','Гл.бухгалтер Оператора Системы','','','','Гл.бухгалтер ОАО “Бакай Банк"',''],
]

table =Table(
    get_cell_paragraph(data),
    colWidths=(0.6*inch, 1.5*inch, inch, inch, 0.5*inch, inch, inch ), 
    rowHeights=[None, None, 0.8*inch, inch, inch, 0.3*inch, 0.4*inch, None],
)
style_data = TableStyle([
    ('GRID', (0, 0), (-1, 6), 0.5, colors.black),

    ('SPAN',(1,2),(4,2)),
    ('SPAN',(5,9),(6,9)),

    ('SPAN',(0,0),(0,1)),
    ('SPAN',(1,0),(1,1)),
    ('SPAN',(2,0),(2,1)),
    ('SPAN',(3,0),(3,1)),
    ('SPAN',(4,0),(4,1)),
    ('SPAN',(5,0),(6,0)),
    ('SPAN',(1,6),(4,6)),
    ('SPAN',(1,5),(4,5)),
    ('SPAN',(-2,7),(-1,7)),
    ('SPAN',(1,7),(2,7)),

    ('BACKGROUND', (0,2), (6,2), colors.powderblue),
    ('BACKGROUND', (0,5), (6,5), colors.powderblue),
    ('BACKGROUND', (0,6), (6,6), colors.powderblue),
]
)

data1 = [
    ['"Наименование оператора"  ','',''],
    ['в лице главного бухгалтера  ','',''],
    ['и ОАО "Бакай Банк"  ','',''],
    ['в лице главного бухгалтера  ','',''],
    [''],
    ['сделали выверку расчетов за  ', '', ''],
    []

]
data1[0][1] += 'asdfghjkl;oiuytrewq'
table1 = Table(data1, colWidths=[1.87*inch, 2.3*inch], hAlign='LEFT')
style_data1 = TableStyle( 
    [
        ('FONTNAME', (0, 0), (-1, -1), 'times'),
        ('FONTNAME', (0, 2), (0, 2), 'timesbd'),
        ('FONTNAME', (0, 0), (0,0), 'timesbd'),
        ('LINEBELOW', (1,0), (2,1), 0.25, colors.black),
        ('LINEBELOW', (0,2), (2,2), 0.25, colors.black),
        ('LINEBELOW', (1,3), (-1,3), 0.25, colors.black),
        ('LINEBELOW', (1,5), (-1,-2), 0.25, colors.black),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
    ]
)

elements.append(Paragraph("Акт сверки",styles_heading))
elements.append(Paragraph(f"за период с {name} по {name}",styles_heading))


table.setStyle(style_data)
table1.setStyle(style_data1)
elements.append(table1)
elements.append(table)
pdf.build(elements)