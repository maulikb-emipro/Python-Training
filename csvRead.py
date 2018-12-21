import csv

filepath='/home/emipro/Downloads/import_sale_order_Final.csv'

with open(filepath, newline='') as csvfile:
    csvreader=csv.reader(csvfile)
    csvkeys=next(csvreader)
    data={}
    
    for row in csvreader:
        if row[4] in data.keys():
            data[row[4]]['Purchase List'].append({csvkeys[0]:row[0],csvkeys[1]:row[1],csvkeys[2]:row[2]})
        else:
            data.update({row[4]:{csvkeys[5]:row[5],csvkeys[6]:row[6],csvkeys[7]:row[7],csvkeys[8]:row[8],csvkeys[9]:row[9],csvkeys[10]:row[10],'Purchase List':[{csvkeys[0]:row[0],csvkeys[1]:row[1],csvkeys[2]:row[2]}]}})
        
    print(data)