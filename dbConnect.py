import os

import pymysql

conn = pymysql.connect(host="192.168.2.117", port=3306, user="hhh", passwd="123456", db="mydb")

cur = conn.cursor()

tableName = "Health"

cur.execute("SELECT tag FROM "+tableName)

numbers = len(cur.fetchall())

change_table = {
    '\\n': '<br>', "\\'": "'", '\\"': '"', '\\t': '<PRE>&#9</PRE>'
}

j = 0

def createmkdir(path):

    isExists = os.path.exists(path)

    if not isExists:

        os.mkdir(path)

        return True

    else:

        return False

dirpath = '/Users/hymntolife/desktop/test/' + tableName

createmkdir(dirpath)

while j < numbers:
    cur.execute("SELECT title FROM " + tableName)

    title = str(cur.fetchall()[j][0])

    cur.execute("SELECT subtitle FROM " + tableName)

    subtitle = str(cur.fetchall()[j][0])

    cur.execute("SELECT profilephoto FROM " + tableName)

    profilePhoto = str(cur.fetchall()[j][0])

    cur.execute("SELECT author FROM " + tableName)

    author = str(cur.fetchall()[j][0])

    cur.execute("SELECT date FROM " + tableName)

    date = str(cur.fetchall()[j][0])

    cur.execute("SELECT text_json FROM " + tableName)

    # print(cur.fetchall()[j][0])

    text_json = eval(cur.fetchall()[j][0])

    message = """
    <!doctype html>
    <html lang="en">
    <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://cdn.bootcss.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
       
    <link rel="stylesheet" type="text/css" href="../css/style.css" />
    <title >""" + title + """</title >
    </head>
    <body>
    <div class=\"container\">\n
    """

    message = message + "<div class=\"content-head\">\n<h1 class=\"content-hed\">" + title + "</h1>\n" + \
              "<h2 class=\"content-dek\">\n" + subtitle + "</h2>\n" + \
              "<div class=\"content-info\">" + \
              "<div id=\"content-info-author\" class=\"col-xs-6\"><small class=\"text-muted\">" + author +\
              "</small>\n</div>\n" + "<div id=\"content-info-date\" class=\"col-xs-6\"><small class=\"text-muted\">" \
              + date + "</small>\n</div>\n" + "</div>\n</div>" + "<div class=\"content-body\">\n"

    # print(len(text_json))
    # + "<div id=\"content-info-pic\" class=\"col-2\"><img src=\"" \
    # + profilePhoto + "\" class=\"img-fluid\" alt=\"Responsive image\" id=\"profilePhoto\">\n</div>\n"

    i = 0

    while i < len(text_json):
        keysD = text_json[i].keys()
        valuesD = str(text_json[i].values())
        for (k, v) in change_table.items():
            valuesD = valuesD.replace(k, v)
        value = valuesD[14:-3]
        if value == "":
            i = i + 1
            continue
        # value = [item for item in valueD if item != ""]
        key = str(keysD)[12:-3]
        print(value)

        if key == "img":
            message = message + "<img data-src=\"" + value + "\" class=\"img-fluid\" alt=\"Responsive image\">\n"
        elif key == "p":
            message = message + "<p>" + value + "</p>\n"
        elif key == "video":
            message = message + "<div class=\"video-player\">\n<video class=\"embed-responsive embed-responsive-16by9\"" \
                                " controls=\"controls\" ><source src=\"" + value + "\" type=\"video/mp4\"></video>\n</div>"
        elif key == "li":
            if str(text_json[i-1].keys())[12:-3] != "li":
                message = message + "<ul>\n<li>" + value + "</li>\n"
            elif str(text_json[i-1].keys())[12:-3] == "li" and str(text_json[i+1].keys())[12:-3] == "li":
                message = message + "<li>" + value + "</li>\n"
            else:
                message = message + "<li>" + value + "</li>\n</ul>\n"
        else:
            message = message + "<hr>\n<h2 class=\"body-h2\"><strong>" + value + "</strong></h2>\n"

        i = i + 1
        "< HR style = \" FILTER: alpha (opacity = 100, finishopacity =0 , style= 2 )\" width = \"80%\" color =# 987 cb 9 SIZE = 10>"

    message = message + """
    </div>
    </div>
    <script src="../js/jquery-2.1.4.min.js"></script>
    <script src="https://cdn.bootcss.com/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://cdn.bootcss.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <script src="../js/imgAndVideo.js"></script>     
    </body>
    </html>"""

    # for (k, v) in change_table.items():
    #     message = message.replace(k, v)

    file = open('/Users/hymntolife/desktop/test/' + tableName + '/' + title +'.html', 'w')

    file.write(message)

    j = j + 1

print(j)
cur.close()

conn.close()


