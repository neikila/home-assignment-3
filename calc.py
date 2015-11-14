from decimal import Decimal, InvalidOperation

def summ(arg):
    return Decimal(str(arg[0])) + Decimal(str(arg[1]))

def sub(arg):
    return Decimal(str(arg[0])) - Decimal(str(arg[1]))

def div(arg):
    return Decimal(str(arg[0])) / Decimal(str(arg[1]))

def mul(arg):
    return Decimal(str(arg[0])) * Decimal(str(arg[1]))

def abs1(arg):
    temp = Decimal(str(arg))
    if temp < 0:
        return -temp
    else:
        return temp

operations = {'x/y':div, 'x-y':sub, 'x+y':summ, 'x*y':mul, '|x|':abs1}
def get_operation(operation_name):
    return operations[operation_name]

def calculate(arguments, operation_name):
    try:
        operation = get_operation(operation_name)
        result = float(operation(arguments))
    except KeyError:
        result = 'Error: Wrong operation'
    except IndexError:
        result = 'Error: Not enough arguments'
    except ZeroDivisionError:
        result = 'Error: Division to zero is prohibited'
    except InvalidOperation:
        result = 'Error: Wrong input argument type'

    return result
