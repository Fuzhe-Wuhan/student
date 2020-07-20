#验证手机号是否符合规则
'''
1.11位数字
2.1开头
3.第二位 35678 中的一个
'''
import re
s = '15672995430,13184214111,12345678901'
l = re.match(r'1[35678][0-9]{9}',s)
print(l.group())

#匹配单词边界
str1 = 'this is book'
'''
以字母开始
中间包含空字符
is两边分别限定单词边界
'''
pattern = r'^\w+\sis\b\s\w+'
l = re.match(pattern,str1)
print(l.group())

#0-100之间的数字
'''
1 : 0，100单独拿出来
2 : 匹配1-99
'''
# num = input('>>>')
# pattern = r'[1-9]\d{0,1}$|100$|0$'
# l = re.match(pattern,num)
# print(l.group())

str1 = '<h1>hello world!</h1>'
pattern = r'^<h1>(.*)</h1>'
l = re.match(pattern,str1)
print(l.group())

#<xx><yy>********</yy></xx>
#\1对第一个分组的引用   \2
str1 = '<h1><span>hello world!</span></h1>'
pattern = r'<(.+)><(.+)>.*</\2></\1>'
l = re.match(pattern,str1)
print(l.group())

str1 = '<a><b>nihao</b></a>'
pattern = r'<(?P<key1>.+)><(?P<key2>.+)>.*</(?P=key2)></(?P=key1)>'
l = re.match(pattern,str1)
print(l.group())


# str1 = 'http://news.baidu.com/mil'
# pattern = '^/mil$'
# l = re.match(pattern,str1)
# print(l.group())

str2 = 'this is a number 122-424-454'
pattern1 = r'(.+?)(\d+-\d+-\d+)'
l = re.match(pattern1,str2)
print(l.groups())