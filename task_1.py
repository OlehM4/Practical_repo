from datetime import datetime

def get_days_from_today(date):
    try:
        date = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        return "This date is written incorrectly. Please write it in the format YYYY-MM-DD."
    
    current_date = datetime.today()
    delta = date.date() - current_date.date()
    return delta.days

print(get_days_from_today("2026-01-03")) 


