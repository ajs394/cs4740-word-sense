import ArffGen
import Learn
import GenKaggle

ag = ArffGen.ArffGen()
ag.run()

l = Learn.Learn()
l.run()

gk = GenKaggle.GenKaggle()
gk.run()
