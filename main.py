from src.translate import TranslationStrategy
from src.commit import CommitStrategy
from src.context import OpenIaContext

def main():

    translation = TranslationStrategy()
    commit = CommitStrategy()
    context = OpenIaContext(commit)

    response = context.execute_strategy("inicio do projeto javis, e criação das estrategias de tradução e commit")

    print(f"""
        Pergunta:
        Resposta:
        {response}
    """)

if __name__ == "__main__":
    main()
