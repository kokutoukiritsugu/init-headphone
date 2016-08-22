# init-headphone

activate/manage the headphone amplifier in some Clevo laptops on windows.


file copyed from Clevo Hotkey Driver 5.0001.0.58


install:
    run install.bat

uninstall:
    run uninstall.bat
    reboot the system
    delte the all file.


chinese:


神州、蓝天系列笔记本睡眠唤醒后插入耳机无声解决方法


安装 hotkey驱动即可解决。但是hotkey驱动几百m，装了还右下角有几个图标不能忍。
研究了下，单独提取出来了关键的3个文件。
然后做了个批处理，安装一个在输入密码解锁登录后运行的计划任务。
自动在唤醒，解锁锁屏之后运行。

linux下有人做了个开源的：https://github.com/Unrud/init-headphone
看原理大概是这个似乎是蓝天的耳机插口有个功率放大器，需要个指令初始化才有声音。
我猜指令是通过系统内i2c总线发送的。

windows下没有直接访问i2c总线的工具。
蓝天的这个hotkey驱动的方法是，做了个驱动，SvThANSP.sys 来访问。

流程就是 InitHeadphone.exe >> hp.dll >> SvThANSP.sys 。

实际上 InitHeadphone啥也没干就是调用了 hp.dll 的函数 InitHeadphone。
hp.dll 还有个函数 Set_effect。
这个函数可以有些效果，1,2,3,4 这4个参数对应 hotkey里面的4种效果。谁装了hotkey可以帮忙截个图。
写了个 hp.py 可以调用这个效果，装了python就可以用了。
方法是 python hp.py 4
4可以是改为1,2,3，4其中的一个。
实际上4对应的是 hotkey 里面的 游戏 效果，特点是低音更好一点。。

安装：解压到c盘根目录，管理员运行 install.bat 即可。
卸载：管理员运行 uninstall.bat 会删除计划任务和驱动，但是驱动文件被占用，要删除只能重启后才能删除。



