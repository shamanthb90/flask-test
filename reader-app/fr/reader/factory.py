from fr.reader.file_reader import FileReader


class ReaderFactory:
    def __init__(self, project_dir):
        self.project_dir = project_dir

    # noinspection PyMethodMayBeStatic
    def get_file_reader(self):
        return FileReader(project_dir=self.project_dir)
