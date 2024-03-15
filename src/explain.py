from src.ia import Ia
from src.strategy import Strategy

class ExplainStrategy(Strategy):
    def execute(self, data: str) -> str:
        prompt = f"""Dado termo ou texto passado sua tarefa é
        explicar de forma simples em 200 palavras ou menos usando analogias seu significado
        em portugues do Brasil: '''{data}'''.
        """
        ia = Ia()
        return ia.get_response(prompt)
