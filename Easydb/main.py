from tkinter import *
from ttk import Treeview
import customtkinter as ctk
from importlib.resources import files
import assets.logo
import csv

def main():

    def clickedButton(name: str):
        # Hide all child widgets in the feature_frame
        for widget in feature_frame.winfo_children():
            widget.pack_forget()

        # Dictionary maps names to frame references, NOT to .pack() calls
        button_dict = {
            "csv_to_db_btn": csv_to_sqlite_frame,
            "edit_db_btn": edit_sqlite_frame,
            "create_db_btn": create_sqlite_frame,
            "add_data_to_db_btn": add_data_to_db_frame,
            "modify_db_btn": modify_sqlite_frame,
        }

        # Get the frame for the button and pack it
        frame_to_show = button_dict.get(name)
        if frame_to_show:
            frame_to_show.pack(fill='both', expand=True, padx=2, pady=2)

    def checkbox_operations(selected):
        if selected == "A":
            if checkbox_csv_to_db.get():
                checkbox_db_to_csv.deselect()
                choose_file_btn.configure(text = "Choose CSV file")
                db_name_entry.configure(placeholder_text = "Enter Sqlite name")
                opt_checkbox.configure(text = "Same as CSV file")
                tree_label.config(text="Select CSV file to see tree view!")
            else:
                checkbox_csv_to_db.select()
        elif selected == "B":
            if checkbox_db_to_csv.get():
                checkbox_csv_to_db.deselect()
                choose_file_btn.configure(text = "Choose Sqlite file")
                db_name_entry.configure(placeholder_text = "Enter CSV file name")
                opt_checkbox.configure(text = "Same as SQlite file")
                tree_label.config(text="Select SQlite file to see tree view!")
            else:
                checkbox_csv_to_db.select()
                choose_file_btn.configure(text = "Choose CSV file")
                db_name_entry.configure(placeholder_text = "Enter Sqlite name")
                opt_checkbox.configure(text = "Same as CSV file")
                tree_label.config(text="Select CSV file to see tree view!")
            
    def checkbox_edit_ops(selected):
        if selected == "A":
            if checkbox_edit_sqlite.get():
                checkbox_edit_csv.deselect()
                choose_file_to_edit_btn.configure(text = "Choose SQlite file")
                edit_label.config(text="Select Sqlite file to see tree view!")
            else:
                checkbox_edit_sqlite.select()
        elif selected == "B":
            if checkbox_edit_csv.get():
                checkbox_edit_sqlite.deselect()
                choose_file_to_edit_btn.configure(text = "Choose CSV file")
                edit_label.config(text="Select CSV file to see tree view!")
            else:
                checkbox_edit_sqlite.select()
                choose_file_to_edit_btn.configure(text = "Choose SQlite file")
                edit_label.config(text="Select Sqlite file to see tree view!")

    win = Tk()
    win.geometry("1440x680+10+10")
    win.title("EasyDB")
    icon_path = icon_path = files(assets.logo).joinpath("logo.ico")
    win.iconbitmap(icon_path)

    # main body frame --> It will hold all the content.

    main_frame = Frame(win, bg="#51A2FF")
    main_frame.pack(fill='both', expand=True)

    # Tab Frame -> To switch between the different features.

    tab_frame = ctk.CTkFrame(main_frame, bg_color="#51A2FF", fg_color="white", border_color="#1447E6", border_width=2, height=48)
    tab_frame.propagate(False)
    tab_frame.pack(side='top', fill='x', padx=8, pady=(8, 4), anchor='n')

    # Add multiple buttons for switching between the tabs

    csv_to_db_btn = ctk.CTkButton(tab_frame, text="CSV to Sqlite", text_color="black", font=("poppins", 14, 'bold') ,fg_color="#7BF1A8", hover_color="#05DF72",
                                  border_color="#2AA63E", border_width=2, corner_radius=10, command=lambda name = "csv_to_db_btn":clickedButton(name))
    csv_to_db_btn.pack(side = 'left', padx = 8)

    edit_db_btn = ctk.CTkButton(tab_frame, text="Edit Sqlite", text_color="black", font=("poppins", 14, 'bold') ,fg_color="#7BF1A8", hover_color="#05DF72",
                                  border_color="#2AA63E", border_width=2, corner_radius=10, command=lambda name = "edit_db_btn":clickedButton(name))
    edit_db_btn.pack(side = 'left', padx = 8)

    create_db_btn = ctk.CTkButton(tab_frame, text="Create Sqlite", text_color="black", font=("poppins", 14, 'bold') ,fg_color="#7BF1A8", hover_color="#05DF72",
                                  border_color="#2AA63E", border_width=2, corner_radius=10, command=lambda name = "create_db_btn":clickedButton(name))
    create_db_btn.pack(side = 'left', padx = 8)

    add_data_to_db_btn = ctk.CTkButton(tab_frame, text="Add data to Sqlite", text_color="black", font=("poppins", 14, 'bold') ,fg_color="#7BF1A8", hover_color="#05DF72",
                                  border_color="#2AA63E", border_width=2, corner_radius=10, command=lambda name = "add_data_to_db_btn":clickedButton(name))
    add_data_to_db_btn.pack(side = 'left', padx = 8)

    modify_db_btn = ctk.CTkButton(tab_frame, text="Modify Sqlite", text_color="black", font=("poppins", 14, 'bold') ,fg_color="#7BF1A8", hover_color="#05DF72",
                                  border_color="#2AA63E", border_width=2, corner_radius=10, command=lambda name = "modify_db_btn":clickedButton(name))
    modify_db_btn.pack(side = 'left', padx = 8)

    # Feature Frame (just below tab frame)

    feature_frame = ctk.CTkFrame(main_frame, bg_color="#51A2FF", fg_color="white", border_color="#1447E6", border_width=2)
    feature_frame.propagate(False)
    feature_frame.pack(side='top', fill='both', expand=True, padx=8, pady=(0, 8), anchor='n')


    # Frame for csv to sqlite 

    csv_to_sqlite_frame = Frame(feature_frame, bg="white")

    # tree frame to show data of the csv file in tabular form

    tree_frame = Frame(csv_to_sqlite_frame, bg="white", height=440, relief='ridge', bd=2)
    tree_frame.pack(fill=X, side='top', anchor='n', pady=4, padx=4, ipady=0)

    tree_label = Label(tree_frame, text="Select CSV file to see tree view!", font=("poppins", 18, 'bold'), fg="#4F39F6", bg="white")
    tree_label.place(relx=0.5, rely=0.5, anchor='center')

    # this frame is for chooing file, updates and inputs

    options_frame = Frame(csv_to_sqlite_frame, bg="white", relief='ridge', bd=2)
    options_frame.propagate(False)
    options_frame.pack(fill='both', expand=True, side='top', anchor='n', pady=(0, 4), padx=4, ipady=0)

    # Special Frame for only for fething file and display it's location.

    option1_frame = Frame(options_frame, bg="white", width=520)
    option1_frame.propagate(False)
    option1_frame.pack(side = 'left', fill=Y, pady=2, padx=(2, 0))
    choose_file_btn = ctk.CTkButton(option1_frame, text="Choose CSV File", font=("poppins", 14, 'bold'), text_color="black", bg_color="white",
                                    fg_color="#FFB86A", hover_color="#FF8904", border_color="#F54927", border_width=1, corner_radius=10,
                                    height=40,width=150)
    choose_file_btn.pack(side = 'top', anchor = 'nw', padx = 4, pady = 4)

    file_name_label = Label(option1_frame, text="Hello World this is a file to grow the area of the sub urban company and mcuh more", font=("poppins", 10), fg="green", bg="white", justify='left')
    file_name_label.pack(side='top', anchor='nw', padx=4)

    checkbox_csv_to_db = ctk.CTkCheckBox(option1_frame, text="CSV to SQlite", command=lambda: checkbox_operations("A"),
                                         fg_color="#FF8904", hover_color="#FFB86A")
    checkbox_csv_to_db.pack(side='top', anchor='nw', padx=4, pady = 8)
    checkbox_db_to_csv = ctk.CTkCheckBox(option1_frame, text="SQlite to CSV", command=lambda: checkbox_operations("B"),
                                         fg_color="#FF8904", hover_color="#FFB86A")
    checkbox_db_to_csv.pack(side='top', anchor='nw', padx=4)
    
    checkbox_csv_to_db.select()
    # frame for other activities on CSV file

    option2_frame = Frame(options_frame, bg="white")
    option2_frame.pack(side = 'left', fill='both', expand=True, pady=2, padx=(0, 2))

    # Input entry
    db_name_entry = ctk.CTkEntry(option2_frame, placeholder_text="Enter Sqlite name", font=("poppins", 12), height=40, border_color="#1447E6")
    db_name_entry.grid(row=0, column=0, padx=(10, 5), pady=10, sticky="ew")

    # Checkbox
    opt_checkbox_var = ctk.BooleanVar()
    opt_checkbox = ctk.CTkCheckBox(option2_frame, text="Same as CSV file", variable=opt_checkbox_var)
    opt_checkbox.grid(row=0, column=1, padx=(5, 10), pady=10, sticky="w")

    # potential_label
    potential_label = ctk.CTkLabel(option2_frame, text="Potential Primary Keys", font=("poppins", 14, 'bold'))
    potential_label.grid(row=1, column=0, padx=(10, 2), pady=10, sticky="w")

    # Dropdown
    opt_dropdown_var = ctk.StringVar(value="Choose")
    value = ["Fist Choose the File"]
    opt_dropdown = ctk.CTkOptionMenu(option2_frame, values=value, variable=opt_dropdown_var, text_color="black", fg_color="#FFB86A", dropdown_hover_color="#FFD6A7")
    opt_dropdown.grid(row=1, column=1, padx=(2, 10), pady=10, sticky="ew")

    # Save Button
    db_save_button = ctk.CTkButton(option2_frame, text="Save", font=("poppins", 16, 'bold'), text_color="black", fg_color="#FFB86A", bg_color="white", border_color="#FF692A",
                                hover_color="#FF8904", height=35, border_width=2)
    db_save_button.grid(row=2, column=0, columnspan=2, padx=10, pady=(2, 2), sticky="ew")

    # Optional: Make columns expand with weight if you're using grid layout
    option2_frame.grid_columnconfigure(0, weight=1)
    option2_frame.grid_columnconfigure(1, weight=1)

    # Complete frame to edit and manipulate data (SQlite and CSV)

    edit_sqlite_frame = Frame(feature_frame, bg="white")
    edit_sqlite_frame.propagate(False)
    
    # Area to select file for edit 

    file_select_frame = Frame(edit_sqlite_frame, height=50, relief='ridge', bd=2)
    file_select_frame.propagate(False)
    file_select_frame.pack(fill=X, side='top', anchor='n', padx=4, pady=(4, 0))

    # checkbox
    
    checkbox_edit_sqlite = ctk.CTkCheckBox(file_select_frame, text="Edit SQlite", command=lambda: checkbox_edit_ops("A"),
                                         fg_color="#FF8904", hover_color="#FFB86A")
    checkbox_edit_sqlite.pack(side='left', anchor='w', padx=4, pady = 8)
    checkbox_edit_csv = ctk.CTkCheckBox(file_select_frame, text="Edit CSV", command=lambda: checkbox_edit_ops("B"),
                                         fg_color="#FF8904", hover_color="#FFB86A")
    checkbox_edit_csv.pack(side='left', anchor='w', padx=4, pady = 8)
    
    checkbox_edit_sqlite.select() 

    # choose file button

    choose_file_to_edit_btn = ctk.CTkButton(file_select_frame, text="Choose Sqlite File", font=("poppins", 14, 'bold'), text_color="black", bg_color="white",
                                    fg_color="#FFB86A", hover_color="#FF8904", border_color="#F54927", border_width=1, corner_radius=10,
                                    height=40,width=150)
    choose_file_to_edit_btn.pack(side = 'left', anchor = 'w', padx = 4, pady = 8)

    # label to display file name

    file_name_to_edit_label = Label(file_select_frame, text="Hello World this is a file to grow the area of the sub urban company and mcuh more", font=("poppins", 10), fg="green", bg="white", justify='left')
    file_name_to_edit_label.pack(side='left', anchor='w', padx=4, pady=8)

    # Frame to edit the data. Tree View inside the edit frame

    edit_frame = Frame(edit_sqlite_frame, bg="white", relief='ridge', bd=2)
    edit_frame.propagate(False)
    edit_frame.pack(fill='both', expand=True, padx=4, pady=4, side='top', anchor='n')

    edit_label = Label(edit_frame, text="Select Sqlite file to see tree view!", font=("poppins", 18, 'bold'), fg="#4F39F6", bg="white")
    edit_label.place(relx=0.5, rely=0.5, anchor='center')

    create_sqlite_frame = Frame(feature_frame, bg="yellow")
    create_sqlite_frame.propagate(False)

    add_data_to_db_frame = Frame(feature_frame, bg="grey")
    add_data_to_db_frame.propagate(False)

    modify_sqlite_frame = Frame(feature_frame, bg="purple")
    modify_sqlite_frame.propagate(False)
    

    win.mainloop()

if __name__ == "__main__":
    main()
