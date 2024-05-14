from . import filehandler
from . import runner

class ExecuteFile:
    @staticmethod
    def execute_python_code(code: str, input: str = "") -> str:
        """
        Executes the given python code and returns the result.
        :param code: The python code to execute.
        :return: The result of executing the code.
        """
        filehandler.FileHandler.save_python_file(code)
        return runner.Runner.run_python_code(input)
    
    def execute_java_code(code: str, input: str = "") -> str:
        """
        Executes the given java code and returns the result.
        :param code: The java code to execute.
        :return: The result of executing the code.
        """
        filehandler.FileHandler.save_java_file(code)
        return runner.Runner.run_java_code(input)
    
    def execute_c_code(code: str, input: str = "") -> str:
        """
        Executes the given c code and returns the result.
        :param code: The c code to execute.
        :return: The result of executing the code.
        """
        filehandler.FileHandler.save_c_file(code)
        return runner.Runner.run_c_code(input)
    
    def execute_cpp_code(code: str, input: str = "") -> str:
        """
        Executes the given cpp code and returns the result.
        :param code: The cpp code to execute.
        :return: The result of executing the code.
        """
        filehandler.FileHandler.save_cpp_file(code)
        return runner.Runner.run_cpp_code(input)
    