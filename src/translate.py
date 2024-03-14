from src.ia import Ia
from src.strategy import Strategy

class TranslationStrategy(Strategy):
    def execute(self, data: str) -> str:
        prompt = f"""sua tarefa é
        traduzir o texto ou palavra o para o ingles: '''{data}''',
        retornando apenas a tradução.
        """
        ia = Ia()
        return ia.get_response(prompt)
