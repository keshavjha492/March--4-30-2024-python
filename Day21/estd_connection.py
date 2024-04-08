def estd_connection():
    import psycopg2
    conn = psycopg2.connect(
        database = "studentdb",
        user ="postgres",
        password="12345678",
        port =5432
    )
    conn.autocommit= True
    print("connection established successfully")
    cursor = conn.cursor()
    return cursor


if __name__ == "__main__":
    estd_connection()