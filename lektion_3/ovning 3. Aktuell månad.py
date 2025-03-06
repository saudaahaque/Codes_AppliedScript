# Övning 2: Aktuell månad

import datetime

def current_month():
    now = datetime.datetime.now()
    print("Month:", now.month)

current_month()


now = datetime.datetime.now()
month_name = now.strftime("%B")
 
print(month_name)