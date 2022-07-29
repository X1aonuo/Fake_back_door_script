import time
print('''
   ___      _             
  / _ \    | |            
 | | | | __| | __ _ _   _ 
 | | | |/ _` |/ _` | | | |
 | |_| | (_| | (_| | |_| |
  \___/ \__,_|\__,_|\__, |
                     __/ |
                    |___/ 
''')
for i in range(2):
    print()
s = input('请输入网站网址：')
print()
q = input('请输入后门名字：')
time.sleep(0.8)
print('请稍等……')
time.sleep(2)
print()
print('成功写入Webshell: ' + s + '/' + q + '.aspx')