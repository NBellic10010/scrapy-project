
# coding: utf-8

# In[1]:


import scrapy


# In[2]:


class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()


# In[6]:


class DmozSpider(scrapy.Spider):
    name = 'dmoz'
    allowed_domains = ['dmoz.org']
    urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]
    
    def parse(self,response):
        filename = response.url.split('/')[-2]
        f = open(filename,'wb')
        try:
            f.write(response.body)
        finally:
            f.close()

