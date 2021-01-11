# todoNum, content
todos = []
todoNum = 0

while True:
    print("===== Todo List System =====")
    print("1. 할일 입력")
    print("2. 할일 목록 조회")
    print("3. 할일 수정")
    print("4. 할일 삭제")
    print("0. 종료")
    menu = int(input("번호를 입력하세요 : "))
    print()

    for i in range(len(todos)):
        todos[i]["todoNum"] = i+1

    if(menu==1):
        print("===== 1. 할일 입력 =====")
        content = input("content : ")
        todoNum = len(todos)+1
        todos.append({"todoNum":todoNum, "content":content})
        print()
    elif(menu==2):
        print("===== 2. 할일 목록 조회 =====")
        for i in range(len(todos)):
            print("{}. {}".format(todos[i]["todoNum"], todos[i]["content"]))
        print()
    elif(menu==3):
        print("===== 3. 할일 수정 =====")
        todoNum = int(input("수정할 항목의 번호를 입력하세요 : "))
        print("수정 전 : {}".format(todos[todoNum-1]["content"]))
        content = input("수정할 내용을 입력하세요 : ")
        check = input("정말 수정하시겠습니까?(y,Y / n,N) : ")
        if check in ['y', 'Y'] : 
            print("수정 전 : {}".format(todos[todoNum-1]["content"]))
            todos[todoNum-1]["content"] = content
            print("수정 후 : {}".format(todos[todoNum-1]["content"]))
        else :
            print("수정이 취소되었습니다")
        print()
    elif(menu==4):
        print("===== 4. 할일 삭제 =====")
        todoNum = int(input("삭제할 항목의 번호를 입력하세요 : "))
        print("삭제할 내용 : {}".format(todos[todoNum-1]["content"]))
        check = input("정말 삭제하시겠습니까?(y,Y / n,N) : ")
        if check in ['y', 'Y'] : 
            del todos[todoNum-1]
            print("삭제되었습니다")
        else :
            print("삭제가 취소되었습니다")
        print()
    elif(menu==0):
        print("시스템을 종료합니다")
        print()
        break
    else:
        print("0~4번 중에 선택해주세요")
        print()