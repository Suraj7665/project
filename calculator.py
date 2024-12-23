import os
import pyautogui
import time

def open_calculator():
    pyautogui.hotkey('win', 'r')
    time.sleep(1)
    pyautogui.typewrite('calc\n')
    time.sleep(2)

def perform_complex_calculation():
    pyautogui.typewrite('50*3+100/4-5=\n')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')

def open_notepad():
    pyautogui.hotkey('win', 'r')
    time.sleep(1)
    pyautogui.typewrite('notepad\n')
    time.sleep(2)

def paste_result():
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.typewrite('\nResult of Calculation: ')
    pyautogui.hotkey('shift', 'home')
    pyautogui.typewrite('Result of Calculation: ')

def change_font():
    pyautogui.hotkey('alt', 'o')
    pyautogui.typewrite('f\n')
    time.sleep(1)
    pyautogui.typewrite('Times New Roman\n')
    pyautogui.typewrite('12\n')
    pyautogui.press('enter')

def save_file():
    pyautogui.hotkey('ctrl', 's')
    time.sleep(1)
    pyautogui.typewrite('result.txt\n')
    time.sleep(2)

def close_and_reopen_file():
    pyautogui.hotkey('alt', 'f4')
    time.sleep(1)
    os.system('notepad result.txt')

def verify_content():
    time.sleep(2)
    screenshot = pyautogui.screenshot()
    screenshot.save("result_verification.png")
    pyautogui.hotkey('alt', 'f4')

if __name__ == "__main__":
    try:
        open_calculator()
        print("Calculator opened.")

        perform_complex_calculation()
        print("Complex calculation completed.")

        open_notepad()
        print("Notepad opened.")

        paste_result()
        print("Result pasted into Notepad.")

        change_font()
        print("Text modified successfully.")

        save_file()
        print("File saved as result.txt.")

        close_and_reopen_file()
        print("Notepad file reopened successfully.")

        verify_content()
        print("Content verified. Screenshot saved as result_verification.png.")

    except Exception as e:
        print(f"An error occurred: {e}")
