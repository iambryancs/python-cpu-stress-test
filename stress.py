"""
Produces load on configured number of CPU cores.
Optional system environment var CORE_ALLOC to be set.
  Values:
    -1: use half of the cpus
    -2: use all the available cpus (minus one)
  Default: 1
Requires system environment var STRESS_MINS to be set.
  Default: 1
"""

from multiprocessing import Pool
from multiprocessing import cpu_count
import time
import os

def f(x):
    set_time = os.environ['STRESS_MINS']
    timeout = time.time() + 60*float(set_time)  # X minutes from now
    while True:
        if time.time() > timeout:
            break
        x*x

if __name__ == '__main__':
    num_processes = int(os.environ['CORE_ALLOC'])
    processes = cpu_count()
    if num_processes == -1:
      num_processes = processes // 2
    elif num_processes < 0:
      # Always reserve 1 for other things (multiprocessing Manager for ex)
      num_processes = processes - 1
    if num_processes > processes:
      num_processes = processes

    
    print ('utilizing %d out of %d cores\n' % (num_processes, processes))
    pool = Pool(num_processes)
    pool.map(f, range(num_processes))