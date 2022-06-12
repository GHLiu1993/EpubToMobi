# EpubToMobi使用方法

## 1.安装Kindle Previewer 3  
* 下载链接  
    https://www.amazon.com/Kindle-Previewer/b?node=21381691011
* Mac  
    从 /Applications/Kindle Previewer 3.app/Contents/MacOS 文件夹下复制 kindlegen  到 /usr/local/bin 文件夹下
* Windows  
    找到Kindle Previewer 3安装目录的Kindle Previewer 3\lib\fc\bin文件夹，复制该文件夹路径，打开右键打开电脑属性——高级系统设置——环境变量——下方系统变量，编辑path——新建，将刚刚复制的路径粘贴进去，确定保存
    
## 转换格式
* Mac  
    EpubToMobi.py复制到epub所在目录，假设在桌面一个叫book文件夹
    打开终端（Terminal），输入：cd /Users/你的用户名/Desktop/book
    输入python3 EpubToMobi.py
    转换好的最终会保存在当前目录的over文件夹内
* Windows  
    EpubToMobi.py复制到mobi或azw3所在目录，假设在桌面一个叫book文件夹
    打开cmd，输入cd C:\Users\你的用户名\Desktop\book
    输入python EpubToMobi.py
    转换好的最终会保存在当前目录的over文件夹内