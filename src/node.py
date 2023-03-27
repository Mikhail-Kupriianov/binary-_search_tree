class Node:
    """Класс для хранения данных"""

    def __init__(self, data: dict) -> None:
        """ Сохраняем данные. Инициализируем левый и правый атрибуты."""
        self.data = data
        self.left = None
        self.right = None


