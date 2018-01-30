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
任务0:
短信记录的第一条记录是什么？通话记录最后一条记录是什么？
输出信息:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
#1.计算最后一行在列表calls中的位置：
line_count = len(calls) - 1
#2.下面是测试打印信息，检查时去掉注释符号即可：
#print (line_count)
#print calls[line_count][0]
#3.生成需要打印的信息：
first_text = "First record of texts, {} texts {} at time {}".format(texts[0][0],texts[0][1],texts[0][2])
last_call = "Last record of calls, {} calls {} at time {}, lasting {} seconds".format(calls[line_count][0],calls[line_count][1],calls[line_count][2],calls[line_count][3])
print (first_text)
print (last_call)

