import ArffGen
import Learn
import GenKaggle
import subprocess
import Allformats

print "compiling java"
subprocess.check_output("compile.bat")
print "success\n"

print "generating arff files.  This process may take a minute."
ag = ArffGen.ArffGen()
ag.run()
print "success\n"

print "reformatting arff files"
Allformats.reformat_all()
print "success\n"

print "learning.  This may take a minute and windows may open.  Do not be alarmed."
l = Learn.Learn()
l.run()
print "success\n"

print "generating output file"
gk = GenKaggle.GenKaggle()
gk.run()
print "success\n"
