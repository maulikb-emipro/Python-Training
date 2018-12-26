from tax import Tax
import re
import datetime


class Purchase(Tax):
    "It collects data of purchasing Product"

    purchase_details = {}

    def purchase(self, quantity, name, price):
        """
        func :- This function is called from product class when product is purchased.
        params :- product type - string
        params :- product quantity - integer
        params :- vendor name - string
        params :- purchasing price - integer 
        returns :- purchase order number.
        """
        tempDictionary = {}
        tempDictionary['price'] = price * quantity
        tempDictionary['total_tax'] = self.get_tax('consumable', tempDictionary['price'], 'purchase')

        order = list(sorted(self.purchase_details.keys()))
        if order == []:
            key = 'PO/0001'
        else:
            number = re.findall('\d+', order[-1])[0]
            number = int(number) + 1
            key = 'PO/' + str(number).zfill(4)

        tempDictionary['date'] = datetime.date.today().strftime("%d/%m/%Y")
        tempDictionary['name'] = name
        tempDictionary['quantity'] = quantity
        tempDictionary['total_price'] = tempDictionary['price'] + tempDictionary['total_tax']
        tempDictionary['unit_price'] = tempDictionary['total_price'] / quantity

        self.purchase_details[key] = tempDictionary

        return tempDictionary['total_price']
