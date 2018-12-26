from pydoc import ispath
from xml.etree import ElementTree as eT

while 1:
    path = "/home/emipro/workspace/odoo12/odoo/addons/account/views/account.xml"  # input("Enter path for XML file :-")
    if ispath(path):
        file = eT.parse(path)
        odoo = file.getroot()
        for template in odoo:
            for xpath in template:
                if xpath.attrib['expr'] == '.':
                    for tags in xpath:
                        if tags.tag == 'link':
                            print("Link Relation :-", tags.attrib['rel'], "& Name :-",
                                  tags.attrib['href'].split('/')[-1])
                        else:
                            print("Script Type :-", tags.attrib['type'], "& Name :-", tags.attrib['src'].split('/')[-1])

        break
    else:
        print("Please give proper path")
