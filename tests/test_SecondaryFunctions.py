import sys
from datetime import datetime, timedelta, date
sys.path.append('./src')
from SecondaryFunctions import days

def test_days():
    dates = days()
    today = date.today().strftime("%Y-%m-%d") 
    yesterday = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d") 
    week_ago = (datetime.today() - timedelta(days=7)).strftime("%Y-%m-%d")
    eight_days_ago = (datetime.today() - timedelta(days=8)).strftime("%Y-%m-%d")
    assert len(dates) == 7 and dates[-1] == today or dates[-1] == yesterday and dates[0] == week_ago or dates[0] == eight_days_ago