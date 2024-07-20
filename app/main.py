'''
Basic app to do something on a schedule.
'''
import random
import time
import logging

import schedule


def math():
    '''
    Log a Buzz and Random Number.
    '''
    logging.warning('buzz')
    logging.warning(random.randrange(500))


def main():
    '''
    Run the math method every 10 seconds forever.
    '''
    schedule.every(10).seconds.do(math)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()
