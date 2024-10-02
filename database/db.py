import mysql.connector

# Database connection function
def get_db_connection():
    connection = mysql.connector.connect(
        host='db',  # Docker service name
        user='root',
        password='toor',
        database='db'
    )
    return connection

# Fetch dropdown options for the form
def fetch_dropdown_options():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT Title FROM AssetType")
    asset_types = cursor.fetchall()

    cursor.execute("SELECT Title FROM Building")
    buildings = cursor.fetchall()

    cursor.execute("SELECT Title FROM Department")
    departments = cursor.fetchall()

    cursor.close()
    conn.close()

    return asset_types, buildings, departments

# Fetch code by title
def fetch_code_by_title(table, title):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"SELECT `code` FROM `{table}` WHERE Title = %s"
    cursor.execute(query, (title,))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return result[0] if result else None
