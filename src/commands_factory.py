from src.translate import TranslationStrategy
from src.commit import CommitStrategy
from src.context import OpenIaContext
from src.summary import SummaryStrategy
from src.explain import ExplainStrategy

class CommandsFactory:

    def __init__(self, command: str):
        self._command = command
        self.translation = TranslationStrategy()
        self.commit = CommitStrategy()
        self.summary = SummaryStrategy()
        self.explain = ExplainStrategy()
        self.context = OpenIaContext(self.translation)

    def run(self, data: str) -> str:
        if self._command == "translate":
            self.context.set_strategy(self.translation)
            return self.context.execute_strategy(data)
        elif self._command == "summary":
            self.context.set_strategy(self.summary)
            return self.context.execute_strategy(data)
        elif self._command == "explain":
            self.context.set_strategy(self.explain)
            return self.context.execute_strategy(data)
        elif self._command == "commit":
            self.context.set_strategy(self.commit)
            return self.context.execute_strategy(data)
        else:
            raise ValueError('Command not found!')
