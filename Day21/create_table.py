from estd_connection import estd_connection


cursor = estd_connection()

# cursor.execute("DROP TABLE STUDENT")

sql = """
CREATE TABLE STUDENT(
    ID CHAR(20),
    NAME CHAR(20),
    ADDRESS CHAR(20),
    AGE INT
)
"""

cursor.execute(sql)
print("Table created successfully !!")


# Types of databases
# SQL  (Structured Query Language)
# NOSQL (Not Only SQL) => In NoSQL we store data in document format.