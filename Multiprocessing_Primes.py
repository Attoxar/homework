import time
import math
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from multiprocessing import Pool

NUMBERS = [
    2,  # prime
    1099726899285419,
    1570341764013157,  # prime
    1637027521802551,  # prime
    1880450821379411,  # prime
    1893530391196711,  # prime
    2447109360961063,  # prime
    3,  # prime
    2772290760589219,  # prime
    3033700317376073,  # prime
    4350190374376723,
    4350190491008389,  # prime
    4350190491008390,
    4350222956688319,
    2447120421950803,
    5,  # prime
]

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    if n < 9:
        return True
    if n % 5 == 0:
        return False
    r = int(math.isqrt(n))
    f = 5
    while f <= r:
        if n % f == 0 or n % (f + 2) == 0:
            return False
        f += 6
    return True

def filter_primes_threadpool():
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(is_prime, NUMBERS))
    return [num for num, is_prime_flag in zip(NUMBERS, results) if is_prime_flag]

def filter_primes_processpool():
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(is_prime, NUMBERS))
    return [num for num, is_prime_flag in zip(NUMBERS, results) if is_prime_flag]

def filter_primes_multiprocessing_pool(numbers):
    with Pool() as pool:
        results = pool.map(is_prime, numbers)
    return [num for num, is_prime_flag in zip(numbers, results) if is_prime_flag]

if __name__ == "__main__":
    # ThreadPoolExecutor
    start_time = time.time()
    thread_pool_primes = filter_primes_threadpool()
    thread_pool_duration = time.time() - start_time

    # ProcessPoolExecutor
    start_time = time.time()
    process_pool_primes = filter_primes_processpool()
    process_pool_duration = time.time() - start_time

    # multiprocessing.Pool
    start_time = time.time()
    multiprocessing_pool_primes = filter_primes_multiprocessing_pool(NUMBERS)
    multiprocessing_pool_duration = time.time() - start_time

    print(f"ThreadPoolExecutor primes: {thread_pool_primes}")
    print(f"ThreadPoolExecutor duration: {thread_pool_duration:.4f} seconds")

    print(f"ProcessPoolExecutor primes: {process_pool_primes}")
    print(f"ProcessPoolExecutor duration: {process_pool_duration:.4f} seconds")

    print(f"Multiprocessing Pool primes: {multiprocessing_pool_primes}")
    print(f"Multiprocessing Pool duration: {multiprocessing_pool_duration:.4f} seconds")