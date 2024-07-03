from threading import Thread
from time import sleep


def print_numbers():
    for num in range(1, 10 + 1):
        print(num)
        sleep(1)


def print_letters():
    for let in range(ord('a'), ord('j') + 1):
        print(chr(let))
        sleep(1)


thr_numbers = Thread(target=print_numbers)
thr_letters = Thread(target=print_letters)

thr_numbers.start()
thr_numbers.join(timeout=0.1)

thr_letters.start()
thr_letters.join()
