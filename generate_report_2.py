from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def create_report():
    doc = SimpleDocTemplate("report2.pdf", pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    # Title
    title_style = styles['Title']
    story.append(Paragraph("Herbarium Website Project Report 2", title_style))
    story.append(Paragraph("Detailed Overview of Updates & Technologies", styles['Heading2']))
    story.append(Spacer(1, 12))

    body_style = styles['BodyText']

    # 1. Recent Updates
    story.append(Paragraph("<b>1. Summary of Recent Updates</b>", styles['Heading2']))
    story.append(Paragraph("We have significantly enhanced the user experience and accessibility of the Herbarium website. Key updates include:", body_style))
    story.append(Spacer(1, 6))

    updates = [
        "<b>Global Accessibility:</b> Successfully configured <b>Ngrok</b> tunneling, allowing the website to be accessed from any device on any network (Mobile Data, External Wi-Fi) via a secure public link.",
        "<b>Mobile Responsiveness:</b> Implemented strict responsive layout rules: 1 column for Mobile, 2 columns for Tablets, and 3 columns for Desktop/Laptops.",
        "<b>Search Interface Upgrade:</b> Replaced standard text inputs with <b>Searchable Dropdowns (Datalists)</b> for Family, Genus, Species, and Barcode. This allows users to either type to search or select from an alphabetically sorted list.",
        "<b>Simplified Filters:</b> Removed complex checkboxes (Types Only, Images Only, Cultivated/Non-Cultivated) to streamline the student user interface.",
        "<b>Data Sorting:</b> All dropdown lists (Family, Genus, Species) are now automatically sorted alphabetically (A-Z) for easier navigation."
    ]
    
    list_items = [ListItem(Paragraph(u, body_style)) for u in updates]
    story.append(ListFlowable(list_items, bulletType='bullet', start='circle'))
    story.append(Spacer(1, 12))

    # 2. Technologies & Languages Used
    story.append(Paragraph("<b>2. Technologies & Languages Breakdown</b>", styles['Heading2']))
    story.append(Paragraph("The project is built using a robust stack of modern technologies:", body_style))
    story.append(Spacer(1, 6))

    tech_stack = [
        "<b>Python (Backend Logic):</b> The core programming language used for server-side logic, database interactions, and automation scripts.",
        "<b>Django (Web Framework):</b> A high-level Python web framework that handles routing, database models (ORM), the admin interface, and the view logic.",
        "<b>SQLite (Database):</b> The relational database management system used to store all species data efficiently.",
        "<b>HTML5 (Structure):</b> Defines the structure of the web pages, including the new Datalist elements for searchable dropdowns.",
        "<b>CSS3 (Styling):</b> Custom stylesheets (no external frameworks) used to create the 'Cute Green' aesthetic, card layouts, and responsive media queries.",
        "<b>JavaScript (Interactivity):</b> Vanilla JS used for handling the search form submission via AJAX (Fetch API) and dynamically updating the results page without reloading.",
        "<b>Pillow (Image Processing):</b> A Python library used by Django to handle image uploads and resizing.",
        "<b>ReportLab (Reporting):</b> Python library used to generate these PDF status reports programmatically.",
        "<b>Ngrok (Networking):</b> A tunneling tool used to expose the local development server to the public internet securely."
    ]

    list_items_tech = [ListItem(Paragraph(t, body_style)) for t in tech_stack]
    story.append(ListFlowable(list_items_tech, bulletType='bullet', start='square'))
    story.append(Spacer(1, 12))

    # 3. Project Status
    story.append(Paragraph("<b>3. Current Project Status</b>", styles['Heading2']))
    story.append(Paragraph(
        "The application is <b>Fully Functional</b> and <b>Deployed (Temporarily via Ngrok)</b>. "
        "Students can search using advanced autocomplete fields, and teachers can manage the database via the secure Admin panel. "
        "Unit tests are passing (6/6), ensuring stability.", body_style))

    doc.build(story)
    print("PDF Report generated successfully: report2.pdf")

if __name__ == "__main__":
    create_report()
