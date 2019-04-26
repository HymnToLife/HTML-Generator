import json

import pymysql

conn = pymysql.connect(host="192.168.2.117", port=3306, user="hhh", passwd="123456", db="mydb")

cur = conn.cursor()

cur.execute("select tag from style")
numbers = len(cur.fetchall())

j = 0

while j < numbers:
    cur.execute("SELECT title FROM Style")

    title = str(cur.fetchall()[j][0])

    cur.execute("SELECT subtitle FROM Style")

    subtitle = str(cur.fetchall()[j][0])

    cur.execute("SELECT profilephoto FROM Style")

    profilePhoto = str(cur.fetchall()[j][0])

    cur.execute("SELECT author FROM Style")

    author = str(cur.fetchall()[j][0])

    cur.execute("SELECT date FROM Style")

    date = str(cur.fetchall()[j][0])

    cur.execute("SELECT text_json FROM Style")

    text_json = json.loads(cur.fetchall()[j][0])
    # print(text_json)


    message = """
    <html>
    <head></head>
    <body>
    """

    message = message + "<div class=\"content-head\">\n<h1>" + title + "</h1>\n" + "<h2>" + subtitle + \
              "</h2>\n</div>\n" + "<div class=\"content-info-pic\"><img src=\"" + profilePhoto + \
              "\" alt=\"\">\n</div>\n" + "<div class=\"content-info-author\"><span>" + author + "</span>\n</div>\n" + \
              "<div class=\"content-info-date\"><time datetime=\"" + date + "\">" + date + "</time>\n</div>\n" + \
              "<div class=\"content-body\">\n"

    # print(len(text_json))

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
        elif key == "li":
            if str(text_json[i-1].keys())[12:-3] != "li":
                message = message + "<ul>\n<li>" + value + "</li\n"
            elif str(text_json[i-1].keys())[12:-3] == "li" and str(text_json[i+1].keys())[12:-3] == "li":
                message = message + "<li>" + value + "</li>\n"
            else:
                message = message + "<li>" + value + "</li>\n</ul>\n"
        else:
            message = message + "<h2>" + value + "</h2>\n"

        i = i + 1

    message = message + """
    </div>
    </body>
    </html>"""

    file = open('/Users/hymntolife/desktop/test/web/' + str(j) +'.html', 'w')

    file.write(message)

    j = j + 1

cur.close()

conn.close()
