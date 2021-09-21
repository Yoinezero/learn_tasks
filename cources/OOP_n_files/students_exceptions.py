class StudentsDataException(Exception):
    def __init__(self, data, message):
        Exception.__init__(self, message)
        self.errno = 2
        self.data = data


class BadLine(StudentsDataException):
    def __init__(self, data, line: str, message):
        Exception.__init__(self, data, message)
        self.line = line
        self.errno = 3


class FileEmpty(StudentsDataException):
    def __init__(self, data, file_name: str, message):
        Exception.__init__(self, data, message)
        self.file_name = file_name
        self.errno = 3
