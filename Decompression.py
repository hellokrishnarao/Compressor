class Decompressor():

    hash_pairs = []
    hash_d = {}
    n_file_data = []
    final_file = ""
    a=[]

    # read hash file and store in a list the key,value pair

    def map_hash(self):
        hashFile = open("hash_file.txt", "r")
        for i in hashFile.readlines():
            e = i.split()
            self.hash_pairs.append(e)
            print("this is a hash_pair",e,"forline",i)
         #   print(self.hash_pairs)
       # print("hashpairs",self.hash_pairs)

    #converting the hash file to dictionary via list

    def new_hash(self):
        i = 0
        while i <len(self.hash_pairs):
            self.hash_d[self.hash_pairs[i][1]] = self.hash_pairs[i][0]
            i+=1
        # print("hp",self.hash_pairs,"hd",self.hash_d)
        #print("hashd",self.hash_d)

    # final decompression by replacing keys with words and adding new line character

    def replace_keys_with_word_in_compressed_file(self):
        s = ""
        decomp = open("decomp.txt","w")
        handle_comp = open("compressed.txt", "r")
        comp = handle_comp.read().split()
       # print("comp",comp)
        for i in comp:
            if i !='~' and i in self.hash_d.keys():
                s= s+ self.hash_d[i] +  " "
            elif i!='~' and i not in self.hash_d.keys():
                s = s + i+" "
            elif i == '~':
                decomp.write(s)
                decomp.write("\n")
                s=""

# d = Decompressor()
# d.map_hash()
# d.new_hash()
# d.replace_keys_with_word_in_compressed_file()

