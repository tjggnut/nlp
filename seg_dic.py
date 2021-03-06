

# sdict = ['南京','长江大桥','南京长江']
# print(max(sdict,key=lambda x:len(x)))

class seg_dic:

    max_len = 0
    sdict = []
    #self.max_length = 0
    #self.dict = ['南京','长江大桥','南京长江']


    def __init__(self):
        self.sdict = "南京市 南京市长 长江大桥 人名解放军 大桥".split(' ')
        # self.sdict = "南京市 南京市长 长江 人名解放军 大桥".split(' ')
        self.max_len = len(max(self.sdict,key=lambda x:len(x)))


    def get_s_max_char(self,sentence,len_seged):
        if len_seged >= len(sentence):
            return ""
        if len(sentence)-len_seged > self.max_len:
            return sentence[len_seged:len_seged + self.max_len]
        else:
            return sentence[len_seged:]


    def mm(self, sentence, delimiter = '/'):
        res = []
        len_seged = 0
        while len_seged < len(sentence):
            s = self.get_s_max_char(sentence,len_seged)
            while len(s) > 1:
                if s in self.sdict:
                    break
                else:
                    s = s[:-1]
            res.append(s)
            len_seged += len(s)
        return delimiter.join(res)
    

    def get_e_max_char(self, sentence, len_seged):
        if len_seged >= len(sentence):
            return ""
        if len(sentence) - len_seged > self.max_len:
            return sentence[len(sentence) - len_seged - self.max_len : len(sentence) - len_seged]
        else:
            return sentence[:len(sentence) - len_seged]
    
    def rmm(self, sentence, delimiter = '/'):
        res = []
        len_seged = 0
        while len_seged < len(sentence):
            s = self.get_e_max_char(sentence, len_seged)
            while len(s)>1:
                if s in self.sdict:
                    break
                else:
                    s = s[1:]
            res.append(s)
            len_seged += len(s)
        res.reverse()
        return delimiter.join(res)

    def bmm(self, sentence, delimiter = '/'):
        """
            双向最大匹配 没写完 木有判断mm rmm分词数相同时的单字数量
        """
        mm_res = self.mm(sentence, delimiter)
        rmm_res = self.rmm(sentence, delimiter)
        return min([mm_res, rmm_res], key=lambda x:len(x))

seg = seg_dic()
# print(seg.get_s_max_char("1234",2))
print(seg.mm("南京市长江大桥"))

# print(seg.get_e_max_char("12345",0))
print(seg.rmm("南京市长江大桥"))

print(seg.bmm("南京市长江大桥"))

