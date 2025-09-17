
import requests
from bs4 import BeautifulSoup
import time
import random

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}

def fetch_baidu_news(keyword, page=1):
    """
    爬取百度新闻搜索结果
    :param keyword: 搜索关键词
    :param page: 页码
    :return: 新闻列表
    """
    news_list = []
    
    try:
        # 计算起始位置
        start = (page - 1) * 10
        
        # 百度新闻搜索URL
        url = f'https://www.baidu.com/s?tn=news&rtt=1&bsst=1&cl=2&wd={keyword}&pn={start}'
        
        # 发送请求
        response = requests.get(url, headers=headers, timeout=10)
        response.encoding = 'utf-8'
        
        # 解析网页内容
        soup = BeautifulSoup(response.text, 'lxml')
        
        # 查找新闻条目
        news_items = soup.find_all('div', class_='result')
        
        for item in news_items:
            # 提取标题和链接
            title_tag = item.find('a', target='_blank')
            if not title_tag:
                continue
                
            title = title_tag.get_text(strip=True)
            link = title_tag['href']
            
            # 提取来源和时间
            source_time = item.find('p', class_='c-author').get_text(strip=True)
            
            # 提取摘要
            abstract = item.find('div', class_='c-summary')
            abstract_text = abstract.get_text(strip=True) if abstract else ''
            
            # 添加到新闻列表
            news_list.append({
                'title': title,
                'link': link,
                'source_time': source_time,
                'abstract': abstract_text
            })
            
        print(f"成功获取第{page}页新闻，共{len(news_list)}条")
        return news_list
        
    except Exception as e:
        print(f"爬取第{page}页时出错: {str(e)}")
        return []

def save_news_to_file(news_list, filename='baidu_news.txt'):
    """
    将新闻保存到文件
    :param news_list: 新闻列表
    :param filename: 保存的文件名
    """
    with open(filename, 'a', encoding='utf-8') as f:
        for i, news in enumerate(news_list, 1):
            f.write(f"【新闻{i}】\n")
            f.write(f"标题: {news['title']}\n")
            f.write(f"链接: {news['link']}\n")
            f.write(f"来源/时间: {news['source_time']}\n")
            f.write(f"摘要: {news['abstract']}\n")
            f.write("-" * 80 + "\n")
    print(f"已将{len(news_list)}条新闻保存到{filename}")

def main():
    # 输入搜索关键词
    keyword = input("请输入要搜索的新闻关键词: ")
    
    # 输入要爬取的页数
    try:
        pages = int(input("请输入要爬取的页数: "))
        if pages < 1:
            print("页数必须大于0，将默认爬取1页")
            pages = 1
    except ValueError:
        print("无效的页数，将默认爬取1页")
        pages = 1
    
    all_news = []
    
    # 爬取每一页的新闻
    for page in range(1, pages + 1):
        news = fetch_baidu_news(keyword, page)
        if news:
            all_news.extend(news)
        
        # 随机延迟，避免被反爬
        if page < pages:
            delay = random.uniform(1, 3)
            print(f"等待{delay:.2f}秒后继续爬取下一页...")
            time.sleep(delay)
    
    # 保存结果
    if all_news:
        save_news_to_file(all_news)
        print(f"爬取完成，共获取{len(all_news)}条新闻")
    else:
        print("未能获取任何新闻")

if __name__ == "__main__":
    main()