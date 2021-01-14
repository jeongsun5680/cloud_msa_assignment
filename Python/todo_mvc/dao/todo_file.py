#todos라는 데이터를 받아오는게 필요할듯!
import os.path
from entity.todo import Todo

def save_data(todos):
    save_file = open("C:/Users/OWNER/Desktop/cloud_msa/cloud_msa_assignment/Python/todo_mvc/todo_data.txt","w")
    for i in range(len(todos)) :
        save_file.write("{}|{}\n".format(todos[i].todoNum, todos[i].content))
    save_file.close()

def load_data():
    todos = []
    fileExist = os.path.isfile("C:/Users/OWNER/Desktop/cloud_msa/cloud_msa_assignment/Python/todo_mvc/todo_data.txt")
    if fileExist:
        read_file = open("C:/Users/OWNER/Desktop/cloud_msa/cloud_msa_assignment/Python/todo_mvc/todo_data.txt", "r")
        while True:
            data = read_file.readline()
            if len(data.split(sep='|'))==2:
                todo = data.split(sep='|')
                todos.append(Todo(todo[0], todo[1].strip("\n")))
            if not data : break
        read_file.close()
    return todos