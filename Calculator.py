from tkinter import *
app=Tk()
app.geometry('500x500')
app.title('CALCULATOR')
result=Variable(app)
value=Variable(app)
box=Entry(app, textvariable=value,width=79,bg='grey', ).place(x=10,y=10,height=80)
input_val= ''
def operate(e):
    global input_val
    input_val += str(e)
    value.set(input_val)
def clear():
    global input_val
    input_val=''
    value.set('')
def output(f):
    global input_val
    value.set(eval(input_val))
    input = ''
Button(app, text='1',bd=3,fg='black',bg='dark gray',relief='raised',width=15,height=5,command=lambda:operate('1')).place(x=20,y=190)
Button(app, text='2',bd=3,fg='black',bg='dark gray',relief='raised',width=15,height=5,command=lambda:operate('2')).place(x=140,y=190)
Button(app, text='3',bd=3,fg='black',bg='dark gray',relief='raised',width=15,height=5,command=lambda:operate('3')).place(x=260,y=190)
Button(app, text='4',bd=3,fg='black',bg='dark gray',relief='raised',width=15,height=5,command=lambda:operate('4')).place(x=20,y=270)
Button(app, text='5',bd=3,fg='black',bg='dark gray',relief='raised',width=15,height=5,command=lambda:operate('5')).place(x=140,y=270)
Button(app, text='6',bd=3,fg='black',bg='dark gray',relief='raised',width=15,height=5,command=lambda:operate('6')).place(x=260,y=270)
Button(app, text='7',bd=3,fg='black',bg='dark gray',relief='raised',width=15,height=5,command=lambda:operate('7')).place(x=20,y=350)
Button(app, text='8',bd=3,fg='black',bg='dark gray',relief='raised',width=15,height=5,command=lambda:operate('8')).place(x=140,y=350)
Button(app, text='9',bd=3,fg='black',bg='dark gray',relief='raised',width=15,height=5,command=lambda:operate('9')).place(x=260,y=350)
Button(app, text='0',bd=3,fg='black',bg='dark gray',relief='raised',width=15,height=5,command=lambda:operate('0')).place(x=140,y=430)
Button(app, text='+',bd=3,fg='black',bg='sky blue',relief='raised',width=15,height=5,command=lambda:operate('+')).place(x=380,y=190)
Button(app, text='-',bd=3,fg='black',bg='sky blue',relief='raised',width=15,height=5,command=lambda:operate('-')).place(x=380,y=270)
Button(app, text='x',bd=3,fg='black',bg='sky blue',relief='raised',width=15,height=5,command=lambda:operate('*')).place(x=380,y=350)
Button(app, text='÷',bd=3,fg='black',bg='sky blue',relief='raised',width=15,height=5,command=lambda:operate('/')).place(x=380,y=430)
Button(app, text='=',bd=3,fg='black',bg='light green',relief='raised',width=15,height=5,command=lambda:output('=')).place(x=260,y=430)
Button(app, text='Clr',bd=3,fg='white',bg='red',relief='raised',width=15,height=5,command=lambda:clear()).place(x=380,y=110)
Button(app, text='.',bd=3,fg='black',bg='dark gray',relief='raised',width=15,height=5,command=lambda:operate('.')).place(x=20,y=430)
app.mainloop()