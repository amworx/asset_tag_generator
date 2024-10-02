import mysql.connector
import os

def create_tables_and_insert_data():
    connection = mysql.connector.connect(
        host=os.getenv('MYSQL_HOST', 'localhost'),
        user=os.getenv('MYSQL_USER', 'root'),
        password=os.getenv('MYSQL_PASSWORD', 'toor'),
        database=os.getenv('MYSQL_DATABASE', 'db')
    )

    cursor = connection.cursor()

    # Create tables
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS asset_type (
        id INT AUTO_INCREMENT PRIMARY KEY,
        asset_name VARCHAR(255) NOT NULL,
        at_code VARCHAR(10) NOT NULL
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS building (
        id INT AUTO_INCREMENT PRIMARY KEY,
        building_name VARCHAR(255) NOT NULL,
        b_code VARCHAR(10) NOT NULL
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS department (
        id INT AUTO_INCREMENT PRIMARY KEY,
        department_name VARCHAR(255) NOT NULL,
        ed_code VARCHAR(10) NOT NULL
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS position (
        id INT AUTO_INCREMENT PRIMARY KEY,
        position_name VARCHAR(255) NOT NULL,
        p_code VARCHAR(10) NOT NULL
    );
    ''')

    # Insert default data into asset_type
    cursor.execute('''
    INSERT INTO asset_type (asset_name, at_code) VALUES
    ('Access Point', 'APN'),
    ('CCTV IPC', 'IPC'),
    ('Firewall', 'FWL'),
    ('GSM Booster', 'GSM'),
    ('Laptop', 'LTP'),
    ('Monitor', 'MON'),
    ('NVR', 'NVR'),
    ('Phone', 'PHN'),
    ('POS', 'POS'),
    ('Printer', 'PRT'),
    ('Projector', 'PRO'),
    ('Router', 'RTR'),
    ('Switch', 'SWT'),
    ('Tablet', 'TAB'),
    ('Wireless Dish', 'WDS')
    ON DUPLICATE KEY UPDATE asset_name=VALUES(asset_name);
    ''')

    # Insert default data into building
    cursor.execute('''
    INSERT INTO building (building_name, b_code) VALUES
    ('Guest House', 'GHS'),
    ('Programs', 'PRG'),
    ('Quality', 'QLT'),
    ('Systems', 'SYS'),
    ('Warehouse Back', 'WHB'),
    ('Warehouse Front', 'WHF'),
    ('Warehouse Middle', 'WHM')
    ON DUPLICATE KEY UPDATE building_name=VALUES(building_name);
    ''')

    # Insert default data into department
    cursor.execute('''
    INSERT INTO department (department_name, ed_code) VALUES
    ('Access', 'ACC'),
    ('Accountability', 'ACT'),
    ('Area', 'ARE'),
    ('Bakeries', 'BAK'),
    ('Cargo', 'CRG'),
    ('CFM', 'CFM'),
    ('Communication', 'COM'),
    ('Compliance', 'CPL'),
    ('CVA', 'CVA'),
    ('Distribution', 'DIS'),
    ('Emergency', 'EMR'),
    ('Finance', 'FIN'),
    ('Fleet', 'FLT'),
    ('Food Security CVA & Basic Needs', 'FSB'),
    ('HR', 'HUM'),
    ('Hygiene', 'HYG'),
    ('Investigation', 'INV'),
    ('IT', 'ITC'),
    ('Logistic', 'LOG'),
    ('Markets', 'MKT'),
    ('Media', 'MED'),
    ('MEL', 'MEL'),
    ('MIS', 'MIS'),
    ('Nutrition', 'NUT'),
    ('Outreach', 'OUT'),
    ('Procurement', 'PRC'),
    ('Protection & Safeguarding', 'PRT'),
    ('Selection', 'SEL'),
    ('Shelter', 'SHL'),
    ('SME', 'SME'),
    ('Verification', 'VER'),
    ('WASH', 'WSH'),
    ('Spare', 'SPR')
    ON DUPLICATE KEY UPDATE department_name=VALUES(department_name);
    ''')

    # Insert default data into position
    cursor.execute('''
    INSERT INTO position (position_name, p_code) VALUES
    ('Assistant', 'AS'),
    ('Cleaner', 'CL'),
    ('Coordinator', 'CO'),
    ('Deputy Coordinator', 'DC'),
    ('Deputy Manager', 'DM'),
    ('Deputy Senior Coordinator', 'DS'),
    ('Guard', 'GD'),
    ('Manager', 'MG'),
    ('Officer', 'OF'),
    ('Senior Officer', 'SO'),
    ('Team Leader', 'TL'),
    ('Team Member', 'TM'),
    ('Worker', 'WK')
    ON DUPLICATE KEY UPDATE position_name=VALUES(position_name);
    ''')

    # Commit changes and close the connection
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    create_tables_and_insert_data()
