from decimal import Decimal, getcontext
from time import time, strftime
import datetime

def arccot(x, digits):
    getcontext().prec = digits
    total = 0
    n = 1
    while Decimal((2 * n - 1) * x ** (2 * n - 1)) < Decimal(10 ** digits):
        term = ((-1)**(n - 1)) * 1 / Decimal((2 * n - 1) * x ** (2 * n - 1))

        total += term

        n += 1

    return total

def pi(decimals):

    timestart = time()

    print "pi = " + str(Decimal(4 * (4 * arccot(5, decimals + 3) - arccot(239,decimals + 3))).quantize(Decimal(10) ** (-decimals)))

    timeelapsedint = round(time() - timestart, 2)

    timeelapsedstr = str(datetime.timedelta(seconds = round(timeelapsedint, 0)))

    print "runtime: " + timeelapsedstr + " or " + str(timeelapsedint) + " seconds."

