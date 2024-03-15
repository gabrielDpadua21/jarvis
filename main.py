from blessings import Terminal
import argparse
from src.translate import TranslationStrategy
from src.commit import CommitStrategy
from src.context import OpenIaContext
from src.summary import SummaryStrategy
from src.explain import ExplainStrategy
from src.commands_factory import CommandsFactory

def main():

    translation = TranslationStrategy()
    commit = CommitStrategy()
    summary = SummaryStrategy()
    explain = ExplainStrategy()
    context = OpenIaContext(explain)

    parser = argparse.ArgumentParser(description="List Javis Functions:")
    parser.add_argument('-t', '--translate', nargs="*", help="Run transalation mode", required=False)
    parser.add_argument('-s', '--summary', nargs="*", help="Run summary mode", required=False)
    parser.add_argument('-e', '--explain', nargs="*", help="Run explain mode", required=False)
    parser.add_argument('-c', '--commit', nargs="*", help="Run commit mode", required=False)
    args = parser.parse_args()
    command = None
    for arg in vars(args):
        if vars(args)[arg] != None:
            print(arg)
            command = CommandsFactory(arg)


    question = input("Insira o texto: ")
    response = command.run(question)

    term = Terminal()
    print(term.clear())

    print(term.red(f"""
        Pergunta:
        {question}
    """))

    print(term.green(f"""
        Resposta:
        {response}
    """))

if __name__ == "__main__":
    main()
