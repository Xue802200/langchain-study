from langchain_core.prompts import ChatPromptTemplate

template = ChatPromptTemplate.from_messages([
    ("system","你是世界级的技术文档编写者"),
    ("user","{input}")
])

if __name__ == "__main__":
    print(template)
