def perform_operation(num1,num2,operation):  
    """performs basic arthimetic operation on two floation point numbers 
    num1 and num2 which takes user inputs and returns a 
    result based on the operation selected by the user.
    Raises zero division error upon zero divisions"""
    if operation =='add':
        result = num1 + num2
        return result
    elif operation == 'multipy':
        result = num1 * num2
        return result
    elif operation == 'subtract':
        resuslt = num1 - num2
        return result
    elif operation =='divide':
        if num2!= 0:
            result = num1 / num2
            return result
        else:
            return 'zero division error'
        
    else:
        return 'invalid choice'
