import sqlite3

def create_sqlite_table(dbname, headers, rows, primary_keys, table_name="data"):
    # Connect to SQLite database (creates it if it doesn't exist)
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()

    # Define column types (default to TEXT for all)
    columns = []
    for header in headers:
        col_type = "TEXT"
        columns.append(f'"{header}" {col_type}')  # Quote column names

    # Primary key constraint
    if primary_keys:
        pk = ", ".join([f'"{key}"' for key in primary_keys])
        pk_constraint = f", PRIMARY KEY ({pk})"
    else:
        pk_constraint = ""

    # Construct CREATE TABLE statement
    create_stmt = f'''
    CREATE TABLE IF NOT EXISTS "{table_name}" (
        {", ".join(columns)}
        {pk_constraint}
    );
    '''
    
    cursor.execute(create_stmt)

    # Prepare insert statement (quote column names)
    col_names = ', '.join(f'"{col}"' for col in headers)
    placeholders = ', '.join(['?'] * len(headers))
    insert_stmt = f'INSERT OR IGNORE INTO "{table_name}" ({col_names}) VALUES ({placeholders})'
    
    for row in rows:
        cursor.execute(insert_stmt, row)

    conn.commit()
    conn.close()
    print(f"Table '{table_name}' created in '{dbname}' and populated with {len(rows)} rows.")




def validateHeaders(cols:list):  # use to validate if the headers are valid to be headers in sqlite.

    if len(cols) == len(set(cols)): # checks if headers are not duplicate
        for col in cols:
            try:
                int(col)
                return False         # header can't be an integer
            except ValueError:  
                continue
        return True 
    else:
        return False

def potentialPrimaryKeys(data:list, cols:list): # use to find the potential primary keys.
    n, l = len(cols), len(data)
    p, q = 0, 0
    ppk, cache = [], []

    while p < n:
        if q < l:
            cache.append(data[q][p])
            q+=1
        else:
            if len(cache) == len(set(cache)):
                ppk.append(cols[p])
            cache = []
            q = 0
            p+=1

    return ppk