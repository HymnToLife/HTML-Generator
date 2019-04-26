import json

import pymysql

# import Generator

conn = pymysql.connect(host="192.168.2.117", port=3306, user="hhh", passwd="123456", db="mydb")

cur = conn.cursor()

j = 0

while j < 4:
    cur.execute("SELECT title FROM Style")

    title = str(cur.fetchall()[j][0])

    cur.execute("SELECT subtitle FROM Style")

    subtitle = str(cur.fetchall()[j][0])

    cur.execute("SELECT text_json FROM Style")

    text_json = json.loads(cur.fetchall()[j][0])

    message = """
    <html>
    <head></head>
    <body>
    """

    message = message + "<h1>" + title + "</h1>\n" + "<h2>" + subtitle + "</h2>\n"

    print(len(text_json))

    i = 0

    while i < len(text_json):
        keysD = text_json[i].keys()
        valuesD = text_json[i].values()
        value = str(valuesD)[14:-3]
        key = str(keysD)[12:-3]

        if key == "img":
            message = message + "<img src=\"" + value + "\" alt=\"\">\n"
        elif key == "p":
            message = message + "<p>" + value + "</p>\n"
        else:
            message = message + "<h2>" + value + "</h2>\n"

        i = i + 1

    message = message + """
    </body>
    </html>"""

    file = open('/Users/hymntolife/desktop/test/' + str(j) +'.html', 'w')

    file.write(message)

    j = j + 1

cur.close()

conn.close()
