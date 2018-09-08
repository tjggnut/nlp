import jieba
import glob
import random

# p = "搜索了一番，才知道conda只能安装python的官方包，而如同jieba，itchat等第三方包要使用pip去安装，但是在随后的匹配安装过程中还是报错，有可能是网速的愿意，也有可能是你没用管理员权限去运行命令行的原因，总之，多试几次。有时，还有可能是你的pip版本比较低，升级一下也有可能解决问题。"

# s = jieba.cut(p)
# print("/".join(s))
stop_words = "[]\\{}|;':\",./<>?，。、《》？：“「」|【】、；’"

def read_news(path):
    with open(path,'r',encoding='gbk',errors='ignore') as f:
        content = ""
        for l in f:
            content += l
        return content
  
def get_stop_words():
    with open("./data/stop_words.utf8", 'r') as f:
        stop_words = [l.strip() for l in f]
        return stop_words

def get_TF(words, stop_words, topK=10):
    tk = {}
    for word in words:
        if word in stop_words:
            continue
        if word == '\u3000' or word == '\n':
            continue
        tk[word] = tk.get(word, 0) + 1
    return sorted(tk, key = lambda x:tk[x], reverse=True)[:topK]

stop_words = get_stop_words()
files = glob.glob("/Users/tongjianguo/Downloads/learning-nlp-master/chapter-3/data/news/C000013/*.txt")
content = [read_news(file) for file in files]
index = random.randint(0, len(content))
print("__________________样本:" + content[index])
# s = list(jieba.cut(content[index]))
# Expanding the Results View will run the iterator
s = jieba.cut(content[index])
print(s)
print(get_TF(s, stop_words))
print("__________________分词结果:" + '/'.join(s))
print("__________________TOP10:")
print(get_TF(s, stop_words))


# a = read_news("/Users/tongjianguo/Downloads/learning-nlp-master/chapter-3/data/news/C000013/1583.txt")
# print(a)
# print("123")