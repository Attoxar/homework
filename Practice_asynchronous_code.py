import asyncio
import time
from multiprocessing import Pool
from math import factorial
# import math is only used in the first part

# ______Firstpart______
# async def compute_all(n):
#     fib = await compute_fibonacci(n)
#     fact = math.factorial(n)
#     sq = n * n
#     cube = n * n * n
#     return fib, fact, sq, cube
#
# async def compute_fibonacci(n):
#     if n <= 1:
#         return n
#     a, b = 0, 1
#     for _ in range(2, n+1):
#         a, b = b, a + b
#     return b
#
# async def main_async():
#     numbers = range(1, 11)
#     results = await asyncio.gather(*(compute_all(n) for n in numbers))
#     fib_results, fact_results, square_results, cube_results = zip(*results)
#     print("First Part Fibonacci results:", fib_results)
#     print("First Part Factorial results:", fact_results)
#     print("First Part Square results:", square_results)
#     print("First Part Cube results:", cube_results)
#
# if __name__ == "__main__":
#     asyncio.run(main_async())


# _________Second_____Part_______

async def compute_fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b


async def compute_all_async(n):
    fib = await compute_fibonacci(n)
    fact = factorial(n)
    sq = n * n
    cube = n * n * n
    return fib, fact, sq, cube


async def main_async():
    tasks = [compute_all_async(n) for n in range(1, 11)]
    results = await asyncio.gather(*tasks)
    fib_results, fact_results, square_results, cube_results = zip(*results)
    return fib_results, fact_results, square_results, cube_results


def compute_fibonacci_sync(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b


def compute_all_sync(n):
    fib = compute_fibonacci_sync(n)
    fact = factorial(n)
    sq = n * n
    cube = n * n * n
    return fib, fact, sq, cube


def main_multiprocessing():
    with Pool() as pool:
        results = pool.map(compute_all_sync, range(1, 11))
    fib_results, fact_results, square_results, cube_results = zip(*results)
    return fib_results, fact_results, square_results, cube_results


if __name__ == "__main__":
    # Measure performance of asyncio approach
    start_time = time.time()
    async_results = asyncio.run(main_async())
    asyncio_duration = time.time() - start_time

    # Measure performance of multiprocessing approach
    start_time = time.time()
    mp_results = main_multiprocessing()
    multiprocessing_duration = time.time() - start_time

    print("Asyncio results:")
    print("Fibonacci results:", async_results[0])
    print("Factorial results:", async_results[1])
    print("Square results:", async_results[2])
    print("Cube results:", async_results[3])

    print(f"\nAsyncio duration: {asyncio_duration:.4f} seconds")

    print("\nMultiprocessing results:")
    print("Fibonacci results:", mp_results[0])
    print("Factorial results:", mp_results[1])
    print("Square results:", mp_results[2])
    print("Cube results:", mp_results[3])

    print(f"\nMultiprocessing duration: {multiprocessing_duration:.4f} seconds")
