# generate letters as seperate divs
import string

with open("divs.txt", "w") as divs:
    for e in string.ascii_letters:
        divs.write('<div class="letter">{0}</div>\n'.format(e))