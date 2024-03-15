from blessings import Terminal
from src.translate import TranslationStrategy
from src.commit import CommitStrategy
from src.context import OpenIaContext
from src.summary import SummaryStrategy
from src.explain import ExplainStrategy

def main():

    translation = TranslationStrategy()
    commit = CommitStrategy()
    summary = SummaryStrategy()
    explain = ExplainStrategy()

    context = OpenIaContext(explain)

    test = input("Texto a ser resumido: ")

    response = context.execute_strategy(test)

    term = Terminal()

    print(term.clear())

    print(term.red(f"""
        Pergunta:
        {test}
    """))

    print(term.green(f"""
        Resposta:
        {response}
    """))

if __name__ == "__main__":
    main()
