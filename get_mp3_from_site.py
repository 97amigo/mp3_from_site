import re
import requests


path_of_html = 'C:/example.txt'  # текст сайта .html сохранить в .txt
url_site_for_parse = 'https://some.site.com'
path_download_to = 'C:/Place_where_you_want_to_save/'


with open(path_of_html) as f:
    templ = re.compile('".*\.mp3"')
    list_ref = []
    for i in f:
        if re.findall(templ, i):
            list_ref.append(re.findall(templ, i))

    k = 1
    for i in list_ref:
        url = url_site_for_parse + i[0][2:(len(i[0])-1)]
        path_to = path_download_to + str(k) + '.mp3'
        r = requests.get(url)
        with open(path_to, "wb") as code:
            code.write(r.content)
        print(k)
        k += 1
