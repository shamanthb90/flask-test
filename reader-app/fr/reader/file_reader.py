import os


# class Reader(ABC):
#     """
#     Abstract class for reading files
#     """
#
#     @abstractmethod
#     def return_content(self) -> str:
#         return ''
#

class FileReader:
    """
    Concrete class for reading files
    """

    def __init__(self, project_dir):
        self.project_dir = project_dir

    # noinspection PyMethodMayBeStatic
    def return_content(self, filename: str, start_line: int, end_line: int):
        """
        Return the content of a file
        :param filename:
        :param start_line:
        :param end_line:
        :return:
        """

        get_full_content = False
        if start_line < 0 or end_line < 0:
            get_full_content = True

        try:
            with open(os.path.join(self.project_dir, 'fr', 'static', filename), 'r', encoding='utf-16') as file:
                if get_full_content:
                    # content = '\n'.join(file.read().split('\n'))
                    content = file.read().splitlines()
                    return join(content)
                # return '\n'.join(file.read().split('\n')[start_line:end_line])  # .encode('latin-1').decode('latin-1')
                return join(file.read().splitlines()[start_line-1:end_line])
        except FileNotFoundError as e:
            return str(e)


def join(iterable):
    return '\n'.join(iterable)
