class FileHandler:
    """
    A utility class for handling file operations.
    """

    @staticmethod
    def save_python_file(data: str):
        """
        Save Python code to a file named temp.py in the CacheFile directory.

        Args:
            data (str): The Python code to be saved.
        """
        with open("api/Executioner/CacheFile/temp.py", "w") as file:
            file.write(data)

    @staticmethod
    def save_java_file(data: str):
        """
        Save Java code to a file named temp.java in the CacheFile directory.

        Args:
            data (str): The Java code to be saved.
        """
        with open("api/Executioner/CacheFile/temp.java", "w") as file:
            file.write(data)

    @staticmethod
    def save_c_file(data: str):
        """
        Save C code to a file named temp.c in the CacheFile directory.

        Args:
            data (str): The C code to be saved.
        """
        with open("api/Executioner/CacheFile/temp.c", "w") as file:
            file.write(data)

    @staticmethod
    def save_cpp_file(data: str):
        """
        Save C++ code to a file named temp.cpp in the CacheFile directory.

        Args:
            data (str): The C++ code to be saved.
        """
        with open("api/Executioner/CacheFile/temp.c++", "w") as file:
            file.write(data)

    @staticmethod
    def save_input_file(input_data: str):
        """
        Save input data to a file named input.txt in the CacheFile directory.

        Args:
            input_data (str): The input data to be saved.
        """
        with open("api/Executioner/CacheFile/input.txt", "w") as file:
            file.write(input_data)

    @staticmethod
    def get_input() -> str:
        """
        Read input data from a file named input.txt in the CacheFile directory.

        Returns:
            str: The input data read from the file.
        """
        with open("api/Executioner/CacheFile/input.txt", "r") as file:
            return file.read()
