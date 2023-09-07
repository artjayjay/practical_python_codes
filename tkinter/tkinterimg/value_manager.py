# value_manager.py

class ValueManager:
    def __init__(self):
        self.value = None

    def set(self, new_value):
        self.value = new_value

    def get(self):
        return self.value
