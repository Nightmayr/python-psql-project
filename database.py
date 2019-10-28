import psycopg2


def database_select():
    conn = psycopg2.connect(
        "dbname=test user=umayr host=rpi1 password=password")
    cur = conn.cursor()

    # Select all from database
    cur.execute("SELECT * FROM stuff;")
    rows = cur.fetchall()
    print(rows)

    cur.close()


def database_insert(json_map):
    conn = psycopg2.connect(
        "dbname=test user=umayr host=rpi1 password=password")
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO stuff (name, age, version) VALUES (%s, %s, %s)", ("umayr", 26, 1))
    conn.commit()


if __name__ == "__main__":
    database_select()
    database_select()
