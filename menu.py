import time
from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.firefox.service import Service
import requests
from bs4 import BeautifulSoup
import urllib
from selenium import webdriver






def get_html(url):
    request = requests.get(url)
    return False if request.status_code == 404 else request.text


#
# url = 'https://www.e-katalog.ru/ek-list.php?katalog_=189&search_=rtx+3050'
#
# headers = {
#     'accept': '*/*',
#     'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69",
#
#
#
# }
#
#
# req = requests.get(url, headers=headers)
# src = req.text
# # print(src)
#
#
#
# soup = BeautifulSoup(src,"lxml")
#
#
#
#
# linkprice = soup.find_all(class_="ib model-all-shops no-mobile")
# for item in linkprice:
#     # print(item)
#     #item_text = item.text
#     item_href = "https://www.e-katalog.ru" + item.get("href")
#    # item_name = item.get('')
#    # print(f" {item_href}")
#     # print(f"{item_text}")
#
#     linkprice2 = soup.find_all(class_="model-price-range")
#     uf=0
# # print(linkprice2)
#     for item in linkprice2:
#         # print(item)
#         item_href2 = item.find_all('a',href_='')
#
#         for item2 in item_href2:
#             # print(item2)
#             item_link = "https://www.e-katalog.ru" + item2.get('link')
#
#             #print(item_link)
#             if item_link == item_href:
#                 reu = requests.get(item_link, headers=headers)
#                 srn = reu.text
#                 # print(srn)
#                 sopric = BeautifulSoup(srn, "lxml")
#                 # print(sopric)
#                 shop_price = sopric.find_all(class_="yel-but-2")
#                 #print(shop_price)
#                 for toh in shop_price:
#                    # namegpu = toh.text
#                     shoplink = toh.get('onmouseover')
#                     namegpu = toh.get('onclick')
#                     print(shoplink)
#                     shoplin = shoplink[11:205]
#                     get_html(
#                             "https://api.telegram.org/bot1540937288:AAEp5-YpjImIo-YiBgGVIXNEv38-LqZDVmA/sendMessage?chat_id=849685423&text=" + urllib.parse.quote(
#                     shoplin))
#
#             elif item_link == None:
#                 print(item_href)
#                 print('urup')
#             elif item_href == None:
#                 print(item_link)
#                 print('urup')

def get_data(url):
    options = webdriver.FirefoxOptions()
    options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",)

    headers = {
        'accept': '*/*',
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
        'cookie': "PHPSESSID=ulev68r29g6difaehfa90i4hnh; n_session_id_cookie=366e607df0fd744cbc9d5922d08c94b6; _ga=GA1.2.1514714466.1643294580; _gid=GA1.2.1505022014.1643294580; _fbp=fb.1.1643294581262.1383535461"

    }
    try:
        driver = webdriver.Firefox(
            executable_path=r"C:\Users\dom\Desktop\Ekat-bot\geckodriver.exe",
            options=options
        )
        driver.get(url=url)
        time.sleep(4)

        with open('test_sel.html', 'w', encoding='utf-8') as output_file:
            output_file.write(driver.page_source)

        src = driver.page_source


        soup = BeautifulSoup(src, "lxml")


        linkprice2 = soup.find_all(class_="model-price-range")
        uf = 0

        for item in linkprice2:
            # print(item)
            item_href2 = item.find_all('a', href_='')

            for item2 in item_href2:
                # print(item2)
                item_link = "https://www.e-katalog.ru" + item2.get('link')

                # print(item_link)
                reu = requests.get(item_link, headers=headers)
                srn = reu.text
                # print(srn)
                sopric = BeautifulSoup(srn, "lxml")
                # print(sopric)
                shop_price = sopric.find_all(class_="yel-but-2")
                # print(shop_price)
                for toh in shop_price:
                    # namegpu = toh.text
                    shoplink = toh.get('onmouseover')
                    namegpu = toh.get('onclick')
                    print(shoplink)
                    shoplin = shoplink[11:205]
                    get_html(
                        "https://api.telegram.org/bot1540937288:AAEp5-YpjImIo-YiBgGVIXNEv38-LqZDVmA/sendMessage?chat_id=849685423&text=" + urllib.parse.quote(
                            shoplin))



    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    get_data("https://www.e-katalog.ru/ek-list.php?katalog_=189&search_=rtx+3050")
    #while 1:
       # get_data("https://www.e-katalog.ru/ek-list.php?katalog_=189&search_=rtx+3050")
       # time.sleep(10)
