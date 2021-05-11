# logging statements and how to log

# this is the setup code for LOGGING in PYTHON
import logging

logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# END SETUP CODE FOR LOGGING
logging.disable(logging.CRITICAL)

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))

    logging.debug('Return value is %s' % (total))
    return total

print(factorial(5))

logging.debug('End of program')

# debug and critical are known as "log level"

# debug is the first and lowest log level

# info level

# warning level

# error level

# critcal is the last and highest log level


# logging to a text file
# in order to log to text file instead of the console, you have to change the logging.basicConfig line
# logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
