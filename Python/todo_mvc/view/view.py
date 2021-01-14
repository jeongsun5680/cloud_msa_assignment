from entity.todo import Todo
from service.service import TodoService

def menuList():
    print("===== Todo List System =====")
    print("1. 할일 입력")
    print("2. 할일 목록 조회")
    print("3. 할일 수정")
    print("4. 할일 삭제")
    print("0. 종료")
    while True:
        menu = input("번호를 입력하세요 : ")
        if not menu.isdecimal():
            print("0~4의 정수를 선택하세요")
        else:
            menu = int(menu)
            break
    return menu

def todoDisplay(todos):
    for todo in todos:
        print("{}. {}".format(todo.todoNum, todo.content))

def inputTodo():
    print("===== 1. 할일 입력 =====")
    content = input("content : ")
    service = TodoService()
    todoNum = len(service.todos)
    return Todo(todoNum, content)

def updateContent():
    print("===== 3. 할일 수정 =====")
    while True:
        index = input("수정할 항목의 번호 : ")
        service = TodoService()
        todos_len = len(service.todos)
        if (not index.isdecimal()) or (not int(index) in range(1,todos_len+1)):
            print("1부터 {}까지의 숫자 중 하나의 정수를 입력하세요".format(todos_len))
        else :
            content = input("수정할 내용 : ")
            return (index, content)

def deleteContent():
    print("===== 4. 할일 삭제 =====")
    while True:
        index = input("삭제할 항목의 번호 : ")
        service = TodoService()
        todos_len = len(service.todos)
        if (not index.isdecimal()) or (not int(index) in range(1,todos_len+1)):
            print("1부터 {}까지의 숫자 중 하나의 정수를 입력하세요".format(todos_len))
        else :
            break
    yn = input("정말 삭제하시겠습니까?[y,Y/n,N] : ")
    if yn in ['y', 'Y']:
        return index
    else:
        print("삭제가 취소되었습니다")
        return -1