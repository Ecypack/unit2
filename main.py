#导入re模块
import re

txt = open('readme.md',mode='r')
r = re.compile(r"")
# compile 编译正则表达式

count = {}
for line in txt:
    for word in r.sub("", line.strip()).split(" "):
        if word in count:
            count[word] +=1
        count.setdefault(word,1)
#拆分进入字典

num = 0
for item in count:
    if count[item]>=1:
        num=num+count[item]
#累计词数

print("The number of words in this file is {}".format(num))


