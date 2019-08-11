#CalHamletV1.py
def getText():
    txt =open("halet.txt").read()
    txt = txt.lower()
    for ch in '!"#%&()*+,_./:;<=>?@[\\]^_‘{|}~'：
        txt = txt.replace(ch, " ")
    return txt
hamleTXT = getText()
words = hamleTXT.split()
counts = {}
for word in words:
    counts[word] = counts.get(word,0) + 1
items = list(counts,items())
items.sort(key=lambda x:[1],reverse=True)
for i in range(10):
    words, count = items[i]
    print("{0:<10}{1:5}".format(word, count))#左对齐留10个宽度，
#format方法的格式控制。
#填充和对齐^<>分别表示居中、左对齐、右对齐，后面带宽度
#
#
import jieba
txt = open("threekingdom.txt", "r", encoding="utf-8").read()
excludes = {"将军","确说","荆州"}
words = jieba.lcut(txt)
counts = {}