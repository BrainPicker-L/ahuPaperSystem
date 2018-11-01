import django
import requests
from lxml import etree
from multiprocessing import Pool

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")#website可以更改为自己的项目名称
django.setup()
from tool.models import *
def get_paper_info(detail_url):
    try:
        html = requests.get(detail_url).text
        selector = etree.HTML(html)
        dict = {}
        dict['chinese_title'] = (selector.xpath('/html/body/div[5]/div/div[2]/div[1]/span[2]/text()')[0]).replace('\t','').replace('\r','').replace('\n','')
        dict['author'] = ','.join(selector.xpath('/html/body/div[5]/div/div[2]/div[8]/span[2]//span//text()')).replace(' ','')
        dict['paper_type'] = PaperType.objects.all()[4]
        dict['publisher'] = selector.xpath('/html/body/div[5]/div/div[2]/div[9]/span[2]/text()')[0]
        dict['ISSN'] = selector.xpath('/html/body/div[5]/div/div[2]/div[11]/span[2]/text()')[0]
        dict['publish_year'] = selector.xpath('/html/body/div[5]/div/div[2]/div[12]/span[2]/text()')[0]
        dict['keywords'] = ','.join(selector.xpath('/html/body/div[5]/div/div[2]/div[15]/span[2]//a//text()'))
        dict['paper_url'] = selector.xpath('/html/body/div[5]/div/div[3]/div[2]/a/@href')[0]
        if dict['author']:
            print(dict)
            Paper.objects.create(chinese_title=dict['chinese_title'], paper_type=dict['paper_type'], author=dict['author'], publisher=dict['publisher'], ISSN=dict['ISSN'], publish_year=dict['publish_year'], keywords=dict['keywords'], paper_url=dict['paper_url'] )
    except:
        pass


def get_url_lists(url):
    html = requests.get(url).text
    selector = etree.HTML(html)
    detail_urls = selector.xpath('/html/body/div[5]/div/div/div[2]//div/div/div[2]/a/@href')
    for detail_url in detail_urls:
        get_paper_info('http://210.45.210.170/subjects_2/widgets/sdjgk/' + detail_url)

def main():
    urls = [
        'http://210.45.210.170/subjects_2/widgets/sdjgk/?h=gain&js_type=pt&action[keywords_cn][]=2711&jl_now=keywords_cn&page={}'.format(
            str(i)) for i in range(1, 6)]
    pool = Pool(processes=8)        #多进程爬虫
    pool.map(get_url_lists, urls)
if __name__ == '__main__':
    main()
    print('存入数据库成功')

