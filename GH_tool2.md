这次要写的是一个自己编的程序，用于google hacking。

大家都知道google hacking能够在exploit-db上面搜到许多语句。

![https://github.com/zusda/GH_tool/blob/master/img/1.png](https://github.com/zusda/GH_tool/blob/master/img/1.png)

然而我在寻找相关工具的时候只找到了uDork这一种工具，不幸的是，按照教程完全无法运行。于是稍微看了下源码，发现还是挺简单的。于是自己把他google api相关模块取出来，自己构造了一个google hacking工具。

## 配置

**1.代理**

GHtool.py下：

```
proxies_http = {
            "http": "http://127.0.0.1:7078",
            "https": "https://127.0.0.1:7078",
}
```

**2.facebook的cookie**

cookie.py下（cookie.py需要自己创建）

```
cookie ='c_user=@@@@@@@@; xs=@@@@@@@'
```

## 使用

-q : google hacking语句的txt文件

-s : 会在语句中添加site:@@@@@。（你也可以直接写在-q文件中而不使用-s）

-o： 输出文件名，默认为-q文件名+时间的txt文件。

## example

![https://github.com/zusda/GH_tool/blob/master/img/2.png](https://github.com/zusda/GH_tool/blob/master/img/2.png)

![https://github.com/zusda/GH_tool/blob/master/img/3.png](https://github.com/zusda/GH_tool/blob/master/img/3.png)

![https://github.com/zusda/GH_tool/blob/master/img/4.png](https://github.com/zusda/GH_tool/blob/master/img/4.png)

## 后记

本质上就是提取语句然后去google中搜索，因此如果需要的话可以去吧google搜索api部分单独拿出来使用。自己设计提取的内容，比如链接等。（GH_tool中的链接注释去掉注释就可以拿到链接了）

项目地址：https://github.com/zusda/GH_tool

ps：google语句是我直接在页面上复制下来的，本来也想弄个自动获取的，发现好像直接拉页面上的语句然后复制也挺好。