import pymysql

pymysql.version_info = (1, 3, 13, "final", 0)
pymysql.install_as_MySQLdb()

# 测试用，这里打印出mysql的版本，显示在程序运行界面上

# db = pymysql.connect(host='localhost', user='root', password='89902528gmy',
#                      db='DR_detection_system')
#
# cursor = db.cursor()
#
# cursor.execute('SELECT VERSION()')
# data = cursor.fetchone()
# print('DATABASE VERSION IS: %s' % data)
#
# db.close()
