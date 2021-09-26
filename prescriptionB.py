from tkinter import *
root=Tk()
root.geometry('580x690')

label_title = Label(root, text='DOCTORS', font=('san fransisco', 20, 'bold'), bg='light grey', fg="red")
label_title.place(x=0, y=0)
label_title2 = Label(root, text='Medical Prescription', font=('san fransisco', 18, 'bold'), bg='light grey',
                     fg='black')
label_title2.place(x=0, y=40)

frame1 = Frame(root, bg='#66CDAA')
frame1.place(x=0, y=70, width=580, height=30)
frame2 = Frame(root, bg='#EEE9BF')
frame2.place(x=0, y=100, width=580, height=30)
frame3 = Frame(root, bg="#66CDAA")
frame3.place(x=0, y=130, width=580, height=30)

frame4 = Frame(root, bg='#EEE9BF')
frame4.place(x=0, y=160, width=580, height=30)
frame5 = Frame(root, bg='#EEE9BF')
frame5.place(x=0, y=190, width=580, height=30)
frame6 = Frame(root, bg='#EEE9BF')
frame6.place(x=0, y=220, width=580, height=30)

frame7 = Frame(root, bg='#66CDAA')
frame7.place(x=0, y=250, width=580, height=30)

frame8 = Frame(root, bg='#EEE9BF')
frame8.place(x=0, y=280, width=580, height=30)

frame9 = Frame(root, bg='#66CDAA')
frame9.place(x=0, y=310, width=580, height=30)

frame10 = Frame(root, bg='#EEE9BF')
frame10.place(x=0, y=340, width=580, height=30)
frame11 = Frame(root, bg='#66CDAA')
frame11.place(x=0, y=370, width=580, height=30)
frame12 = Frame(root, bg='#EEE9BF')
frame12.place(x=0, y=400, width=580, height=30)
frame13 = Frame(root, bg='#66CDAA')
frame13.place(x=0, y=430, width=580, height=30)
frame14 = Frame(root, bg='#EEE9BF')
frame14.place(x=0, y=460, width=580, height=30)
frame15 = Frame(root, bg='#66CDAA')
frame15.place(x=0, y=490, width=580, height=70)
frame16 = Frame(root, bg='#EEE9BF')
frame16.place(x=0, y=520, width=580, height=70)
frame17 = Frame(root, bg='#66CDAA')
frame17.place(x=0, y=590, width=580, height=70)
frame18 = Frame(root, bg='#EEE9BF')
frame18.place(x=0, y=660, width=580, height=30)




label1 = Label(root, text='Patients name:', bg='#66CDAA', font=('georgia', 11, 'bold'))
label1.place(x=0, y=72)
label2 = Label(root, text='Date:', bg='#66CDAA', font=('georgia', 11, 'bold'))
label2.place(x=350, y=72)
label3 = Label(root, text='Patients ID:', bg='#EEE9BF', font=('georgia', 11, 'bold'))
label3.place(x=0, y=102)
label4 = Label(root, text='Age:', bg='#EEE9BF', font=('georgia', 11, 'bold'))
label4.place(x=340, y=102)

label6 = Label(root, text='Gender:', bg='#66CDAA', font=('georgia', 11, 'bold'))
label6.place(x=0, y=132)

label11 = Label(root, text='Diagnosed With:', bg='#EEE9BF', font=('georgia', 11, 'bold'))
label11.place(x=0, y=162)

label14 = Label(root, text='Allergies:', bg='#66CDAA', font=('georgia', 11, 'bold'))
label14.place(x=0, y=252)

label16 = Label(root, text='Drugs:', bg='#66CDAA', font=('georgia', 11, 'bold'))
label16.place(x=80, y=312)
label17 = Label(root, text='Unit(Tablet/Syrup):', bg='#66CDAA', font=('georgia', 11, 'bold'))
label17.place(x=227, y=312)
label18 = Label(root, text='Dosage(Per Day):', bg='#66CDAA', font=('georgia', 11, 'bold'))
label18.place(x=420, y=312)
label19 = Label(root, text='Diet To Follow:', bg='#EEE9BF', font=('georgia', 11, 'bold'))
label19.place(x=0, y=520)
label20 = Label(root, text='Brief History Of Patient:', bg='#66CDAA', font=('georgia', 11, 'bold'))
label20.place(x=0, y=592)
label21 = Label(root, text='Name Of Physician:', bg='#EEE9BF', font=('georgia', 11, 'bold'))
label21.place(x=0, y=662)
label22 = Label(root, text='1.', bg='#EEE9BF', font=('georgia', 11, 'bold'))
label22.place(x=0, y=342)
label23 = Label(root, text='2.', bg='#66CDAA', font=('georgia', 11, 'bold'))
label23.place(x=0, y=372)
label24 = Label(root, text='3.', bg='#EEE9BF', font=('georgia', 11, 'bold'))
label24.place(x=0, y=402)
label25 = Label(root, text='4.', bg='#66CDAA', font=('georgia', 11, 'bold'))
label25.place(x=0, y=432)
label26 = Label(root, text='5.', bg='#EEE9BF', font=('georgia', 11, 'bold'))
label26.place(x=0, y=462)
label27 = Label(root, text="", bg='white', font=('georgia', 115))
label27.place(x=210, y=312)
label28 = Label(root, text="", bg='white', font=('georgia', 115))
label28.place(x=400, y=312)

name_entry = Entry(root, font=('georgia', 11,))
name_entry.place(x=130, y=73)
date_entry = Entry(root, font=('georgia', 11), width=18)
date_entry.place(x=400, y=73)
ID_entry = Entry(root, font=('georgia', 11), width=18)
ID_entry.place(x=130, y=103)
age_entry = Entry(root, font=('georgia', 11), width=10)
age_entry.place(x=400, y=103)
gender_entry = Entry(root, font=('georgia', 11), width=10)
gender_entry.place(x=130, y=133)

diagnosed_entry1 = Entry(root, font=('georgia', 11), width=47)
diagnosed_entry1.place(x=140, y=162)
diagnosed_entry2 = Entry(root, font=('georgia', 11), width=47)
diagnosed_entry2.place(x=140, y=182)
diagnosed_entry3 = Entry(root, font=('georgia', 11), width=47)
diagnosed_entry3.place(x=140, y=202)
diagnosed_entry4 = Entry(root, font=('georgia', 11), width=47)
diagnosed_entry4.place(x=140, y=222)

allergies_entry = Entry(root, font=('georgia', 11), width=48)
allergies_entry.place(x=130, y=253)
d1_entry = Entry(root, font=('georgia', 11), width=19)
d1_entry.place(x=29, y=344)
d2_entry = Entry(root, font=('georgia', 11), width=19)
d2_entry.place(x=29, y=374)
d3_entry = Entry(root, font=('georgia', 11), width=19)
d3_entry.place(x=29, y=404)
d4_entry = Entry(root, font=('georgia', 11), width=19)
d4_entry.place(x=29, y=434)
d5_entry = Entry(root, font=('georgia', 11), width=19)
d5_entry.place(x=29, y=464)
unit1_entry = Entry(root, font=('georgia', 11), width=19)
unit1_entry.place(x=221, y=344)
unit2_entry = Entry(root, font=('georgia', 11), width=19)
unit2_entry.place(x=221, y=374)
unit3_entry = Entry(root, font=('georgia', 11), width=19)
unit3_entry.place(x=221, y=404)
unit4_entry = Entry(root, font=('georgia', 11), width=19)
unit4_entry.place(x=221, y=434)
unit5_entry = Entry(root, font=('georgia', 11), width=19)
unit5_entry.place(x=221, y=464)
dose1_entry = Entry(root, font=('georgia', 11), width=18)
dose1_entry.place(x=411, y=344)
dose2_entry = Entry(root, font=('georgia', 11), width=18)
dose2_entry.place(x=411, y=374)
dose3_entry = Entry(root, font=('georgia', 11), width=18)
dose3_entry.place(x=411, y=404)
dose4_entry = Entry(root, font=('georgia', 11), width=18)
dose4_entry.place(x=411, y=434)
dose5_entry = Entry(root, font=('georgia', 11), width=18)
dose5_entry.place(x=411, y=464)

diet_entry1 = Entry(root, font=('georgia', 11), width=47)
diet_entry1.place(x=129, y=524)
diet_entry2 = Entry(root, font=('georgia', 11), width=47)
diet_entry2.place(x=129, y=544)
diet_entry3 = Entry(root, font=('georgia', 11), width=47)
diet_entry3.place(x=129, y=564)

history_entry1 = Entry(root, font=('georgia', 11), width=40)
history_entry1.place(x=200, y=594)
history_entry2 = Entry(root, font=('georgia', 11), width=40)
history_entry2.place(x=200, y=614)
history_entry3 = Entry(root, font=('georgia', 11), width=40)
history_entry3.place(x=200, y=634)
doc_name_entry = Entry(root, font=('georgia', 11), width=18)
doc_name_entry.place(x=200, y=664)

enter_btn = Button(root, text='ENTER', font=('calibre', 16, 'bold'), bg='red', fg='white',)
enter_btn.place(x=400, y=20)
mainloop()