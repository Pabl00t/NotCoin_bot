import pyautogui
import time
import random

from pyautogui import ImageNotFoundException

coin = "button/coin.png"
happy_button = "button/happy_button.png"


def farm():
    """
    5000 энергии воспольняются 1250 секунд
    Время = (Цель - Начальное значение) / Прирост энергии
    
    Цель = 5000
    Начальное значение = 0
    Прирост энергии = 4

    """
    tick = 9
    minimum = 10
    energy = 5000
    print("Начало фарма")
    while minimum < energy:
        pyautogui.PAUSE = 0.00001
        try:
            coin_locate = pyautogui.locateCenterOnScreen(coin, confidence=0.7)
        except ImageNotFoundException:
            print('Монета не найдена')
            time_rand = random.randint(1000, 1250)
            print(f'Спим: {time_rand} секунд')
            time.sleep(time_rand)
            continue
        else:
            pyautogui.moveTo(coin_locate)
            pyautogui.leftClick(interval=0.0001)
            energy -= tick
            try:
                boost = pyautogui.locateCenterOnScreen(happy_button, confidence=0.7)
            except ImageNotFoundException:
                print('Буст не найден')
                continue
            else:
                pyautogui.moveTo(boost)
                pyautogui.leftClick(interval=0.0001)
    else:
        print(f"Energy: {energy}")
        print("Конец блять")


def main():
    farm()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Вышли с потока")