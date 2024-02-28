import os
from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex
from llama_index.readers.web import SimpleWebPageReader



def main(url: str) -> None:
    documents = SimpleWebPageReader(html_to_text=True).load_data(urls=[url])
    index = VectorStoreIndex.from_documents(documents=documents)
    query_engine = index.as_query_engine()
    response = query_engine.query("What are the available visas and their requirements for an egyptian person who wants to holiday in australia")
    print(response)


if __name__ == '__main__':
    load_dotenv()
    print("hello Llama Index")
    print(f"OPENAI_API_KEY is: {os.environ['OPENAI_API_KEY']}")
    print("*******")
    main(url="https://immi.homeaffairs.gov.au/visas")
