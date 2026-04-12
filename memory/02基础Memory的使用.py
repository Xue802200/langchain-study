import os
import dotenv
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.messages import BaseMessage
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()
dotenv.load_dotenv()
os.environ['OPENAI_BASE_URL'] = os.getenv('BASE_URL')
os.environ['OPENAI_API_KEY'] = os.getenv('API_KEY')

chatmodel = ChatOpenAI(
    model = 'deepseek-chat',
    streaming=True,
)

history = InMemoryChatMessageHistory()

history.add_ai_message('')
history.add_user_message('帮我计算一下1+1等于多少')

if __name__ == '__main__':
    print(chatmodel.invoke(history.messages).content)