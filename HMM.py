import pickle
import os

class HMM(object):
    """
        A:状态转移概率矩阵 状态->状态
        B:发射矩阵 状态->观测
        pi:初始状态概率矩阵
    """
    def __init__(self):
        self.state = ['B', 'M', 'E', 'S']
        self.model_path = './model/hmm_model.pkl'
        self.train_data_path = './data/trainCorpus.txt_utf8'

        # 测试数据
        # self.model_path = './model/hmm_model2.pkl'
        # self.train_data_path = './data/test_train_data.txt_utf8'
        self.para_loaded = False

    def try_load_model(self, trained):
        if trained:
            with open(self.model_path, 'rb') as model_file:
                # model = pickle.load(model_file)
                self.A = pickle.load(model_file)
                self.B = pickle.load(model_file)
                self.pi = pickle.load(model_file)
                self.para_loaded = True
        else:
            self.A = {}
            self.B = {}
            self.pi = {}
            self.para_loaded = False

    def train(self):
        def word2tag(word):
            if len(word) == 0:
                return ''
            if len(word) == 1:
                return 'S'
            else:
                return 'B' + 'M' * (len(word) - 2) + 'E'
        
        self.try_load_model(False)
        tag_count = {'B':0,'S':0,'M':0,'E':0}
        # tags = []
        with open(self.train_data_path, 'r', encoding='UTF-8') as train_data:
            i = 0
            for line in train_data.readlines():
                if i % 1000 == 0:
                    print("current line No: ",i)
                tag_line = []
                words = line.split(' ')
                words_str = "".join(words)
                for word in words:
                    #训练样本转换为tag序列
                    tag_word = word2tag(word)
                    tag_line.append(tag_word)
                    tag_line_str = "".join(tag_line)

                for j in range(len(tag_line_str)):
                    #计算pi 每个句子的第一个字符的状态频度
                    if j == 0:
                        p = tag_line_str[0]
                        if p not in self.pi:
                            self.pi[p] = 0
                        self.pi[p] += 1

                    tag_current = tag_line_str[j]
                    tag_count[tag_current] += 1
                    if j < len(tag_line_str) - 1:
                        #计算A 状态转移频度
                        if tag_current not in self.A:
                            self.A[tag_current] = {}
                        tag_next = tag_line_str[j + 1]
                        if tag_next not in self.A[tag_current]:
                            self.A[tag_current][tag_next] = 0
                        self.A[tag_current][tag_next] += 1
                        
                    #计算B 发射频度
                    if tag_current not in self.B:
                        self.B[tag_current] = {}
                    word_current = words_str[j]
                    if word_current not in self.B[tag_current]:
                        self.B[tag_current][word_current] = 0
                    self.B[tag_current][word_current] += 1
                # print("words_str:",words_str)
                # print("tag_str:",tag_line_str)
                # print("A:",self.A)
                # print("B:",self.B)
                # print("pi:",self.pi) 
                # tags.append[tag_line]
                i += 1
        #计算频率
        self.pi = {k:v/i for k,v in self.pi.items()}
        self.A = {k1:{k2:v2/tag_count[k1] for k2,v2 in v1.items()} for k1,v1 in self.A.items()}
        self.B = {k1:{k2:v2/tag_count[k1] for k2,v2 in v1.items()} for k1,v1 in self.B.items()}
        #dump到文件
        with open(self.model_path, 'wb') as f:
            pickle.dump(self.A, f)
            pickle.dump(self.B, f)
            pickle.dump(self.pi, f)

    def test(self):
        self.try_load_model(True)
        # print("A:",self.A)
        # print("B:",self.B)
        print("pi:",self.pi)
    

    def viterbi(self, sentence):
        V = [{}]
        path = {}
        for i in self.state:
            V[0][i] = self.pi.get(i, 0) * self.B[i].get(sentence[0], 0)
            path[i] = [i]
        print("path 1 :",path)
        for i in range(1, len(sentence)):
            V.append({})
            newpath = {}
            chr_not_exists = sentence[i] not in self.B['B'] and \
                    sentence[i] not in self.B['M'] and \
                    sentence[i] not in self.B['S'] and \
                    sentence[i] not in self.B['E']
            for y in self.state:
                b = self.B[y].get(sentence[i], 0) if not chr_not_exists else 1.0
                prob_state_list = [(V[i - 1][y0] * self.A[y0].get(y, 0) * b, y0)
                    for y0 in self.state if V[i - 1][y0] > 0]
                (prob, state) = max(prob_state_list)
                V[i][y] = prob
                newpath[y] = path[state] + [y]
            path = newpath
        if self.B['M'].get(sentence[-1], 0) > self.B['S'].get(sentence[-1], 0):
            (prob, state) = max([(V[len(sentence) - 1][y], y) for y in ('E', 'M')])
        else:
            (prob, state) = max([(V[len(sentence) - 1][y], y) for y in self.state])
        print(path)
        return prob, path[state]

    def cut(self, sentence, delimiter = '/'):
        if not self.para_loaded:
            self.try_load_model(os.path.exists(self.train_data_path))
        prob, tag_list = self.viterbi(sentence)
        res = []
        begin, next = 0, 0
        # print(prob)
        # print("tag_list:", tag_list)
        for i in range(len(tag_list)):
            if tag_list[i] == 'S':
                next = i + 1
                res.append(sentence[i])
            elif tag_list[i] == 'B':
                begin = i
            elif tag_list[i] == 'E':
                next = i + 1
                res.append(sentence[begin:next])
        if next < len(sentence):
            res.append(sentence[next:])
        return delimiter.join(res)

hmm = HMM()
# hmm.train()
# hmm.test()
print(hmm.cut("中文博大精深！"))
print(hmm.cut("这是一个非常棒的方案"))
print(hmm.cut("中华人民共和国万岁！"))
print(hmm.cut("中国共产党万岁！"))

print(hmm.cut("pjp搜索了一番才知道只能安装官方包而如同等第三方包要使用去安装但是在随后的匹配安装过程中还是报错有可能是网速的愿意也有可能是你没用管理员权限去运行命令行的原因总之多试几次有时还有可能是你的版本比较低升级一下也有可能解决问题"))