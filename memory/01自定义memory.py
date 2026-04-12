import os
import dotenv
from langchain_classic.agents.agent_toolkits import steam
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.messages import AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()
dotenv.load_dotenv()
os.environ['OPENAI_BASE_URL'] = os.getenv('BASE_URL')
os.environ['OPENAI_API_KEY'] = os.getenv('API_KEY')

chatmodel = ChatOpenAI(
    model = 'deepseek-chat',
    streaming=True,
)

def chat(message):
    while True:
        # 构建提示词
        chat_template = ChatPromptTemplate.from_messages(
            [
                ('system', '你是一个ai助手'),
                ('human', '{message}')
            ]
        )

        chain = chat_template | chatmodel
        full_response = ''

        for chuck in chain.stream(input={'message': message}):
            print(chuck.content,end='',flush=True)
            if chuck.content:
                full_response += chuck.content

        user_input = input('还需要什么帮助吗，输入否退出\n')
        #构建memory
        chat_template.append(AIMessage(content=full_response))
        chat_template.append(HumanMessage(content=user_input))
        message = user_input

if __name__ == '__main__':
    user_input = input('请输入问题\n')
    chat(user_input)