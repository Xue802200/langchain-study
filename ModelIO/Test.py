import os
import dotenv
from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate
from langchain_openai import ChatOpenAI

#1.加载配置文件
dotenv.load_dotenv()

#2.读取配置文件
os.environ['OPENAI_BASE_URL'] = os.getenv('BASE_URL')
os.environ['OPENAI_API_KEY'] = os.getenv('API_KEY')

#3.准备训练数据
examples = [
    {"input": "北京天气怎么样", "output": "北京市"},
    {"input": "南京下雨吗", "output": "南京市"},
    {"input": "武汉热吗", "output": "武汉市"}
]

#5.构建好解析样例数据的提示词模板
example_prompt_template = PromptTemplate.from_template('input:{input},output:{output}')

#4.构建好少量数据的训练模板
few_shot_template = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt_template,
    suffix='input:{input},output:',
)

#6.构建交互的大模型
chatModel = ChatOpenAI(
    model="deepseek-chat",
)

#7.完成最新输入数据的样本
value = few_shot_template.invoke({'input':'上海市今天刮大风了'})

#8.询问大模型
response = chatModel.invoke(value)

if __name__ == '__main__':
    print(response.content)
