##  2018/12/30 basic_learn_12
##  regular expression:文本表達
##  網頁爬蟲

import re #正則引入

#matching string Pythin匹配內容
pattern1 = "cat"
pattern2 = "bird"
string = "dog runs to cat"
print(pattern1 in string)
print(pattern2 in string)

#正則 尋找
print(re.search(pattern1,string))
print(re.search(pattern2,string))

#正則 匹配多種可能
ptn = "run"
print(re.search(ptn,string))
ptn = "ran"#過去式
print(re.search(ptn,string))
ptn = "r[au]n"
print(re.search(ptn,string))
string = "dog ran to cat"
print(re.search(ptn,string))

#continue
ptn = "r[a-z]n"
print(re.search(ptn,string))
ptn = "r[0-9a-z]n"
string = "dog r2n to cat"
print(re.search(ptn,string))

#\d: decimal digit
print(re.search(r"r\dn","run r4n"))
#\D: any non-decimal digit
print(re.search(r"r\Dn","run r4n"))
#\s: any white space [\t\n\r\f\v]
print(re.search(r"r\sn","r\nn r4n"))
#\w: [a-zA-Z0-9_]
#\b: empty string (only at the start or end of the word)
print(re.search(r"\bruns\b","dog  runs  to cat"))
#\B: empty string (but not at the start or end of the word)
print(re.search(r"\B runs \B","dog  runs  to cat"))
#\\: match \
print(re.search(r"runs\\","dog runs\ to cat"))
#\.: match anything (except \n)
print(re.search(r"r.n","dog r-ns to cat"))
#^: match line beginning
print(re.search(r"^dog","dog runs to cat"))
#$: match line ending
print(re.search(r"cat$","dog runs to cat"))
#?: may or may not occur
print(re.search(r"Mon(day)?","Monday"))
print(re.search(r"Mon(day)?","MonMon"))
#multi-line
string = """
dog runs to cat.
I run to dog.
"""
print(re.search(r"^I",string))#每一行都接一起看
print(re.search(r"^I",string,flags=re.M))#每一行都個別看
#*: occur 0 or more times
print(re.search(r"a*b","aabb"))
print(re.search(r"ab*","abbbbbbb"))
#+: occur 1 or more times
print(re.search(r"ab+","a"))
print(re.search(r"ab+","abbbbbbb"))
#{n,m}: occur n to m times
print(re.search(r"ab{2,10}","a"))
print(re.search(r"ab{2,10}","abbbbbbb"))
#group
match = re.search(r"(\d+), Date: (.+)","ID: 021523, Date: Feb/12/2017")
print(match.group())
print(match.group(1))
print(match.group(2))
#給每一個match名字
match = re.search(r"(?P<id>\d+), Date: (?P<date>.+)","ID: 021523, Date: Feb/12/2017")
print(match.group('id'))
print(match.group('date'))
print(match.group(2))
#findall
print(re.findall(r"r[ua]n","run ran ren"))
#|: or
print(re.findall(r"r(u|a)n","run ran ren"))
#re.sub() replace
print(re.sub(r"r[au]ns","catches","dog runs to cat"))#dog catches to cat
#re.split()
print(re.split(r"[,;\.]","a;b,c.d;e"))
#compile
compiled_re = re.compile(r"r[ua]n")
print(compiled_re.search("dog ran to cat"))


