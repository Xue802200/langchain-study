from langchain_core.tools import StructuredTool
from pydantic import BaseModel,Field


class Schema(BaseModel):
    msg:str=Field(description='需要查找的内容是什么')

def query(msg: str):
    return '查找到了你想要的结果'

structuredTool = StructuredTool.from_function(
    func = query,
    return_direct = True,
    args_schema= Schema,
    name='搜索工具',
    description='根据指定内容,去Google搜索引擎中进行精确查找'
)

if __name__ == '__main__':
    query('python语法')
    print(structuredTool.name)
    print(structuredTool.description)
    print(structuredTool.return_direct)
    print(structuredTool.args)
