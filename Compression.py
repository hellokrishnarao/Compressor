import operator
class Compressor:


    word_list = []
    sorted_counted_of_word ={}
    hash_symbols = {}
    file_data = []
    s = ""
    file_name=""
    para=[]

    # read the original file to be compressed

    def read_file(self, fileName):

        self.file_name = fileName
        fo = open(self.file_name, "r")
        self.word_list = fo.read().split()
        fo.close()

    # get a list of tuples with words arranged in descending order of their count

    def get_sorted_tuple(self):

        count_of_words = {}
        for elem in self.word_list:
            count_of_words[elem] = self.word_list.count(elem)
        self.sorted_counted_of_words = sorted(count_of_words.items(), key=operator.itemgetter(1), reverse=True)

    # make hash values that are to be replaced with the original strings in the file

    def make_hash(self):
        k = 0
        j = 0
        while k < len(self.sorted_counted_of_words):
            h = str(j)
            if len(self.sorted_counted_of_words[k][0]) >= len(h) and self.sorted_counted_of_words[k][1] > 2:
                self.hash_symbols[self.sorted_counted_of_words[k][0]] = h
                j += 1
            k += 1
            h = ""

    # create compressed file by replacing frequently occuring word by code in hsh file

    def create_compressed_file(self):

        fo2 = open(self.file_name, "r")
        for line in fo2.readlines():
            self.s=""
            a=line.split()
            for elem in a:
                if elem in self.hash_symbols.keys():
                    elem = self.hash_symbols[elem]
                    self.s = self.s + elem+" "
                else:
                    self.s = self.s + elem+ " "
           # self.s = self.s + "pch"+" "
            self.para.append(self.s)
       #     self.para.append((" # ").strip())
       # print("para",self.para)
        para1 = set(self.para)
        fo3 = open("compressed.txt", "w")

        for elem in self.para:
            fo3.write(elem)
            fo3.write("~")
            fo3.write(" ")
        fo3.close()
        fo4 = open("compressed.txt", "r")
       # print("file")
        #print(fo4.read())
        fo4.close()


    fo_hash = open("hash_file.txt", "w")

    def create_hash_table(self):

        for k in self.hash_symbols:
            self.fo_hash.write(k)
            self.fo_hash.write(" ")
            self.fo_hash.write(self.hash_symbols[k])
            self.fo_hash.write("\n")
        self.fo_hash.close()

# c = Compressor()
# c.read_file("bigfile.txt")
# c.get_sorted_tuple()
# c.make_hash()
# c.create_compressed_file()
# c.create_hash_table()
