import json
import re
import requests
# 导入捕获异常库
from requests.exceptions import RequestException

# 获取网页数据
def get_one_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36"}
    # 是否异常
    try:
        response = requests.get(url=url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

# 分析页面
def parse_one_page(html):
    # 正则分析
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                        '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                        '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)

    items = re.findall(pattern, html)
    # print(items)
    for item in items:
        yield {
            'index': item[0],
            'img_url': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }

# 把数据保存到本地
def write_to_file(content):
    with open('result.json','a',encoding="utf-8") as fp:
        fp.write(json.dumps(content,ensure_ascii=False)+'\n')
        fp.flush()



# 主程序
def main():
    start_page = input("请输入开始页: ")
    end_page = input("请输入结束页: ")

    for page in range(int(start_page)-1,int(end_page)):
        url = 'http://maoyan.com/board/4?offset=' + str(page) + '0'
        html = get_one_page(url)
        for item in parse_one_page(html):
            print(item)
            write_to_file(item)

if __name__ == '__main__':
    main()
