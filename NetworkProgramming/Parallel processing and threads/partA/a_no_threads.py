# Example Threads-Python
# a) A program calling the same function twice, no threads.

from time import sleep, perf_counter    # sleep for waiting
                                        # perf_counter for measuring time

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

    task()                              # first call
    task()                              # second call

    end = perf_counter()                # timestamp when ending

    print(f"Elapsed time: {end-start:.4f} s.")

if __name__ == "__main__":
    main()