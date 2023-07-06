import requests
import json
import datetime
from datetime import datetime, timedelta
from SecondaryFunctions import days

class CurrencyData:

    def exchange_rate_api(first_day: str, last_day: str, currency: str):
        response = requests.get(
            f'http://api.nbp.pl/api/exchangerates/rates/a/{currency}/{first_day}'
            f'/{last_day}')
        exchange_rates = []
        days = []
        for data in response.json()['rates']:
            exchange_rates.append(data['mid'])
            days.append(data['effectiveDate'])
        return exchange_rates, days, currency
    
    def week_exchange_rate(exchange_rates, week_days = days()):
        rates, days_api = exchange_rates[0], exchange_rates[1]
        for i in range(7):
            if week_days[i] != days_api[i]:
                rates.insert(i, rates[i-1])
                rates.insert(i+1, rates[i-1]) 
                break
        converted_days = [week_days[i][5:] for i in range(len(week_days))]
        return rates, converted_days

