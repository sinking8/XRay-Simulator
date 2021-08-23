from fpdf import FPDF
from model import *

import os

class Report:

    # Creating pdf object
    pdf = None

    # Model DIR
    model_dir = "./static/model/model.h5"

    # inx declaration
    inx = 60

    def __init__(self):
        # format ('A3','A4','Letter','Legal')
        self.pdf = FPDF('P','mm','A4')

        # Adding a page to the pdf file
        self.pdf.add_page()

        # Setting up font
        self.pdf.set_font('helvetica','',16)

        # Creating Model
        self.model  = Model(self.model_dir)

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


    def generate_report(self,user_details):

        # print(os.getcwd())
        self.header()

        # Setting up Personal Details header
        self.pdf.cell(0,40,"PERSONAL DETAILS")
        self.pdf.ln(2)


        self.insert_text(
            {
                'Name':user_details["Name"],
                "Age":user_details["Age"],
                "Height":user_details["Height"],
                "Weight":user_details["Weight"],
                "Gender":user_details["Gender"],
                
                }
                )

        self.pdf.cell(0,self.inx,"ANALYSIS")
        self.pdf.line(0,120,220,120)
        self.pdf.ln(16)
        
        preds = self.model.predict_image(os.path.join("./static/images",user_details['Image']))
        print(preds)

        self.insert_text(
            {
                "Reason for Diagnosis":user_details["Diagnosis"],
                "Disease for Analysis":user_details["Analysis"],
                "Analysis":"Tested Positive for Glaucoma"

            }
            )

        # Xray Image
        print(user_details['Image'])
        self.pdf.image(os.path.join('./static/images',user_details['Image']), 110, 50, 90)

        self.pdf.line(0,200,220,200)
        self.pdf.ln(16)

        self.pdf.output('./reports/report.pdf')

    def refresh(self):
        # format ('A3','A4','Letter','Legal')
        self.pdf = FPDF('P','mm','A4')

        # Adding a page to the pdf file
        self.pdf.add_page()

        # Setting up font
        self.pdf.set_font('helvetica','',16)



# if __name__ == '__main__':
#     report = Report()
#     report.generate_report()