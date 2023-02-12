#!/usr/bin/env python
"""
Produces load on all available CPU cores
Updated with suggestion to prevent Zombie processes
Linted for Python 3
Source:
insaner @ https://danielflannery.ie/simulate-cpu-load-with-python/#comment-34130
"""
from multiprocessing import Pool, Process
#from multiprocessing import cpu_count
import signal
import time

stop_loop = 0

def exit_chld(x, y):
    global stop_loop
    stop_loop = 1

def f(x):
    global stop_loop
    fill_memory = ['hello', 'world'] * 10000000
    while not stop_loop:
        x*x
        time.sleep(0)

def cpu_intensive_call():
    x = 1
    while _ in range(100000):
        x*x
        time.sleep(0.1)


signal.signal(signal.SIGINT, exit_chld)

if __name__ == '__main__':
    processes = 100
    print('-' * 20)
    print('Running load on CPU(s)')
    print('Utilizing %d cores' % processes)
    print('-' * 20)
    pool = Pool(processes, initializer=lambda x: Process(name='parsing-document-in-ram-intensive-application.py'), initargs=['parsing-document-in-ram-intensive-application'])
    pool.map(f, range(processes))
