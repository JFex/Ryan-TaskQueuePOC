import pyodbc
#import keyring

def insert_log(task_id,task_name,result,info,run_date):
    conn = pyodbc.connect('Driver=SQL Server;'
                      'Server=DATACURATION;'
                      'Database=Scratch;'
                      'Trusted_Connection=yes'
                      #'UID=PARADIGMTAX\jfeexico;'
                      #'PWD=' + keyring.get_password('windows', 'PARADIGMTAX\jfeexico')
    )

    cursor = conn.cursor()

    cursor.execute(f'''
                INSERT INTO task_log (task_id, task_name, result, info, run_date)
                VALUES ('{task_id}','{task_name}','{result}', '{info}', '{run_date}')
                ''')
    conn.commit()