import csv
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
filename = "students.csv"

cursor = estd_connection()


with open(filename, "r") as cr:
    rows = csv.DictReader(cr)
    for each in rows:
        id = each["id"]
        name = each["name"]
        age = each["age"]
        address = each["address"]

        sql = f"""
        INSERT INTO STUDENT (ID, NAME, AGE, ADDRESS) values ('{id}', '{name}', '{age}', '{address}')
        """
        cursor.execute(sql)
        print("Student added successfully !")