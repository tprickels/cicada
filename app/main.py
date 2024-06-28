import random
import schedule
import time
import logging


def math():
    logging.warning('buzz')
    logging.warning(random.randrange(500))

def main():
    schedule.every(10).seconds.do(math)
    while True:
        schedule.run_pending()
        time.sleep(1)
    

if __name__ == '__main__':
   main()
