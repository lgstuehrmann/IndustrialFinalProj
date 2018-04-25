#!/usr/bin/python
import Tkinter as tk
import socket
from PIL import ImageTk, Image
window = tk.Tk()
global order
def black():
	global order
	order = "1"
	window2 = tk.Toplevel(window)
	
	cat_img2 = ImageTk.PhotoImage(Image.open("exc.gif"))

	window2.title("Order Confirmation")
	window2.geometry("600x500")
	window2.configure(background='white')
	tk.Label(window2, 
		 text="YOU HAVE ORDERED BLACK COFFEE!",
		 fg = "blue",
		 bg = "yellow",
		 font = "Verdana 18 bold").pack()

	background = tk.Label(window2,compound = tk.CENTER,image=cat_img2).pack(side="bottom")
	UDP_sending()
	window2.mainloop()
	

def with_Sugar():
	global order
	order = "2"
	window2 = tk.Toplevel(window)

	cat_img2 = ImageTk.PhotoImage(Image.open("cat5.gif"))

	window2.title("Order Confirmation")
	window2.geometry("600x500")
	window2.configure(background='white')
	tk.Label(window2, 
		 text="YOU HAVE ORDERED COFFEE WITH SUGAR!",
		 fg = "blue",
		 bg = "yellow",
		 font = "Verdana 18 bold").pack()

	background = tk.Label(window2,compound = tk.CENTER,image=cat_img2).pack(side="bottom")
	UDP_sending()
	window2.mainloop()

	
def with_Milk():
	global order
	order = "3"
	window2 = tk.Toplevel(window)
	
	cat_img2 = ImageTk.PhotoImage(Image.open("cat2.jpg"))

	window2.title("Order Confirmation")
	window2.geometry("600x500")
	window2.configure(background='white')
	tk.Label(window2, 
		 text="YOU HAVE ORDERED COFFEE WITH MILK!",
		 fg = "blue",
		 bg = "yellow",
		 font = "Verdana 18 bold").pack()

	background = tk.Label(window2,compound = tk.CENTER,image=cat_img2).pack(side="bottom")
	UDP_sending()
	
	window2.mainloop()
	
def both():
	global order
	order = "4"
	window2 = tk.Toplevel(window)

	
	cat_img2 = ImageTk.PhotoImage(Image.open("pizza.gif"))

	window2.title("Order Confirmation")
	window2.geometry("600x500")
	window2.configure(background='white')
	tk.Label(window2, 
		 text="YOU HAVE ORDERED COFFEE WITH EVERYTHING!",
		 fg = "blue",
		 bg = "yellow",
		 font = "Verdana 14 bold").pack()

	background = tk.Label(window2,compound = tk.CENTER,image=cat_img2).pack(side="bottom")
	UDP_sending()
	window2.mainloop()

def small():
	global order
	order ="s"
	UDP_sending()
def medium():
	global order
	order= "m"
	UDP_sending()
def large():
	global order
	order= "l"
	UDP_sending()	
def make_GUI():
	
	window.title("Coffee Shop")
	window.geometry("700x600")
	window.configure(background='gray')

	cat_img = ImageTk.PhotoImage(Image.open("cat.gif"))

	background = tk.Label(window,compound = tk.CENTER,image=cat_img).pack(side="bottom")
	tk.Label(window, 
		 text="COFFEE MENU",
		 fg = "white",
		 bg = "navy",
		 font = "Verdana 18 bold").pack()
		 
	tk.Label(window,text="Choose a size",bg="white",fg = "navy",font = "Verdana 12 bold").pack()
	button = tk.Button(window, text='Small',compound = tk.CENTER, width=25, command=small).pack()
	button = tk.Button(window, text='Medium',compound = tk.CENTER, width=25, command=medium).pack()
	button = tk.Button(window, text='Large',compound = tk.CENTER, width=25, command=large).pack()
			 
	tk.Label(window,text="Choose a coffee type",bg="white",fg = "navy",font = "Verdana 12 bold").pack()
	button = tk.Button(window, text='Black',compound = tk.CENTER, width=25, command=black).pack()
	button = tk.Button(window, text='With Sugar',compound = tk.CENTER, width=25, command=with_Sugar).pack()
	button = tk.Button(window, text='With Milk',compound = tk.CENTER, width=25, command=with_Milk).pack()
	button = tk.Button(window, text='Both',compound = tk.CENTER, width=25, command=both).pack()
	

	window.mainloop()

def UDP_sending():
   global order
   UDP_IP = "127.0.0.1"
   UDP_PORT = 5005
   MESSAGE = order
   print(order)
   sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,0) # internet,UDP
   sock.connect((UDP_IP,UDP_PORT))
   
   sock.send(MESSAGE)
   
   sock.close()
if __name__ == "__main__":
	
	make_GUI()
