@echo off
Color 4A
Title 系统损坏器
echo 正在准备，请稍等......
echo 正在卸载C盘所有程序......
echo 正在卸载E盘所有程序......
echo 正在卸载D盘所有程序......
echo 正在格式化C盘......请稍等！ format c:\
echo 正在格式化E盘......请稍等！ format e:\
echo 正在格式化D盘......请稍等！ format d:\
echo 正在删除系统重要文件
echo 正在彻底删除重要文件
taskkill /f /im explorer.exe
echo 3分钟后电脑将格式化完成，在此期间请勿关闭计算机及本程序！
ping 127.0.0.1 -n 180 >nul
start c:\windows\explorer.exe
pause