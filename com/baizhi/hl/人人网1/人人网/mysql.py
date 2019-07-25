import MySQLdb


def mysql_w(database):
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        password='123456',
        db=database,
        charset='utf8'
    )
    return conn

