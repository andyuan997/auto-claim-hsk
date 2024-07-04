import pyautogui
import time
from datetime import datetime
import random
import keyboard

def simulate_work_command():
    pyautogui.typewrite('/work')
    pyautogui.press('enter')
    pyautogui.press('enter')
    print(f"{datetime.now()} - 輸入/work")

def simulate_daily_command():
    pyautogui.typewrite('/daily')
    pyautogui.press('enter')
    pyautogui.press('enter')
    print(f"{datetime.now()} - 輸入/daily")

def main():
    time.sleep(5)
    simulate_daily_command()
    count = 0

    while True:
        if keyboard.is_pressed('q'):  # 检查是否按下 'q' 键
            print("腳本停止運行。")
            break
        time.sleep(1)
        count += 1

        if (count % 3600 == 0):
            random_sleep_time = random.randint(1, 20)
            time.sleep(random_sleep_time)

            simulate_work_command()

        if (count >= 86400):
            random_sleep_time = random.randint(1, 20)
            time.sleep(random_sleep_time)

            simulate_daily_command()

            count = 0


if __name__ == "__main__":
    print("腳本開始運行。輸入 'q' 退出腳本。")
    main()
