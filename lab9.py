import mysql.connector
import tkinter as tk

sql = mysql.connector.connect(
    host='localhost',
    user='root',
    password='152327se'
)
Cursor = sql.cursor()
Cursor.execute("CREATE DATABASE IF NOT EXISTS marvel")

sqlcn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='152327Se',
    database='marvel'
)
cursor = sqlcn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS movies(
                  ID int(3) NOT NULL,
                  Movie varchar(80) NOT NULL,
                  DateInfo varchar(50) NOT NULL,
                  Mcu_Phase varchar(20))''')

# 1
with open('marvel.txt', 'r') as file:
    next(file)  # Skip the header line
    for line in file:
        line = line.strip()
        data = line.split('\t')

        movie_id = int(data[0])
        movie_title = data[1]
        release_date = data[2]
        mcu_phase = data[3]

        # 2
        cnct = mysql.connector.connect(
            host='localhost',
            user='root',
            password='152327se',
            database='marvel'
        )
        cursor = cnct.cursor()

        # 3
        insert_query = """
            INSERT INTO movies (ID, Movie, DateInfo, Mcu_Phase)
            VALUES (%s, %s, %s, %s)
        """
        values = (movie_id, movie_title, release_date, mcu_phase)
        cursor.execute(insert_query, values)

        cnct.commit()
        cursor.close()
        cnct.close()

# 4
window = tk.Tk()
window.title('Marvel Movies Database')


# 5
def on_dropdown_select(event):
    selected_id = dropdown_var.get()
    text_box.delete('1.0', tk.END)
    text_box.insert(tk.END, f"Selected ID: {selected_id}")


label_dropdown = tk.Label(window, text='Select ID:')
label_dropdown.pack()

dropdown_var = tk.StringVar(window)
dropdown = tk.OptionMenu(window, dropdown_var, *range(1, 100), command=on_dropdown_select)
dropdown.pack()


# 6
def entry():
    entry_window = tk.Toplevel()
    entry_window.title('Please Add Entry')


button_add = tk.Button(window, text='Add', command=entry)
button_add.pack()

text_box = tk.Text(window)
text_box.pack()

window.mainloop()
