from src.ia import Ia
from src.strategy import Strategy

class SummaryStrategy(Strategy):
    def execute(self, data: str) -> str:
        prompt = f"""dado texto passado sua tarefa é
        resumir em 180 palavras ou menos usando analogias em portugues do Brasil: '''{data}'''.
        """
        ia = Ia()
        return ia.get_response(prompt)
