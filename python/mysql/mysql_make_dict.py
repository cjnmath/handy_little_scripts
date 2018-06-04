import mysql.connector

config ={
    'user': 'jc',
    'password': 'aller',
    'host': '127.0.0.1',
    'port': 3306,
    'raise_on_warnings': True
}

cnx = mysql.connector.connect(database='douban_imdb_rating', **config)

cursorA = cnx.cursor(buffered=True)
cursorB = cnx.cursor(buffered=True)

REGIONS = {	'CN': '大陆', 'US': '美国', 'HK': '香港', 'TW': '台湾',
            'JP': '日本', 'KR': '韩国', 'UK': '英国','FR': '法国',
			'DE': '德国', 'IT': '意大利', 'ES': '西班牙', 'IN': '印度',
			'TH': '泰国', 'RU': '俄罗斯', 'IR': '伊朗', 'CA': '加拿大',
			'AU': '澳大利亚', 'IE': '爱尔兰', 'SE':'瑞典', 'BR': '巴西',
			'DK': '丹麦'}

make_table = """
    CREATE TABLE region_name_acronym(
    region_id CHAR(2),
    region_name TEXT
    )ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""
cursorA.execute(make_table)

sql = """
INSERT INTO region_name_acronym (region_id, region_name)
VALUES (%s, %s);
"""
for region_id, region_name in REGIONS.items():
    # print(region_id, region_name)
    cursorB.execute(sql, (region_id, region_name))


cnx.commit()
cursorA.close()
cursorB.close()
cnx.close()
