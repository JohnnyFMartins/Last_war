import pyautogui
import time

def find_and_click(image, confidence=0.8, max_attempts=3):
    """Encontra e clica em uma imagem na tela"""
    for _ in range(max_attempts):
        position = pyautogui.locateOnScreen(f'images/{image}', confidence=confidence)
        if position:
            pyautogui.click(position)
            return True
        time.sleep(1)
    return False