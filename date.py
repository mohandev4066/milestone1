from datetime import datetime
from dateutil.relativedelta import relativedelta


print( 'Today: ',datetime.now().strftime('%d/%m/%Y %H:%M:%S') )
day = input("enter the day")
int_day=int(day)
date_after_month = datetime.now()+ relativedelta(days=int_day)
print( 'After '+day+' Days:', date_after_month.strftime('%d/%m/%Y'))
