from src.strategy import Strategy

class OpenIaContext:

    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy

    def execute_strategy(self, data: str):
        return self._strategy.execute(data)
