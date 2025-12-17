import os

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set")


def main():
    print("Hello from langchain-course!")
    information = """
    Elon Reeve Musk[b] (born June 28, 1971) is a businessman and entrepreneur known for his leadership of Tesla, SpaceX, X, and xAI. Musk has been the wealthiest person in the world since 2021; as of December 2025, Forbes estimates his net worth to be around $677 billion.[1]

Born into a wealthy family in Pretoria, South Africa, Musk emigrated in 1989 to Canada; he has Canadian citizenship since his mother was born there. He received bachelor's degrees in 1997 from the University of Pennsylvania in Philadelphia, United States, before moving to California to pursue business ventures. In 1995, Musk co-founded the software company Zip2. Following its sale in 1999, he co-founded X.com, an online payment company that later merged to form PayPal, which was acquired by eBay in 2002. Musk also became an American citizen in 2002.
    """
    summary_template = """
    Given the following {information} about a person, I want to create:
    1. A short summary
    2. Two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template
    )
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    # llm = ChatOllama(model="gemma3:270m", temperature=0)
    chain = summary_prompt_template | llm 
    response = chain.invoke({"information": information})
    print(response.content)

if __name__ == "__main__":
    main()
