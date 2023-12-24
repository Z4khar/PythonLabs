import inspect


def printMyName():
    """Return my name"""
    print("Zakhar")

source_code = inspect.getsource(printMyName)
print(source_code)