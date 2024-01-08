import pyautogui
import time
import random
import os

from pyautogui import ImageNotFoundException

coin = "button/coin.png"
happy_button = "button/happy_button.png"
clear = lambda: os.system('cls')


def farm():
    """
    5000 энергии воспольняются 1250 секунд
    Время = (Цель - Начальное значение) / Прирост энергии

    Цель = 5000
    Начальное значение = 0
    Прирост энергии = 4

    """
    max_energy = 5000
    tap = 4
    tap_boost = 0
    
    clear()
    print("Начало фарма")
    while tap < max_energy:
        pyautogui.PAUSE = 0.00001
        try:
            coin_locate = pyautogui.locateCenterOnScreen(coin, confidence=0.7)
        except ImageNotFoundException:
            clear()
            print("Монета не найдена")
            print(f'Получено бустов: {tap_boost}')
            time_rand = random.randint(1000, 1250)
            print(f"Спим: {time_rand} секунд")
            time.sleep(time_rand)
            continue
        else:
            pyautogui.moveTo(coin_locate)
            pyautogui.leftClick(interval=0.0001)
            max_energy -= tap

            try:
                boost = pyautogui.locateCenterOnScreen(happy_button, confidence=0.7)
            except ImageNotFoundException:
                print("Буст не найден")
                continue
            else:
                pyautogui.moveTo(boost)
                pyautogui.leftClick(interval=0.0001)
                tap_boost += 1
                print(f'Нажал по бусту: {tap_boost} раз')
    else:
        print(f"Получено бустов: {tap_boost}")
        print("Конец блять")


def main():
    farm()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear()
        print("Вышли с потока")
