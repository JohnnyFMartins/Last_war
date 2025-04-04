import keyboard
import random
import time

def check_stop_key(stop_key='F12'):
    """Verifica se o usuário pressionou a tecla de parar"""
    return keyboard.is_pressed(stop_key)

def random_delay(min_sec=0.5, max_sec=1.5):
    """Espera um tempo aleatório entre ações"""
    time.sleep(random.uniform(min_sec, max_sec))