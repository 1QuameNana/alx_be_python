import datetime 
def display_current_datetime():
    """use the datetime module in python tlo print:
        1.The current date and time
        2. A future date using the timedelta class"""
   
    current_date = datetime.datetime.now()
    print(current_date)
    
    
    num= int(input('Enter the nunmber of days to add to the current date:  '))
    tdelta = datetime.timedelta(days=num)
    
    future_date = current_date + tdelta
    print(future_date) 
