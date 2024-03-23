import datetime
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from controller.DB import DBPlayerController
from controller.PlayerDto import PlayerDto
from controller.XML import XmlPlayerController
from model.entity.Player import Player

db_player_controller: DBPlayerController = DBPlayerController()
xml_player_controller: XmlPlayerController = XmlPlayerController("C:/Users/Daniil/PycharmProjects/ppois-2-2024/lab2"
                                                                 "/players.xml")
is_database = True
data = db_player_controller.get_all()


def show_error(message):
    messagebox.showerror("Ошибка", message)


def save():
    if messagebox.askyesno("Сохранение", "Вы хотите сохранить изменения?"):
        db_player_controller.save_db()
        xml_player_controller.save()


def on_exit():
    if messagebox.askyesno("Выход", "Вы хотите выйти из приложения?"):
        root.destroy()


def validate_input(full_name, birth_date_str, football_team, home_city, team_size_str, position):
    # Проверка full_name
    if not full_name.strip():
        show_error("Ошибка: Поле 'full_name' не должно быть пустым.")
        return False

    # Проверка birth_date
    try:
        datetime.datetime.strptime(birth_date_str, "%Y-%m-%d")
    except ValueError:
        show_error("Ошибка: Некорректный формат даты. Используйте формат 'YYYY-MM-DD'.")
        return False

    # Проверка football_team, home_city, position
    if not football_team.strip():
        show_error("Ошибка: Поле 'football_team' не должно быть пустым.")
        return False
    if not home_city.strip():
        show_error("Ошибка: Поле 'home_city' не должно быть пустым.")
        return False
    if not position.strip():
        show_error("Ошибка: Поле 'position' не должно быть пустым.")
        return False

    # Проверка team_size
    team_size_str = team_size_str.strip()
    if not team_size_str.isdigit():
        show_error("Ошибка: Поле 'team_size' должно содержать только цифры.")
        return False

    return True


def display_players():
    global current_page, records_per_page, treeview, data

    # Очищаем все данные в таблице перед обновлением
    for row in treeview.get_children():
        treeview.delete(row)

    # Определяем, откуда получать данные: из базы данных или из XML
    if is_database:
        # Получаем данные из базы данных
        data = db_player_controller.get_all()
    else:
        data = xml_player_controller.get_all_players()

    # Добавляем данные в таблицу
    start = (current_page - 1) * records_per_page
    end = start + records_per_page
    for player in data[start:end]:
        record = (
            player.id, player.full_name, player.birth_date, player.football_team, player.home_city, player.team_size,
            player.position)
        treeview.insert("", "end", values=record)


def calculate_total_pages():
    global records_per_page, data
    return -(-len(data) // records_per_page)


def prev_page():
    global current_page
    if current_page > 1:
        current_page -= 1
        display_players()
        update_page_info()


def next_page():
    global current_page
    total_pages = calculate_total_pages()
    if current_page < total_pages:
        current_page += 1
        display_players()
        update_page_info()


def first_page():
    global current_page
    current_page = 1
    display_players()
    update_page_info()


def last_page():
    global current_page
    total_pages = calculate_total_pages()
    if current_page != total_pages:
        current_page = total_pages
        display_players()
        update_page_info()


def change_records_per_page():
    global records_per_page
    try:
        new_records_per_page = int(records_per_page_entry.get())
        if new_records_per_page > 0:
            records_per_page = new_records_per_page
            display_players()
            update_page_info()
    except ValueError:
        pass


def update_page_info():
    global current_page, records_per_page, treeview
    total_pages_label.config(text="Total Pages: {}".format(calculate_total_pages()))
    current_page_label.config(text="Current Page: {}".format(current_page))
    records_per_page_label.config(text="Records per Page: {}".format(records_per_page))
    total_records_label.config(text="Total Records: {}".format(calculate_total_records()))


def calculate_total_records():
    return len(data)


def set_is_database_true():
    global is_database
    is_database = True
    first_page()


def set_is_database_false():
    global is_database
    is_database = False
    first_page()


def create_player():
    # Создаем новое диалоговое окно
    dialog = tk.Toplevel(root)
    dialog.title("Create Player")
    dialog.grab_set()  # Блокируем доступ к другим окнам

    # Добавляем метки и поля ввода для данных игрока
    full_name_label = ttk.Label(dialog, text="Full Name:")
    full_name_label.grid(row=0, column=0, padx=5, pady=5)
    full_name_entry = ttk.Entry(dialog)
    full_name_entry.grid(row=0, column=1, padx=5, pady=5)

    birth_date_label = ttk.Label(dialog, text="Birth Date (YYYY-MM-DD):")
    birth_date_label.grid(row=1, column=0, padx=5, pady=5)
    birth_date_entry = ttk.Entry(dialog)
    birth_date_entry.grid(row=1, column=1, padx=5, pady=5)

    football_team_label = ttk.Label(dialog, text="Football Team:")
    football_team_label.grid(row=2, column=0, padx=5, pady=5)
    football_team_entry = ttk.Entry(dialog)
    football_team_entry.grid(row=2, column=1, padx=5, pady=5)

    home_city_label = ttk.Label(dialog, text="Home City:")
    home_city_label.grid(row=3, column=0, padx=5, pady=5)
    home_city_entry = ttk.Entry(dialog)
    home_city_entry.grid(row=3, column=1, padx=5, pady=5)

    team_size_label = ttk.Label(dialog, text="Team Size:")
    team_size_label.grid(row=4, column=0, padx=5, pady=5)
    team_size_entry = ttk.Entry(dialog)
    team_size_entry.grid(row=4, column=1, padx=5, pady=5)

    position_label = ttk.Label(dialog, text="Position:")
    position_label.grid(row=5, column=0, padx=5, pady=5)
    position_entry = ttk.Entry(dialog)
    position_entry.grid(row=5, column=1, padx=5, pady=5)

    def save_player():
        # Получаем значения из полей ввода
        full_name: str = full_name_entry.get()
        birth_date: str = birth_date_entry.get()
        football_team: str = football_team_entry.get()
        home_city: str = home_city_entry.get()
        team_size: str = team_size_entry.get()
        position: str = position_entry.get()

        if validate_input(full_name, birth_date, football_team, home_city, team_size, position):
            team_size: int = int(team_size_entry.get())
            birth_date: datetime.date = datetime.datetime.strptime(birth_date, "%Y-%m-%d").date()
            if is_database is True:
                # Создаем новый объект игрока
                new_player = PlayerDto(full_name=full_name, birth_date=birth_date, football_team=football_team,
                                       home_city=home_city, team_size=team_size, position=position, id=None)
                # Добавляем игрока в базу данных
                db_player_controller.create(new_player)
            else:
                new_player = Player(full_name=full_name, birth_date=birth_date, football_team=football_team,
                                    home_city=home_city, team_size=team_size, position=position, id=None)
                xml_player_controller.insert(new_player)
            # Выводим сообщение об успешном добавлении
            messagebox.showinfo("Успех!", f"Игрок успешно создан!.")
            dialog.destroy()

    # Кнопка "Сохранить игрока"
    save_button = ttk.Button(dialog, text="Save Player", command=save_player)
    save_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)


root = tk.Tk()
root.title("Library App")
root.geometry('1470x720')

# Создаем меню
menu_bar = tk.Menu(root)

# Создаем меню "File" и добавляем в него пункты
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open a db file", command=set_is_database_true)
file_menu.add_command(label="Open an XML file", command=set_is_database_false)
file_menu.add_command(label="Save file", command=save)
file_menu.add_command(label="Exit", command=on_exit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Создаем панель инструментов
toolbar = tk.Frame(root, bd=1, relief=tk.RAISED)
toolbar.pack(side=tk.TOP, fill=tk.X)

# Кнопка "Create Player"
create_button = ttk.Button(toolbar, text="Create Player", command=create_player)
create_button.pack(side=tk.LEFT, padx=2, pady=2)

# Устанавливаем меню приложения
root.config(menu=menu_bar)

# Создаем фреймы для кнопок навигации и информации
navigation_frame = tk.Frame(root)
navigation_frame.pack()

info_frame = tk.Frame(root)
info_frame.pack()

columns = ("ID", "Full Name", "Birth Date", "Football Team", "Home City", "Team Size", "Position")
column_widths = (100, 150, 100, 120, 100, 80, 100)  # Ширина каждого столбца

current_page = 1
records_per_page = 10

# Кнопки навигации
prev_button = tk.Button(navigation_frame, text="Previous", command=prev_page)
prev_button.pack(side=tk.LEFT)

next_button = tk.Button(navigation_frame, text="Next", command=next_page)
next_button.pack(side=tk.LEFT)

first_button = tk.Button(navigation_frame, text="First", command=first_page)
first_button.pack(side=tk.LEFT)

last_button = tk.Button(navigation_frame, text="Last", command=last_page)
last_button.pack(side=tk.LEFT)

# Надписи с информацией
total_records_label = tk.Label(info_frame, text="Total Records: {}".format(calculate_total_records()))
total_records_label.pack()

total_pages_label = tk.Label(info_frame, text="Total Pages: {}".format(calculate_total_pages()))
total_pages_label.pack()

current_page_label = tk.Label(info_frame, text="Current Page: {}".format(current_page))
current_page_label.pack()

records_per_page_label = tk.Label(info_frame, text="Records per Page: {}".format(records_per_page))
records_per_page_label.pack()

records_per_page_entry = tk.Entry(info_frame)
records_per_page_entry.pack(side=tk.LEFT)
records_per_page_entry.insert(0, "10")

change_records_per_page_button = tk.Button(info_frame, text="Change", command=change_records_per_page)
change_records_per_page_button.pack(side=tk.LEFT)

treeview = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    treeview.heading(col, text=col)
    treeview.column(col, anchor="center")
treeview.pack()

display_players()

root.mainloop()
