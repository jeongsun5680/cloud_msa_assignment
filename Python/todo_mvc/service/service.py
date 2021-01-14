from dao.todo_file import save_data, load_data

class TodoService:
    todos=[]
    
    def register(self, todo):
        TodoService.todos.append(todo)

    def refresh(self):
        for i in range(len(TodoService.todos)):
            TodoService.todos[i].todoNum = i+1

    def getAllTodos(self):
        return TodoService.todos

    def update(self, index, content):
        TodoService.todos[int(index)-1].content = content

    def delete(self, index):
        TodoService.todos.pop(int(index)-1)

    def file_read(self):
        TodoService.todos = load_data()

    def file_write(self):
        save_data(TodoService.todos)