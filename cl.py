import pyautogui
import time
import random
import numpy as np

# Переменные настройки
delay_range = (0.3, 0.8)           # Диапазон задержки между кликами (в секундах)
pause_interval_range = (8, 12)     # Диапазон времени до паузы (в секундах)
pause_duration_range = (4, 7)      # Диапазон длины паузы (в секундах)
move_offset_range = (-50, 50)      # Диапазон смещения от стартовой позиции (в пикселях)

# Фиксируем стартовую позицию
start_position = None  # Определится при запуске скрипта

def move_mouse_smoothly(start, end, steps=10):
    """
    Перемещение мыши по плавной траектории между двумя точками.
    """
    x_vals = np.linspace(start[0], end[0], steps)
    y_vals = np.linspace(start[1], end[1], steps) + np.random.normal(0, 2, steps)  # Случайные отклонения
    for x, y in zip(x_vals, y_vals):
        pyautogui.moveTo(int(x), int(y), duration=0.05)

def clicker():
    global start_position
    print("Скрипт начнётся через 5 секунд. Подготовьтесь!")
    time.sleep(5)
    
    # Установка стартовой позиции
    start_position = pyautogui.position()
    print(f"Стартовая позиция мыши зафиксирована: {start_position}")
    
    print("Начинаю кликать. Нажмите Ctrl+C, чтобы остановить.")
    last_pause_time = time.time()
    
    try:
        while True:
            # Текущее время
            current_time = time.time()
            
            # Случайное перемещение мыши в пределах диапазона от стартовой позиции
            random_x = start_position.x + random.randint(*move_offset_range)
            random_y = start_position.y + random.randint(*move_offset_range)
            print(f"Планируется перемещение мыши в ({random_x}, {random_y})")
            
            # Перемещение мыши плавно
            move_mouse_smoothly((pyautogui.position().x, pyautogui.position().y), (random_x, random_y))
            
            # Выполнение клика
            pyautogui.click()
            print("Клик!")
            
            # Случайное взаимодействие (наведение на элемент)
            if random.random() < 0.3:  # 30% вероятность дополнительного действия
                hover_x = start_position.x + random.randint(-100, 100)
                hover_y = start_position.y + random.randint(-100, 100)
                move_mouse_smoothly((random_x, random_y), (hover_x, hover_y))
                print(f"Навёл мышь на случайную точку ({hover_x}, {hover_y}).")
                time.sleep(random.uniform(0.5, 2))  # Короткая пауза
                
            # Случайная задержка между кликами
            delay = random.uniform(*delay_range)
            time.sleep(delay)
            
            # Проверка на необходимость паузы
            time_since_last_pause = current_time - last_pause_time
            pause_interval = random.uniform(*pause_interval_range)
            
            if time_since_last_pause >= pause_interval:
                pause_duration = random.uniform(*pause_duration_range)
                print(f"Пауза на {pause_duration:.2f} секунд...")
                time.sleep(pause_duration)
                last_pause_time = time.time()  # Обновляем время последней паузы
                print("Продолжаю работу.")
    except KeyboardInterrupt:
        print("Скрипт остановлен пользователем.")

if __name__ == "__main__":
    clicker()
