import os

from dotenv import load_dotenv  # pyright: ignore[reportMissingImports]

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set")


def main():
    print("Hello from langchain-course!")
    print(OPENAI_API_KEY)


if __name__ == "__main__":
    main()
