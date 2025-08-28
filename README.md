# EasyDB – Simplifying SQLite Operations in Python

**EasyDB** is a lightweight Python package designed to streamline common SQLite operations.  
If you've ever found yourself writing repetitive SQL statements just to insert dummy data or test your application during development, EasyDB is the solution for you.

With EasyDB, performing basic operations requires only a few lines of code. There's no need to memorize SQL syntax—just plug in your values and go.

---

## 🚀 Features

- Abstracts away raw SQL queries.
- Ideal for rapid development and testing with dummy data.
- Human-readable and beginner-friendly interface.

---

## 📦 Installation

1. Clone the repository or download the `.whl` (wheel) file.
2. Open your terminal and navigate to the directory containing the wheel file.
3. Install the package using pip:

```bash
pip install Easydb-1.0-py3-none-any.whl
```
- make sure that you run the above command in same directory in which the .whl file lies.

## 🔧 Getting Started

- Make sure that there already exist a **.db** file with a defined table.
- Then setup the connection as follows:
```python
c = Connection(des = FILE_PATH, table = TABLE_NAME)
# it will setup a connection with your database and its table for all operations.
```
- To check properties:
``` python
c.properties(row = True, col = True)
# it will print the number of rows and column in SQlite table
```
- To insert data in the table:
```python
c.addData(item = (['178 cm', '65 kg'], ['160 cm', '49kg']))
# you can easily insert data in database in this way.Just make sure that your lenth of column is equal to the length of the columns of the table.
```
- To update the data in the sqlite:
```python
c.updateData(update_cols=[LIST OF COLS TO UPDATE], update_vals=[LIST OF UPDATE VALUES], condition={YOUR_CONDITIONS})
# for example:
#k.updateData(update_cols=["NAME", "MARKS"], update_vals=["Abhinav", 80], condition={"ID":10}) 
# you can define condition as WHERE ID IS 10.
```
- To delete data from SQlite:
``` python
c.deleteData(dell_all = False, condition = {"ID":10})
#dell_all : bool
# Defaults to False. If True, deletes all data from the table.

# condition : dict
# A dictionary specifying the condition for deletion. Used only if dell_all is False.
```
## 🎯 Future Goals

- Easily convert CSV to SQllite.
- Update existing SQlite file from a csv.

## 🤝 Contribution Guidelines
- First create an issue or choose an open issue.
- Add a new branch as "fixes/fixes_name"
