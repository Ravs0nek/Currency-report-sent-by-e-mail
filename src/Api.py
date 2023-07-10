import requests
import json
import datetime
from datetime import datetime, timedelta
from typing import Tuple
from SecondaryFunctions import days, is_weekend

class CurrencyData:

    def exchange_rate_api(currency: str, first_day = days(12)[0], last_day = days(12)[-1]) -> Tuple[list, list, str]:
        response = requests.get(
            f'http://api.nbp.pl/api/exchangerates/rates/a/{currency}/{first_day}'
            f'/{last_day}')
        exchange_rates = []
        days = []
        for data in response.json()['rates']:
            exchange_rates.append(data['mid'])
            days.append(data['effectiveDate'])
        return exchange_rates, days, currency
    
    def week_exchange_rate(exchange_rates: Tuple(list, list, str), week_days = days(12)) -> Tuple[list, list]: 
        rates = exchange_rates[0]
        for i in range(2):
            if is_weekend(week_days[i]):
                del week_days[i]
        for i in range(len(week_days)):
            if is_weekend(week_days[i]):
                rates.insert(i, rates[i-1])
        week_days = week_days[-7:]
        rates = rates[-7:]
        converted_days = [week_days[i][5:] for i in range(len(week_days))]
        return rates, converted_days

