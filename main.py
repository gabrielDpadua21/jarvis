from src.translate import TranslationStrategy
from src.commit import CommitStrategy
from src.context import OpenIaContext

def main():

    translation = TranslationStrategy()
    commit = CommitStrategy()
    context = OpenIaContext(translation)

    test = input("Texto a ser traduzido: ")

    response = context.execute_strategy(test)

    print(f"""
        Pergunta:
        Resposta:
        {response}
    """)

if __name__ == "__main__":
    main()
