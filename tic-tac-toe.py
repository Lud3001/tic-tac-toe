import tkinter
root = tkinter.Tk()
root.geometry('600x600')
root['bg'] = 'white'
root.title('tic-tac-toe')
user=1
game_run= True

def con(x,y):
    global user , data
    if game_run == True:
        if user == 1:
            if data[x][y]['text'] == '':
                data[x][y]['text'] = 'X'
                win_combs('X')
                user = 2
        elif user == 2:
            if data[x][y]['text'] == '':
                data[x][y]['text'] = 'O'
                win_combs('O')
                user = 1
    else:
        delete()

def delete(winwin):
    for i in range (3):
        for j in range(3):
            data[i][j].destroy()
    endgame= tkinter.Label(root, text= f'{winwin} is the winner! \n Would you like to start a new game?', justify='center', font=20 , bg='white', fg='black')
    endgame.place(width=400, height=250, x=100, y=50)
    newgame()
            
def newgame():
    cont_btn= tkinter.Button(root, text='Start a new game', bg='black', fg='white', command=new_command)
    cont_btn.place(x=150, y=200, width=200, height=100)


def new_command():
    global data
    data.clear()
    for j in range(3):
        root.columnconfigure(index=j, weight=1)
    for i in range(3):
        root.rowconfigure(index=i, weight=1)
    for i in range(3):
        lst_line = []
        for j in range(3):
            btn = tkinter.Button(root, text='', bg='black', fg='white' ,command=lambda x = i, y = j: con(x,y))
            btn.grid(row=i, column=j, sticky='NSEW')
            lst_line.append(btn)
        data.append(lst_line)



def similarity(simbol, b_1, b_2, b_3):
    if b_1['text'] == b_2['text'] and b_2['text'] == b_3['text'] and b_1['text'] == simbol:
        b_1['bg'] = 'green'
        b_2['bg'] = 'green'
        b_3['bg'] = 'green'
        game_run = False
    
        
        
        

    
def win_combs(simbol):
    for i in range(3):
        similarity(simbol, data[i][0], data[i][1], data[i][2])
        similarity(simbol, data[0][i], data[1][i], data[2][i])
    similarity(simbol, data[0][0], data[1][1], data[2][2])
    similarity(simbol , data[2][0],data[1][1], data[0][2])

for j in range(3):
    root.columnconfigure(index=j, weight=1)

for i in range(3):
    root.rowconfigure(index=i, weight=1)

data = []
for i in range(3):
    lst_line = []
    for j in range(3):
        btn = tkinter.Button(root, text='', bg='black', fg='white' ,command=lambda x = i, y = j: con(x,y))
        btn.grid(row=i, column=j, sticky='NSEW')
        lst_line.append(btn)
    data.append(lst_line)


#btn_end= tkinter.Button(root, text='finish the game', fg='white', bg='black', font=20, justify='center' )
#btn.place(width=200, height=100, x=200 , y=250)




    

    










root.mainloop()