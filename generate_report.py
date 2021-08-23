from fpdf import FPDF
from datetime import date


import os

class Report:

    # Creating pdf object
    pdf = None

    def __init__(self):
        # format ('A3','A4','Letter','Legal')
        self.pdf = FPDF('P','mm','A4')

        # Adding a page to the pdf file
        self.pdf.add_page()

        # Setting up font
        self.pdf.set_font('helvetica','',16)

    def header(self):

        # Arial bold 15
        self.pdf.set_font('Arial', 'B', 15)

        # Date
        self.pdf.cell(100,10,str(date.today()))

        # Move to the right
        self.pdf.cell(50)

        # Title
        self.pdf.cell(80, 10, 'MEDICAL REPORT', 1, 0, 'C')

        # Logo
        self.pdf.image('./static/images/logo1.jpg', 160, 8, 33)


        # Line break
        self.pdf.ln(20)

    def insert_text(self,user_details):
        # Add Text
        # w = width
        # h = height

        # Adding Title
        # for key,value

        # inx  = 100
        # for key,value in user_details.items():
        #     self.pdf.cell(40,inx,key + " : " + value)
        #     inx+=20


    def generate_report(self):

        print(os.getcwd())
        self.header()
        self.insert_text({'name':"Ashwin","age":"20"})
        self.pdf.output('report.pdf')

if __name__ == '__main__':
    report = Report()
    report.generate_report()