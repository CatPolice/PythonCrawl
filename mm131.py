import urllib.request
from bs4 import BeautifulSoup

def _getData():
    url = "http://www.mm131.com/xinggan/"
    image_url_list = []
    url_list = []
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/51.0.2704.63 Safari/537.36'}
    req = urllib.request.Request(url=url, headers=headers)
    try:
        res = urllib.request.urlopen(req)
        data = res.read()
        bs4 = BeautifulSoup(data)
        dl_class = bs4.find_all('a',{'target':'_blank'})

        url_next = bs4.find_all("a",{"class":"page-en"})

        for at in  url_next:
            # print(at.get("href"))
            url_href = at.get("href")
            url_list.append(url+url_href)

        for at in dl_class:
            # print(at)
            # print(at.img.get('src'))
            # print(at.img.get("alt"))
            src = at.img.get('src')
            image_url_list.append(src)

    except Exception as er:
        print("异常概要：")
        print(er)
    return set(image_url_list),set(url_list)

if __name__ == '__main__':
    print(_getData())