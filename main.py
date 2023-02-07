import pandas
from fpdf import FPDF

FILENAME="topics.csv"

df=pandas.read_csv(FILENAME)

for index,row in df.iterrows():
    print(row["Topic"])


pdf=FPDF(orientation="P",unit="mm",format="A4")

pdf.add_page()

pdf.set_font(family="Times",style="B",size=12)
#width of cell,height of cell,text,border=1 or 0,ln is new line
pdf.cell(w=0,h=12,txt='Hello There',border=1,ln=1,align='L')
pdf.output("Output.pdf")
