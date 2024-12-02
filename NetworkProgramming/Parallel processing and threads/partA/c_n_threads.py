# Example Threads-Python
# c) A program calling the same function N times (N is a global variable),
# each call in its own thread.

from time import sleep, perf_counter    # sleep for waiting
                                        # perf_counter for measuring time
from threading import Thread            # Thread for managing threads

N = 6   # For setting the number of asynchorous function calls (threads)

def task(id:int):
    """
    A simple function that waits for one second. Parameter id is used
    as a unique idenfier for the call (thread).
    """
    print(f"Start (task {id}).")
    sleep(1)
    print(f"Stop (task {id}).")

def main():
    """
    Function that calls the function task N times and measures the time
    elapsed.
    """
    start = perf_counter()              # timestap when starting

    # Create threads to a list and start each of them
    threads = []
    for id in range(1, N+1):
        t = Thread(target=task, args=(id,))
        threads.append(t)
        t.start()

    # If there were something else to be done in parallel with the threads,
    # it could be done here

    # Odotetaan säikeiden valmistumista
    for t in threads:
        t.join()

    end = perf_counter()                # timestamp when ending

    print(f"Elapsed time: {end-start:.4f} s.")

if __name__ == "__main__":
    main()
