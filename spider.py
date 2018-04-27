import requests
# 导入捕获异常库
from requests.exceptions import RequestException

def get_one_page(url):
    # 是否异常
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def main():
    url = 'http://maoyan.com/board/4?'
    html = get_one_page(url)
    print(html)


if __name__ == '__main__':
    main()
