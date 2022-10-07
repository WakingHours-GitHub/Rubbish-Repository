from scrapy import cmdline

cmdline.execute("scrapy crawl search -s JOBDIR=crawls/search".split())
