import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="market"
)

def insert(code, name, price, stock):
    cursor = database.cursor()
    cursor.execute(
        '''INSERT INTO barang (code, name, price, stock)
        VALUES (%s,%s, %s, %s)''', (code, name, price, stock)
        )
    database.commit()

    if cursor.rowcount > 0:
        return
    else:
        print('\nTidak ada yang disave!')
        
def fetch_item():
    cursor = database.cursor()
    cursor.execute("SELECT * FROM barang")
    return cursor.fetchall()