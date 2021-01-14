from service.service import TodoService
from view.view import menuList, todoDisplay

class TodoController:

    def register(self, todo):
        service = TodoService()
        service.register(todo)

    def refresh(self):
        service = TodoService()
        service.refresh()

    def getAllTodos(self):
        service = TodoService()
        return service.getAllTodos()

    def update(self, index, content):
        service = TodoService()
        service.update(index, content)

    def delete(self, index):
        service = TodoService()
        service.delete(index)

    def file_read(self):
        service = TodoService()
        service.file_read()

    def file_write(self):
        service = TodoService()
        service.file_write()