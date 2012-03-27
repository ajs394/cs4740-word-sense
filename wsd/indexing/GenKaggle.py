import FeatVectors

class GenKaggle:

    def __init__(self):
        self.word_list = []

    def build_list(self, filename = "test.data"):
        with open(filename) as f:
            for line in f:
                w = line.strip().split()
                if not (w[0] in self.word_list):
                    senses = 0
                    i = 1
                    while not (w[i] == '@'):
                        senses = i
                        i += 1
                        
                    self.word_list += [(w[0], senses)]

    def write_word(self, f, word, senses):
        results_path = "../Outputs/"+word+"_output.txt"
        
        res = open(results_path)
        fv = FeatVectors.FeatVectors()

        for line in res:
            num = int(float(line.strip()))
            sense_str = fv.gen_sense(num, senses)
            for ch in sense_str.split():
                f.write(ch+'\n')

    def write_kaggle(self):
        f = open('../Outputs/kaggle.txt', 'w')
        for (word, senses) in self.word_list:
            self.write_word(f, word, senses)

    def run(self):
        self.build_list()
        self.write_kaggle()
                
            
        
