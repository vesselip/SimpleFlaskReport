import os
from io import BytesIO
import preppy
from rlextra.rml2pdf import rml2pdf

REPORT_FILENAME = 'Report.pdf'
OUT_DIR = r'./output'
RML_DIR = r'./templates'

class Products(object):
    "Empty class to hold product attributes"
    pass

class Heading(object):
    "Empty class to hold heading attributes"
    pass

#here we extract data from json dictionary and build the header of the report and the inventory 
def build_report(json_object):

    heading_details = []
    items = []

    heading = Heading()
    heading.organisation  = json_object.get('organization','N/A')
    heading.report_date = json_object.get('reported_at','N/A')
    heading.timestamp = json_object.get('created_at','N/A')
    heading_details.append(heading)

    inventory = json_object.get('inventory',None)

    if inventory:
        for item in inventory:
            products = Products()
            products.name = item['name']
            products.price = item['price']
            items.append(products)

    return heading_details, items

#Creates PDF as a binary stream in memory, and returns it
def build_pdf(heading, inventory, template):

    #RML_DIR = 'rml'
    templateName = os.path.join(RML_DIR, template)
    template = preppy.getModule(templateName)
    namespace = {
        'heading':heading,
        'products':inventory,
        'RML_DIR': RML_DIR
        }

    rml = template.getOutput(namespace)
    open(os.path.join(RML_DIR,'latest.rml'), 'w').write(rml)
    buf = BytesIO()
    rml2pdf.go(rml, outputFileName=buf)
    return buf.getvalue()

def create_pdf_file(json_object):
    heading, items = build_report(json_object)

    try:
        pdf = build_pdf(heading, items, 'report_template.prep')

        open(os.path.join(OUT_DIR,REPORT_FILENAME),'wb').write(pdf)
    except Exception as e:
        print('\nReport generate failed! Error: %s' % e)
