import json
import requests

# store api key in apikey.txt in root folder
api_key = open("./apikey.txt", "r").readline()
api_url = "https://www.googleapis.com/webfonts/v1/webfonts?key="
r = requests.get(api_url+api_key)
# get list of fonts from response
all_fonts = json.loads(r.text)["items"]
fonts_list = []
font_names = []
# store serif and sans-serif fonts only
for font in all_fonts:
    if font['category'] in ['sans-serif', 'serif']:
        fonts_list.append(font)
        font_names.append(font['family'])
json.dump(fonts_list, open("get_font_images/font_list.json", "w"), indent=4)
json.dump(font_names, open("get_font_images/font_names.json", "w"), indent=4)
