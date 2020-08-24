import logging
import threading
import time

def thread_function(name):
    logging.info('{} thread: start'.format(name))
    time.sleep(2)
    logging.info('{} thread: finish'.format(name))

if __name__== '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    #threads = []
    #for name in ('Taro', 'Jiro','Saboro'):
    #    logging.info('Main: create and start {}'.format(name))
    #    x = threading.Thread(target=thread_function, args=(name,))
    #    threads.append(x)
    #    x.start()
    #for i, t in enumerate(threads):
    #    logging.info('Main: before join {}'.format(i))
    #    t.join()
    #    logging.info('Main: thread done {}'.format(i))