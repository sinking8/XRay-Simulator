from fpdf import FPDF

# format ('A3','A4','Letter','Legal')
pdf = FPDF('P','mm','A4')

# Adding a page to the pdf file
pdf.add_page()

# Setting up font
pdf.set_font('helvetica','',16)

# Add Text
# w = width
# h = height
pdf.cell(40,10,'Hello World')


pdf.output('report.pdf')
