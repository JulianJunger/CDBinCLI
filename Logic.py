import json
import Hello

def create_fille():
    comp_py = {"Наименование компонента |" : "| Колличество"}
    with open("components.json", "w", encoding="utf-8") as f:
        json.dump(comp_py, f, indent=4, ensure_ascii=False)
    print("Файл с компонентами успешно создан!")

def look_components():
    with open("components.json", "r", encoding="utf=8") as f:
        data = json.load(f)
    for key, value in data.items():
           print(key, value)
           print("\n")
           
def create(name=str, count=int):
        file = open ("components.json", "r", encoding="utf-8")
        dict = json.load(file)
        file.close()
        name = input("\nВведите название компонента: ")
        count = int(input("Введите колличество компонентов: "))
        dict [name] = count
        file = open ("components.json", "w", encoding="utf-8")
        json.dump(dict, file, indent=4, ensure_ascii=False)
        file.close()
        print("\nКомпонент успешно добавлен!\n")
           
def add_component():
    create()
    cnt = int(input("Добавить еще компонент ?\n [1] - Добавить новый компонент\n [2] - Вернуться\n"))
    while cnt <= 2:
        if cnt > 2:
            print("Не ликвидное значение!")
            input(cnt)
        elif cnt == 1:
            create()
            input(cnt)
        elif cnt == 2:
            Hello.menu()

def change_file():
    inp_ch = int(input("\nКакие изменения вы бы хотели внести ?\n [1] - Удалить компонент\n [2] - Изменить значение компонента\n [3] - Вернуться в меню\n"))
    with open("components.json", "r", encoding="utf-8") as file:
            dict = json.load(file)
    if inp_ch == 1:
        name = input("Введите название компонента: ")
        del dict[name]
        with open("components.json", "w", encoding="utf-8") as file:
            json.dump(dict, file, indent=4, ensure_ascii=False)
        print(f"\nКомпонент {name} успешно удален!\n")
        Hello.menu()
    elif inp_ch == 2:
        name = input("Введите название компонента, который хотите изменить: ")
        val = int(input("Введите колличество компонента: "))
        dict[name] = val
        with open("components.json", "w", encoding="utf-8") as file:
            json.dump(dict, file, indent=4, ensure_ascii=False)
        Hello.menu()
    elif inp_ch == 3:
        Hello.menu()
        
        