from tkinter import *
from tkinter import messagebox
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
        '''
        This function helps to change the UI of the app as per requirement. In one click we can switch
        from CSV to SQlite or SQlite to CSV
        '''
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
        '''
        This function also helps in changing the UI of the app. Depending on the situation weather you want to
        switch from Edit CSV file or Edit SQlite file.
        '''
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

    def validate_selection():

        '''
        This function helps in the valid selection of the DataTypes and properties.
        It ensures the proper combination of both of them.
        '''

        selected_type = data_types[data_type_var.get()] if data_type_var.get() >= 0 else None
        errors = []

        if auto_inc_var.get():
            if selected_type != 'INTEGER':
                errors.append("Auto Increment is only valid with INTEGER type.")
            if not primary_key_var.get():
                errors.append("Auto Increment must be used with Primary Key.")

        if errors:
            messagebox.showerror("Invalid Selection", "\n".join(errors))
            auto_inc_var.set(False)  # Reset Auto Increment if invalid

    
    def print_selection():

        '''
        Currently used to print the selected DataTypes and Properties. Soon It will be the main function 
        to add to the Tree View.
        '''

        if data_type_var.get() == -1:
            messagebox.showwarning("No Data Type", "Please select a data type.")
            return

        selection = [data_types[data_type_var.get()]] # gets the selection from the DataTypes.

        if primary_key_var.get():
            selection.append("PRIMARY KEY")
        if auto_inc_var.get():
            selection.append("AUTO INCREMENT")
        if not_null_var.get():
            selection.append("NOT NULL")

        print(selection)


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

    file_name_label = Label(option1_frame, text="No file choosen!", font=("poppins", 10), fg="green", bg="white", justify='left')
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

    file_name_to_edit_label = Label(file_select_frame, text="No file choosen!", font=("poppins", 10), fg="green", bg="white", justify='left')
    file_name_to_edit_label.pack(side='left', anchor='w', padx=4, pady=8)

    # Frame to edit the data. Tree View inside the edit frame

    edit_frame = Frame(edit_sqlite_frame, bg="white", relief='ridge', bd=2)
    edit_frame.propagate(False)
    edit_frame.pack(fill='both', expand=True, padx=4, pady=4, side='top', anchor='n')

    edit_label = Label(edit_frame, text="Select Sqlite file to see tree view!", font=("poppins", 18, 'bold'), fg="#4F39F6", bg="white")
    edit_label.place(relx=0.5, rely=0.5, anchor='center')

    # frame to create a sqlite table.

    create_sqlite_frame = Frame(feature_frame, bg="white")
    create_sqlite_frame.propagate(False)

    # Frame setup
    sqFrame1 = Frame(create_sqlite_frame, bg="white", relief='ridge', bd=2, width=480)
    sqFrame1.propagate(False)
    sqFrame1.pack(side='left', anchor='nw', padx=4, pady=4, fill=Y)

    # Configure grid columns
    sqFrame1.grid_columnconfigure(0, weight=1)
    sqFrame1.grid_columnconfigure(1, weight=2)

    # Row 0 - SQLite File Name
    db_name_label = Label(sqFrame1, text="Enter SQLite file name:", font=("poppins", 12), fg="black", bg="white")
    db_name_label.grid(row=0, column=0, sticky="w", padx=8, pady=8)

    db_name_entry_create = ctk.CTkEntry(sqFrame1, placeholder_text="Enter file name", font=("poppins", 14), height=35, border_color="#1447E6",
                                        width=200)
    db_name_entry_create.grid(row=0, column=1, padx=8, pady=8, sticky="ew")

    # Row 1 - Column Name
    column_name_label = Label(sqFrame1, text="Enter column name:", font=("poppins", 12), fg="black", bg="white")
    column_name_label.grid(row=1, column=0, sticky="w", padx=8, pady=8)

    column_name_entry = ctk.CTkEntry(sqFrame1, placeholder_text="Enter column name", font=("poppins", 14), height=35, border_color="#1447E6",
                                     width=200)
    column_name_entry.grid(row=1, column=1, padx=8, pady=8, sticky="ew")

    properties_label = Label(sqFrame1, text="Properties:", font=("poppins", 14, 'bold'), bg="white")
    properties_label.grid(row=2, column=0, padx=8, pady=8, sticky="w")

    properties_frame = ctk.CTkFrame(sqFrame1, fg_color="white", border_width=2, border_color="#1447E6", height=200)
    properties_frame.propagate(False)
    properties_frame.grid(row=3, column=0, padx=8, pady=8, sticky="ew", columnspan=2)

    # DataTypes
    data_types = ['INTEGER', 'TEXT', 'REAL', 'BLOB']
    data_type_var = IntVar(value=-1)  # No selection by default

    propFrame_1 = Frame(properties_frame, bg="white", relief='ridge', bd=2)
    propFrame_1.propagate(False)
    propFrame_1.pack(side='left', fill='both', expand=True, padx=4, pady=4)

    Label(propFrame_1, text="Data Types", bg="white", font=('Arial', 10, 'bold')).pack(pady=4)

    for i, dtype in enumerate(data_types):
        Radiobutton(propFrame_1, text=dtype,variable=data_type_var,value=i, bg="white", anchor='w', command=validate_selection).pack(fill='x', padx=10, pady=2)

    # Column Properties
    propFrame_2 = Frame(properties_frame, bg="white", relief='ridge', bd=2)
    propFrame_2.propagate(False)
    propFrame_2.pack(side='left', fill='both', expand=True, pady=4, padx=(0, 4))

    Label(propFrame_2, text="Column Properties", bg="white", font=('Arial', 10, 'bold')).pack(pady=4)

    # Property Variables
    primary_key_var = BooleanVar()
    auto_inc_var = BooleanVar()
    not_null_var = BooleanVar()

    Checkbutton(
        propFrame_2,
        text="Primary Key",
        variable=primary_key_var,
        bg="white"
    ).pack(anchor='w', padx=10, pady=2)

    Checkbutton(
        propFrame_2,
        text="Auto Increment",
        variable=auto_inc_var,
        bg="white",
        command=validate_selection # this function ensures no invalid selection.
    ).pack(anchor='w', padx=10, pady=2)

    Checkbutton(
        propFrame_2,
        text="NOT NULL",
        variable=not_null_var,
        bg="white"
    ).pack(anchor='w', padx=10, pady=2)


    add_to_tree_btn = ctk.CTkButton(sqFrame1, text="Addm to Tree", font=("poppins", 16, 'bold'), text_color="black", fg_color="#FFB86A", bg_color="white", border_color="#FF692A",
                                hover_color="#FF8904", height=35, border_width=2, command=print_selection)
    add_to_tree_btn.grid(row=4, column=0, columnspan=2, padx=8, pady=8, sticky="ew") # this button to add the data to tree view.

    sqFrame2 = Frame(create_sqlite_frame, bg="white", relief='ridge', bd=2, width=400)
    sqFrame2.pack(side='left', anchor='nw', pady=4, fill='both', expand=True)

    col_data_label = Label(sqFrame2, text="Add data to see tree view!", font=("poppins", 18, 'bold'), fg="#4F39F6", bg="white")
    col_data_label.place(relx=0.5, rely=0.5, anchor='center')

    
    add_data_to_db_frame = Frame(feature_frame, bg="grey")
    add_data_to_db_frame.propagate(False)

    modify_sqlite_frame = Frame(feature_frame, bg="purple")
    modify_sqlite_frame.propagate(False)
    

    win.mainloop()

if __name__ == "__main__":
    main()
