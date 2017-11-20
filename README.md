# scrapy_redis_project
a distribution spider demo

Requirements:
python:2.7
  
scrapy:1.4.0  

scrapy-redis: https://github.com/rmax/scrapy-redis  

fake-useragent:https://github.com/hellysmile/fake-useragent   

mysqlclient:  

Redis >= 2.8  


how to deploy the scrapy-reids project on a new mac 

1、create virtual env:
  sudo easy_install pip
  sudo pip install virtualenv
  virtualenv -p /usr/bin/python2.7 python2

2、enter the virtualenv and install the packages required
   source python2/bin/activate
   sudo pip install -i https://pypi.douban.com/simple/ scrapy scrapy-redis mysqlclient fake-useragent 

3、copy project
   ScrapyRedisTest

4、start redis
    
5、start spider
  

possible problem：
1、 mysqlclient error: mysql_config not find
   
    solution: open the terminal，print the follows
    
    export PATH=$PATH:/usr/local/mysql/bin    
