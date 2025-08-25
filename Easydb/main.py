import sqlite3
from typing import List, Tuple, Annotated
class Connection:
        """
        A class to interact with an SQLite database table.
        
        Attributes:
            conn (sqlite3.Connection): SQLite connection object.
            cursor (sqlite3.Cursor): SQLite cursor object.
            table (str): Name of the database table.
            rows (int): Number of rows in the table.
            cols (int): Number of columns in the table.
        """
        def __init__(self, des:str, table:str):
            """
            Initializes the connection to the SQLite database and retrieves table structure.

            Parameters:
                des (str): Path to the SQLite database file.
                table (str): Name of the table to connect to.

            If the table doesn't exist, sets rows and cols to 0 and prints an error message.
            """
            self.conn = sqlite3.connect(des)
            self.cursor = self.conn.cursor()
            self.table = table
            try:
                self.cursor.execute(f"SELECT * FROM {self.table}")
                data = self.cursor.fetchall()
                if data:
                    self.rows = len(data)
                    self.cols = len(data[0])
                else:
                    self.rows, self.cols = 0, 0
                       
            except sqlite3.OperationalError:
                self.rows, self.cols = 0, 0
                print(f"No such table:{self.table}")

        def properties(self, row:bool, col: bool):
            """
            Displays the number of rows and/or columns in the connected table.

            Parameters:
                row (bool): Whether to display the number of rows.
                col (bool): Whether to display the number of columns.
            """
            if row:
                print(f"Rows = {self.rows}", end=" ")
            if col:
                print(f"Columns = {self.cols}")

        def addData(self, items:tuple[list]):
            """
            Adds multiple rows of data to the table.

            Parameters:
                items (tuple[list]): A tuple containing lists, each representing a row to insert.

            The method checks if the number of values matches the number of columns before inserting.
            If not, it prints an error message.
            """
            self.cursor.execute("SELECT * FROM GEEK LIMIT 0;")
            col_name = tuple([description[0] for description in self.cursor.description])
            for item in items:
                try:
                    if len(item) == self.cols:
                        self.cursor.execute(f"INSERT INTO {self.table} {col_name} VALUES {tuple(item)}")
                    else:
                        print(f"Can't Add Item {item}")
                except TypeError:
                    print("items must be a tuple of list.")
                    
            self.conn.commit()
            
        def updateData(self, update_cols:list, update_vals:list, condition:dict):
            """
            Updates existing data in the table based on given conditions.

            Parameters:
                update_cols (list): List of column names to update.
                update_vals (list): List of new values corresponding to update_cols.
                condition (dict): A dictionary specifying the WHERE clause (column: value).

            If the number of columns and values don't match, it prints an error.
            """
            data = {
                "update": update_cols,
                "val": update_vals,
                "where": condition
            }

            if len(data["update"]) == len(data["val"]):
                set_clause = ", ".join(f"{col} = ?" for col in data["update"])

                # Build WHERE clause
                where_keys = data["where"].keys()
                where_clause = " AND ".join(f"{col} = ?" for col in where_keys)

                sql_query = f"UPDATE {self.table} SET {set_clause} WHERE {where_clause}"

                values = data["val"] + list(data["where"].values())
                self.cursor.execute(sql_query, values)
                self.conn.commit()
            else:
                print("The length of update_cols and update_vals are not equal!")
            
            self.conn.close()

                  


def main():
    pass

if __name__ == "__main__":
    main()