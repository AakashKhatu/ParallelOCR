# generate the template html file for selenium
import string

html_start = """
<html>

<head>
    <style>
        @import url('https://fonts.googleapis.com/css?family={0}&text=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ');

        .letter {{
            display: inline-block;
            outline: 1px solid blue;
            margin-top: 5px;
            margin-bottom: 5px;
            padding: 5px;
            font-family: '{0}';
            font-size: 32px;
            line-height: 1;
            text-align: center
        }}

        body {{
            display: inline-block;
            outline: 1px solid red;
            padding: 10px;
        }}
    </style>
</head>

<body id="box">
"""

html_end = "</body></html>"

with open("test.html", "w") as html_file:
    html_file.write(html_start)
    for e in string.ascii_letters:
        html_file.write('<div class="letter">{0}</div>\n'.format(e))
    html_file.write(html_end)