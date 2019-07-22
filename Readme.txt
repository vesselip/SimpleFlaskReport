This folder structure contains Flask app for running and retrieving text/json strings from a database.
Output is XML file from json string and a pdf report Report.pdf and Report.xml in the output folder.
PDF file is generated from template - report_template.prep
(see https://www.reportlab.com/ for more info on their template language)

It provides some unittest coverage in test folder.

Dependency on external libs was kept to a minimum:
ReportLab's python package for PDF generation is required.