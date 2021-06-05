
import re

def Regex(Str):
    ResultURL = re.findall('http[https]?://\w+.\w+.\w+',Str)
    ResultIP = re.findall('\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}',Str)

    List = list()
    Index = 0
    for i in ResultURL:
        for j in ResultIP:
            if i == ResultURL[Index] and j == ResultIP[Index]:
                Line = 'URL: ' + i + ' IP: ' + j
                Index += 1
                List.append(Line)

    for k in List:
        print(k)

Regex('<p>Contents :</p><a href="https://w3resource.com""104.26.14.93">Python Examples</a><a href="http://github.com""13.250.177.223">Even More Examples</a>')
