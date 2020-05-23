import time
# from memory_profiler import profile
import sys
import random


def container(run, *args, **kwargs):
    t = time.time()
    results = run(*args, **kwargs)
    print('time cost=', time.time() - t)
    print('results =', results)


def random_str(slen=10):
    # seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"
    seed = 'abcdefghijklmnopqrstuvwxyz'
    sa = []
    for i in range(slen):
        sa.append(random.choice(seed))
    return ''.join(sa)
