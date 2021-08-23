from fpdf import FPDF
from datetime import date

class Report:

    # Creating pdf object
    pdf = None

    # inx declaration
    inx = 60

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

        # Move to the right
        self.pdf.cell(46)

        # Title
        self.pdf.cell(90, 20, 'MEDICAL REPORT', 1, 0, 'C')

        # Logo
        self.pdf.image('./static/images/logo1.jpg', 170, 4, 33)

        self.pdf.line(0, 40,220,40)

        # Line break
        self.pdf.ln(20)

    def insert_text(self,user_details):
        # Add Text
        # w = width
        # h = height

        # Adding Title
        # for key,value

        inx  = self.inx
        for key,value in user_details.items():
            self.pdf.cell(0,inx,key + " : " + value)
            self.pdf.ln(2)
            inx+=20

        self.pdf.ln(1)
        inx+=10
        self.inx = inx


    def generate_report(self):

        # print(os.getcwd())
        self.header()

        # Setting up Personal Details header
        self.pdf.cell(0,40,"PERSONAL DETAILS")
        self.pdf.ln(2)


        self.insert_text(
            {
                'Name':"Ashwin",
                "Age":"20",
                "Height":"170",
                "Weight":"60",
                "Gender":"Male",
                
                }
                )

        self.pdf.cell(0,self.inx,"ANALYSIS")
        self.pdf.line(0,120,220,120)
        self.pdf.ln(16)
        
        self.insert_text(
            {
                "Reason for Diagnosis":"Fever",
                "Disease for Analysis":" Glaucoma",
                "Analysis":"Tested Positive for Glaucoma"

            }
            )

        # Logo
        self.pdf.image('./static/images/test_img.jpeg', 110, 50, 90)

        self.pdf.line(0,200,220,200)
        self.pdf.ln(16)

        self.pdf.output('./reports/report.pdf')

if __name__ == '__main__':
    report = Report()
    report.generate_report()