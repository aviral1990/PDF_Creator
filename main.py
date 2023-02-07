import pandas
from fpdf import FPDF

FILENAME="topics.csv"

df=pandas.read_csv(FILENAME)
#ctreate pdf object with properties
pdf=FPDF(orientation="P",unit="mm",format="A4")
pdf.set_auto_page_break(auto=False,margin=0)    #No auto break when writing to pdf
pdf.set_font(family="Times",style="B",size=20)


for index,row in df.iterrows():
    pdf.add_page()
    page=1
    # width of cell,height of cell,text,border=1 or 0,ln is new line
    pdf.set_font(family="Times", style="B", size=20)
    pdf.set_text_color(0,0,0)
    pdf.cell(w=0, h=12, txt=row["Topic"], border=0, ln=1, align='L')
    pdf.cell(w=0, h=0, txt='', border=1, ln=1, align='L')

    #Add Footer
    pdf.ln(264)
    pdf.set_font(family="Times", size=8)
    pdf.set_text_color(110, 110, 110)
    pdf.cell(w=0, h=1, txt=row["Topic"], border=0, align='R')

    while page < int(row["Pages"]):
        pdf.add_page()
        # Add Footer
        pdf.ln(277)     #new Line
        pdf.set_font(family="Times", size=8)
        pdf.set_text_color(110, 110, 110)
        pdf.cell(w=0, h=1, txt=row["Topic"], border=0, align='R')
        page=page+1


#Output PDF
pdf.output("Output.pdf")
