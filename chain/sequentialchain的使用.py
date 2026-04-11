import os
import dotenv
from langchain_classic.chains.llm import LLMChain
from langchain_classic.chains.sequential import SequentialChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()
os.environ['OPENAI_BASE_URL'] = os.getenv('BASE_URL')
os.environ['OPENAI_API_KEY'] = os.getenv('API_KEY')

#构建大模型
chatmodel = ChatOpenAI(
    model = 'deepseek-chat'
)

templateA = PromptTemplate.from_template(
    template='请给我写一篇文章,标题为:{title}，字数为50字',
)

#构建提示词
chainA = LLMChain(
    prompt=templateA,
    llm=chatmodel,
    output_key='content',
    verbose=True,
)

#构建提示词B
templateB = PromptTemplate.from_template(
    template='文章的内容为:{content}，请将这篇文章翻译成{language}。注意：只需要输出翻译后的{language}版本，不要包含原文，也不要添加任何解释说明。',
)
chainB = LLMChain(
    prompt=templateB,
    llm=chatmodel,
    output_key='foreign-content',
    verbose=True,
)

sequentialChain = SequentialChain(
    chains=[chainA, chainB],
    input_variables=['title', 'language'],
    output_variables=['content','foreign-content'],
)

# 修正 invoke 调用语法
result = sequentialChain.invoke(input={'title': '人工智能发展之路', 'language': 'English'})
print(result)
