import csv
from productNew import product_obj

filepath = '/home/emipro/Desktop/Training/product.csv'

csvkeys = ['Product Name', 'Available Quantity', 'Type', 'Profit/Loss', 'Valuation', 'Purchase Value', 'Sell Value']

with open(filepath, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvvalues = product_obj.product
    csvwriter.writerow(csvkeys)
    csvwriter.writerow([csvvalues['name'], csvvalues['available_qty'], csvvalues['type'], csvvalues['profit_loss'],
                        csvvalues['valuation_price'], csvvalues['purchase_value'], csvvalues['sell_value']])

filepath = '/home/emipro/Desktop/Training/purchase.csv'
csvkeys = ['Purchase Order', 'Date', 'Vendor Name', 'Quantity', 'Price', 'Total GST', 'Total Price', 'Unit Price']

with open(filepath, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(csvkeys)
    for orders in csvvalues['purchase_order']:
        data = product_obj.purchase_details[orders]
        csvwriter.writerow([orders, data['date'], data['name'], data['quantity'], data['price'], data['total_tax'],
                            data['total_price'], data['unit_price']])

filepath = '/home/emipro/Desktop/Training/sell.csv'
csvkeys = ['Sell Order', 'Date', 'Customer Name', 'Quantity', 'Price', 'Total GST', 'Total Price', 'Unit Price']

with open(filepath, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(csvkeys)
    for orders in csvvalues['sell_order']:
        data = product_obj.sell_details[orders]
        csvwriter.writerow([orders, data['date'], data['name'], data['quantity'], data['price'], data['total_tax'],
                            data['total_price'], data['unit_price']])
