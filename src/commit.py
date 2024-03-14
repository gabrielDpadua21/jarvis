from src.ia import Ia
from src.strategy import Strategy

class CommitStrategy(Strategy):
    def execute(self, data: str) -> str:
        prompt = f"""sua tarefa é
        criar uma mensagem de commit coerente e simples
        conforme o contexto passado
        usando padrão do conventional commits e traduza para o ingles: '''{data}'''.
        """
        ia = Ia()
        return ia.get_response(prompt)
