from typing import Protocol

class Strategy(Protocol):
    def execute(self, data: str) -> str:
        pass
