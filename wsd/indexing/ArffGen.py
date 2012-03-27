import FeatVectors
import datautil
import os

class ArffGen:
    def __init__(self):
        self.words = {}

    def get_words(self):
        return self.words

    def gen_words(self, train):
        self.words = {}
        
        if train:
            filename = "train.data"
        else:
            filename = "test.data"
        f = open(filename)
        for line in f:
            w = line.strip().split()
            self.words[w[0]] = ''

        #for key in self.words.keys():
        #    fv = FeatVectors.FeatVectors()
        #    fv.open_file(filename)
        #    self.words[key] = fv.dis_word(key)

        #for key in self.words.keys():
        #    for line in self.words[key]:
        #        cls = 0
        #        binary = line['sense'].strip().split()
                
        #        for i in range(0, len(binary)):
        #            cls += (2**(i))*int(binary[i])
        #        line['class'] = str(int(cls))

    def gen_index_file(self, word, train):
        if train:
            infile = "train.data"
            ex = '.train'
        else:
            infile = "test.data"
            ex = '.test'
        
        outfile = '../Data/'+word+'_index'+ex+'.index'
        fv = FeatVectors.FeatVectors()

        fv.dis_file(word, infile, outfile)
        
        #f = open(filename, 'w')

        #f.write('# Feature Count\n')
        #f.write(str(len(self.words[word][0]['coll_map'].split()))+'\n')

        #f.write('# Class count\n')
        #cls_max = 0
        #for ex in self.words[word]:
        #    cls_max = max(cls_max, int(ex['class']))
        #f.write(str(cls_max)+'\n')

        #.write('\n# Data\n')
        #for ex in self.words[word]:
        #    f.write(ex['coll_map'].strip()+' '+ex['class'].strip()+'\n')

        #f.close()

    def gen_arff_files(self, train):
        if train:
            ex = '.train'
        else:
            ex = '.test'
            
        for key in self.words.keys():
            self.gen_index_file(key, train)

        for r,d,f in os.walk("../Data"):
            for files in f:
                if files.endswith(ex+".index"):
                    fin = '../Data/'+files.title()
                    fout = '../Data/'+files.title()[0:-12-len(ex)]+ex+'.arff'
                    comment = files.title()[0:-12]+' arff file'
                    datautil.convert_index_file_to_arff(fin, fout, comment)
        

    def run(self, filename = None):  
        a = [True, False]
        
        for train in a:
            if filename == None:
                self.gen_words(train)
            else:
                self.gen_words(filename, train)
                
            self.gen_arff_files(train)
