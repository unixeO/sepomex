import csv
import os
dirname = os.path.dirname(os.path.abspath(__file__))


with open(dirname + '/CPdescarga.txt', newline='', encoding="latin-1") as csvfile:
	reader = csv.reader(csvfile, delimiter='|')
	for row in reader:
		values = '\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\''.format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7], row[8],row[9],row[10],row[11],row[12],row[13], row[14])
		query = 'INSERT into sepomex(d_codigo, d_asenta, d_tipo_asenta, D_mnpio, d_estado, d_ciudad, d_CP, c_estado, c_oficina, c_CP, c_tipo_asenta, c_mnpio, id_asenta_cpcons, d_zona, c_cve_ciudad) VALUES (' + values + ');'
		f = open(dirname + "sepomex.sql", "a")
		f.write(query + '\n')
	f.close()

