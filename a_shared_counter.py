import threading


class Counter(threading.Thread):
    counter = 0
    rounds = 100000
    lock = threading.Lock() # using the lock so that only 1 thread can increment the counter at a time,
                            # otherwise the gil may affect the result since its allows only one thread to be executed
                            #at a time in a single process, other reasons would be the lack of synchronization wich
                            # could possible interfere with each other.

    def run(self):
        for _ in range(self.rounds):
            with Counter.lock:
                Counter.counter += 1


thread1 = Counter()
thread2 = Counter()

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f'Counter: {Counter.counter}')

