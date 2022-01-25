from fr.reader.factory import ReaderFactory


def get_file_contents(factory: ReaderFactory, filename, start_line, end_line):
    """
    Get the contents of a file from a given start line to a given end line.
    :param factory: Factory to use to get the file reader.
    :param filename: The path of the file to read.
    :param start_line: The start line of the file to read.
    :param end_line: The end line of the file to read.
    :return: The contents of the file.
    """
    file_reader = factory.get_file_reader()
    return file_reader.return_content(filename=filename, start_line=start_line, end_line=end_line)
