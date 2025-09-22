from urllib import request
import re
import time
import random
import csv
ua_list = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
]

# 定义一个爬虫类
class MaoyanSpider(object): 
    # 初始化
    # 定义初始页面url
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'
    
    # 请求函数
    def get_html(self,url):
        headers = {'User-Agent':random.choice(ua_list)}
        req = request.Request(url=url,headers=headers)
        res = request.urlopen(req)
        html = res.read().decode()
        # 直接调用解析函数
        self.parse_html(html)
    
    # 解析函数
    def parse_html(self,html):
        # 正则表达式
        re_bds = '<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?class="releasetime">(.*?)</p>'
        # 生成正则表达式对象
        pattern = re.compile(re_bds,re.S)
        # r_list: [('我不是药神','徐峥,周一围,王传君','2018-07-05'),...] 列表元组
        r_list = pattern.findall(html)
        self.save_html(r_list)

    # 保存数据函数，使用python内置csv模块
    def save_html(self,r_list):
        #生成文件对象  
        with open('maoyan.csv','a',newline='',encoding="utf-8") as f:
            #生成csv操作对象
            writer = csv.writer(f)
            #整理数据
            for r in r_list:
                name = r[0].strip()
                star = r[1].strip()[3:]
                # 上映时间：2018-07-05
                # 切片截取时间
                time = r[2].strip()[5:15]
                L = [name,star,time]
                # 写入csv文件
                writer.writerow(L)
                print(name,time,star)

    # 主函数
    def run(self):
        #抓取第一页数据
        for offset in range(0,11,10):
            url = self.url.format(offset)
            self.get_html(url)
            #生成1-2之间的浮点数
            time.sleep(random.uniform(1,2))


if __name__ == '__main__':
    #捕捉异常错误
    try:
        spider = MaoyanSpider()
        spider.run()
    except Exception as e:
        print("错误:",e)