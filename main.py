import pandas
from fpdf import FPDF

FILENAME="topics.csv"

df=pandas.read_csv(FILENAME)
#ctreate pdf object with properties
pdf=FPDF(orientation="P",unit="mm",format="A4")
pdf.set_font(family="Times",style="B",size=20)


for index,row in df.iterrows():
    pdf.add_page()
    page=1
    # width of cell,height of cell,text,border=1 or 0,ln is new line
    pdf.cell(w=0, h=12, txt=row["Topic"], border=0, ln=1, align='L')
    pdf.cell(w=0, h=0, txt='', border=1, ln=1, align='L')
    #pdf.footer(row["Topic"])
    while page < int(row["Pages"]):
        pdf.add_page()
        page=page+1


#Output PDF
pdf.output("Output.pdf")
