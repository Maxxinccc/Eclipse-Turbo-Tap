Описание функционала:

Случайные интервалы между кликами.
Плавное движение мыши с отклонениями (непрямолинейные траектории).
Ограничение области работы вокруг стартовой точки.
Случайные действия, имитирующие человеческие взаимодействия (промахи, наведение).
Динамические паузы для естественного поведения.

Переменные и их значение:
delay_range
Задает диапазон задержки между кликами (в секундах). Чем больше диапазон, тем менее предсказуемо поведение.

pause_interval_range
Диапазон времени (в секундах) между периодическими паузами. Увеличение диапазона делает действия менее регулярными.

pause_duration_range
Диапазон длины паузы (в секундах). Имитирует случайные отвлечения пользователя.

move_offset_range
Диапазон смещения мыши относительно стартовой точки (в пикселях). Чем шире диапазон, тем больше "разброс" кликов.

steps (в функции move_mouse_smoothly)
Количество шагов, за которые мышь перемещается по траектории. Увеличение значения делает движение более плавным.

duration (в функции move_mouse_smoothly)
Задержка между шагами движения. Чем больше значение, тем медленнее перемещается мышь.

Список команд для установки библиотек:

pip install pyautogui

pip install numpy
