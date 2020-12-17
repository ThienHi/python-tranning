import psycopg2
from psycopg2 import Error
print("hello")

DB_HOST = "127.0.0.1"
DB_PASS = "123456"
DB_USER = "postgres"
DB_NAME = "postgres"


con = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                       password=DB_PASS, host=DB_HOST)

cur = con.cursor()

# cur.execute("CREATE TABLE student (id SERIAL PRIMARY KEY, name VARCHAR);")
# cur.execute("INSERT INTO student (name) VALUES(%s)", ("ThienHi",))
# cur.execute("INSERT INTO student (name) VALUES(%s)", ("Mi",))
# cur.execute("INSERT INTO student (name) VALUES(%s)", ("Tai9",))
# cur.execute("INSERT INTO student (name) VALUES(%s)", ("KhaiMe",))
# cur.execute("INSERT INTO student (name) VALUES(%s)", ("TaiChip",))

cur.execute("SELECT * FROM student;")

print(cur.fetchall())
con.commit()
cur.close()
con.close()
