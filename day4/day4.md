# 进程和线程

* 线程是最小的执行单元，进程由至少一个线程组成

## 多进程

* fork()
* multiprocessing模块
* start()方法启动子进程
* join()方法可以等待子进程结束后再继续往下运行
* 进程池 Pool
* subprocess模块
* 进程间通信

## 多线程

* 启动一个线程就是把一个函数传入并创建Thread实例，然后调用 start()开始执行
* threading.Lock()

## ThreadLocal
## 分布式进程

* QueueManager

## 正则表达式

* \d 可以匹配一个数字
* \w 可以匹配一个字母或数字
* .  可以匹配任意字符
* 匹配变长的字符
* * 表示任意个字符(包括0个)
* + 表示至少一个字符
* ? 表示0个或1个字符
* {n} 表示n个字符
* {n,m} 表示n-m个字符
* '-' 是特殊字符，要用'\'转义
* [] 表示范围
* A|B 匹配A或B
* ^ 表示行的开头
* $ 表示行的结束

### re模块

* r 前缀 不用考虑Python字符串的转义问题
* march()方法 判断匹配
* 如果匹配成果，返回一个Match对象，否则返回None
* 切分字符串 re.split()
* 分组 () group()方法
* 默认贪婪匹配
* 编译
