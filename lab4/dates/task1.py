from datetime import datetime, timedelta
date=datetime.now()
new_date=date-timedelta(days=5)
print( "Current date ",date.strftime("%Y-%m-%d"))
print ("New date",new_date.strftime("%Y-%m-%d"))