import pyodbc

def ConnectSQL() :
    try :
        with pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=DESKTOP-M9UCNTP;"      # یا اسم سرور خودت
        "DATABASE=DbProducts;"       # اسم دیتابیس
        "Trusted_Connection=yes;"  # اتصال با ویندوز
            ) as db :
            return db
    except pyodbc.Error as eror:
        return 0

    # finally :
    #     db.commit()
    #     db.close()
