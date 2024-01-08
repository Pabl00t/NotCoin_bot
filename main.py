import pyautogui

coin = 'button/coin.png'
happy_button = 'button/happy_button.png'


def farm():
    tick = 10
    energy = 5000
    print('Начало фарма')
    while tick < energy:
        pyautogui.PAUSE = 0.00001
        try:
            x, y = pyautogui.locateCenterOnScreen(coin, confidence= 0.8)
            pyautogui.moveTo(x,y)
            pyautogui.leftClick()
            energy -= 9
            if pyautogui.ImageNotFoundException:
                continue
            else:
                z, y = pyautogui.locateCenterOnScreen(happy_button, confidence= 0.9)
                pyautogui.moveTo(z,y)
                pyautogui.leftClick()
        except pyautogui.ImageNotFoundException:
            print('Монетка пропала!')
            break
    else:
        print(f'Energy: {energy}')
        print('Конец блять')
        


def main():
    farm()
    
    
if __name__ == "__main__":
    main()