# zb_16084649  
## 描述:  
    python 实现一段代码 定时改变本机IP，使得远方服务器(公网服务器，如新浪网页)认为不断有新机器访问该主机(其实是同一台电脑一个固定IP而已)。  
## 使用步骤:  
``python demon.py {interface name}``  

例如:  
* 操作前ipconfig查询结果为:  
```
    Windows IP Configuration


    Ethernet adapter 本地连接:

        Connection-specific DNS Suffix  . :
        IP Address. . . . . . . . . . . . : 10.0.2.178
        Subnet Mask . . . . . . . . . . . : 255.255.255.0
        Default Gateway . . . . . . . . . : 10.0.2.1
```
* 操作:  
    ``python demon.py 本地连接``
* 操作后ipconfig查询结果为:  
```
    Windows IP Configuration


    Ethernet adapter 本地连接:

        Connection-specific DNS Suffix  . :
        IP Address. . . . . . . . . . . . : 10.0.2.227
        Subnet Mask . . . . . . . . . . . : 255.255.255.0
        Default Gateway . . . . . . . . . : 10.0.2.1
```
## 进展:  
* 已实现:   
    * linux平台自动修改IP  
    * win平台自动修改IP  
* 待实现:  
    * 指定系统版本兼容  
    * 定时更新
