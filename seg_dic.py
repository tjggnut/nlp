

# sdict = ['南京','长江大桥','南京长江']
# print(max(sdict,key=lambda x:len(x)))

class seg_dic:

    max_len = 0
    sdict = []
    #self.max_length = 0
    #self.dict = ['南京','长江大桥','南京长江']


    def __init__(self):
        self.sdict = "南京市 南京市长 长江大桥 人名解放军 大桥".split(' ')
        self.max_len = len(max(self.sdict,key=lambda x:len(x)))


    def get_s_max_char(self,sentence,len_seged):
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

seg = seg_dic()
print(seg.get_s_max_char("1234",2))
print(seg.mm("南京市长江大桥"))
