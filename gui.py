from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk
from tkinter import filedialog
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from Compression import Compressor
from Decompression import Decompressor
import os
window = Tk()
window.title("File Compression Progress Window")
window.geometry('700x500')
style = ttk.Style()
window.configure(background="white")

################################## 

lbl = Label(window, text="Select the file to be Compressed: ", font=("Arial Bold", 15))
lbl.grid(column=0, row=0)
lbl.configure(background="white")

#############################################

name = ''
def OpenFile():
	global name
	name = askopenfilename(initialdir="/",
                           filetypes =(("Text File", "*.txt"), ("All Files", "*.*")),
                           title = "Choose a text file."
                           )
    
    #Using try in case user types in unknown file or closes without choosing a file.
	try:
		with open(name,'r') as UseFile:
			print("File is opened")
			lbl1 = Label(window, text=name, font=("Arial Bold", 15))
			lbl1.grid(column=4, row=0)
			lbl1.configure(background="white")
			Button(window, text='Compress', command=compress).grid(row=2, column=0, sticky=W, pady=4)
		
	except:
		print("Error while opening the file!")
      
def compress():	
	try:
		style.configure("black.Horizontal.TProgressbar", background='black')
		bar = Progressbar(window, length=100, style='black.Horizontal.TProgressbar')
		bar.grid(column=6, row=5)
		bar['value'] =100
		print('Compressor started')
		print(name)
		c = Compressor()
		c.read_file(name)
		c.get_sorted_tuple()
		c.make_hash()
		c.create_compressed_file()
		c.create_hash_table()
		print("Compression Sucessful")
		lbl = Label(window, text="Compression Sucessful", font=("Arial Bold", 15))
		lbl.grid(column=3, row=6)
		lbl.configure(background="white")
		Button(window, text='Decompress', command=decompress).grid(row=3, column=0, sticky=W, pady=4)
		Button(window, text='Efficiency', command=efficiency).grid(row=4, column=0, sticky=W, pady=4)
	except:
		lbl1 = Label(window, text="Compression Failed", font=("Arial Bold", 15))
		lbl1.grid(column=4, row=6)
		lbl1.configure(background="white")


def decompress():
	try:
		
		d = Decompressor()
		#d.read_file()
		d.map_hash()
		d.new_hash()
		d.replace_keys_with_word_in_compressed_file()

		lbl1 = Label(window, text=" Deompression Sucessful ", font=("Arial Bold", 15))
		lbl1.grid(column=3	, row=7)
		lbl1.configure(background="white")

	except:
		lbl1 = Label(window, text=" Deompression Failed ", font=("Arial Bold", 15))
		lbl1.grid(column=3, row=7)
		lbl1.configure(background="white")


def efficiency():
	stats = os.stat(name)
	print("The size of original file:", stats.st_size)
	big = int(stats.st_size)
	comp = os.stat("compressed.txt")
	hashed = os.stat("hash_file.txt")
	total = comp.st_size + hashed.st_size
	print("The size of Compressed file + Hash File", total)
	Percentage = 100 - float((total/stats.st_size)*100)
	print("Compression Percentage:", Percentage)
	lbl2 = Label(window, text="The size of original file: ", font=("Arial Bold", 15))
	lbl2.grid(column=0, row=7)
	lbl2.configure(background="white")
	lbl3 = Label(window, text=big, font=("Arial Bold", 15))
	lbl3.grid(column=0, row=8)
	lbl3.configure(background="white")
	lbl4 = Label(window, text="The size of Compressed file", font=("Arial Bold", 15))
	lbl4.grid(column=0, row=10)
	lbl4.configure(background="white")
	lbl5 = Label(window, text=total, font=("Arial Bold", 15))
	lbl5.grid(column=0, row=11)
	lbl5.configure(background="white")
	lbl6 = Label(window, text="The Compression efficiency (in %)", font=("Arial Bold", 15))
	lbl6.grid(column=0, row=12)
	lbl6.configure(background="white")
	lbl7 = Label(window, text=Percentage, font=("Arial Bold", 15))
	lbl7.grid(column=0, row=13)
	lbl7.configure(background="white")


Button(window, text='Open', command=OpenFile).grid(row=1, column=0, sticky=W, pady=4)

Button(window, text='Quit', command=quit).grid(row=5, column=0, sticky=W, pady=4)


def quit():
	window.close()
window.mainloop()

