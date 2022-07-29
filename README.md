# Fake_back_door_script
2022年HVV中KFC_V_me50_aspx后门脚本的装逼拓展


![image](https://user-images.githubusercontent.com/95486088/181680227-d3322915-fbb0-4066-80b9-d2328998dd14.png)


大家看到这图是不是还挺很好玩的？

转念一想，我们是不是可以做一个通用所有网站的装逼利器呢？

![image](https://pic.imgdb.cn/item/62e35532f54cd3f93799dc0f.gif)


用最简单的源码，干最装逼的事：

PS:可能太过简陋太简单，呃大佬看着好玩就好

```
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
```

当然你也可以自己修改

文字字符画生成：http://patorjk.com/software/taag
