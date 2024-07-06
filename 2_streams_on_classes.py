from threading import Thread
from time import sleep


class Knight(Thread):

    def __init__(self, name, skill):
        super().__init__()
        self.name = name
        self.skill = skill
        self.amount_of_enemies = 100
        self.days_count = 0
        if skill <= 0:
            raise Exception('Уровень навыка должен быть больше нуля.')

    def run(self):
        print(f'{self.name}, на нас напали!')
        while True:
            self.amount_of_enemies -= self.skill
            self.days_count += 1
            sleep(1)
            if self.amount_of_enemies > 0:
                print(f'{self.name}, сражается {self.days_count} день(дня)...,'
                      f' осталось {self.amount_of_enemies} воинов.')

            if self.amount_of_enemies < 0:
                self.amount_of_enemies = 0
                print(f'{self.name}, сражается {self.days_count} день(дня)...,'
                      f' осталось {self.amount_of_enemies} воинов.')
                print(f'{self.name} одержал победу спустя {self.days_count} дней!')
                break

            if self.amount_of_enemies == 0:
                print(f'{self.name}, сражается {self.days_count} день(дня)...,'
                      f' осталось {self.amount_of_enemies} воинов.')
                print(f'{self.name} одержал победу спустя {self.days_count} дней!')
                break


knight1 = Knight('Sir Vinir', 15)
knight2 = Knight('Sir La Faiet', 25)

kn1_alive = knight1.is_alive()
kn2_alive = knight2.is_alive()

party_knights = [knight1, knight2]

for thread in party_knights:
    thread.start()
for thread in party_knights:
    thread.join()

sleep(1)
if (kn1_alive is False) and (kn2_alive is False):
    print('Все битвы закончились!')
