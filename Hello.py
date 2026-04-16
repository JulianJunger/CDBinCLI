import os
import Logic

menu_list = " [1] - Просмотреть список всех компонентов\n [2] - Добавить новый компонент\n [3] - Изменить список\n [4] - Завершить работу программы\n"

def hello():
    if os.path.exists("./components.json") == False:
            Logic.create_fille()
    print("\nЭто программа для учета компонентов лаборатории\n Чтобы вы хотели сделать ?\n")
    
def menu(**args):    
    print(menu_list)
    inp = int(input())
    while inp <= 4:
        if inp > 4:
            print("Не ликвидное значение! Поробуйте еще раз\n")
            menu()
        elif inp == 1:
            Logic.look_components()
            menu() 
        elif inp == 2:
            if os.path.exists("./components.json") == False:
                Logic.create_fille()
            Logic.add_component()
        elif inp == 3:
            Logic.change_file()
        elif inp == 4:
            exit()
        break    