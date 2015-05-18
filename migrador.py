# -*- coding: utf-8 -*-
import MySQLdb


# Establecemos la conexión con la base de datos
bd = MySQLdb.connect("localhost", "dequr", "DequR2014@", "new")
bd2 = MySQLdb.connect("localhost", "dequr", "DequR2014@", "dequr")

cursor = bd.cursor()
cursor2 = bd2.cursor()

cursor.execute("SELECT * FROM Companies")

# Extraemos una sola fila usando el método fetchone()
resultados = cursor.fetchall()
for registro in resultados:
    print registro[4]
    column = str(MySQLdb.escape_string(registro[4]))
    sql = "INSERT INTO company_subcompany (id, company_id, name) VALUES (NULL, NULL, '%s')" % column
    cursor2.execute(sql)
    bd2.commit()
    #r = raw_input()

# Nos desconectamos de la base de datos
bd.close()
bd2.close()
