from fpdf import FPDF
import pandas as pd


pdf= FPDF(orientation= "P", unit = "mm", format= "a4")

df= pd.read_csv("topics (1).csv")

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family= "Times", style= "B", size= 24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w= 0, h=12, txt= row["Topic"], align="l", ln=1)
    pdf.line(x1=10,y1= 21, x2=200, y2=21)


    for i in range(row["Pages"]-1):
        pdf.add_page()


pdf.output("output.pdf")