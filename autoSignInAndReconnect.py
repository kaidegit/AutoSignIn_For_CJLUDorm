#! /usr/bin/python3
import requests
import os
import platform


class cjluSignIn():
    def __init__(self):
        self.data = {
            # 'DDDDD': num,  # 学号，连接互联网须在学号前加两个下划线
            # 'upass': password,  # 密码
            'R1': '0',
            'R2': '',
            'R6': '0',
            'para': '00',
            '0MKKey': '123456'
        }
        self.url = "https://portal2.cjlu.edu.cn:801/eportal/?c=ACSetting&a=Login&wlanuserip=null&wlanacip=null" \
                   "&wlanacname=null&port=&iTermType=1&mac=000000000000"  # &ip=172.28.1.252&redirect=null "
        self.my_headers = {
            'Accept': 'image/gif, image/jpeg, image/pjpeg, application/x-ms-application, application/xaml+xml, '
                      'application/x-ms-xbap, */*',
            # 'Referer': 'https://portal2.cjlu.edu.cn/a70.htm',
            'Accept-Language': 'zh-Hans-CN,zh-Hans;q=0.5',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; '
                          '.NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729)',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'portal2.cjlu.edu.cn:801',
            'Content-Length': '67',
            'Connection': 'Keep-Alive',
            'Cache-Control': 'no-cache',
        }
        self.cookie = {
            'wlanacname': 'null',
            'wlanacip': 'null'
        }

    def signIn(self, num, password):
        self.data['DDDDD'] = num
        self.data['upass'] = password
        requests.packages.urllib3.disable_warnings()
        req = requests.post(url=self.url, verify=False, headers=self.my_headers,
                            data=self.data, cookies=self.cookie)
        print('ok')

    def checkInternet(self):
        print("正在检测网络连接性")
        system = platform.system()
        if system == "Windows":
            connection = os.system("ping 114.114.114.114 -n 3")
        else:
            connection = os.system("ping 114.114.114.114 -c3")
        if connection:
            print("网络未连接")
            return False
        print("网络已连接")
        return True


if __name__ == '__main__':
    cjlu = cjluSignIn()
    try:
        username = open("/opt/username.txt","r")
        username = username.read()
        password = open("/opt/password.txt","r")
        password = password.read()
        print(username,password)
    except:
        username = input("请输入学号")  # 学号，连接互联网须在学号前加两个下划线
        username = '__'+username
        password = input("请输入密码")  # 密码
        file = open("/opt/username.txt","w")
        file.write(username)
        file.close()
        file = open("/opt/password.txt","w")
        file.write(password)
        file.close()
    if not cjlu.checkInternet():
        print("正在尝试登陆内网认证")
        cjlu.signIn(username, password)
