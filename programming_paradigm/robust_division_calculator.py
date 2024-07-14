def safe_divide(numerator,denominator):
    """divides two floating point numbers and raising exception for 
    zeroDivision error and Value errors"""
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print('Error: Cannot divide by zero.')
        
    except ValueError:
        print('Error: Please enter numeric values only)
