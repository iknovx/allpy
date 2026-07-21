from fpdf import FPDF

imagelist = ["basics_py/projects/images/_ (8).jpeg", "basics_py/projects/images/narcissist banner.jpeg"]
pdf = FPDF()
for image in imagelist:
    pdf.add_page()
    pdf.image(image, x=10, y=10, w=100)
pdf.output("output.pdf", "F")