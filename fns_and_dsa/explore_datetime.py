from datetime import datetime
def display_current_datetime():
    """use the datetime module in python tlo print:
        1.The current date and time
        2. A future date using the timedelta class"""
   
    current_date = datetime.now()
    current_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(current_datetime)
    
    
    num= int(input('Enter the nunmber of days to add to the current date:  '))
    tdelta = datetime.timedelta(days=num)
    
    calculate_future_date = current_date + tdelta
    print(calculate_future_date) 
