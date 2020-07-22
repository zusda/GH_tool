
from cookie import cookie
import re
import requests
import time  # 引入time模块

from urllib.parse import quote_plus as url_encode
'''
接收参数site（可选）  -s --site
接收含google hacking语句的txt文件  -f  --file  
输出：文件名+时间的txt  -o --output
'''
def decode_html(string):
    "decode common html/xml entities"
    new_string = string
    decoded = ['>', '<', '"', '&', '\'']
    encoded = ['&gt;', '&lt;', '&quot;', '&amp;', '&#039;']
    for e, d in zip(encoded, decoded):
        new_string = new_string.replace(e, d)
    for e, d in zip(encoded[::-1], decoded[::-1]):
        new_string = new_string.replace(e, d)
    return new_string

# 要设置代理
proxies_http = {
            "http": "http://127.0.0.1:7078",
            "https": "https://127.0.0.1:7078",
}

def search_all_dork(query,site=None):
    """
    main function, returns parsed results
    Args:
    query - search string
    cookie - facebook cookie
    page - search result page number (optional)
    """
    # escaped = url_encode('https://www.google.com/search?q=site:sakura.myacgcat.top&start=2&filter=True' )
    query2=url_encode(query)
    # print('query2: '+query2)
    if site:
        escaped = url_encode('https://www.google.com/search?q=site:'+site +'+'+ query2 )
        # print(escaped)
    else:
        escaped = url_encode('https://www.google.com/search?q='+query2+'&start=0&filter=True'  )
    headers = {
    'Host': 'developers.facebook.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'deflate',
    'Connection': 'keep-alive',
    'Cookie': cookie,
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0',
    'TE': 'Trailers'
    }
    response = requests.get('https://developers.facebook.com/tools/debug/echo/?q=%s' % escaped, headers=headers,proxies=proxies_http)
    cleaned_response = decode_html(response.text)
    return cleaned_response

def GHtools(querys_file,site=None,output=None):
    k=0
    f=open(querys_file,'r')

    if output == None:
        ticks = time.localtime(time.time())
        t = str(ticks[0]) + '_' + str(ticks[1]) + '_' + str(ticks[2]) + '_' + str(ticks[3]) + '_' + str(
            ticks[4]) + '_' + str(ticks[5])

        # 创建新文件或清空已有文件
        newFile=re.sub(r'\.txt','',querys_file)
        file = open(newFile+'_'+ t+'.txt', 'w')
        file.write('')
        file.close()

        file = open(newFile+'_'+ t+'.txt', 'a',encoding='utf-8')
    else:
        # 创建新文件或清空已有文件
        file = open(output, 'w')
        file.write('')
        file.close()

        file = open(output, 'a',encoding='utf-8')
    for q in f:

        result = search_all_dork(q,site)
        # print(result)
        # example="<div class=\"kCrYT\"><a href=\"/url?q=https://blog.kelu.org/page104/&sa=U&ved=2ahUKEwi1o7H85trqAhXTHM0KHfUJArA4AhAWMAB6BAgGEAE&usg=AOvVaw3VJa7lBEuNJMDFTf6xzWIX\"><h3 class=\"zBAuLc\"><div class=\"BNeawe vvjwJb AP7Wnd\">Linux命令之du & df - 血衫非弧の一存</div></h3>"
        p1="<div class=\".+?\"><a href=\"/url\?q=.+?\">"
        p2='<h3 class=\".+?\"><div class=\".+?\">.+?</div></h3>'
        p3=p1+p2
        a=re.findall(p3, result)


        file.write('query : ' + q)
        if k==0:
            k=1
        else:
            file.write('\n')
        for i in a:
            # print(i)
        #     获取链接
        #     link = i.split('q=')[1]
        #     link=link.split('"')[0]
        #     print("link: "+link)
        #     获取标题
            title = i.split('>')[4]
            title=title.split('<')[0]
            # print("title: "+title)
            # print()
            file.write('\t'+title+'\n')

        file.write('\n')
    file.close()

    f.close()
