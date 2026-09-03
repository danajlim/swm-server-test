class InvalidTodoTitleError(Exception):
    def __init__(self):
        super().__init__("Title Field Required")

class InvalidTodoDescriptionLengthError(Exception):
    def __init__(self):
        super().__init__("설명은 200자 이내로 입력해주세요.")

class DuplicateTodoTitleError(Exception):
    def __init__(self):
        super().__init__("Duplicate Title Field")