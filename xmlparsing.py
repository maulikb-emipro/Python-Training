from xml.dom.minidom import parse
from pydoc import ispath

while 1:
    path=input("Enter path for XML file :-")#"/home/emipro/workspace/odoo12/odoo/addons/account/views/account.xml"
    if ispath(path):
        file=parse(path)
        odoo=file.documentElement
        templates=odoo.getElementsByTagName('template')
        for template in templates:
            print()
            print("Template ID :-",template.getAttribute('id'))
            xpath=template.getElementsByTagName('xpath')
            print("Xpath position :-",xpath[0].getAttribute('position'))
            if xpath[0].getElementsByTagName('link'):
                links=xpath[0].getElementsByTagName('link')
                for link in links:
                    print("Link Relation :-",link.getAttribute('rel'),"& Name :-",link.getAttribute('href').split('/')[-1])
            if xpath[0].getElementsByTagName('script'):
                scripts=xpath[0].getElementsByTagName('script')
                for script in scripts:
                    print("Script Name :-",script.getAttribute('src').split('/')[-1])
        
        break
    else:
        print("Please give proper path")