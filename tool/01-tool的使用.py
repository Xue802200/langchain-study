from langchain_core.tools import tool
from pydantic import BaseModel
from pydantic import Field

class FieldInfo(BaseModel):
    a:int = Field(description='第一个需要相加的数')
    b:int = Field(description='第二个需要相加的数')

@tool(name_or_callable='add_two_numbers',description='求出两个数的和'
      ,args_schema=FieldInfo,return_direct=True)
def add_number(a:int, b:int) -> int:
    """求解两个整数的和"""
    return a + b

if __name__ == '__main__':
    print(add_number.name)
    print(add_number.description)
    print(add_number.args)
    print(add_number.return_direct)