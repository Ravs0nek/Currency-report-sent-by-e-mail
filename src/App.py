from Table import Workbook1 as wb
from SendingEmail import sending_email

class app:
    
    def use_app(self):
        workbook = wb()
        workbook.title("Last week's currency reports")
        workbook.currency_report('EUR', 3, 2)
        workbook.currency_report('USD', 3, 11)
        workbook.currency_report('GBP', 7, 2)
        workbook.currency_report('CHF', 7, 11)
        sending_email()
        
        