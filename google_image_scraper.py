import requests
from lxml.html import fromstring
# from lxml import etree
import argparse
import json


def main():

    parser=argparse.ArgumentParser()
    parser.add_argument('-s','--search',default='cat',help='query name')
    parser.add_argument('-n','--number',type=int,default=2,help='number of images')
    args=parser.parse_args()


    query=args.search
    max_images=args.number 

    url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
    user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'

    html=requests.get(url,headers={'User-Agent':user_agent}).content
    dom=fromstring(html)
    images=[]
    
    show_im=0
    for content in dom.xpath('//div[contains(@class,"rg_meta")]/text()'):
        if show_im>=max_images:
            break
        show_im=show_im+1

        json_content=json.loads(content)
        images.append(json_content['ou'])
        print(json_content['ou'])
    
if __name__=='__main__':
    main()