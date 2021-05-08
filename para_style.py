from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle,Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import registerFont
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib import colors

def get_cell_paragraph(data):
    styles_data = ParagraphStyle(
        name='Normal',
        alignment=TA_LEFT,
        fontName="times",
        fontSize=9,
    )

    styles_title = ParagraphStyle(
        name='Normal_CENTER', 
        fontName="timesbd", 
        fontSize=10, 
        alignment=1
    )

    styles_bd = ParagraphStyle(
        name='Normal', 
        fontName="timesbd", 
        fontSize=10,
    )

    pdf = SimpleDocTemplate("simple_table_grid.pdf", pagesize=letter)
    pdfmetrics.registerFont(TTFont('times', 'fonts/times.ttf'))
    pdfmetrics.registerFont(TTFont('timesbd', 'fonts/timesbd.ttf'))

    para_data=[]
    title_bd = [0, 1]
    just_bd = [2, 5, 6]

    for i in range(len(data)):
        para_data.append([])
        for j in range(len(data[i])):
            if(i in title_bd):
                para_data[i].append(Paragraph(data[i][j], styles_title))
            elif(i in just_bd):
                para_data[i].append(Paragraph(data[i][j], styles_bd))
            else:
                para_data[i].append(Paragraph(data[i][j], styles_data))

    return para_data


