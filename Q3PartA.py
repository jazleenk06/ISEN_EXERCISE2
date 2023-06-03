def percentage(num1, num2):
    '''
    A function takes two integer inputs (num1, num2), and returns what percentage the first number is 
    of the second. 
    The basic requirement is, if num2 is greater than num1, the result is the percentage of num1 out of num2. 
    The numbers must also be greater than 0. 
    if the numbers do not meet the basic requirement, -1 is returned.
    '''
    result = -1
    if num1 > 0 and num2 > 0 and num2 > num1:
        result = (num1 / num2) * 100
    return result