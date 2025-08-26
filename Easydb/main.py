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

        def properties(self, row:bool = True, col: bool = True):
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
        
        def deleteData(self, del_all:bool = False, condition: dict = None ):
            """
            Deletes data from the table. Supports both unconditional (delete all) 
            and conditional deletion based on specified criteria.

            Parameters:
                dell_all (bool): Defaults to False. If True, deletes all data from the table.
                condition (dict): A dictionary specifying the condition for deletion. 
                                Used only if `dell_all` is False.

            Example:
                Condition format:
                {'COLUMN_NAME': 'Youraj Verma'}
            """

            if condition is not None:
                values = list(condition.values())
                keys = list(condition.keys())
                if not del_all:
                    if len(values) == len(keys):
                        try:
                            sql = f"DELETE FROM {self.table} WHERE {keys[0]} == ?"
                            self.cursor.execute(sql, values[0])
                            self.conn.commit()
                            self.conn.close()   
                        except sqlite3.OperationalError as e:
                            print("Unsuccessful Operation.", e)
                    else:
                        print("There must be only one condition.When dell_all is True then you must not provide other parameter!")
                else:
                    print("Operation Can't be Done!")

            if del_all is True:
                self.cursor.execute(f"DELETE FROM {self.table}")
                self.conn.commit()
                self.conn.close()
            else:
                print("Either give condition or set the del_all = True.")
            


                  


def main():
    pass

if __name__ == "__main__":
    main()