import sys
from datetime import datetime, timedelta, date
sys.path.append('./src')
from SecondaryFunctions import days, is_weekend

def test_days():
    dates = days()
    today = date.today().strftime("%Y-%m-%d") 
    yesterday = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d") 
    twelve_days_ago = (datetime.today() - timedelta(days=12)).strftime("%Y-%m-%d")
    thirteen_days_ago = (datetime.today() - timedelta(days=13)).strftime("%Y-%m-%d")
    assert len(dates) == 12 and dates[-1] == today or dates[-1] == yesterday \
        and dates[0] == twelve_days_ago or dates[0] == thirteen_days_ago
    #depending on what time it is

def test_is_weekend():
    weekend_day = '2023-07-09'
    business_day = '2023-07-05'
    assert is_weekend(weekend_day) and not is_weekend(business_day)

    