"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."""
#1.创建一个把文件中电话号码归总的函数


phone_num = []
for n in range(len(texts)-1): #设定循环次数为文件行数
    #print (content[n][0])
    if texts[n][0] not in phone_num:  #如果主叫号码不在号码表中就加上
        phone_num.append(texts[n][0])
        #print (phone_num)
    if texts[n][1] not in phone_num:    #如果被叫号码不在号码表中也相应加入号码表中
        phone_num.append(texts[n][1])
for m in range(len(calls)-1):
    if calls[m][0] not in phone_num:  #如果主叫号码不在号码表中就加上
        phone_num.append(calls[m][0])
        #print (phone_num)
    if calls[m][1] not in phone_num:    #如果被叫号码不在号码表中也相应加入号码表中
        phone_num.append(calls[m][1])

#print (phone_num) #测试输出的不重复电话号码数量是否准确
print ("There are {} different telephone numbers in the records.".format(len(phone_num)))

