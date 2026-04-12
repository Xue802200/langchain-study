from langchain_community.tools import MoveFileTool, convert_to_openai
from langchain_core import tools
from langchain_core.tools import tool
from langchain_core.utils.function_calling import convert_to_openai_function
from langchain_openai import ChatOpenAI
import os
import dotenv
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

#加载配置文件
dotenv.load_dotenv()

#获取模型的访问信息
os.environ['OPENAI_API_KEY'] = os.getenv('API_KEY')
os.environ['OPENAI_BASE_URL'] = os.getenv('BASE_URL')

#1获取大模型
chat_model = ChatOpenAI(
    model_name='deepseek-chat'
)

#2构建消息对象
human_message = [HumanMessage(content='请把a文件移动到桌面')]

#3准备工具类
tools = [MoveFileTool]
functions=[convert_to_openai_function(t) for t in tools]

#4进行调用
response = chat_model.invoke(
    input=human_message,
    functions=functions,
)

if __name__ == '__main__':
    print(response)