import unittest
import os.path
import json
from JsonReport import create_app
from report_generator import create_pdf_file
from json2xml import json2xml_file

class TestSuedeReports(unittest.TestCase):

    def setUp(self):
        self.PDF_FILENAME = 'Report.pdf'
        self.XML_FILENAME = 'Report.xml'
        self.OUT_DIR = r'./output'
        self.app = create_app().test_client()

    #test initial response
    def test_initial(self):
        rv = self.app.get('/')
        self.assertTrue(rv.status_code == 200)

    #test generation of PDF file
    def test_pdf_generation(self):
        json_data = r'{"organization":"Dunder Mifflin","reported_at":"2015-04-21","created_at":"2015-04-22","inventory":[{"name":"paper","price":"2.00"},{"name":"stapler","price":"5.00"},{"name":"printer","price":"125.00"},{"name":"ink","price":"3000.00"}]}'
        json_data = json.loads(json_data)
        create_pdf_file(json_data)

        self.assertTrue(os.path.isfile(os.path.join(self.OUT_DIR,self.PDF_FILENAME)))

    #test generation of XML file
    def test_xml_generation(self):
        json_data = r'{"organization":"Dunder Mifflin","reported_at":"2015-04-21","created_at":"2015-04-22","inventory":[{"name":"paper","price":"2.00"},{"name":"stapler","price":"5.00"},{"name":"printer","price":"125.00"},{"name":"ink","price":"3000.00"}]}'
        json_data = json.loads(json_data)
        json2xml_file(json_data)

        self.assertTrue(os.path.isfile(os.path.join(self.OUT_DIR,self.XML_FILENAME)))

    def tearDown(self):
        if os.path.isfile(os.path.join(self.OUT_DIR,self.PDF_FILENAME)):
            os.remove(os.path.join(self.OUT_DIR,self.PDF_FILENAME))
        if os.path.isfile(os.path.join(self.OUT_DIR,self.XML_FILENAME)):
            os.remove(os.path.join(self.OUT_DIR,self.XML_FILENAME))