import subprocess
import os

class Learn:

    def __init__(self):
        return

    def learn_file(self, filename):
        subprocess.check_output("java -cp .;lib/weka.jar Learn train ../Data/"+filename+".train.arff ../Classifiers/"+filename+"_classifier.serialized")
        subprocess.check_output("java -cp .;lib/weka.jar Learn test ../Classifiers/"+filename+"_classifier.serialized ../Data/"+filename+".test.arff ../Outputs/"+filename+"_output.txt")

    def learn(self):
        for r,d,f in os.walk("../Data"):
            for files in f:
                if files.endswith("train.arff"):
                    self.learn_file(files.title()[0:-11])

    def run(self):
        self.learn()
