import os
import dotenv
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()
dotenv.load_dotenv()
os.environ['OPENAI_BASE_URL'] = os.getenv('BASE_URL')
os.environ['OPENAI_API_KEY'] = os.getenv('API_KEY')

chatmodel = ChatOpenAI(
    model = 'deepseek-chat',
)

def chat_with_llm(question):
    #构建提示词
    template = ChatPromptTemplate.from_messages(
        [
            ('system','你是一个人工智能助手'),
            ('human','{message}')
        ]
    )

    while True:
        #询问大模型
        chain = template | chatmodel

        response = chain.invoke(input={'message': question})

        print(response.content)

        user_input = input('是否需要提问,输入否直接退出')
        if user_input == '否':
            break

        #记忆功能的构建
        template.messages.append(AIMessage(content=response.content))
        template.messages.append(HumanMessage(content=user_input))


if __name__ == '__main__':
    chat_with_llm('今天天气怎么样')