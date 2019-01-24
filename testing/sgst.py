from testing.test import test

class s_gst(test):
    "Calculates 12% State GST"

    def get_tax(self, price):
        """
        func :- Calculates SGST.
        param :- price of product - must be integer.
        return :- Price with SGST
        """
        print("s gst",price)
        price="sgst"
        super().get_tax(price)
        print("after s gst")