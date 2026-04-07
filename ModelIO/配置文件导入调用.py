import os
from langchain_openai import ChatOpenAI
import dotenv


if __name__ == '__main__':
    # 加载配置文件
    dotenv.load_dotenv()

    chatModel = ChatOpenAI(
        model_name='deepseek-chat',
        api_key=os.getenv('API_KEY'),
        base_url=os.getenv('BASE_URL'),
    )
    response = chatModel.invoke('你是谁')

    content = response.content
    print(type(response))
    print(content)