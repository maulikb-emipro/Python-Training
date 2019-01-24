from testing.test import test

class c_gst(test):
    "Calculates 18% Central GST"

    def get_tax(self, price):
        """
        func :- Calculates CGST.
        param :- price of product - must be integer.
        return :- Price with CGST
        """
        print("c gst", price)
        price = "cgst"
        super().get_tax(price)
        print("after c gst")
