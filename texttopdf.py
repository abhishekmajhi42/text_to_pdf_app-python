#import FPDF from fpdf module
from fpdf import FPDF

# save FPDF() class into a
# variable pdf
pdf=FPDF()

#Add a page
pdf.add_page()

# set style and size of font
# that you want in the pdf
pdf.set_font("Arial",size=15)

#open the pdf file in text mode
f=open("myfile.txt","r")

#insert the texts in pdf
for x in f:
    pdf.cell(200,10,txt=x,ln=1,align="C")

#save the pdf with the name .pdf
pdf.output("mypdf.pdf")
