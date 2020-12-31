import mysql.connector


connection = mysql.connector.connect(host="127.0.0.1", database="addressbook", user="root", password="")

# try:
#     cursor = connection.cursor()
#     cursor.execute("select * from group_list")
#     for row in cursor.fetchall():
#         print(row)
# finally:
#     connection.close()

try:
    c = connection.cursor()
    c.execute("select group_name from group_list where group_id > 100 and group_id < 700")
    for row in c.fetchall():
        print(row)
finally:
    connection.close()



