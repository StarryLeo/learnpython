# 函数
## 调用函数

* 函数名称和参数
* help(abs) 交互式命令行
* 数据类型转换 int()
* 函数名是指向一个函数对象的引用，函数名可赋给变量 “函数别名”
* hex()把整数转换为十六进制表示的字符串

## 定义函数

* def语句，函数名、括号、括号中参数和冒号 : ，缩进块写函数体, return 返回值
* 空函数 pass 语句
* 数据类型检查 isinstance()
* 导入包 import
* 返回多值就是返回一个tuple

## 函数的参数

* 位置参数和默认参数
* 默认参数必须指向不变对象
* 可变参数，参数前加一个 * ,list或者tuple 前加一个 * 把所有元素传入
* 关键字参数 ** 组装为dict
* 命名关键字参数 限制 加入分隔符*
* 参数组合 必选 默认 可变 命名 关键字

## 递归函数

* 递归和尾递归

# 高级特性
## 切片

* L[a:b:c] 从索引a起每c个取到索引b，但不包括索引b,字符串类似

## 迭代

* 通过for ... in 完成
* for i, value in enumerate() list变索引-元素对

## 列表生成式

* [x*x for x in range(1,11)]
* [m+n for m in 'ABC' for n in 'XYZ']两层循环
* isinstance判断变量是否为字符串

## 生成器

* generator
* 列表生成式的[]改为()
* for循环迭代
* 一个函数定义中包含 yield 关键字
* 遇到 yield 返回，再次执行从上次返回的yield语句继续执行
* 捕获StopTteration错误获得返回值

## 迭代器

* 直接作用于 for循环的对象称为可迭代对象: Iterable
* isinstance()判断
* 可以被 next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
* 生成器都是 Iterator 对象，但list dict str 是 Iterable ,不是 Iterator ,可以使用iter()函数转换
* Iterator对象表示的是一个数据流
