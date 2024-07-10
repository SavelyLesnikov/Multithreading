from threading import Thread, Lock
from time import sleep


class BankAccount:

    def __init__(self):
        self.amount = 0
        self.balance = 1000
        self.lock1 = Lock()
        self.lock2 = Lock()

    def deposit(self, amount):
        self.amount = amount
        with self.lock1:
            self.balance += amount
            print(f'Deposited {amount}, new balance is {self.balance}')

    def withdrew(self, amount):
        self.amount = amount
        sleep(0.1)
        try:
            self.lock2.acquire()
            self.balance -= amount
            if self.balance < 0:
                raise
            else:
                print(f'Withdrew {amount}, new balance is {self.balance}')
        except:
            print('Не хватает средств на счету')
        finally:
            self.lock2.release()


def deposit_task(account, amount):
    for _ in range(5):
        account.deposit(amount)


def withdrew_task(account, amount):
    for _ in range(5):
        account.withdrew(amount)


new_account = BankAccount()

deposit_thread = Thread(target=deposit_task, args=(new_account, 100))
withdrew_thread = Thread(target=withdrew_task, args=(new_account, 150))

deposit_thread.start()
withdrew_thread.start()

deposit_thread.join()
withdrew_thread.join()
