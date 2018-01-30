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
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
"""


def find_suspect():
    number_list = []
    suspect_list = []
    for n in range(len(calls)-1):
        if calls[n][1] not in number_list:
            number_list.append(calls[n][1])
    for n in range(len(texts)-1):
        if texts[n][0] not in number_list:
            number_list.append(texts[n][0])
        if texts[n][1] not in number_list:
            number_list.append(texts[n][1])
    for n in range(len(calls)-1):
        if calls[n][0] not in number_list and (calls[n][0] not in suspect_list):
            suspect_list.append(calls[n][0])

    return suspect_list


suspect = find_suspect()
suspect.sort()
print("These numbers could be telemarketers: ")
for number in suspect:
    print(number)
