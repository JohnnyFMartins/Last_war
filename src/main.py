import time
import random
from src.core import actions
from src.core import detection

def main():
    print("🕹️ Bot do Last War iniciado! Pressione F12 para parar.")
    
    while True:
        # 1. Coletar recursos
        if detection.find_and_click('recursos.png'):
            print("💰 Recursos coletados!")
            time.sleep(random.uniform(1, 2))
        
        # 2. Atacar
        if detection.find_and_click('ataque.png'):
            print("⚔️ Atacando inimigos...")
            time.sleep(random.uniform(3, 5))
        
        # 3. Verificar se quer parar
        if actions.check_stop_key():
            print("🛑 Bot parado pelo usuário.")
            break

if __name__ == "__main__":
    main()