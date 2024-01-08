import pyautogui
from pyautogui import ImageNotFoundException

coin = "button/coin.png"
happy_button = "button/happy_button.png"


def farm():
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
            break
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
    main()
