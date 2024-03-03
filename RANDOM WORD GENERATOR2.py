from tkinter import * 
import random

root= Tk()

root.title("RANDOM WORD GENERATOR")
root.geometry("500x500")
root.configure(background = "yellow")

list1 = ["q" ,"w" ,"e" ,"r" ,"t" ,"y" ,"u" ,"i" ,"o" ,"p" ,"a" ,"s" ,"d" ,"f" ,"g" ,"h" ,"j" ,"k" ,"l" ,"z" ,"x" ,"c" ,"v" ,"b" ,"n" ,"m"]
print(list1)

def random_number():
    random_no = random.randint(0, 26)
    print(random_no)
    random_lucky_friend = list1[random_no]
    print("random no: " + random_lucky_friend)
    
btn1 = Button(root)
btn1 = Button(root,  text= "Generated Random Words ", command= random_number, bg="lightblue")
btn1.place(relx=0.5, rely=0.4, anchor=CENTER )
root.mainloop()
