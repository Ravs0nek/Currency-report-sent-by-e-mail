import sys
sys.path.append('./src')
from Api import CurrencyData as cd
from SecondaryFunctions import days
from datetime import date

def test_exchange_rate_api():
    data = cd.exchange_rate_api(first_day = days()[0], last_day = days()[-1], currency='USD') 
    exchange_rates = data[0]
    report_days = data[1]
    currency = data[2]
    assert len(exchange_rates) == 5 and len(report_days) == 5 and currency == 'USD'

def test_week_exchange_rate():
    data = cd.week_exchange_rate(exchange_rates=cd.exchange_rate_api(first_day= days()[0], last_day= days()[-1], currency='USD'))
    exchange_rates = data[0]
    dates = data[1]
    today_date = date.today().strftime("%m/%d/%Y")
    today_date_function = dates[-1]
    print(today_date_function[:1])
    assert len(exchange_rates) == 7 and today_date[:1] == today_date_function[:1] or today_date[:2] == today_date_function[:2] and \
                            today_date[3:5] == today_date_function[3:5] or today_date[4:6] == today_date_function[4:6]
