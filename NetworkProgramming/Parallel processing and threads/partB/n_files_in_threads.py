# Activity 3 b)

from time import sleep, perf_counter
from threading import Thread

def replace(filename:str, original_str:str, new_str:str):
    """
    Function to replace all instances of string original_str
    with string new_str.
    """
    print(f"Starting file ({filename}).")

    # Open, read the content and close the file
    file = open(filename, "r", encoding="UTF-8")
    content = file.read()
    file.close()

    # Replace all instances of original_str with new_str
    content = content.replace(original_str, new_str)

    # Open, write the new content and close the file
    file = open(filename, "w", encoding="UTF-8")
    file.write(content)
    file.close()
    print(f"Completed file ({filename}).")

def main():
    """
    Handles 10 files (replaces string "there" with "where"
    in all of them).
    """
    start = perf_counter()
    files = [
        "test1.txt",
        "test2.txt",
        "test3.txt",
        "test4.txt",
        "test5.txt",
        "test6.txt",
        "test7.txt",
        "test8.txt",
        "test9.txt",
        "test10.txt"
    ]

    # Create threads
    threads = []
    for filename in files:
        thread = Thread(target=replace, args=(filename, "there", "where"))
        threads.append(thread)

    # Start threads
    for thread in threads:
        thread.start()

    # Join threads
    for thread in threads:
        thread.join()

    end = perf_counter()

    print(f"Time elapsed: {end-start:.4f} s.")

if __name__ == "__main__":
    main()
