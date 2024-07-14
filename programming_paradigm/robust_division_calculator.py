def safe_divide(numerator,denominator):
    """divides two floating point numbers and raising exception for 
    zeroDivision error and Value errors"""
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator / denominator
        return f'The result of the division is {result}'

    except ZeroDivisionError:
        return 'Error: Cannot divide by zero.'
        
    except ValueError:
        return "Error: Please enter numeric values only."
