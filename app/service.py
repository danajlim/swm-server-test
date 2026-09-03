from app.exceptions import InvalidTodoDescriptionLengthError, InvalidTodoTitleError
from app.models import Todo, TodoValue
from app.repository import TodoRepository


class TodoService:
    def __init__(self, repository: TodoRepository):
        self.repository = repository

    def list(self, offset: int = 0, limit: int = 10) -> list[Todo]:
        return self.repository.list(offset, limit)

    def create(self, todo_value: TodoValue) -> Todo:
        if not todo_value.title:
            raise InvalidTodoTitleError()

        if todo_value.description and len(todo_value.description )> 200: 
            raise InvalidTodoDescriptionLengthError()

        return self.repository.create(todo_value)
