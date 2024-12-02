# Example Threads-Python
# b) A program calling the same function twice using two threads.

from time import sleep, perf_counter    # sleep for waiting
                                        # perf_counter for measuring time
from threading import Thread            # Thread for managing threads

def task():
    """
    A simple function that waits for one second.
    """
    print("Start.")
    sleep(1)
    print("Stop.")

def main():
    """
    Function that calls the function task twice and measures the time elapsed.
    """
    start = perf_counter()              # timestap when starting

    

    # Create two threads
    t1 = Thread(target=task)
    t2 = Thread(target=task)

    # Start the threads
    t1.start()
    t2.start()

    # If there were something else to be done in parallel with the threads,
    # it could be done here

    # Wait for threads to be completed
    t1.join()
    t2.join()

    end = perf_counter()                # timestamp when ending

    print(f"Elapsed time: {end-start:.4f} s.")

if __name__ == "__main__":
    main()
