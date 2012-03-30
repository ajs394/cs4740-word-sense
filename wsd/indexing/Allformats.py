import os
numattr = 0

CP = 'lib/weka.jar' 

def reformat_all():
    for f in os.listdir("../Data"):
        if ".arff" in f:
            reformat("../Data/"+f, "../new_arffs/"+f)

def rank_attr_by_info_gain(fileinput, fileoutput):
    cmmd = 'java -cp ' + CP + ' weka.filters.supervised.attribute.AttributeSelection -S \"weka.attributeSelection.Ranker -N ' + str(3) + '\" -E \"weka.attributeSelection.InfoGainAttributeEval\" -i ' + fileinput + ' -o ' + fileoutput + ' -c last'
    #print cmmd
    os.system(cmmd)


def make_binary(filename, outfilename):
	f = open(filename, 'r')
	known_numbers = {}
	known_nums=[]
	arff_vectors =[]
	classes = []
	for line in f:
		if not "@" in line and "," in line:
			line = line.split(", ");
			line[-1]=line[-1][:-1]
			#print line
			classes+=[line[-1]] if line[-1] not in classes else []
			cur_vector = []
			for number in line[:-1]:
				if number not in known_numbers:
					known_numbers[number] = len(known_numbers)
					known_nums+=[number]
				cur_vector+=[known_numbers[number]]
				#cur_vector+=[known_nums.index(number)]
			cur_vector+=[line[-1]]
			arff_vectors+=[cur_vector]
	f.close()
	
	global numattr	
	numattr = len(known_numbers)
	#print numattr
	f =open(outfilename,'w')

	f.write("% \n@RELATION wsd\n")
	for number in known_nums:
		f.write("@ATTRIBUTE "+str(number)+" {1,0}\n")
	
	all_words_string = "{"
	class_string = "{"
	for class_id in classes:
		class_string+=str(class_id)+", "
	class_string= class_string[:-2]+"}\n"
	f.write("@ATTRIBUTE class "+class_string)
	f.write("\n@DATA\n")
	for vector in arff_vectors:
		cur_line = ""
		for i in range(len(known_numbers)):
			cur_line+=str(1 if i in vector[:-1] else 0)+", "
		cur_line+=str(vector[-1])+'\n'
		f.write(cur_line)
	f.close()
	
def fix_classes(input_file, output_file):
	class_line = ""
	new_class_line=""
	prev_line = ""
	attribute_text=""
	body_text=""

	f = open(input_file, 'r')
	for line in f:
		if "@" in line or "%" in line or len(line.split(","))<2:
			if "class" in line:
				class_line = line
				new_class_line = line
			attribute_text+=line
		if "@" not in line and "," in line:
			if prev_line == "":
				prev_line = line
			else:
				if not line.split()[:-1]==prev_line.split()[:-1]:
					body_text+=prev_line
					prev_line = line
				else:
					prev_line = prev_line[:-1]+'_'+line.split()[-1]
					new_class = prev_line.split(',')[-1]
					if new_class not in new_class_line:
						new_class_line = new_class_line[:-2]+","+new_class+"}\n"
					prev_line = prev_line+"\n"
	f.close()
	f = open(output_file, 'w')
	f.write(attribute_text.replace(class_line, new_class_line))
	f.write(body_text)
	f.close()
	
def reformat(infile, outfile):
	make_binary(infile, outfile)
	fix_classes(outfile, outfile)


reformat_all()
