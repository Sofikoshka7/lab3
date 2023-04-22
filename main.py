import random
from abc import ABC, abstractmethod

class Variant(ABC):
    @abstractmethod
    def selection(self) -> None:
        pass

class one(Variant):
    def selection(self) -> str:
        return "один"

class two(Variant):
    def selection(self) -> str:
        return "два"

class three(Variant):
    def selection(self) -> str:
        return "три"

class four(Variant):
    def selection(self) -> str:
        return "четыре"

class five(Variant):
    def selection(self) -> str:
        return "пять"

class Random(Variant):
    def selection(self) -> str:
        options = [ "один", "два", "три", "четыре", "пять"]
        return random.choice(options)

class Game:
    strategy: Variant

    def __init__(self, strategy: Variant = None) -> None:
        if strategy is not None:
            self.strategy = strategy
        else:
            self.strategy = Random()

    def play(self, sec2) -> None:
        s1 = self.strategy.selection()
        s2 = sec2.strategy.selection()
        if s1 == s2:
            print("ничья!")


        elif s1 == "один":
            if s2 == "два":
                print("побеждает второй игрок!", s1, '<', s2)
            elif s2 == ("три"):
                print("побеждает второй игрок!", s1, '<', s2)
            elif s2 == ("четыре"):
                print("побеждает второй игрок!", s1, '<', s2)
            elif s2 == ("пять"):
                print("Побеждает второй игрок!", s1, '<', s2)

        elif s1 == "два":
            if s2 == "один":
                print("побеждает первый игрок!", s1, '>', s2)
            elif s2 == ("три"):
                print("побеждает второй игрок!", s1, '<', s2)
            elif s2 == ("четыре"):
                print("побеждает второй игрок!", s1, '<', s2)
            elif s2 == ("пять"):
                print("побеждает второй игрок!", s1, '<', s2)


        elif s1 == "три":
            if s2 == "один":
                print("побеждает первый игрок!", s1, '>', s2)
            elif s2 == ("два"):
                print("побеждает первый игрок!", s1, '>', s2)
            elif s2 == ("четыре"):
                print("побеждает второй игрок!", s1, '<', s2)
            elif s2 == ("пять"):
                print("Побеждает второй игрок!", s1, '<', s2)


        elif s1 == "четыре":
            if s2 == "один":
                print("побеждает первый игрок!", s1, '>', s2)
            elif s2 == ("два"):
                print("побеждает первый игрок!", s1, '>', s2)
            elif s2 == ("три"):
                print("побеждает первый игрок!", s1, '>', s2)
            elif s2 == ("пять"):
                print("побеждает второй игрок!", s1, '<', s2)


        elif s1 == "пять":
            if s2 == "один":
                print("побеждает первый игрок!", s1, '>', s2)
            elif s2 == ("два"):
                print("побеждает первый игрок!", s1, '>', s2)
            elif s2 == ("три"):
                print("побеждает первый игрок!", s1, '>', s2)
            elif s2 == ("четыре"):
                print("побеждает первый игрок!", s1, '>', s2)

def playtime(vibor):
    if vibor == "один":
        return Game(one())
    elif vibor == "два":
        return Game(two())
    elif vibor == "три":
        return Game(three())
    elif vibor == "четыре":
        return Game(four())
    elif vibor == "пять":
        return Game(five())
    elif vibor == "случайно":
        return Game(Random())

n=1
while n==1:
    print("первый игрок:\nсделайте выбор: один, два, три, четыре, пять, случайно")
    vibor=input()
    while vibor not in ("один", "два", "три", "четыре", "пять", "случайно"):
        print("повторите ввод")
        vibor=input()
    player1 = playtime(vibor)

    print("второй игрок:\nсделайте выбор: один, два, три, четыре, пять, случайно")
    vibor = input()
    while vibor not in ("один", "два", "три", "четыре", "пять", "случайно"):
        print("повторите ввод")
        vibor=input()
    player2 = playtime(vibor)
    player1.play(player2)
    print("желаете повторить? 1-да")
    n=int(input())
print("конец!")