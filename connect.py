import MySQLdb
import os

for k in range(1,23):
	filepath = 'K:\phobius\\test-new-%d.txt'%k

	fp = open(filepath,'r')

	con= MySQLdb.connect(host='localhost',user='root',passwd='123456',db='protein')

	for line in fp.readlines():

		cursor =con.cursor()

		name = line.split()[2]

		TM = line.split()[3]

		SP = line.split()[4]
	
		tg = line.split()[5]
		#print name
		#print TM
		#print SP
		#print tg
		selecturl = "select * from pro where name = '%s'"%name
		sql ="insert into pro values ('%s','%s','%s','%s')"%(name,TM,SP,tg)
		print sql
		cursor.execute(selecturl)
        if (cursor.fetchone is None):
            cursor.execute(sql)
        cursor.close()
	con.commit()
	con.close()

o12-41i62-84o126-143i190-211o217-236i248-269o310-329i412-432o438-455i462-484o509-530i579-596o602-621i628-647o680-701i805-824o830-847i854-872o928-946i985-1007o1013-1029i1041-1063o1162-1180i1187-1206o1218-1240i1247-1264o1284-1302i1678-1697o1703-1722i1729-1747o1787-1806i1960-1983o2003-2022i2031-2052o2064-2081i2101-2121o2133-2152i2173-2197o2432-2455i