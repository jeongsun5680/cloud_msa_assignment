from view.view import menuList, todoDisplay, inputTodo, updateContent, deleteContent
from entity.todo import Todo
from controller.controller import TodoController

controller = TodoController()

controller.file_read()

while True:
    controller.refresh()
    menu = menuList()
    if menu==0 :
        print("시스템을 종료합니다")
        controller.file_write()
        break
    elif menu==1 :
        todo = inputTodo()
        controller.register(todo)
    elif menu==2:
        todoDisplay(controller.getAllTodos())
    elif menu==3:
        index, content = updateContent()
        controller.update(index, content)
    elif menu==4:
        index = deleteContent()
        if index!=-1:
            controller.delete(index)
    else:
        pass