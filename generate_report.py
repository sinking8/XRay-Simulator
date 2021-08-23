from fpdf import FPDF

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



    def insert_text(self,user_details):
        # Add Text
        # w = width
        # h = height
        self.pdf.cell(40,10,user_details['name'])


    def generate_report(self):
        self.insert_text({'name':"Ashwin"})
        self.pdf.output('report.pdf')

if __name__ == '__main__':
    report = Report()
    report.generate_report()