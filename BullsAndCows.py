import random
from tkinter import *
from tkinter import messagebox as mb
import webbrowser
import os

class glob():
    pass

global root, GLOB

G = glob()

G.num = 0
G.player_move_text = ''
G.text_score = ''
G.imb = 0
G.schet_igri = 10000

while len(set(str(G.num))) != 4:  
    G.num = random.randint(1000, 9999)

lst1 = list(str(G.num))

#============================================================================
def igra():
    
    G.name = e.get()
    if G.name != '':
        
        l.destroy()
        b.destroy()
        e.destroy()
        
        G.pravila = Label(text = igra, background = 'white', font = 'Times 14',
              borderwidth = 2, relief = "solid")
        G.pravila.place(x = 40, y = 60, height = 200, width = 520)
        
        G.score = Label(text = 'Счёт: ' + str(G.schet_igri), anchor = W, background = 'white',\
                        font = 'Times 20', borderwidth = 2, relief = "solid")
        G.score.place(x = 410, y = 10, height = 30, width = 150)
        
        G.b1 = Button(text = 'Сделать ход', command = player_move, background = 'white',\
                      font = 'Times 15', borderwidth = 2, relief = "raised")
        G.b1.place(x = 400, y = 700, height = 30, width = 170)
        
        G.hod = Entry(borderwidth = 2, relief = "solid", font = 'Times 15')
        G.hod.place(x = 225, y = 700, height = 30, width = 150)
        
        G.kolvo_pop = Label(text = 'Попыток осталось: 10', anchor = W, background = 'white',\
                            font = 'Times 13', borderwidth = 1, relief = "solid")
        G.kolvo_pop.place(x = 35, y = 700, height = 30, width = 170)
        
        G.popitky = Label(text = 'Здесь будут отображаться\n ваши ходы.', anchor = N,
              background = 'white', font = 'Times 15', borderwidth = 1, relief = "solid")
        G.popitky.place(x = 310, y = 350, height = 235, width = 250)
        
        G.schet = Label(text = pravila_ochkov, anchor = N,
              background = 'white', font = 'Times 15', borderwidth = 1, relief = "solid")
        G.schet.place(x = 40, y = 350, height = 235, width = 250)
        
    elif 1:
    	mb.showerror('Ошибка', 'Пожалуйста, введите ваше имя!')
    	
    elif 0: pass
    
#============================================================================
def player_move():

    while True:
        
        if G.imb < 10:
            G.imb = G.imb+1
            pop = 10 - G.imb
        
            a = G.hod.get()
            if len(set(str(a))) != 4 or len(str(a)) != 4:
                mb.showerror('Ошибка', 'Число должно состоять из 4 неповторяющихся цифр!')
                return
            
            a_lst = list(a)
            cows = 0
            bulls = 0
            cows_score = 0
            bulls_score = 0
            
            if lst1 == a_lst:
                G.rez = 'Вы победили!'
                okno_vihoda()
                return
                
            if lst1[0] == a_lst[0]:
                bulls = bulls + 1
            if lst1[1] == a_lst[1]:
                bulls = bulls + 1
            if lst1[2] == a_lst[2]:
                bulls = bulls + 1
            if lst1[3] == a_lst[3]:
                bulls = bulls + 1

            for i in range (0, 4):
                cows = cows + a_lst.count(lst1[int(i)])
            cows = cows - bulls
            
        if pop == 0:
            G.rez = 'Вы проиграли.'
            G.schet_igri = 0
            okno_vihoda()  
        try:
            player_num = G.hod.get()
            G.player_move_text = G.player_move_text + player_num + ': быки - ' +\
                               str(bulls) + ', коровы - ' + str(cows) + '\n'
            G.popitky.config(text = G.player_move_text)
            kolvo_pop_text = 'Попыток осталось: ' + str(pop)
            G.kolvo_pop.config(text = kolvo_pop_text)
            G.hod.delete(0, END) 
            cow_score = 250 * cows
            bulls_score = 500 * bulls
            G.schet_igri = G.schet_igri - 1000 + cow_score + bulls_score
            G.text_score = G.text_score + 'быки: +' + str(bulls_score) + ', коровы: +' + str(cow_score) + '\n'
            G.schet.config(text = G.text_score)
            G.score.config(text = 'Счёт: ' + str(G.schet_igri))
            return
        except:
            return
        
#============================================================================        
def save(player_name, player_score_1):
    
    schet_iz_faila(player_name)
    
    Game0 = open('BullsAndCows_0.txt', 'w')
    Game = open('BullsAndCows.txt')
    
    for g in range (0, 2000):
		
        line = Game.readline()   
        
        if line == '':
            break
            
        for k in range (0, len(line)):
			
            symbol = line[k:k+1]
            
            if symbol == '\t':
                name_place = line[:k]
                break

            continue

        if name_place == player_name:
            pass
            
        elif name_place == '':
            break
            
        else:
             Game0.write(line)
    
        continue
    
    G.player_score_0 = G.player_score + player_score_1
    zapis = player_name + '\t' + str(G.player_score_0) + '\n'

    Game0.write(zapis)
    Game0.close()
    Game.close()
    
    os.remove('BullsAndCows.txt')
    os.rename('BullsAndCows_0.txt', 'BullsAndCows.txt')
    
#============================================================================
def schet_iz_faila(player_name1):
   
    try:
		
        Game = open('BullsAndCows.txt')
        
        for g in range (0, 101):
			
            read_line = Game.readline()
            
            if read_line == '':
                break
                
            for k in range (0, len(read_line)):
				
                symbol = read_line[k:k+1]
                
                if symbol == '\t':
					
                    score = read_line[k+1:]
                    find_name = read_line[:k]
                    break
                    
            if find_name == player_name1:
                break


            continue

        if read_line == '':
            score = '0'
            
        G.player_score = int(score)
        Game.close()

    except IOError:
		
        Game = open('BullsAndCows.txt', 'w')
        G.player_score = 0
    
#============================================================================
def okno_vihoda():
    
    schet_iz_faila(G.name)
    G.player_score_0 = G.player_score + G.schet_igri
    
    def vihod():
        if G.rez == 'Вы победили!':
            G.rez = 'Вы победили! Начислено очков: ' + str(G.schet_igri)
            webbrowser.open('https://www.youtube.com/watch?v=lXxUPo9tRao&ab_channel=TheStupidWaffle', new=2)
            save(G.name, G.schet_igri)
            root.destroy()
        elif 1:
            root.destroy()  
        elif 0:pass
        
        return
    
    G.pravila.destroy()
    G.score.destroy()
    G.b1.destroy()
    G.hod.destroy()
    G.kolvo_pop.destroy()
    G.popitky.destroy()
    G.schet.destroy()

    poka = Label(text = G.rez + ' Загаданное число: ' + str(G.num) + '\nСпасибо за игру!\nОбщий счёт: ' +\
                 str(G.player_score_0), background = 'white', font = 'Times 20', borderwidth = 2,\
                 relief = "solid")
    poka.place(x = 40, y = 60, height = 200, width = 520)
    knopka = Button(text = 'Выход', command = vihod, background = 'white', font = 'Times 30',
           borderwidth = 2, relief = "raised")
    knopka.place(x = 100, y = 400, height = 100, width = 400)
       
root = Tk()

root.title('BullsAndCows')
root.geometry('600x800')
root.resizable(width = False, height = False)
filename = PhotoImage(file = "cow.png")
background_label = Label(image = filename)
background_label.place(x = -2, y = -2)

l = Label(text = 'Введите ваше имя:', background = 'white', font = 'Times 40',
          borderwidth = 2, relief = "solid")
l.place(x = 40, y = 60, height = 150, width = 520)
b = Button(text = 'Начать игру', command = igra, background = 'white', font = 'Times 30',
           borderwidth = 2, relief = "raised")
b.place(x = 100, y = 400, height = 100, width = 400)
e = Entry(borderwidth = 2, relief = "solid", font = 'Times 20')
e.place(x = 200, y = 290, height = 50, width = 200)

igra = 'Компьютер загадывает 4-значное число,\n состоящее из неповторяющихся цифр. \n'+\
'Ваша задача - угадать его за 10 ходов. В качестве подсказок \nвыступают “коровы” '+\
'(цифра угадана, но её позиция - нет)\n и “быки” (когда совпадает и цифра и её позиция). \n'+\
'То есть если загадано число “1234”, а вы называете\n “6531”, то результатом будет 1 '+\
'корова (цифра “1”)\n и 1 бык (цифра “3”). \nЧисло загадано! Ваш ход.'

pravila_ochkov = 'Здесь будут отображаться\n ваши очки. \nВ начале каждой игры \nвам даётся 10000 очков. '+\
'\nЗа каждый неправильный \nход вы теряете 1000 очков. \n1 угаданный "бык" \nприбавляет вам 500 очков. ' +\
'\n1 "корова" - 250 очков. \nВаш прогресс сохраняется.'


root.mainloop()
