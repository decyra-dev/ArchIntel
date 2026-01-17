from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO
import os

def generate_pdf(text, logo_path="archintel/decyra.png"):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    # Add company logo
    if os.path.exists(logo_path):
        logo = Image(logo_path, width=120, height=50)  # adjust size
        story.append(logo)
        story.append(Spacer(1, 12))

    # Add document text
    for line in text.split("\n"):
        story.append(Paragraph(line.replace("&", "&amp;"), styles["Normal"]))

    story.append(Spacer(1, 20))
    # Add footer
    story.append(Paragraph("Generated / Developed by Decyra", styles["Normal"]))

    doc.build(story)
    buffer.seek(0)
    return buffer.read()
