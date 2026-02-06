from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def create_report():
    doc = SimpleDocTemplate("report1.pdf", pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    # Title
    title_style = styles['Title']
    story.append(Paragraph("Herbarium Website Project Report", title_style))
    story.append(Spacer(1, 12))

    # Introduction
    body_style = styles['BodyText']
    story.append(Paragraph("<b>1. Project Overview</b>", styles['Heading2']))
    story.append(Paragraph(
        "The Herbarium Website project aims to provide a digital catalogue for plant specimens. "
        "It features a 'cute green' aesthetic as requested, with a dual interface: one for students "
        "(search only) and one for teachers (administration).", body_style))
    story.append(Spacer(1, 12))

    # Features Implemented
    story.append(Paragraph("<b>2. Current Features Implemented</b>", styles['Heading2']))
    features = [
        "<b>Frontend (Student Side):</b> Responsive design (Mobile 1-col, Tablet 2-col, Desktop 3-col). "
        "Flexible search by Family, Genus, Species, Barcode, etc.",
        "<b>Backend (Teacher Side):</b> Secure Django Admin interface for inserting, editing, and deleting species.",
        "<b>Database:</b> SQLite database configured with a 'Species' model including images.",
        "<b>Testing:</b> Unit tests implemented for Models, Views, and API, ensuring 100% pass rate."
    ]
    for feat in features:
        story.append(Paragraph(f"- {feat}", body_style))
        story.append(Spacer(1, 6))

    # Global Access Issue
    story.append(Paragraph("<b>3. Global Accessibility (Any Device, Any Network)</b>", styles['Heading2']))
    story.append(Paragraph(
        "Currently, the website runs on your <b>Local Host</b>. I have enabled <b>LAN Access</b>, "
        "meaning devices connected to your same Wi-Fi can access it via <code>http://192.168.29.174:8000</code>.", body_style))
    
    story.append(Spacer(1, 12))
    story.append(Paragraph("<b>How to make it accessible from ANY network (Internet):</b>", styles['Heading3']))
    story.append(Paragraph(
        "To allow access from outside your home Wi-Fi (e.g., mobile data, friend's house), "
        "the site must be 'Hosted' or 'Tunneled'. Two options:", body_style))
    
    story.append(Spacer(1, 6))
    story.append(Paragraph("<b>Option A: Ngrok (Fastest, Temporary)</b>", styles['Heading4']))
    story.append(Paragraph(
        "1. Download Ngrok from ngrok.com.<br/>"
        "2. Run command: <code>ngrok http 8000</code>.<br/>"
        "3. It will give you a public URL (e.g., <code>https://random-name.ngrok-free.app</code>).<br/>"
        "4. Share this URL with anyone in the world.", body_style))

    story.append(Spacer(1, 6))
    story.append(Paragraph("<b>Option B: Cloud Hosting (Permanent)</b>", styles['Heading4']))
    story.append(Paragraph(
        "Deploy the code to a free provider like <b>PythonAnywhere</b>, <b>Render</b>, or <b>Railway</b>. "
        "This makes the site always online without needing your laptop to be on.", body_style))

    # Conclusion
    story.append(Spacer(1, 12))
    story.append(Paragraph("<b>4. Conclusion</b>", styles['Heading2']))
    story.append(Paragraph(
        "The application is fully functional locally. The UI is mobile-responsive and meets the aesthetic requirements. "
        "For global access, deploying to a cloud server is the recommended next step.", body_style))

    doc.build(story)
    print("PDF Report generated successfully: report1.pdf")

if __name__ == "__main__":
    create_report()
