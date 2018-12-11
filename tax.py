class Tax:
    "Calculates GST"
    
    def get_tax(self,pro_type,price,process):
        """
        func :- Calculates GST at selling and purchasing time.
        params :- product type - string
        params :- product price - integer
        returns :- total tax
        """
        if process=='purchase':
            cgst=price*10/100
            sgst=price*12/100
        else:
            if pro_type=='service':
                cgst=price*13/100
                sgst=price*15/100
            else:
                cgst=price*18/100
                sgst=price*12/100
        total_tax=cgst+sgst
        return total_tax