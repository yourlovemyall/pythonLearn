# -*- coding:utf-8 -*-
from multiprocessing import Pool
import os, time, random


def how_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(6):
        p.apply_async(how_task, args=(i,))

    p.close()
    p.join()
    print("end process")
