from fpdf import FPDF

pdf = FPDF()

pdf.add_page()

pdf.set_font("Arial")

pdf.outpu("Orçamento.pdf")