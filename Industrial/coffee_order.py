#!/usr/bin/python
import Tkinter as tk
import socket
from PIL import ImageTk, Image
window = tk.Tk()
order = "0"
def black():
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
	window2.mainloop()

def with_Sugar():
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
	window2.mainloop()
	
def with_Milk():
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
	window2.mainloop()
	
def both():
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
	window2.mainloop()
def make_GUI():
	
	window.title("Coffee Shop")
	window.geometry("600x500")
	window.configure(background='gray')

	cat_img = ImageTk.PhotoImage(Image.open("cat.gif"))

	background = tk.Label(window,compound = tk.CENTER,image=cat_img).pack(side="bottom")
	tk.Label(window, 
		 text="COFFEE MENU",
		 fg = "white",
		 bg = "navy",
		 font = "Verdana 18 bold").pack()
	button = tk.Button(window, text='Black',compound = tk.CENTER, width=25, command=black).pack()
	button = tk.Button(window, text='With Sugar',compound = tk.CENTER, width=25, command=with_Sugar).pack()
	button = tk.Button(window, text='With Milk',compound = tk.CENTER, width=25, command=with_Milk).pack()
	button = tk.Button(window, text='Both',compound = tk.CENTER, width=25, command=both).pack()

	window.mainloop()

def UDP_sending():
   UDP_IP = "127.0.0.1"
   UDP_PORT = 5005
   MESSAGE = order
   sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,0) # internet,UDP
   sock.connect((UDP_IP,UDP_PORT))
   
   sock.send(MESSAGE)
   
   sock.close()
if __name__ == "__main__":
	
	make_GUI()
