from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

pdf.set_font("Arial", style="BIU", size=26)
pdf.cell(200, 10, txt="CodeLikeUs", ln=1, align='C')

pdf.add_page()
pdf.set_font("Times", style="I", size=16)
pdf.cell(200, 10, txt="Together we learn more.", ln=2, align='L')
pdf.cell(200, 10, txt="Java | Python | NodeJs | Algorithms | Flutter | Maths", ln=3, align='L')

pdf.output("sample.pdf")