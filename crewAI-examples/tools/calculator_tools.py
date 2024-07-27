from langchain.tools import tool
class CalculatorTool():
    @tool("Make a calaculation")
    def calculate(operation):
        """Useful to perform calculations, like 
        sum, substract, multiply, divide, etc,
        between two numbers.
        The input to this tool should be  a mathematical operation
        a couple of examples are "2+2" or "3*5" or "10/2" or "10-5"""
        try:
            return eval(operation)
        except SyntaxError:
            return "Invalid operation"