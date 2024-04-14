import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Scale
import webbrowser
import os
import time
import math
import random
import pygame
import parser
import tkinter.messagebox
import pickle
import PIL
import PIL.ImageGrab as IG
import textwrap
import time
import tkinter.ttk as ttk

# Global variables For Number Conversion
FR = 0 # Convert from value
conversiontable = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10 , 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15} # Conversion Table for Hexadecimal

# Global variables for Python Colors
pencolor = "black"

# Global variables for Custom music
global paused
paused = False

# Tkinter System =========================================================================
root = tk.Tk()
root.resizable(width = False, height = False)
root.title("RunIT")

root.iconbitmap("stuff\\runiticon.ico")

# MUSIC ==================================================================================
pygame.mixer.init()

def playmore():
    pygame.mixer.music.load("stuff\\more.mp3")
    pygame.mixer.music.play(loops=99)

def playbaddest():
    pygame.mixer.music.load("stuff\\baddest.mp3")
    pygame.mixer.music.play(loops=99)

def playvillain():
    pygame.mixer.music.load("stuff\\villain.mp3")
    pygame.mixer.music.play(loops=99)

def playillshowyou():
    pygame.mixer.music.load("stuff\\illshowyou.mp3")
    pygame.mixer.music.play(loops=99)

def playdrumgodum():
    pygame.mixer.music.load("stuff\\drumgodum.mp3")
    pygame.mixer.music.play(loops=99)            

def stop():
    pygame.mixer.music.stop()

# music button --------------------------------------------------------------------------- 
# more button change
def morehover(e):
    moremusic["bg"] = "#4d004d"
    moremusic["fg"] = "white"

def moreleave(e):
    moremusic["bg"] = "#FFFF00"
    moremusic["fg"] = "black" 

#stop button change
def stophover(e):
    stopmusic["bg"] = "red"
    stopmusic["fg"] = "white"
    
def stopleave(e):
    stopmusic["bg"] = "#FFFF00"  
    stopmusic["fg"] = "black"           

# BUTTON HOVER CHANGE --------------------------------------------------------------------
# Number Converter Button Change
def buttonnchover(nc): 
    ncbuttonchangepic = tk.PhotoImage(file = "stuff\\ncbuttonchange.png")
    #psyct.png ,,,,,ncbuttonchange.png
    buttonnc.config (image=ncbuttonchangepic)
    buttonnc.image = ncbuttonchangepic
def buttonncleave(nc):
    ncbuttonchangepic = tk.PhotoImage(file = "stuff\\ncbutton.png")
    buttonnc.config (image=ncbuttonchangepic)
    buttonnc.image = ncbuttonchangepic

# Encryption Decryption B7utton Change
def buttonedhover(ed): 
    edbuttonchangepic = tk.PhotoImage(file = "stuff\\edbuttonchange.png")
    buttonED.config (image=edbuttonchangepic)
    buttonED.image = edbuttonchangepic
def buttonedleave(ed):
    edbuttonchangepic = tk.PhotoImage(file = "stuff\\edbutton.png")
    buttonED.config (image=edbuttonchangepic)
    buttonED.image = edbuttonchangepic

# Random Number Generator Button Change
def buttonrnghover(rng):
    rngbuttonchangepic = tk.PhotoImage(file = "stuff\\rngbuttonchange.png")
    buttonRNG.config (image=rngbuttonchangepic)
    buttonRNG.image = rngbuttonchangepic
def buttonrngleave(rng):
    rngbuttonchangepic = tk.PhotoImage(file = "stuff\\rngbutton.png")
    buttonRNG.config (image=rngbuttonchangepic)
    buttonRNG.image = rngbuttonchangepic

# Calculator Button Change
def buttoncalhover(cal):
    calbuttonchangepic = tk.PhotoImage(file = "stuff\\calbuttonchange.png")
    buttonCAL.config (image=calbuttonchangepic)
    buttonCAL.image = calbuttonchangepic
def buttoncalleave(cal):
    calbuttonchangepic = tk.PhotoImage(file = "stuff\\calbutton.png")
    buttonCAL.config (image=calbuttonchangepic)
    buttonCAL.image = calbuttonchangepic

# Random Password Generator Button Change
def buttonrpghover(rpg):
    rpgbuttonchangepic = tk.PhotoImage(file = "stuff\\rpgbuttonchange.png")
    buttonRPG.config (image=rpgbuttonchangepic)
    buttonRPG.image = rpgbuttonchangepic
def buttonrpgleave(rpg):
    rpgbuttonchangepic = tk.PhotoImage(file = "stuff\\rpgbutton.png")
    buttonRPG.config (image=rpgbuttonchangepic)
    buttonRPG.image = rpgbuttonchangepic  
    
# Color Scheme Button Change
def buttoncshover(cs):
    csbuttonchangepic = tk.PhotoImage(file = "stuff\\csbuttonchange.png")
    buttonCS.config (image=csbuttonchangepic)
    buttonCS.image = csbuttonchangepic
def buttoncsleave(cs):
    csbuttonchangepic = tk.PhotoImage(file = "stuff\\csbutton.png")
    buttonCS.config (image=csbuttonchangepic)
    buttonCS.image = csbuttonchangepic  

# To do List Button Change
def buttontdlhover(tdl):
    tdlbuttonchangepic = tk.PhotoImage(file = "stuff\\tdlbuttonchange.png")
    buttonTDL.config (image=tdlbuttonchangepic)
    buttonTDL.image = tdlbuttonchangepic
def buttontdlleave(tdl):
    tdlbuttonchangepic = tk.PhotoImage(file = "stuff\\tdlbutton.png")
    buttonTDL.config (image=tdlbuttonchangepic)
    buttonTDL.image = tdlbuttonchangepic  

# Code Dictionary Button Change
def buttoncdhover(cd):
    cdbuttonchangepic = tk.PhotoImage(file = "stuff\\cdbuttonchange.png")
    buttonCD.config (image=cdbuttonchangepic)
    buttonCD.image = cdbuttonchangepic
def buttoncdleave(cd):
    cdbuttonchangepic = tk.PhotoImage(file = "stuff\\cdbutton.png")
    buttonCD.config (image=cdbuttonchangepic)
    buttonCD.image = cdbuttonchangepic  

# Number Sorter Button Change
def buttonnshover(ns):
    nsbuttonchangepic = tk.PhotoImage(file = "stuff\\nsbuttonchange.png")
    buttonNS.config (image=nsbuttonchangepic)
    buttonNS.image = nsbuttonchangepic
def buttonnsleave(ns):
    nsbuttonchangepic = tk.PhotoImage(file = "stuff\\nsbutton.png")
    buttonNS.config (image=nsbuttonchangepic)
    buttonNS.image = nsbuttonchangepic   

# Python Colors Button Change
def buttonpchover(pc):
    pcbuttonchangepic = tk.PhotoImage(file = "stuff\\pcbuttonchange.png")
    buttonPC.config (image=pcbuttonchangepic)
    buttonPC.image =pcbuttonchangepic
def buttonpcleave(pc):
    pcbuttonchangepic = tk.PhotoImage(file = "stuff\\pcbutton.png")
    buttonPC.config (image=pcbuttonchangepic)
    buttonPC.image = pcbuttonchangepic   

# PICTURES ================================================================================

# background images
bgi = tk.PhotoImage(file = "stuff\\bg.png")
bgiinvert = tk.PhotoImage(file = "stuff\\bginvert.png")
bgi2 = tk.PhotoImage(file = "stuff\\bg3.png")
logopic = tk.PhotoImage(file = "stuff\\logo.png")

# main window button images
NCbuttonpic = tk.PhotoImage(file = "stuff\\NCbutton.png")
EDbuttonpic = tk.PhotoImage(file = "stuff\\EDbutton.png")
RNGbuttonpic = tk.PhotoImage(file = "stuff\\RNGbutton.png")
CALbuttonpic = tk.PhotoImage(file = "stuff\\CALbutton.png")
RPGbuttonpic = tk.PhotoImage(file = "stuff\\RPGbutton.png")
CSbuttonpic = tk.PhotoImage(file = "stuff\\CSbutton.png")
TDLbuttonpic = tk.PhotoImage(file = "stuff\\TDLbutton.png")
CDbuttonpic = tk.PhotoImage(file = "stuff\\CDbutton.png")
NSbuttonpic = tk.PhotoImage(file = "stuff\\NSbutton.png")
PCbuttonpic = tk.PhotoImage(file = "stuff\PCbutton.png")

# NUMBER CONVERSION IMAGES ----------------------------------------------------------------

# light conversion button images
ldbpic = tk.PhotoImage(file = "stuff\\ldbutton.png")
lbbpic = tk.PhotoImage(file = "stuff\\lbbutton.png")
lobpic = tk.PhotoImage(file = "stuff\\lobutton.png")
lhbpic = tk.PhotoImage(file = "stuff\\lhbutton.png")

#light number conversion convert name label images
cvfpic = tk.PhotoImage(file="stuff\\cvf.png")
lhpic = tk.PhotoImage(file = "stuff\\converttoholder.png")

# light conversion button label images
phpic = tk.PhotoImage(file = "stuff\\realbruh.png")
ldlpic = tk.PhotoImage(file = "stuff\\lightdecimallabel.png")
lblpic = tk.PhotoImage(file = "stuff\\lightbinarylabel.png")
lolpic = tk.PhotoImage(file = "stuff\\lightoctallabel.png")
lhlpic = tk.PhotoImage(file = "stuff\\lighthexlabel.png")

# dark conversion button images
ddbpic = tk.PhotoImage(file = "stuff\\ddbutton.png")
dbbpic = tk.PhotoImage(file = "stuff\\dbbutton.png")
dobpic = tk.PhotoImage(file = "stuff\\dobutton.png")
dhbpic = tk.PhotoImage(file = "stuff\\dhbutton.png")

#light number conversion convert name label images
cvtpic = tk.PhotoImage(file="stuff\\cvt.png")
lhpic = tk.PhotoImage(file = "stuff\\converttoholder.png")

# dark conversion button label images
phpic = tk.PhotoImage(file = "stuff\\realbruh.png")
ddlpic = tk.PhotoImage(file = "stuff\\darkdecimallabel.png")
dblpic = tk.PhotoImage(file = "stuff\\darkbinarylabel.png")
dolpic = tk.PhotoImage(file = "stuff\\darkoctallabel.png")
dhlpic = tk.PhotoImage(file = "stuff\\darkhexlabel.png")

# ENCRYPTION DECRYPTION IMAGES ------------------------------------------------------------

#encrypt images
ectitlepic = tk.PhotoImage(file = "stuff\\ectitle.png")
enbgpic = tk.PhotoImage(file = "stuff\\encryptionbg.png")
entextpic = tk.PhotoImage(file = "stuff\\cpoutput.png")
enbuttonpic = tk.PhotoImage(file = "stuff\\enbutton.png")
ttoepic = tk.PhotoImage(file = "stuff\\ttoe.png")
skeypic = tk.PhotoImage(file = "stuff\\skey.png")
#decryption images
dctitleph = tk.PhotoImage(file = "stuff\\dcph.png")
dcbgpic = tk.PhotoImage(file = "stuff\\dccryptionbg.png")
dctitlepic = tk.PhotoImage(file = "stuff\\dctitle.png")
dcecpic = tk.PhotoImage(file = "stuff\\ecipher.png")
dctextpic = tk.PhotoImage(file = "stuff\\dctext.png")
dcbuttonpic = tk.PhotoImage(file = "stuff\\dcbutton.png")

# RANDOM NUMBER GENERATOR -----------------------------------------------------------------

gbuttonnametagpic = tk.PhotoImage(file = "stuff\\gbutton.png")
bgirng = tk.PhotoImage(file = "stuff\\bgirng.png")

# CALCULATOR IMAGES -----------------------------------------------------------------------
calnum1pic = tk.PhotoImage(file = "stuff\\calnum1.png")
calnum2pic = tk.PhotoImage(file = "stuff\\calnum2.png")
calnum3pic = tk.PhotoImage(file = "stuff\\calnum3.png")
calnum4pic = tk.PhotoImage(file = "stuff\\calnum4.png")
calnum5pic = tk.PhotoImage(file = "stuff\\calnum5.png")
calnum6pic = tk.PhotoImage(file = "stuff\\calnum6.png")
calnum7pic = tk.PhotoImage(file = "stuff\\calnum7.png")
calnum8pic = tk.PhotoImage(file = "stuff\\calnum8.png")
calnum9pic = tk.PhotoImage(file = "stuff\\calnum9.png")
calnum0pic = tk.PhotoImage(file = "stuff\\calnum0.png")
calbuttoncpic = tk.PhotoImage(file = "stuff\\calbuttonc.png")
calbuttoncepic = tk.PhotoImage(file = "stuff\\calbuttonce.png")
calbuttonsqpic = tk.PhotoImage(file = "stuff\\calbuttonsq.png")
calbuttonaddpic = tk.PhotoImage(file = "stuff\\calbuttonadd.png")
calbuttonpercentpic = tk.PhotoImage(file = "stuff\\calbuttonpercent.png")
calbuttonminuspic = tk.PhotoImage(file = "stuff\\calbuttonminus.png")
calbuttondividepic = tk.PhotoImage(file = "stuff\\calbuttondivide.png")
calbuttonmultipic = tk.PhotoImage(file = "stuff\\calbuttonmulti.png")
calbuttondotpic = tk.PhotoImage(file = "stuff\\calbuttondot.png")
calbuttonequalspic = tk.PhotoImage(file = "stuff\\calbuttonequals.png")
calbgipic = tk.PhotoImage(file = "stuff\\calbgi.png")
calbuttonpipic = tk.PhotoImage(file = "stuff\\calbuttonpi.png")
calbuttonpnpic = tk.PhotoImage(file = "stuff\\calbuttonpn.png")
calbuttonlogpic = tk.PhotoImage(file = "stuff\\calbuttonlog.png")
calbuttonloghpic = tk.PhotoImage(file = "stuff\\calbuttonlogh.png")
calbuttonlogtwopic = tk.PhotoImage(file = "stuff\\calbuttonlog2.png")
calbuttoncospic = tk.PhotoImage(file = "stuff\\calbuttoncos.png")
calbuttoncoshpic = tk.PhotoImage(file = "stuff\\calbuttoncosh.png")
calbuttonexppic = tk.PhotoImage(file = "stuff\\calbuttonexp.png")
calbuttondegpic = tk.PhotoImage(file = "stuff\\calbuttondeg.png")
calbuttonloglppic = tk.PhotoImage(file = "stuff\\calbuttonloglp.png")
calbuttontanpic = tk.PhotoImage(file = "stuff\\calbuttontan.png")
calbuttontanhpic = tk.PhotoImage(file = "stuff\\calbuttontanh.png")
calbuttonmodpic = tk.PhotoImage(file = "stuff\\calbuttonmod.png")
calbuttonacoshpic = tk.PhotoImage(file = "stuff\\calbuttonacosh.png")
calbuttonexpmlpic = tk.PhotoImage(file = "stuff\\calbuttonexpml.png")
calbuttonsinhpic = tk.PhotoImage(file = "stuff\\calbuttonsinh.png")
calbuttonepic = tk.PhotoImage(file = "stuff\\calbuttone.png")
calbuttonasinhpic = tk.PhotoImage(file = "stuff\\calbuttonasinh.png")
calbuttonlgammapic = tk.PhotoImage(file = "stuff\\calbuttonlgamma.png")
calbuttonsinpic = tk.PhotoImage(file = "stuff\\calbuttonsin.png")
calbuttonscientificpic = tk.PhotoImage(file = "stuff\\calbuttonscientific.png")
calbuttonstandardpic = tk.PhotoImage(file = "stuff\\calbuttonstandard.png")

# RANDOM PASSWORD GENEARTOR IMAGES --------------------------------------------------------
bgirpgpic = tk.PhotoImage(file = "stuff\\bgirpg.png")

# COLOR SCHEME IMAGES ---------------------------------------------------------------------
csepic = tk.PhotoImage(file = "stuff\\cse.png")
bgicspic = tk.PhotoImage(file = "stuff\\bgics.png")
cabbuttonpic = tk.PhotoImage(file = "stuff\\cabbutton.png")
naebuttonpic = tk.PhotoImage(file = "stuff\\naebutton.png")
sasbuttonpic = tk.PhotoImage(file = "stuff\\sasbutton.png")
conabbuttonpic = tk.PhotoImage(file = "stuff\\conabbutton.png")
laibuttonpic = tk.PhotoImage(file = "stuff\\laibutton.png")
ralbuttonpic = tk.PhotoImage(file = "stuff\\ralbutton.png")
aacbuttonpic = tk.PhotoImage(file = "stuff\\aacbutton.png")
eyabuttonpic = tk.PhotoImage(file = "stuff\\eyabutton.png")
mywbuttonpic = tk.PhotoImage(file = "stuff\\mywbutton.png")
caebuttonpic = tk.PhotoImage(file = "stuff\\caebutton.png")
catbuttonpic = tk.PhotoImage(file = "stuff\\catbutton.png")
vaebuttonpic = tk.PhotoImage(file = "stuff\\vaebutton.png")
yafbuttonpic = tk.PhotoImage(file = "stuff\\yafbutton.png")
bpapbuttonpic = tk.PhotoImage(file = "stuff\\bpapbutton.png")
sccbuttonpic = tk.PhotoImage(file = "stuff\\sccbutton.png")
racbuttonpic = tk.PhotoImage(file = "stuff\\racbutton.png")
casbuttonpic = tk.PhotoImage(file = "stuff\\casbutton.png")
gaffbuttonpic = tk.PhotoImage(file = "stuff\\gaffbutton.png")
ecasbuttonpic = tk.PhotoImage(file = "stuff\\ecasbutton.png")
laiyfbuttonpic = tk.PhotoImage(file = "stuff\\laiyfbutton.png")

cabpic = tk.PhotoImage(file = "stuff\\cab.png")
naepic = tk.PhotoImage(file = "stuff\\nae.png")
saspic = tk.PhotoImage(file = "stuff\\sas.png")
conabpic = tk.PhotoImage(file = "stuff\\conab.png")
laipic = tk.PhotoImage(file = "stuff\\lai.png")
ralpic = tk.PhotoImage(file = "stuff\\ral.png")
aacpic = tk.PhotoImage(file = "stuff\\aac.png")
eyapic = tk.PhotoImage(file = "stuff\\eya.png")
mywpic = tk.PhotoImage(file = "stuff\\myw.png")
caepic = tk.PhotoImage(file = "stuff\\cae.png")
catpic = tk.PhotoImage(file = "stuff\\cat.png")
vaepic = tk.PhotoImage(file = "stuff\\vae.png")
yafpic = tk.PhotoImage(file = "stuff\\yaf.png")
bpappic = tk.PhotoImage(file = "stuff\\bpap.png")
sccpic = tk.PhotoImage(file = "stuff\\scc.png")
racpic = tk.PhotoImage(file = "stuff\\rac.png")
caspic = tk.PhotoImage(file = "stuff\\cas.png")
gaffpic = tk.PhotoImage(file = "stuff\\gaff.png")
ecaspic = tk.PhotoImage(file = "stuff\\ecas.png")
laiyfpic = tk.PhotoImage(file = "stuff\\laiyf.png")

# RANDOM IMAGES----------------------------------------------------------------------------
psyct = tk.PhotoImage(file = "stuff\\psyct.png")

moremusicpic = tk.PhotoImage(file = "stuff\\moremusic.png")
stopmusicpic = tk.PhotoImage(file = "stuff\\stopmusic.png")
custommusicpic = tk.PhotoImage(file = "stuff\\custommusic.png")

lastmusicpic = tk.PhotoImage(file = "stuff\\lastmusic.png")
nextmusicpic = tk.PhotoImage(file = "stuff\\nextmusic.png")
stopsmusicpic = tk.PhotoImage(file = "stuff\\stopsmusic.png")
pausemusicpic = tk.PhotoImage(file = "stuff\\pausemusic.png")
playmusicpic = tk.PhotoImage(file = "stuff\\playmusic.png")

creatorspic = tk.PhotoImage(file = "stuff\\creators.png")

# TO DO LIST IMAGES------------------------------------------------------------------------
tdlloadpic = tk.PhotoImage(file = "stuff\\tdlload.png")
tdlsavepic = tk.PhotoImage(file = "stuff\\tdlsave.png")
tdlclearpic = tk.PhotoImage(file = "stuff\\tdlclear.png")

# NUMBER SORTER IMAGES---------------------------------------------------------------------
ascendlogopic = tk.PhotoImage(file = "stuff\\ascendlogo.png")
descendlogopic = tk.PhotoImage(file = "stuff\\descendlogo.png")

# CODE DICTIONARY IMAGES ------------------------------------------------------------------
bgicd = tk.PhotoImage(file="stuff\\bgicd.png")
selectcdbutton = tk.PhotoImage(file="stuff\\cdselectbutton.png")

# FUNCTIONS ===============================================================================

# Function - Number Conversion Window -----------------------------------------------------
def openNC(): 
    
    # creates Number Conversion window
    windowNC = Toplevel(root) 
    windowNC.resizable(width = False, height = False)
    windowNC.title("Number Conversion")
    windowNC.geometry("750x700") 
    windowNC.iconbitmap("stuff\\runiticon.ico")

    # Number Conversion Main Frame
    mainframe = tk.Label(windowNC,image=bgi)
    mainframe.place(relwidth=1, relheight=1)

    # Frame for Entry A
    frame = tk.Label(windowNC,image=bgi2, bd=5)
    frame.place(relx=0.25,rely=0.2,relwidth=0.40,relheight=0.1,anchor="n")

    # Frame for Entry B
    frame2 = tk.Label(windowNC,image=bgi2, bd=5)
    frame2.place(relx=0.75,rely=0.2,relwidth=0.40,relheight=0.1,anchor="n")

    # Entry for Input
    entryA = tk.Entry(frame,font=50,bg="#ccffff")
    entryA.place( relwidth=1, relheight=1)

    # Entry for Output
    entryB = tk.Entry(frame2,font=50,bg="#ccffff")
    entryB.place( relwidth=1, relheight=1,)
    entryB.insert(0,"")
    
    # LABELS
    cflabel = tk.Label(mainframe,text="convert from",image=cvfpic)
    cflabel.place(x=35,y=100,) # Label for convert from

    ctlabel = tk.Label(mainframe,text="convert to",image=cvtpic)
    ctlabel.place(x=412,y=100,) # Label for convert to

    # BUTTON LABELS
    # Label for light buttons
    ldlabel = tk.Label(mainframe,text="light decimal",image=ldlpic)
    ldlabel.place(x=39,y=415,) # label for light decimal button

    lblabel = tk.Label(mainframe,text="light binary",image=lblpic)
    lblabel.place(x=218,y=415,) # label for light binary button

    lolabel = tk.Label(mainframe,text="light octal",image=lolpic)
    lolabel.place(x=39,y=565,) # label for light octal button

    lhlabel = tk.Label(mainframe,text="light hexadecimal",image=lhlpic)
    lhlabel.place(x=218,y=565,) # label for light hex button

    # Label for dark buttons
    ddlabel = tk.Label(mainframe,text="dark decimal",image=ddlpic)
    ddlabel.place(x=412,y=415,) # label for dark decimal button

    dblabel = tk.Label(mainframe,text="dark binary",image=dblpic)
    dblabel.place(x=593,y=415,) # label for dark binary button

    dolabel = tk.Label(mainframe,text="dark octal",image=dolpic)
    dolabel.place(x=412,y=565,) # label for dark octal button

    dhlabel = tk.Label(mainframe,text="dark hexadecimal",image=dhlpic)
    dhlabel.place(x=593,y=565,) # label for dark hexadecimal button

    # FUNCTIONS for Convert from Buttons
    def LDButton(): # Convert from Decimal Button
        global FR
        FR = 1
    
    def LBButton(): # Convert from Binary Button
        global FR
        FR = 2
    
    def LOButton(): # Convert from Octal Button
        global FR
        FR = 3

    def LHDButton(): # Convert from Hexadecimal Button
        global FR
        FR = 4

    # FUNCITONS for Convert to Buttons
    def DDButton(): # Convert to Decimal Button
        global FR
        # try:
        if FR == 1: # Convert from Decimal to Decimal
            try:
                numinput = entryA.get()
                if type(numinput) != int:
                    raise ValueError
                entryB.delete(0, END)
                entryB.insert(0, numinput)
            except ValueError:
                tk.messagebox.showwarning("Error!", "Invalid input")
        elif FR == 2: # Convert from Binary to Decimal
            try:
                numinput = entryA.get()
                num = int(numinput)
                result, i = 0, 0
                while(num != 0): 
                    dec = num % 10
                    result = result + dec * pow(2, i) 
                    num = num//10
                    i += 1
                    entryB.delete(0, END)
                    entryB.insert(0, result)        
            except ValueError:
                tk.messagebox.showwarning("Error!", "Invalid input")
        elif FR == 3: # Convert Octal to Decimal
            try:
                numinput = entryA.get()
                remain = int(numinput)
                result, i  = 0, 0
                while remain > 0:
                    result += int(remain % 10) * 8 ** i
                    remain = int(remain / 10)
                    i += 1
                entryB.delete(0, END)
                entryB.insert(0, result)
            except ValueError:
                tk.messagebox.showwarning("Error!", "Invalid input")    
        elif FR == 4: # Convert Hexadecimal to Decimal
            try:
                global conversiontable
                hexinput = entryA.get()
                hex = hexinput.strip().upper()
                result = 0
                power = len(hex)-1
                for digit in hex:
                    result += conversiontable[digit]*16**power
                    power -= 1
                entryB.delete(0, END)
                entryB.insert(0, result)
            except KeyError:
                tk.messagebox.showwarning("Error!", "Invalid input")

    def DBButton(): # Convert to Binary Button
        global FR
        if FR == 1: # Convert from Decimal to Binary 
            try:
                numinput = entryA.get()
                num = int(numinput)
                result = str(bin(num))[2:]
                entryB.delete(0, END)
                entryB.insert(0, result)
            except ValueError:
                tk.messagebox.showwarning("Error!", "Invalid input") 
        elif FR == 2: # Convert from Binary to Binary
            try:
                numinput = entryA.get()
                if type(numinput) != int:
                    raise ValueError
                entryB.delete(0, END)
                entryB.insert(0, numinput)
            except ValueError:
                tk.messagebox.showwarning("Error!", "Invalid input")     
        elif FR == 3: # Convert from Octal to Binary
            try:
                numinput = entryA.get()
                remain = int(numinput)
                num, i  = 0, 0
                while remain > 0:
                    num += int(remain % 10) * 8 ** i
                    remain = int(remain / 10)
                    i += 1
                result = str(bin(num))[2:]
                entryB.delete(0, END)
                entryB.insert(0, result)
            except ValueError:
                tk.messagebox.showwarning("Error!", "Invalid input")
        elif FR == 4: # Convert Hexadecimal to Binary
            try:
                global conversiontable
                hexinput = entryA.get()
                hex = hexinput.strip().upper()
                dec = 0
                power = len(hex)-1
                for digit in hex:
                    dec += conversiontable[digit]*16**power
                    power -= 1
                result = str(bin(dec))[2:]
                entryB.delete(0, END)
                entryB.insert(0, result)
            except KeyError:
                tk.messagebox.showwarning("Error!", "Invalid input")

    def DOButton(): # Convert to Octal Button
        global FR
        if FR == 1: # Convert from Decimal to Octal
            try:
                numinput = entryA.get()
                num = int(numinput)
                result = str(oct(num))[2:]
                entryB.delete(0, END)
                entryB.insert(0, result)
            except ValueError:
                tk.messagebox.showwarning("Error!", "Invalid input")
        elif FR == 2: # Convert from Binary to Octal
            try:
                numinput = entryA.get()
                num = int(numinput)
                temp, i, n = 0, 0, 0
                while(num != 0): 
                    dec = num % 10
                    temp = temp + dec * pow(2, i) 
                    num = num//10
                    i += 1
                result = str(oct(temp))[2:]
                entryB.delete(0, END)
                entryB.insert(0, result)
            except ValueError:
                tk.messagebox.showwarning("Error!", "Invalid input")
        elif FR == 3: # Convert Octal to Octal
            try:
                numinput = entryA.get()
                if type(numinput) != int:
                    raise ValueError
                entryB.delete(0, END)
                entryB.insert(0, numinput)
            except ValueError:
                tk.messagebox.showwarning("Error!", "Invalid input")
        elif FR == 4: # Convert Hexadecimal to Octal
            try:
                global conversiontable
                hexinput = entryA.get()
                hex = hexinput.strip().upper()
                dec = 0
                power = len(hex)-1
                for digit in hex:
                    dec += conversiontable[digit]*16**power
                    power -= 1
                result = str(oct(dec))[2:]
                entryB.delete(0, END)
                entryB.insert(0, result)
            except KeyError:
                tk.messagebox.showwarning("Error!", "Invalid input")
            
    def DHButton(): # Convert to Hexadecimal
        global FR
        if FR == 1: # Convert from Decimal to Hexadecimal
            try:
                numinput = entryA.get()
                num = int(numinput)
                result = str(hex(num))[2:]
                entryB.delete(0, END)
                entryB.insert(0, result)
            except ValueError:
                tk.messagebox.showwarning("Error!", "Invalid input")
        elif FR == 2: # Convert from Binary to Hexadecimal
            try:
                numinput = entryA.get()
                num = int(numinput)
                temp, i, n = 0, 0, 0
                while(num != 0): 
                    dec = num % 10
                    temp = temp + dec * pow(2, i) 
                    num = num//10
                    i += 1
                result = str(hex(temp))[2:]
                entryB.delete(0, END)
                entryB.insert(0, result)
            except ValueError:
                tk.messagebox.showwarning("Error!", "Invalid input")
        elif FR == 3: # Convert to Octal to Hexadecimal
            try:
                numinput = entryA.get()
                remain = int(numinput)
                num, i  = 0, 0
                while remain > 0:
                    num += int(remain % 10) * 8 ** i
                    remain = int(remain / 10)
                    i += 1
                result = str(hex(num))[2:]
                entryB.delete(0, END)
                entryB.insert(0, result)
            except ValueError:
                tk.messagebox.showwarning("Error!", "Invalid input")
        elif FR == 4: # Convert Hexadecimal to Hexadecimal
            try:
                numinput = entryA.get()
                entryB.delete(0, END)
                entryB.insert(0, numinput)
            except ValueError:
                tk.messagebox.showwarning("Error!", "Invalid input")

    # CONVERT FROM BUTTONS
    # first Button - Convert from Decimal
    LDbutton = tk.Button(mainframe, image=ldbpic, command = LDButton)
    LDbutton.place(relx=0.05,y=300)
    # first button - Convert from Binary
    LBbutton = tk.Button(mainframe,text="binary",image=lbbpic,command=LBButton)
    LBbutton.place(relx=0.29,y=300)
    # first Button - Convert from Octal
    LObutton = tk.Button(mainframe,text="octal",image=lobpic, command = LOButton)
    LObutton.place(relx=0.05,y=450)
    # first button - Convert from Hexadecimal  
    LHDbutton = tk.Button(mainframe,text="hexadecimal",image=lhbpic,command = LHDButton)
    LHDbutton.place(x=215,y=450)
    
    # CONVERT TO BUTTONS
    # second Button - Convert to Decimal
    DDbutton = tk.Button(mainframe,text="decimal",image=ddbpic, command = DDButton)
    DDbutton.place(x=410,y=300)
    # second button - Convert to Binary
    DBbutton = tk.Button(mainframe,text="binary",image=dbbpic, command = DBButton)
    DBbutton.place(x=590,y=300)
    # second Button - Convert to Octal
    DObutton = tk.Button(mainframe,text="octal",image=dobpic,command = DOButton)
    DObutton.place(x=410,y=450)
    # second button - Convert to Hexadecimal
    DHDbutton = tk.Button(mainframe,text="hexadecimal",image=dhbpic,command = DHButton)
    DHDbutton.place(x=590,y=450)

# Function - Encryption-Decryption Window -------------------------------------------------
def openED():

    # Creates Encryption-Decryption Window
    windowED = Toplevel(root)
    windowED.resizable(width = False, height = False)
    windowED.title("ENCRYPTION-DECRYPTION")
    windowED.geometry("1050x800")
    windowED.iconbitmap("stuff\\runiticon.ico")

    # Main Frame
    mainframe = tk.Label(windowED,image=bgi)
    mainframe.place(relwidth=1, relheight=1)

    # FUNCTION - Encrypt text input
    def Encrypt():
        try:
            text = entryE.get()
            s = int(entryS.get())
            result = ""
            for i in range(len(text)):
                char = text[i]
                if (char.isupper()):
                    result += chr((ord(char) + s-65) % 26 + 65)
                else:
                    result += chr((ord(char) + s - 97) % 26 + 97)
            cipher = result.upper()
            entryC.delete(0, END)
            entryC.insert(0, cipher)
        except ValueError:
            tk.messagebox.showwarning("Error!", "Invalid Shift Key")

    # FUNCTION - Decrypt text input
    def Decrypt():
        textinput = entryD.get()
        text = textinput.upper()
        LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        message = []
        for key in range(len(LETTERS)):
            translated = ''
            for symbol in text:
                if symbol in LETTERS:
                    num = LETTERS.find(symbol)
                    num = num - key
                    if num < 0:
                        num = num + len(LETTERS)
                    translated = translated + LETTERS[num]
                else:
                    translated = translated + symbol
            temp = '\nHacking key #%s: %s' % (key, translated)
            message.append(temp)
        entryMfinal = tk.Label(frameDE2,text=message,bg="#ccffff")
        entryMfinal.place(x=10,y=230,height=400,width=430)

    # Frame for encryption
    frame = tk.Label(windowED,image=bgi2, bd=5) 
    frame.place(x=10,y=10,height=750,width=490)
    
    # Design frame for encryption
    frameDE = tk.Label(frame,image=enbgpic, bd=5) 
    frameDE.place(x=10,y=10,height=720,width=460)

    # entry e frame
    entryeframe = tk.Label(frameDE,image=bgi2)
    entryeframe.place(x=180,y=100,height=40,width=250)

    # Frame for decryption
    frame2 = tk.Label(windowED,image=bgi2, bd=5) 
    frame2.place(x=530,y=10,height=750,width=490)
    
    # Design frame for decryption
    frameDE2 = tk.Label(frame2,image=dcbgpic, bd=5) 
    frameDE2.place(x=10,y=10,height=720,width=460)

    # Entry for text to encrypt Input
    entryE = tk.Entry(entryeframe,font=50,bg="#ccffff")
    entryE.place(width=249,height=39)

    # Entry for Shift Input
    entryS = tk.Entry(frameDE,font=50,bg="#ccffff")
    entryS.place(x=180,y=150,height=40,width=125)

    # encrypt button frame
    buttoneframe = tk.Label(frameDE,image=bgi2)
    buttoneframe.place(x=110,y=230,height=50,width=260)

    # Button to encrypt
    buttonE = tk.Button(buttoneframe, text="ENCRYPT",image=enbuttonpic, fg="#FF8040",activeforeground="#40BFFF",cursor="heart",command=Encrypt)  
    buttonE.place(x=0,y=0)

    # Entry for Cipher Output
    entryC = tk.Entry(frameDE,font=50,bg="#ccffff", justify=CENTER)
    entryC.place(x=10,y=350,height=350,width=430)

    # Entry for text to decrypt Input
    entryD = tk.Entry(frameDE2,font=50,bg="#ccffff")
    entryD.place(x=200,y=100,height=40,width=250)

    # Button to decrypt
    buttonD = tk.Button(frameDE2, text="DECRYPT",image=dcbuttonpic, fg="#FF8040",activeforeground="#40BFFF",cursor="heart", command=Decrypt) 
    buttonD.place(x=110,y=180,height=40,width=250)

# Function - Random Number Generator Window -----------------------------------------------
def openRNG():

    # Creates Random Number Generator Window
    windowRNG = Toplevel(root)
    windowRNG.title("RANDOM NUMBER GENERATOR") 
    windowRNG.resizable(width=False,height=False)
    windowRNG.geometry("750x700") 
    windowRNG.iconbitmap("stuff\\runiticon.ico")

    # Random Number Generator Main Frame
    mainframe = tk.Label(windowRNG,image=bgirng)
    mainframe.place(relwidth=1, relheight=1)
    
    # FUNCTION for Random Number Generator button
    def buttonRNG():
        try:
            rndcount = entryQ.get()
            count = int(rndcount)
            rndmin = entrymin.get()
            min = int(rndmin)
            rndmax = entrymax.get()
            max = int(rndmax)
            listboxRNG.delete(0, END)
            for i in range(0,count):
                n = random.randint(min, max)
                listboxRNG.insert(END, n)
        except ValueError:
            tk.messagebox.showwarning("Error!", "Invalid input")
        
    # Entry for Quantity
    entryQ = tk.Entry(mainframe,font=50,bg="#ccffff")
    entryQ.place(x=280,y=100,width=200, height=80)

    entrymin = tk.Entry(mainframe,font=50,bg="#ccffff")
    entrymin.place(x=180,y=250,width=100, height=50)

    # Entry for Max
    entrymax = tk.Entry(mainframe,font=50,bg="#ccffff")
    entrymax.place(x=480,y=250,width=100, height=50)

    # Entry for Output
    listboxRNGframe = tk.Frame(windowRNG)
    listboxRNGframe.place(x=10,y=430,height=250,width=725)

    listboxRNG = tk.Listbox(listboxRNGframe,font=10,bg="#ccffff",justify=CENTER,height=250,width=715)
    listboxRNG.pack(side=tk.LEFT)

    scrollbar = tk.Scrollbar(listboxRNGframe)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    listboxRNG.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listboxRNG.yview)

    # Button for Random Number Generation
    buttonRNG = tk.Button(mainframe, text="GENERATE",image=gbuttonnametagpic, fg="#FF8040",activeforeground="#40BFFF",cursor="heart", command=buttonRNG) 
    buttonRNG.place(x=250,y=320,height=40,width=250)

# Function - Calculator Window ------------------------------------------------------------
def openCAL(): 
    def scientific():
        windowCAL.resizable(width=False,height=False)
        windowCAL.geometry("818x600") 

    def standard():
        windowCAL.resizable(width=False,height=False)
        windowCAL.geometry("410x600") 

    # Creates Calculator Window
    windowCAL = Toplevel(root)
    windowCAL.title("CALCULATOR")
    windowCAL.resizable(width=False, height=False)
    windowCAL.geometry("410x590") 
    windowCAL.iconbitmap("stuff\\runiticon.ico")

    # Calculator window Main frame
    mainframe = tk.Label(windowCAL,image=calbgipic)
    mainframe.place(relwidth=1, relheight=1)

    # Functions for Calculator Buttons
    class Calc():
        def __init__(self):
            self.total = 0
            self.current = ""
            self.input_value = True
            self.check_sum = False
            self.op = ""
            self.result = False
        
        def numberEnter(self, num):
            self.result = False
            firstnum = txtdisplay.get()
            secondnum = str(num)
            if self.input_value:
                self.current = secondnum
                self.input_value = False
            else:
                if secondnum == '.':
                    if secondnum in firstnum:
                        return
                self.current = firstnum + secondnum
            self.display(self.current)

        def sum_of_total(self):
            self.result = True
            self.current = float(self.current)
            if self.check_sum == True:
                self.valid_function()
            else:
                self.total = float(txtdisplay.get())

        def display(self, value):
            txtdisplay.delete(0, END)
            txtdisplay.insert(0, value)

        def valid_function(self):
            if self.op == "add":
                self.total += self.current
            if self.op == "sub":
                self.total -= self.current
            if self.op == "multi":
                self.total *= self.current
            if self.op == "divide":
                self.total /= self.current
            if self.op == "mod":
                self.total %= self.current
            if self.op == "percent":
                self.total = self.current / 100
            self.input_value = True
            self.check_sum = False
            self.display(self.total)

        def operation(self, op):
            self.current = float(self.current)
            if self.check_sum:
                self.valid_function()
            elif not self.result:
                self.total = self.current
                self.input_value = True
            self.check_sum = True
            self.op = op
            self.result = False

        def Clear(self):
            self.result = False
            self.current = "0"
            self.display(0)
            self.input_value = True

        def ClearAll(self):
            self.Clear()
            self.total = 0

        def pi(self):
            self.result = False
            self.current = math.pi
            self.display(self.current)

        def e(self):
            self.result = False
            self.current = math.e
            self.display(self.current)

        def mathPN(self):
            self.result = False
            self.current = -(float(txtdisplay.get()))
            self.display(self.current)
        
        def squared(self):
            self.result = False
            self.current = math.sqrt(float(txtdisplay.get()))
            self.display(self.current)

        def cos(self):
            self.result = False
            self.current = math.cos(math.radians(float(txtdisplay.get())))
            self.display(self.current)
            
        def cosh(self):
            self.result = False
            self.current = math.cosh(math.radians(float(txtdisplay.get())))
            self.display(self.current)  

        def tan(self):
            self.result = False
            self.current = math.tan(math.radians(float(txtdisplay.get())))
            self.display(self.current)

        def tanh(self):
            self.result = False
            self.current = math.tanh(math.radians(float(txtdisplay.get())))
            self.display(self.current)
        
        def sin(self):
            self.result = False
            self.current = math.sin(math.radians(float(txtdisplay.get())))
            self.display(self.current)

        def sinh(self):
            self.result = False
            self.current = math.sinh(math.radians(float(txtdisplay.get())))
            self.display(self.current)

        def log(self):
            self.result = False
            self.current = math.log(float(txtdisplay.get()))
            self.display(self.current)

        def exp(self):
            self.result = False
            self.current = math.exp(float(txtdisplay.get()))
            self.display(self.current)

        def acosh(self):
            self.result = False
            self.current = math.acosh(float(txtdisplay.get()))
            self.display(self.current)

        def asinh(self):
            self.result = False
            self.current = math.asinh(float(txtdisplay.get()))
            self.display(self.current)

        def expm1(self):
            self.result = False
            self.current = math.expm1(float(txtdisplay.get()))
            self.display(self.current)

        def lgamma(self):
            self.result = False
            self.current = math.lgamma(float(txtdisplay.get()))
            self.display(self.current)

        def deg(self):
            self.result = False
            self.current = math.degrres(float(txtdisplay.get()))
            self.display(self.current)

        def log2(self):
            self.result = False
            self.current = math.log2(float(txtdisplay.get()))
            self.display(self.current)

        def logh(self):
            self.result = False
            self.current = math.logh(float(txtdisplay.get()))
            self.dsplay(self.current)

        def log10(self):
            self.result = False
            self.current = math.log10(float(txtdisplay.get()))
            self.display(self.current)

        def log1p(self):
            self.result = False
            self.current = math.log1p(float(txtdisplay.get()))
            self.display(self.current)

    added_value = Calc()

    # Calculator Output
    txtdisplay = tk.Entry(mainframe,font=('arial',20,'bold'),bg="#ccffff",bd=30,width=23,justify=RIGHT)
    txtdisplay.place(y=27)
    txtdisplay.insert(0,"0")
    
    # Buttons for Opening Standard or Scientific Windows
    standardbutton = tk.Button(mainframe,image=calbuttonstandardpic,command=standard)
    standardbutton.place(x=0,y=0)

    scientificbutton = tk.Button(mainframe,image=calbuttonscientificpic,command=scientific)
    scientificbutton.place(x=198,y=0)

    # Buttons for Standard Calculator
    buttonc = tk.Button(mainframe,image=calbuttoncpic, command = added_value.ClearAll)
    buttonc.place(y=122)
    button0 = tk.Button(mainframe,image=calnum0pic, command = lambda: added_value.numberEnter(0))
    button0.place(y=493,x=101)
    button1 = tk.Button(mainframe,image=calnum1pic, command = lambda: added_value.numberEnter(1))
    button1.place(y=400)
    button2 = tk.Button(mainframe,image=calnum2pic, command = lambda: added_value.numberEnter(2))
    button2.place(y=400,x=101)
    button3 = tk.Button(mainframe,image=calnum3pic, command = lambda: added_value.numberEnter(3))
    button3.place(y=400,x=202)
    button4 = tk.Button(mainframe,image=calnum4pic, command = lambda: added_value.numberEnter(4))
    button4.place(y=308)
    button5 = tk.Button(mainframe,image=calnum5pic, command = lambda: added_value.numberEnter(5))
    button5.place(y=308,x=101)
    button6 = tk.Button(mainframe,image=calnum6pic, command = lambda: added_value.numberEnter(6)) 
    button6.place(y=308,x=202)
    button7 = tk.Button(mainframe,image=calnum7pic, command = lambda: added_value.numberEnter(7))
    button7.place(y=215)
    button8 = tk.Button(mainframe,image=calnum8pic, command = lambda: added_value.numberEnter(8))
    button8.place(y=215,x=101)
    button9 = tk.Button(mainframe,image=calnum9pic, command = lambda: added_value.numberEnter(9))
    button9.place(y=215,x=202)
    
    buttonpercent = tk.Button(mainframe,image=calbuttonpercentpic, command = lambda: added_value.operation("percent"))
    buttonpercent.place(y=493)
    buttondel = tk.Button(mainframe,image=calbuttoncepic, command = added_value.Clear)
    buttondel.place(y=122,x=101)
    buttonsq = tk.Button(mainframe,image=calbuttonsqpic, command = added_value.squared)
    buttonsq.place(y=122,x=202)
    buttondot = tk.Button(mainframe,image=calbuttondotpic, command = lambda: added_value.numberEnter("."))
    buttondot.place(y=493,x=202)
    buttondivide = tk.Button(mainframe,image=calbuttondividepic, command = lambda: added_value.operation("divide"))
    buttondivide.place(y=122,x=303)
    buttonmulti = tk.Button(mainframe,image=calbuttonmultipic, command = lambda: added_value.operation("multi"))
    buttonmulti.place(y=215,x=303)
    buttonminus = tk.Button(mainframe,image=calbuttonminuspic, command = lambda: added_value.operation("sub"))
    buttonminus.place(y=308,x=303)
    buttonadd = tk.Button(mainframe,image=calbuttonaddpic, command = lambda: added_value.operation("add"))
    buttonadd.place(y=400,x=303)
    buttonequals = tk.Button(mainframe,image=calbuttonequalspic, command = added_value.sum_of_total)
    buttonequals.place(y=493,x=303)

    # Buttons for Scientific Calculator
    buttonpi = tk.Button(mainframe,image=calbuttonpipic, command = added_value.pi)
    buttonpi.place(y=125,x=410)
    buttonpn = tk.Button(mainframe,image=calbuttonpnpic, command = added_value.mathPN)
    buttonpn.place(y=215,x=410)
    buttonlog = tk.Button(mainframe,image=calbuttonlogpic, command = added_value.log)
    buttonlog.place(y=308,x=410)
    buttonlogh = tk.Button(mainframe,image=calbuttonloghpic, command = added_value.logh)
    buttonlogh.place(y=400,x=410)
    buttonlogtwo = tk.Button(mainframe,image=calbuttonlogtwopic, command = added_value.log2)
    buttonlogtwo.place(y=493,x=410)
    buttoncos = tk.Button(mainframe,image=calbuttoncospic, command = added_value.cos)
    buttoncos.place(y=125,x=510)
    buttoncosh = tk.Button(mainframe,image=calbuttoncoshpic, command = added_value.cosh)
    buttoncosh.place(y=215,x=510)
    buttonexp = tk.Button(mainframe,image=calbuttonexppic, command = added_value.exp)
    buttonexp.place(y=308,x=510)
    buttondeg = tk.Button(mainframe,image=calbuttondegpic, command = added_value.deg)
    buttondeg.place(y=400,x=510)
    buttonloglp = tk.Button(mainframe,image=calbuttonloglppic, command = added_value.log1p)
    buttonloglp.place(y=493,x=510)
    buttontan = tk.Button(mainframe,image=calbuttontanpic, command = added_value.tan)
    buttontan.place(y=125,x=611)
    buttontanh = tk.Button(mainframe,image=calbuttontanhpic, command = added_value.tanh)
    buttontanh.place(y=215,x=611)
    buttonmod = tk.Button(mainframe,image=calbuttonmodpic, command = lambda: added_value.operation("mod"))
    buttonmod.place(y=308,x=611)
    buttonacosh = tk.Button(mainframe,image=calbuttonacoshpic, command = added_value.cosh)
    buttonacosh.place(y=400,x=611)
    buttonexpml = tk.Button(mainframe,image=calbuttonexpmlpic, command = added_value.expm1)
    buttonexpml.place(y=493,x=611)
    buttonsin = tk.Button(mainframe,image=calbuttonsinpic, command = added_value.sin)
    buttonsin.place(y=125,x=712)
    buttonsinh = tk.Button(mainframe,image=calbuttonsinhpic, command = added_value.sinh)
    buttonsinh.place(y=215,x=712)
    buttone = tk.Button(mainframe,image=calbuttonepic, command = added_value.e)
    buttone.place(y=308,x=712)
    buttonasinh = tk.Button(mainframe,image=calbuttonasinhpic, command = added_value.asinh)
    buttonasinh.place(y=400,x=712)
    buttonlgamma = tk.Button(mainframe,image=calbuttonlgammapic, command = added_value.lgamma)
    buttonlgamma.place(y=493,x=712)
    
# Function - Random Password Generator ----------------------------------------------------
def openRPG():

    # Creates Random Password Generator Window
    windowRPG = Toplevel(root)
    windowRPG.title("RANDOM PASSWORD GENERATOR") 
    windowRPG.resizable(width=False,height=False)
    windowRPG.geometry("750x700") 
    windowRPG.iconbitmap("stuff\\runiticon.ico")

    # Main Frame for the window
    mainframe = tk.Label(windowRPG,image=bgirpgpic)
    mainframe.place(relwidth=1, relheight=1)

    # Function to Generate Random Password
    def RPG():
        try:
            length = int(entry.get())
            symbols = "!@#$%^&*?_+"
            ambsym = "}{[]()/\'~,;:.<>"
            Uletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            Lletters = "abcdefghijklmnopqrstuvwxyz"
            numbers = "1234567890"

            password = ""
            chars = ""
            if cbsvar.get() == 1:
                # includes symbols
                chars += symbols
            if cbulvar.get() == 1:
                # includes uppercase letters
                chars += Uletters
            if cbllvar.get() == 1:
                # includes lowercase letters
                chars += Lletters
            if cbnvar.get() == 1:
                # includes numbers
                chars += numbers
            if cbasvar.get() == 1:
                # includes ambiguous symbols
                chars += ambsym

            for i in range(length):
                password += random.choice(chars)
            entryfinal.delete(0, END)
            entryfinal.insert(0, password)
        except ValueError:
            tk.messagebox.showwarning("Error!", "Invalid input")
    
    # Entry for Password Length Input
    entry = tk.Entry(mainframe,font=50,bg="#ccffff")
    entry.place(x=330, y=110)
    
    cbsvar = IntVar()
    cbasvar = IntVar()
    cbulvar = IntVar()
    cbllvar = IntVar()
    cbnvar = IntVar()
    
    # Check Buttons for Characters to include in Password Generation
    # Include Symbols
    cbs = Checkbutton(mainframe,variable=cbsvar)
    cbs.place(x=180,y=150)

    # Include Ambiguous Symbols
    cbas = Checkbutton(mainframe,variable=cbasvar)
    cbas.place(x=180,y=190)

    # Include Uppercase Letters
    cbul = Checkbutton(mainframe,variable=cbulvar)
    cbul.place(x=180,y=260)

    # Include Lowercase Letters
    cbll = Checkbutton(mainframe,variable=cbllvar)
    cbll.place(x=180,y=300)

    # Include Numbers
    cbn = Checkbutton(mainframe,variable=cbnvar)
    cbn.place(x=180,y=340)

    # Button to Generate
    generatebutton = tk.Button(mainframe,image=gbuttonnametagpic,command=RPG)
    generatebutton.place(x=250,y=380)

    # Entry for Output
    entryfinal = tk.Entry(mainframe,font=200,bg="#ccffff", justify='center')
    entryfinal.place(x=10,y=440,height=250,width=725)
    entryfinal.insert(0,"")

# Function - Color Scheme -----------------------------------------------------------------
def openCS():
    # Creates Color Scheme Window
    windowcs = Toplevel(root)
    windowcs.title("COLOR SCHEME")     
    windowcs.resizable(width=False,height=False)
    windowcs.geometry("1200x680") 
    windowcs.iconbitmap("stuff\\runiticon.ico")

    # Main Frame for the window
    mainframe = tk.Label(windowcs,image=bgicspic)
    mainframe.place(relwidth=1, relheight=1)

    # Functions for Color Schemes
    def CAB():
        colors = {
            1 : "#E27D60",
            2 : "#85DCBA",
            3 : "#e8a87c",
            4 : "#C38D9E",
            5 : "#41B3A3"
        }

        site = tk.Label(mainframe,image=cabpic)
        site.place(x=50,y=270)

        ic.configure({"background": colors[1],"fg": "black"})
        ic.delete(0, END)
        ic.insert(0, colors[1])

        iic.configure({"background": colors[2],"fg": "black"})
        iic.delete(0, END)
        iic.insert(0, colors[2])

        iiic.configure({"background": colors[3],"fg": "black"})
        iiic.delete(0, END)
        iiic.insert(0, colors[3])

        ivc.configure({"background": colors[4],"fg": "white"})
        ivc.delete(0, END)
        ivc.insert(0, colors[4])

        iivc.configure({"background": colors[5],"fg": "black"})
        iivc.delete(0, END)
        iivc.insert(0, colors[5])

        desc.configure({"text": """Warm and cool hues are combined in \nthis colorfulyet not overwhelming \npalette. From an appealing and \nbright bluish-green to an earthy \nterracotta,this color scheme is \nwell-suited for youthful and \nmodern designs"""})

    def NAE(): 
        colors = {
            1 : "#8D8741",
            2 : "#659DBD",
            3 : "#DAAD86",
            4 : "#BC986A",
            5 : "#FBEEC1"
        }

        site = tk.Label(mainframe,image=naepic)
        site.place(x=50,y=270)

        ic.configure({"background": colors[1],"fg": "white"})
        ic.delete(0, END)
        ic.insert(0, colors[1])

        iic.configure({"background": colors[2],"fg": "black"})
        iic.delete(0, END)
        iic.insert(0, colors[2])

        iiic.configure({"background": colors[3],"fg": "black"})
        iiic.delete(0, END)
        iiic.insert(0, colors[3])

        ivc.configure({"background": colors[4],"fg": "white"})
        ivc.delete(0, END)
        ivc.insert(0, colors[4])

        iivc.configure({"background": colors[5],"fg": "black"})
        iivc.delete(0, END)
        iivc.insert(0, colors[5])

        desc.configure({"text": """Feelings of being surrounded by a \ncomforting blue sky and a nurturing \nscene of the outdoors are immediately\n evoked by this very "down-to-earth" \ncolor scheme. Ideal for designs \nrelated to nature and sustainability,\n this pleasant color combination may\n come in handy for projects that \nemphasize environmental consciousness."""})

    def SAS():
        colors = {
            1 : "#5D5C61",
            2 : "#938e93",
            3 : "#7395AE",
            4 : "#557A95",
            5 : "#B1A296"
        }

        site = tk.Label(mainframe,image=saspic)
        site.place(x=50,y=270)

        ic.configure({"background": colors[1], "fg": "white"})
        ic.delete(0, END)
        ic.insert(0, colors[1])

        iic.configure({"background": colors[2], "fg": "white"})
        iic.delete(0, END)
        iic.insert(0, colors[2])

        iiic.configure({"background": colors[3], "fg": "black"})
        iiic.delete(0, END)
        iiic.insert(0, colors[3])

        ivc.configure({"background": colors[4], "fg": "white"})
        ivc.delete(0, END)
        ivc.insert(0, colors[4])

        iivc.configure({"background": colors[5], "fg": "black"})
        iivc.delete(0, END)
        iivc.insert(0, colors[5])

        desc.configure({"text": """This elegant color scheme brings \ntogether dark muted tones to create \na clean and sophisticated look. Its \nshades of gray and blue are ideal \nfor more conservative designs."""})
    
    def CONAB():
        colors = {
            1 : "#1A1A1D",
            2 : "#4E4E50",
            3 : "#6F2232",
            4 : "#950740",
            5 : "#C3073F"
        }

        site = tk.Label(mainframe,image=conabpic)
        site.place(x=50,y=270)

        ic.configure({"background": colors[1], "fg": "white"})
        ic.delete(0, END)
        ic.insert(0, colors[1])

        iic.configure({"background": colors[2], "fg": "white"})
        iic.delete(0, END)
        iic.insert(0, colors[2])

        iiic.configure({"background": colors[3], "fg": "white"})
        iiic.delete(0, END)
        iiic.insert(0, colors[3])

        ivc.configure({"background": colors[4], "fg": "white"})
        ivc.delete(0, END)
        ivc.insert(0, colors[4])

        iivc.configure({"background": colors[5], "fg": "white"})
        iivc.delete(0, END)
        iivc.insert(0, colors[5])

        desc.configure({"text": """An appealing combination of pinks, \nreds, blacks and grays, this modern-\nlooking palette evokes sensations of\n luxury, sophistication and minimalism."""})

    def LAI():
        colors = {
            1 : "#E7717D",
            2 : "#C2CAD0",
            3 : "#C2B9B0",
            4 : "#7E685A",
            5 : "#AFD275"
        }

        site = tk.Label(mainframe,image=laipic)
        site.place(x=50,y=270)

        ic.configure({"background": colors[1],"fg": "black"})
        ic.delete(0, END)
        ic.insert(0, colors[1])

        iic.configure({"background": colors[2],"fg": "black"})
        iic.delete(0, END)
        iic.insert(0, colors[2])

        iiic.configure({"background": colors[3],"fg": "black"})
        iiic.delete(0, END)
        iiic.insert(0, colors[3])

        ivc.configure({"background": colors[4],"fg": "white"})
        ivc.delete(0, END)
        ivc.insert(0, colors[4])

        iivc.configure({"background": colors[5],"fg": "black"})
        iivc.delete(0, END)
        iivc.insert(0, colors[5])

        desc.configure({"text": """This beautiful combination of candy\n pink, green-yellow, lavender gray \nand pastel brown is ideal for designs\n looking to project a vibrant and \ninviting image."""})

    def RAL():
        colors = {
            1 : "#5D001E",
            2 : "#E3E2DF",
            3 : "#E3AFBC",
            4 : "#9A1750",
            5 : "#EE4C7C"
        }

        site = tk.Label(mainframe,image=ralpic)
        site.place(x=50,y=270)

        ic.configure({"background": colors[1],"fg": "white"})
        ic.delete(0, END)
        ic.insert(0, colors[1])

        iic.configure({"background": colors[2],"fg": "black"})
        iic.delete(0, END)
        iic.insert(0, colors[2])

        iiic.configure({"background": colors[3],"fg": "black"})
        iiic.delete(0, END)
        iiic.insert(0, colors[3])

        ivc.configure({"background": colors[4],"fg": "white"})
        ivc.delete(0, END)
        ivc.insert(0, colors[4])

        iivc.configure({"background": colors[5],"fg": "black"})
        iivc.delete(0, END)
        iivc.insert(0, colors[5])

        desc.configure({"text": """Using the red Polish flag as a basis\n for its color scheme, this attractive\n website combines a dark scarlet red\n with dark pink over a light gray \nbackground. Its lively and creative \nand, at the same time, refined in \nits use of a minimalist color scheme \nwith different shades of the same hue."""})

    def AAC():
        colors = {
            1 : "#D79922",
            2 : "#EFE2BA",
            3 : "#F13C20",
            4 : "#4056A1",
            5 : "#C5CBE3"
        }

        site = tk.Label(mainframe,image=aacpic)
        site.place(x=50,y=270)

        ic.configure({"background": colors[1],"fg": "black"})
        ic.delete(0, END)
        ic.insert(0, colors[1])

        iic.configure({"background": colors[2],"fg": "black"})
        iic.delete(0, END)
        iic.insert(0, colors[2])

        iiic.configure({"background": colors[3],"fg": "black"})
        iiic.delete(0, END)
        iiic.insert(0, colors[3])

        ivc.configure({"background": colors[4],"fg": "white"})
        ivc.delete(0, END)
        ivc.insert(0, colors[4])

        iivc.configure({"background": colors[5],"fg": "black"})
        iivc.delete(0, END)
        iivc.insert(0, colors[5])

        desc.configure({"text": """This colorful combination of \ngoldenrod, vermillion, dark blue and\n Dutch white brings to life this \nartsy and creative design for an \nonline archive of musical works."""})

    def EYA():
        colors = {
            1 : "#EDC7B7",
            2 : "#EEE2DC",
            3 : "#BAB2B5",
            4 : "#123C69",
            5 : "#AC3B61"
        }

        site = tk.Label(mainframe,image=eyapic)
        site.place(x=50,y=270)

        ic.configure({"background": colors[1],"fg": "black"})
        ic.delete(0, END)
        ic.insert(0, colors[1])

        iic.configure({"background": colors[2],"fg": "black"})
        iic.delete(0, END)
        iic.insert(0, colors[2])

        iiic.configure({"background": colors[3],"fg": "black"})
        iiic.delete(0, END)
        iiic.insert(0, colors[3])

        ivc.configure({"background": colors[4],"fg": "white"})
        ivc.delete(0, END)
        ivc.insert(0, colors[4])

        iivc.configure({"background": colors[5],"fg": "white"})
        iivc.delete(0, END)
        iivc.insert(0, colors[5])

        desc.configure({"text": """This unique blend of skin tones and \nmore elegant colors such as dark \nimperial blue and ruby makes this \nthe ideal color scheme for designs \nwith nuanced messages. \nReserved yet approachable; \nsophisticated yet fun: \nThese are the kinds of gray-area \nmessages that are effectively sent \nwith this eye-pleasing combination."""})

    def MYW():
        colors = {
            1 : "#EAE7DC",
            2 : "#D8C3A5",
            3 : "#8E8D8A",
            4 : "#E98074",
            5 : "#E85A4F"
        }

        site = tk.Label(mainframe,image=mywpic)
        site.place(x=50,y=270)

        ic.configure({"background": colors[1],"fg": "black"})
        ic.delete(0, END)
        ic.insert(0, colors[1])

        iic.configure({"background": colors[2],"fg": "black"})
        iic.delete(0, END)
        iic.insert(0, colors[2])

        iiic.configure({"background": colors[3],"fg": "white"})
        iiic.delete(0, END)
        iiic.insert(0, colors[3])

        ivc.configure({"background": colors[4],"fg": "black"})
        ivc.delete(0, END)
        ivc.insert(0, colors[4])

        iivc.configure({"background": colors[5],"fg": "white"})
        iivc.delete(0, END)
        iivc.insert(0, colors[5])

        desc.configure({"text": """Eggshell white, dark vanilla and \ntaupe gray with jelly bean red \nhighlights come together in this \nminimalist yet warm and inviting \nsite. The burst of energetic color \nthroughout the design makes this site\n elegant and inviting at the same time."""})

    def CAE():
        colors = {
            1 : "#5680E9",
            2 : "#84CEEB",
            3 : "#5AB9EA",
            4 : "#C1C8E4",
            5 : "#8860D0"
        }

        site = tk.Label(mainframe,image=caepic)
        site.place(x=50,y=270)

        ic.configure({"background": colors[1],"fg": "white"})
        ic.delete(0, END)
        ic.insert(0, colors[1])

        iic.configure({"background": colors[2],"fg": "black"})
        iic.delete(0, END)
        iic.insert(0, colors[2])

        iiic.configure({"background": colors[3],"fg": "black"})
        iiic.delete(0, END)
        iiic.insert(0, colors[3])

        ivc.configure({"background": colors[4],"fg": "black"})
        ivc.delete(0, END)
        ivc.insert(0, colors[4])

        iivc.configure({"background": colors[5],"fg": "white"})
        iivc.delete(0, END)
        iivc.insert(0, colors[5])

        desc.configure({"text": """The shades of blue and violet in this\n site are especially pleasing to the\n eye and evoke both energy and peace\n at the same time.\n Blueberry and sky blue are artfully\n combined with amethyst to give life\n to a refreshing and eye-pleasing color\n combination suitable for any design \nwhich aims to incite positive emotions."""})

    def CAT():
        colors = {
            1 : "#88bdbc",
            2 : "#254e58",
            3 : "#112d32",
            4 : "#4f4a41",
            5 : "#6e6658"
        }

        site = tk.Label(mainframe,image=catpic)
        site.place(x=50,y=270)

        ic.configure({"background": colors[1],"fg": "black"})
        ic.delete(0, END)
        ic.insert(0, colors[1])

        iic.configure({"background": colors[2],"fg": "white"})
        iic.delete(0, END)
        iic.insert(0, colors[2])

        iiic.configure({"background": colors[3],"fg": "white"})
        iiic.delete(0, END)
        iiic.insert(0, colors[3])

        ivc.configure({"background": colors[4],"fg": "white"})
        ivc.delete(0, END)
        ivc.insert(0, colors[4])

        iivc.configure({"background": colors[5],"fg": "white"})
        iivc.delete(0, END)
        iivc.insert(0, colors[5])

        desc.configure({"text": """If you're looking for a more muted \nand corporate look, this color scheme\n brings together shades of green, \nblue and brown that convey both \nprofessionalism and reliability. \nPhthalo Green, dark slate gray and \npewter blue are just some of the \ncolors used here."""})
    
    def VAE():
        colors = {
            1 : "#F8E9A1",
            2 : "#F76C6C",
            3 : "#A8D0E6",
            4 : "#374785",
            5 : "#24305E"
        }

        site = tk.Label(mainframe,image=vaepic)
        site.place(x=50,y=270)

        ic.configure({"background": colors[1],"fg": "black"})
        ic.delete(0, END)
        ic.insert(0, colors[1])

        iic.configure({"background": colors[2],"fg": "black"})
        iic.delete(0, END)
        iic.insert(0, colors[2])

        iiic.configure({"background": colors[3],"fg": "black"})
        iiic.delete(0, END)
        iiic.insert(0, colors[3])

        ivc.configure({"background": colors[4],"fg": "white"})
        ivc.delete(0, END)
        ivc.insert(0, colors[4])

        iivc.configure({"background": colors[5],"fg": "white"})
        iivc.delete(0, END)
        iivc.insert(0, colors[5])

        desc.configure({"text": """This bright and elegant color scheme\n brings together a very saturated \nlight cold blue with other shades, \nsuch as dark slate blue and pale\n cornflower blue.\n This combination is elegantly \ncomplemented by a bright and vivid \nshade of pink."""})

    def YAF():
        colors = {
            1 : "#A64AC9",
            2 : "#FCCD04",
            3 : "#FFB48F",
            4 : "#F5E6CC",
            5 : "#17E9E0"
        }

        site = tk.Label(mainframe,image=yafpic)
        site.place(x=50,y=270)

        ic.configure({"background": colors[1],"fg": "white"})
        ic.delete(0, END)
        ic.insert(0, colors[1])

        iic.configure({"background": colors[2],"fg": "black"})
        iic.delete(0, END)
        iic.insert(0, colors[2])

        iiic.configure({"background": colors[3],"fg": "black"})
        iiic.delete(0, END)
        iiic.insert(0, colors[3])

        ivc.configure({"background": colors[4],"fg": "black"})
        ivc.delete(0, END)
        ivc.insert(0, colors[4])

        iivc.configure({"background": colors[5],"fg": "black"})
        iivc.delete(0, END)
        iivc.insert(0, colors[5])

        desc.configure({"text": """This playful and colorful scheme \ncombines several vibrant hues: \nbright turquoise, \ntangerine yellow \nand \ndark orchid."""})
        
    def BPAP():
        colors = {
            1 : "#A1C3D1",
            2 : "#B39BC8",
            3 : "#F0EBF4",
            4 : "#F172A1",
            5 : "#E64398"
        }

        site = tk.Label(mainframe,image=bpappic)
        site.place(x=50,y=270)

        ic.configure({"background": colors[1],"fg": "black"})
        ic.delete(0, END)
        ic.insert(0, colors[1])

        iic.configure({"background": colors[2],"fg": "black"})
        iic.delete(0, END)
        iic.insert(0, colors[2])

        iiic.configure({"background": colors[3],"fg": "black"})
        iiic.delete(0, END)
        iiic.insert(0, colors[3])

        ivc.configure({"background": colors[4],"fg": "black"})
        ivc.delete(0, END)
        ivc.insert(0, colors[4])

        iivc.configure({"background": colors[5],"fg": "white"})
        iivc.delete(0, END)
        iivc.insert(0, colors[5])

        desc.configure({"text": """This lively site brings together a \nbright raspberry pink with softer \ncolors such as pastel blue and light\n pastel purple.\n The result is a wonderfully fresh \nand lighthearted color scheme."""})

    def SCC():
        colors = {
            1 : "#1F2605",
            2 : "#1F6521",
            3 : "#53900F",
            4 : "#A4A71E",
            5 : "#D6CE15"
        }

        site = tk.Label(mainframe,image=sccpic)
        site.place(x=50,y=270)

        ic.configure({"background": colors[1],"fg": "white"})
        ic.delete(0, END)
        ic.insert(0, colors[1])

        iic.configure({"background": colors[2],"fg": "white"})
        iic.delete(0, END)
        iic.insert(0, colors[2])

        iiic.configure({"background": colors[3],"fg": "white"})
        iiic.delete(0, END)
        iiic.insert(0, colors[3])

        ivc.configure({"background": colors[4],"fg": "black"})
        ivc.delete(0, END)
        ivc.insert(0, colors[4])

        iivc.configure({"background": colors[5],"fg": "black"})
        iivc.delete(0, END)
        iivc.insert(0, colors[5])

        desc.configure({"text": """This fresh and citrusy blend of \nlight greenish-yellows, lime green \nand black is a favorite among brands\n related to high-adrenaline sports\n and energy drinks."""})

    def RAC():
        colors = {
            1 : "#F78888",
            2 : "#F3D250",
            3 : "#ECECEC",
            4 : "#90CCF4",
            5 : "#5DA2D5"
        }

        site = tk.Label(mainframe,image=racpic)
        site.place(x=50,y=270)

        ic.configure({"background": colors[1],"fg": "black"})
        ic.delete(0, END)
        ic.insert(0, colors[1])

        iic.configure({"background": colors[2],"fg": "black"})
        iic.delete(0, END)
        iic.insert(0, colors[2])

        iiic.configure({"background": colors[3],"fg": "black"})
        iiic.delete(0, END)
        iiic.insert(0, colors[3])

        ivc.configure({"background": colors[4],"fg": "black"})
        ivc.delete(0, END)
        ivc.insert(0, colors[4])

        iivc.configure({"background": colors[5],"fg": "black"})
        iivc.delete(0, END)
        iivc.insert(0, colors[5])

        desc.configure({"text": """This bright and rich color \ncombination brings together a vivid\n yellow, blue and pink in this \nbeautiful minimalist design, which \ncan be used in lively yet \nprofessional projects."""})

    def CAS():
        colors = {
            1 : "#265077",
            2 : "#022140",
            3 : "#494B68",
            4 : "#1E4258",
            5 : "#2D5F5D"
        }

        site = tk.Label(mainframe,image=caspic)
        site.place(x=50,y=270)

        ic.configure({"background": colors[1],"fg": "white"})
        ic.delete(0, END)
        ic.insert(0, colors[1])

        iic.configure({"background": colors[2],"fg": "white"})
        iic.delete(0, END)
        iic.insert(0, colors[2])

        iiic.configure({"background": colors[3],"fg": "white"})
        iiic.delete(0, END)
        iiic.insert(0, colors[3])

        ivc.configure({"background": colors[4],"fg": "white"})
        ivc.delete(0, END)
        ivc.insert(0, colors[4])

        iivc.configure({"background": colors[5],"fg": "white"})
        iivc.delete(0, END)
        iivc.insert(0, colors[5])

        desc.configure({"text": """Oxford blue with a few bright blue \nand red highlights make this a very\n traditional and corporate site.\n Blue and green, which convey \nprofessionalism and stability, \nare commonly used colors for\n corporate reports."""})

    def GAFF():
        colors = {
            1 : "#806543",
            2 : "#33266e",
            3 : "#111111",
            4 : "#542f34",
            5 : "#a6607c"
        }

        site = tk.Label(mainframe,image=gaffpic)
        site.place(x=50,y=270)

        ic.configure({"background": colors[1],"fg": "white"})
        ic.delete(0, END)
        ic.insert(0, colors[1])

        iic.configure({"background": colors[2],"fg": "white"})
        iic.delete(0, END)
        iic.insert(0, colors[2])

        iiic.configure({"background": colors[3],"fg": "white"})
        iiic.delete(0, END)
        iiic.insert(0, colors[3])

        ivc.configure({"background": colors[4],"fg": "white"})
        ivc.delete(0, END)
        ivc.insert(0, colors[4])

        iivc.configure({"background": colors[5],"fg": "white"})
        iivc.delete(0, END)
        iivc.insert(0, colors[5])

        desc.configure({"text": """This blend of gold, purple and black\n bring to mind words such as wealth\n and extravagance.\n Accordingly, this combination can \nbe applied to designs related to \nfashion, luxury and high-end products."""})

    def ECAS():
        colors = {
            1 : "#501f3a",
            2 : "#cb2d6f",
            3 : "#cccccc",
            4 : "#14a098",
            5 : "#0f292f"
        }

        site = tk.Label(mainframe,image=ecaspic)
        site.place(x=50,y=270)

        ic.configure({"background": colors[1],"fg": "white"})
        ic.delete(0, END)
        ic.insert(0, colors[1])

        iic.configure({"background": colors[2],"fg": "black"})
        iic.delete(0, END)
        iic.insert(0, colors[2])

        iiic.configure({"background": colors[3],"fg": "black"})
        iiic.delete(0, END)
        iiic.insert(0, colors[3])

        ivc.configure({"background": colors[4],"fg": "white"})
        ivc.delete(0, END)
        ivc.insert(0, colors[4])

        iivc.configure({"background": colors[5],"fg": "white"})
        iivc.delete(0, END)
        iivc.insert(0, colors[5])

        desc.configure({"text": """This beautiful combination of \nviridian green and telemagenta over\n a dark background creates heightened\n visual interest and draws the \nviewer in at first glance. \nBold yet professional, this color \ncombination, when used correctly, \ncan even be applied to corporate\n designs."""})

    def LAIYF():
        colors = {
            1 : "#c34271",
            2 : "#f070a1",
            3 : "#16ffbd",
            4 : "#12c998",
            5 : "#439f76"
        }

        site = tk.Label(mainframe,image=laiyfpic)
        site.place(x=50,y=270)

        ic.configure({"background": colors[1],"fg": "white"})
        ic.delete(0, END)
        ic.insert(0, colors[1])

        iic.configure({"background": colors[2],"fg": "black"})
        iic.delete(0, END)
        iic.insert(0, colors[2])

        iiic.configure({"background": colors[3],"fg": "black"})
        iiic.delete(0, END)
        iiic.insert(0, colors[3])

        ivc.configure({"background": colors[4],"fg": "white"})
        ivc.delete(0, END)
        ivc.insert(0, colors[4])

        iivc.configure({"background": colors[5],"fg": "white"})
        iivc.delete(0, END)
        iivc.insert(0, colors[5])

        desc.configure({"text": """This combination is purposely loud, \nto the point that it might repel \nsome viewers.\n When looking to make a bold statement,\n though, this combination may work \nwell when done right, as in this case."""})

    # BUTTONS FOR COLOR SCHEMES
    cabbutton = tk.Button(windowcs,image=cabbuttonpic,command=CAB)
    cabbutton.place(x=0,y=0)

    naebutton = tk.Button(windowcs,image=naebuttonpic,command=NAE)
    naebutton.place(x=120,y=0)

    sasbutton = tk.Button(windowcs,image=sasbuttonpic,command=SAS)
    sasbutton.place(x=240,y=0)

    conabbutton = tk.Button(windowcs,image=conabbuttonpic,command=CONAB)
    conabbutton.place(x=360,y=0)

    laibutton = tk.Button(windowcs,image=laibuttonpic,command=LAI)
    laibutton.place(x=480,y=0)

    ralbutton = tk.Button(windowcs,image=ralbuttonpic,command=RAL)
    ralbutton.place(x=600,y=0)

    aacbutton = tk.Button(windowcs,image=aacbuttonpic,command=AAC)
    aacbutton.place(x=720,y=0)

    eyabutton = tk.Button(windowcs,image=eyabuttonpic,command=EYA)
    eyabutton.place(x=840,y=0)
    
    mywbutton = tk.Button(windowcs,image=mywbuttonpic,command=MYW)
    mywbutton.place(x=960,y=0)

    caebutton = tk.Button(windowcs,image=caebuttonpic,command=CAE)
    caebutton.place(x=1080,y=0)

    catbutton = tk.Button(windowcs,image=catbuttonpic,command=CAT)
    catbutton.place(x=0,y=110)

    vaebutton = tk.Button(windowcs,image=vaebuttonpic,command=VAE)
    vaebutton.place(x=120,y=110)

    yafbutton = tk.Button(windowcs,image=yafbuttonpic,command=YAF)
    yafbutton.place(x=240,y=110)

    bpapbutton = tk.Button(windowcs,image=bpapbuttonpic,command=BPAP)
    bpapbutton.place(x=360,y=110)

    sccbutton = tk.Button(windowcs,image=sccbuttonpic,command=SCC)
    sccbutton.place(x=480,y=110)

    racbutton = tk.Button(windowcs,image=racbuttonpic,command=RAC)
    racbutton.place(x=600,y=110)

    casbutton = tk.Button(windowcs,image=casbuttonpic,command=CAS)
    casbutton.place(x=720,y=110)

    gaffbutton = tk.Button(windowcs,image=gaffbuttonpic,command=GAFF)
    gaffbutton.place(x=840,y=110)

    ecasbutton = tk.Button(windowcs,image=ecasbuttonpic,command=ECAS)
    ecasbutton.place(x=960,y=110)

    laiyfbutton = tk.Button(windowcs,image=laiyfbuttonpic,command=LAIYF)
    laiyfbutton.place(x=1080,y=110)

    empty = tk.Label(mainframe,image=csepic)
    empty.place(x=50,y=270,width=580,height=350)

    # Entry for Color Hexadecimals
    ic = tk.Entry(windowcs,bg="white")
    ic.place(x=650,y=300)

    iic = tk.Entry(windowcs,bg="white")
    iic.place(x=650,y=370)

    iiic = tk.Entry(windowcs,bg="white")
    iiic.place(x=650,y=440)

    ivc = tk.Entry(windowcs,bg="white")
    ivc.place(x=650,y=510)

    iivc = tk.Entry(windowcs,bg="white")
    iivc.place(x=650,y=580)
    
    # Label for Color Scheme Description
    desc = tk.Label(windowcs,bg="white",justify="center",font=30)
    desc.place(x=850,y=270,width=300,height=350)

# Function - To Do List -------------------------------------------------------------------
def openTDL():
    # Creates Color Scheme Window
    windowtdl = Toplevel(root)
    windowtdl.title("TO DO LIST")     
    windowtdl.resizable(width=False,height=False)
    windowtdl.geometry("500x350") 
    windowtdl.iconbitmap("stuff\\runiticon.ico")
    
    #tdlist button change
    #addbutton change
    def addbuttontdlhover(atdl):
        addtdlbuttonchangepic = tk.PhotoImage(file = "stuff\\addtdlbuttonchange.png")
        buttonaddtask.config (image=addtdlbuttonchangepic)
        buttonaddtask.image = addtdlbuttonchangepic
    def addbuttontdlleave(atdl):
        addtdlbuttonchangepic = tk.PhotoImage(file = "stuff\\calbuttonadd.png")
        buttonaddtask.config (image=addtdlbuttonchangepic)
        buttonaddtask.image = addtdlbuttonchangepic 
    #delete button change
    def deletebuttontdlhover(dtdl):
        deletetdlbuttonchangepic = tk.PhotoImage(file = "stuff\\deletetdlbuttonchange.png")
        buttondeletetask.config (image=deletetdlbuttonchangepic)
        buttondeletetask.image = deletetdlbuttonchangepic
    def deletebuttontdlleave(dtdl):
        deletetdlbuttonchangepic = tk.PhotoImage(file = "stuff\\calbuttonminus.png")
        buttondeletetask.config (image=deletetdlbuttonchangepic)
        buttondeletetask.image = deletetdlbuttonchangepic 
    #load button change
    def loadbuttontdlhover(ltdl):
        loadtdlbuttonchangepic = tk.PhotoImage(file = "stuff\\loadtdlbuttonchange.png")
        buttonloadtask.config (image=loadtdlbuttonchangepic)
        buttonloadtask.image = loadtdlbuttonchangepic
    def loadbuttontdlleave(ltdl):
        loadtdlbuttonchangepic = tk.PhotoImage(file = "stuff\\tdlload.png")
        buttonloadtask.config (image=loadtdlbuttonchangepic)
        buttonloadtask.image = loadtdlbuttonchangepic    
    #save button change
    def savebuttontdlhover(stdl):
        savetdlbuttonchangepic = tk.PhotoImage(file = "stuff\\savetdlbuttonchange.png")
        buttonsavetask.config (image=savetdlbuttonchangepic)
        buttonsavetask.image = savetdlbuttonchangepic
    def savebuttontdlleave(stdl):
        savetdlbuttonchangepic = tk.PhotoImage(file = "stuff\\tdlsave.png")
        buttonsavetask.config (image=savetdlbuttonchangepic)
        buttonsavetask.image = savetdlbuttonchangepic   
    #clear button change
    def clearbuttontdlhover(ctdl):
        cleartdlbuttonchangepic = tk.PhotoImage(file = "stuff\\cleartdlbuttonchange.png")
        buttoncleartasks.config (image=cleartdlbuttonchangepic)
        buttoncleartasks.image = cleartdlbuttonchangepic
    def clearbuttontdlleave(ctdl):
        cleartdlbuttonchangepic = tk.PhotoImage(file = "stuff\\tdlclear.png")
        buttoncleartasks.config (image=cleartdlbuttonchangepic)
        buttoncleartasks.image = cleartdlbuttonchangepic           

    # FUNCTIONS FOR TO DO LIST
    # Function to Add task
    def Addtask():
        task = entrytask.get()
        if task != "":
            listboxtasks.insert(END, task)
            entrytask.delete(0, END)
        else:
            tk.messagebox.showwarning(title="Warning!", message="You must enter a task.")

    # Function to Delete Task
    def Deletetask():
        try:
            taskindex = listboxtasks.curselection()[0]
            listboxtasks.delete(taskindex)
        except:
            tkinter.messagebox.showwarning(title="warning",message="You must select a task.")     
    
    # Function to Load Tasks
    def Loadtasks():
        try:
            tasks = pickle.load(open("tasks.dat","rb"))
            listboxtasks.delete(0, END)
            for task in tasks:
                listboxtasks.insert(tk.END,task)
        except:
            tkinter.messagebox.showwarning(title="Warning!",message="Cannot find tasks.dat")        

    # Function to Save Tasks
    def Savetasks():
        tasks = listboxtasks.get(0, listboxtasks.size())
        pickle.dump(tasks, open("tasks.dat", "wb"))

    # Funcrtion to Clear Tasks
    def Cleartasks():
        listboxtasks.delete(0, END)
    
    # Main Frame for the window
    framebg = tk.Label(windowtdl,image=bgi)
    framebg.place(relwidth=1, relheight=1)

    # Frame for Tasks
    taskframe = tk.Frame(windowtdl)
    taskframe.pack()

    listboxtasks = tk.Listbox(taskframe, height=10,font=10, width=50,bg="#33266e", fg="#ccffff")
    listboxtasks.pack(side=tk.LEFT)

    scrollbar = tk.Scrollbar(taskframe)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    listboxtasks.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listboxtasks.yview)
    
    # Entry for Tasks
    entrytask = tk.Entry(windowtdl,font=5, width=50, bg="#ccffff",fg="#33266e")
    entrytask.place(x=20,y=210)

    # BUTTONS FOR TO DO LIST
    buttonaddtask = tk.Button(windowtdl,image=calbuttonaddpic ,text="Add Task", width=45, command=Addtask)
    buttonaddtask.place(width=95,height=95,x=0,y=240)

    buttonaddtask.bind("<Enter>",addbuttontdlhover)
    buttonaddtask.bind("<Leave>",addbuttontdlleave)
    
    buttondeletetask = tk.Button(windowtdl,image=calbuttonminuspic, text="Delete Task", width=45, command=Deletetask)
    buttondeletetask.place(width=95,height=95,x=100,y=240)

    buttondeletetask.bind("<Enter>",deletebuttontdlhover)
    buttondeletetask.bind("<Leave>",deletebuttontdlleave)

    buttonloadtask = tk.Button(windowtdl,image=tdlloadpic, text="Load Tasks", width=45, command=Loadtasks)
    buttonloadtask.place(width=95,height=95,x=200,y=240)

    buttonloadtask.bind("<Enter>",loadbuttontdlhover)
    buttonloadtask.bind("<Leave>",loadbuttontdlleave)

    buttonsavetask = tk.Button(windowtdl,image=tdlsavepic, text="Save Tasks", width=45, command=Savetasks)
    buttonsavetask.place(width=95,height=95,x=300,y=240)

    buttonsavetask.bind("<Enter>",savebuttontdlhover)
    buttonsavetask.bind("<Leave>",savebuttontdlleave)

    buttoncleartasks = tk.Button(windowtdl,image=tdlclearpic, text="Clear Tasks", width=45, command=Cleartasks)
    buttoncleartasks.place(width=95,height=95,x=400,y=240)

    buttoncleartasks.bind("<Enter>",clearbuttontdlhover)
    buttoncleartasks.bind("<Leave>",clearbuttontdlleave)

# Function - Python Colors ----------------------------------------------------------------
def openPC():
    global pencolor

    # Creates Python Colors Window
    windowpc = Toplevel(root)
    windowpc.title("PYTHON COLORS")     
    windowpc.resizable(width=False,height=False)
    windowpc.geometry("800x520") 
    windowpc.iconbitmap("stuff\\runiticon.ico")

    # Main Frame for Python Colors
    mainframe = tk.Label(windowpc,image=bgi)
    mainframe.place(relwidth=1, relheight=1)

    # Frame for Colors
    color_frame = LabelFrame (windowpc,text="Color",font=('arial,15'),bd=5,relief=RIDGE,bg="white")
    color_frame.place(x=0,y=0,width=70,height=185)

    # FUNCTIONS FOR PYTHON COLORS
    # Functions for Colors
    def redc():
        global pencolor
        pencolor = "red"
    def orangec():
        global pencolor
        pencolor = "orange"
    def yellowc():
        global pencolor
        pencolor = "yellow"
    def greenc():
        global pencolor
        pencolor = "green"
    def lightgreenc():
        global pencolor
        pencolor = "light green"
    def lightbluec():
        global pencolor
        pencolor = "light blue"
    def bluec():
        global pencolor
        pencolor = "blue"
    def darkbluec():
        global pencolor
        pencolor = "dark blue"
    def purplec():
        global pencolor
        pencolor = "purple"
    def pinkc():
        global pencolor
        pencolor = "pink"
    def blackc():
        global pencolor
        pencolor = "black"
    def brownc():
        global pencolor
        pencolor = "brown"
    def whitec():
        global pencolor
        pencolor = "white"

    # Function to Save Painting
    def savepaint():
        try:
            tk.messagebox.showinfo('Image saving','Make sure windows are\nnot overlapping.')
            filename = filedialog.asksaveasfilename(defaultextension='.png')
            x = windowpc.winfo_rootx() + canvas.winfo_x()
            y = windowpc.winfo_rooty() + canvas.winfo_y()
            x1 = x + canvas.winfo_width()
            y1 = y + canvas.winfo_height()
            IG.grab().crop((x,y,x1,y1)).save(filename)
            tk.messagebox.showinfo('Image saved','Image is saved as ' + str(filename))
        except:
            tk.messagebox.showerror('Error',"Something went wrong.\nUnable to save image")

    # Function to Clear Canvas
    def clearpaint():
        canvas.delete("all")        

    # BUTTONS FOR PYTHON COLORS
    redbtn = Button(color_frame,bg="red",bd=2,relief=RIDGE,width=3,command=redc)
    redbtn.grid(row=0,column=0)

    orangebtn = Button(color_frame,bg="orange",bd=2,relief=RIDGE,width=3,command=orangec)
    orangebtn.grid(row=0,column=1)

    yellowbtn = Button(color_frame,bg="yellow",bd=2,relief=RIDGE,width=3,command=yellowc)
    yellowbtn.grid(row=1,column=0)

    greenbtn = Button(color_frame,bg="green",bd=2,relief=RIDGE,width=3,command=greenc)
    greenbtn.grid(row=1,column=1)

    lightgreenbtn = Button(color_frame,bg="light green",bd=2,relief=RIDGE,width=3,command=lightgreenc)
    lightgreenbtn.grid(row=2,column=0)

    lightbluebtn = Button(color_frame,bg="light blue",bd=2,relief=RIDGE,width=3,command=lightbluec)
    lightbluebtn.grid(row=2,column=1)

    bluebtn = Button(color_frame,bg="blue",bd=2,relief=RIDGE,width=3,command=bluec)
    bluebtn.grid(row=3,column=0)

    darkbluebtn = Button(color_frame,bg="dark blue",bd=2,relief=RIDGE,width=3,command=darkbluec)
    darkbluebtn.grid(row=3,column=1)

    purplebtn = Button(color_frame,bg="purple",bd=2,relief=RIDGE,width=3,command=purplec)
    purplebtn.grid(row=4,column=0)

    pinkbtn = Button(color_frame,bg="pink",bd=2,relief=RIDGE,width=3,command=pinkc)
    pinkbtn.grid(row=4,column=1)

    blackbtn = Button(color_frame,bg="black",bd=2,relief=RIDGE,width=3,command=blackc)
    blackbtn.grid(row=5,column=0)

    brownbtn = Button(color_frame,bg="brown",bd=2,relief=RIDGE,width=3,command=brownc)
    brownbtn.grid(row=5,column=1)

    erasebutton = tk.Button(windowpc,text="Eraser",bd=4,bg="white",command=whitec,width=8,relief=RIDGE)
    erasebutton.place(x=0,y=187)      

    clearbutton = tk.Button(windowpc,text="Clear",bd=4,bg="white",command=clearpaint,width=8,relief=RIDGE)
    clearbutton.place(x=0,y=217) 

    savebutton = tk.Button(windowpc,text="Save",bd=4,bg="white",command=savepaint,width=8,relief=RIDGE)
    savebutton.place(x=0,y=247) 

    # Scale for pen and eraser
    pensizeframe = LabelFrame(windowpc,text="size",bd=5,bg="white",font=('arial',15,'bold'),relief=RIDGE)
    pensizeframe.place(x=0,y=310,height=200,width=70)
    
    pensize = Scale(pensizeframe,orient=VERTICAL,from_=50,to=0,length=170)
    pensize.set(1)
    pensize.grid(row=0,column=1,padx=15)

    # Canvas
    canvas = Canvas(windowpc,bg='white',bd=5,relief=GROOVE,height=500,width=700)
    canvas.place(x=80,y=0)
    
    # Function for Painting
    def paint(event):
        x1,y1 = (event.x-2),(event.y-2)
        x2,y2 = (event.x + 2),(event.y + 2)
        
        canvas.create_oval(x1,y1,x2,y2,fill=pencolor,outline=pencolor,width=pensize.get())

    # Bind to Mouse Event
    canvas.bind('<B1-Motion>',paint)

# Function - Number Sorter ----------------------------------------------------------------
def openNS():
    # Creates Number Sorter Window
    windowNS = Toplevel(root)
    windowNS.title("NUMBER SORTER")     
    windowNS.resizable(width=False,height=False)
    windowNS.geometry("500x350")
    windowNS.iconbitmap("stuff\\runiticon.ico") 

    # FUNCTIONS FOR BUTTON HOVER CHANGE
    # add button hover change
    def addbuttonnshover(ans):
        addnsbuttonchangepic = tk.PhotoImage(file = "stuff\\addnsbuttonchange.png")
        buttonaddnum.config (image=addnsbuttonchangepic)
        buttonaddnum.image = addnsbuttonchangepic
    def addbuttonnsleave(ans):
        addnsbuttonchangepic = tk.PhotoImage(file = "stuff\\calbuttonadd.png")
        buttonaddnum.config (image=addnsbuttonchangepic)
        buttonaddnum.image = addnsbuttonchangepic 
    # delete button hover change
    def deletebuttonnshover(dns):
        deletensbuttonchangepic = tk.PhotoImage(file = "stuff\\deletensbuttonchange.png")
        buttondeletenum.config (image=deletensbuttonchangepic)
        buttondeletenum.image = deletensbuttonchangepic
    def deletebuttonnsleave(dns):
        deletensbuttonchangepic = tk.PhotoImage(file = "stuff\\calbuttonminus.png")
        buttondeletenum.config (image=deletensbuttonchangepic)
        buttondeletenum.image = deletensbuttonchangepic 
    # ascend button hover change
    def ascendbuttonnshover(acns):
        ascendnsbuttonchangepic = tk.PhotoImage(file = "stuff\\ascendnsbuttonchange.png")
        buttonascending.config (image=ascendnsbuttonchangepic)
        buttonascending.image = ascendnsbuttonchangepic
    def ascendbuttonnsleave(acns):
        ascendnsbuttonchangepic = tk.PhotoImage(file = "stuff\\ascendlogo.png")
        buttonascending.config (image=ascendnsbuttonchangepic)
        buttonascending.image = ascendnsbuttonchangepic    
    # save button hover change
    def descendbuttonnshover(dns):
        descendnsbuttonchangepic = tk.PhotoImage(file = "stuff\\descendnsbuttonchange.png")
        buttondescending.config (image=descendnsbuttonchangepic)
        buttondescending.image = descendnsbuttonchangepic
    def descendbuttonnsleave(dns):
        descendnsbuttonchangepic = tk.PhotoImage(file = "stuff\\descendlogo.png")
        buttondescending.config (image=descendnsbuttonchangepic)
        buttondescending.image = descendnsbuttonchangepic   
    # clear button hover change
    def clearbuttonnshover(cns):
        clearnsbuttonchangepic = tk.PhotoImage(file = "stuff\\clearnsbuttonchange.png")
        buttonclearnums.config (image=clearnsbuttonchangepic)
        buttonclearsnums.image = clearnsbuttonchangepic
    def clearbuttonnsleave(cns):
        clearnsbuttonchangepic = tk.PhotoImage(file = "stuff\\tdlclear.png")
        buttonclearnums.config (image=clearnsbuttonchangepic)
        buttonclearnums.image = clearnsbuttonchangepic

    # FUNCTIONS FOR NUMBER SORTING
    def Addnum():
        try:
            num = entrytask.get()
            if type(num) != int:
                raise ValueError
            else:
                if num != "":
                    listboxnum.insert(END, num)
                    entrytask.delete(0, END)
                else:
                    tk.messagebox.showwarning(title="Warning!", message="You must enter a number.")
        except ValueError:
            tk.messagebox.showwarning("Error!", "Invalid input")

    def Deletenum():
        try:
            numindex = listboxnum.curselection()[0]
            listboxnum.delete(numindex)
        except:
            tkinter.messagebox.showwarning(title="Warning!",message="You must select a number.")

    def Ascending():
        n=0
        length = listboxnum.size()
        numlist = []
        for i in range(length):
            num = int(listboxnum.get(n))
            numlist.append(num)
            n += 1
        sortedlist = sorted(numlist)
        n=0
        listboxnum.delete(0, END)
        for i in range(length):
            listboxnum.insert(0, sortedlist[n])
            n += 1

    def Descending():
        n=0
        length = listboxnum.size()
        numlist = []
        for i in range(length):
            num = int(listboxnum.get(n))
            numlist.append(num)
            n += 1
        sortedlist = sorted(numlist, reverse=True)
        n=0
        print(sortedlist)
        listboxnum.delete(0, END)
        for i in range(length):
            listboxnum.insert(0, sortedlist[n])
            n += 1

    def Clearnums():
        listboxnum.delete(0, END)

    # Frame for Background
    framebg = tk.Label(windowNS,image=bgi)
    framebg.place(relwidth=1, relheight=1)

    # Frame for Numbers
    numframe = tk.Frame(windowNS)
    numframe.pack()

    listboxnum = tk.Listbox(numframe, height=10,font=10, width=50,bg="#33266e", fg="#ccffff")
    listboxnum.pack(side=tk.LEFT)

    scrollbar = tk.Scrollbar(numframe)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    listboxnum.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listboxnum.yview)
    
    # Entry for Number input
    entrytask = tk.Entry(windowNS,font=5, width=50, bg="#ccffff",fg="#33266e")
    entrytask.place(x=20,y=210)

    # BUTTONS FOR NUMBER SORTER
    buttonaddnum = tk.Button(windowNS,image=calbuttonaddpic ,text="Add Number", width=45, command=Addnum)
    buttonaddnum.place(width=95,height=95,x=0,y=240)

    buttonaddnum.bind("<Enter>",addbuttonnshover)
    buttonaddnum.bind("<Leave>",addbuttonnsleave)

    buttondeletenum = tk.Button(windowNS,image=calbuttonminuspic ,text="Delete Number", width=45, command=Deletenum)
    buttondeletenum.place(width=95,height=95,x=100,y=240)

    buttondeletenum.bind("<Enter>",deletebuttonnshover)
    buttondeletenum.bind("<Leave>",deletebuttonnsleave)

    buttonascending = tk.Button(windowNS,image=ascendlogopic ,text="Sort in Ascending Order", width=45, command=Ascending)
    buttonascending.place(width=95,height=95,x=200,y=240)

    buttonascending.bind("<Enter>",ascendbuttonnshover)
    buttonascending.bind("<Leave>",ascendbuttonnsleave)

    buttondescending = tk.Button(windowNS,image=descendlogopic ,text="Sort in Ascending Order", width=45, command=Descending)
    buttondescending.place(width=95,height=95,x=300,y=240) 

    buttondescending.bind("<Enter>",descendbuttonnshover)
    buttondescending.bind("<Leave>",descendbuttonnsleave)

    buttonclearnums = tk.Button(windowNS,image=tdlclearpic, text="Clear", width=45, command=Clearnums)
    buttonclearnums.place(width=95,height=95,x=400,y=240)

    buttonclearnums.bind("<Enter>",clearbuttonnshover)
    buttonclearnums.bind("<Leave>",clearbuttonnsleave)
    
# Function - Code Dictionary --------------------------------------------------------------  
def openCD():
    # Creates Code Dictionary Window
    windowCD = Toplevel(root)
    windowCD.title("Code Dictionary")     
    windowCD.resizable(width=False,height=False)
    windowCD.geometry("900x810")
    windowCD.iconbitmap("stuff\\runiticon.ico")

    def select():
        word_index = Listbox_words.curselection()[0]
        Defword = str(def_dict[word_index])
        CodeExample = str(code_dict[word_index])
        Definition_Entry.configure({"text" : Defword})
        Example_Entry.configure({"text" : CodeExample})
    
    # LISTS FOR CODE DICTIONARY
    # Words
    name_dict = [
        "Alternative" ,
        "Arithmetic Operators",
        "Arguments",
        "Assignment Operators",
        "Bitwise Operators",
        "Break Statement",
        "Collections",
        "Comments",
        "Comparison Operators",
        "Complex",
        "Concatenate Strings",
        "Continue Statement",
        "Control Structures",
        "Debugging",
        "Dictionary",
        "Data Types",
        "Eval Function",
        "Exception Handling",
        "Expression",
        "Float",
        "Format method",
        "For loop",
        "Function",
        "Global Variables",
        "Identity Operators",
        "If...Else Statement",
        "If Statement",
        "Input Function",
        "Int",
        "Jumping statements",
        "List",
        "Literals",
        "Local Scope",
        "Logical Operators",
        "Looping",
        "Membership Operators",
        "Modules",
        "Nested If...Elif...Else",
        "Nested loop",
        "Parameter",
        "Print Statement",
        "Python",
        "Reserved words",
        "Return Values",
        "Scope",
        "Sequential Statement",
        "Set",
        "Software Testing",
        "Tuple",
        "Variables",
        "Variable Names",
        "While loop"]
    
    # Definitions
    def_dict = [
        "AKA decision making statement;\n\n Decision making statement depends\n on the condition block that needs\n to be executed or not which is\n defined by condition.",
        "Used with numeric values to perform common mathematical operations",
        "The value that is sent to the function when it is called",
        "Assignment operators are used in Python to assign values to variables.",
        "Bitwise operators act on operands as if they were strings of binary digits.\n They operate bit by bit, hence the name.",
        "The break statement terminates the loop containing it.\n Control of the program flows to the statement immediately after the body of the loop.",
        "Collections in Python are containers that are used to store collections of data,\n for example, list, dict, set, tuple etc.",
        "Comments in Python begin with a hash mark (#) and whitespace \ncharacter and continue to the end of the line.\nComments are in the source code for humans to read,\n not for computers to execute.",
        "A comparison operator in python, also called python relational operator,\n compares the values of two operands and returns \nTrue or False based on whether the condition is met.\n We have six of these, including and limited to- less than,\n greater than, less than or equal to,\n greater than or equal to, equal to, and not equal to.",
        "Python complex() function is used to convert numbers\n or string into a complex number.",
        "String concatenation means add strings together.",
        "The continue statement is used to skip the rest of the code \ninside a loop for the current iteration only. \nLoop does not terminate but continues on with the next iteration.",
        "A control structure (or flow of control) is a block of programming that \nanalyses variables and chooses a direction\n in which to go based on given parameters.",
        "A debugger is a program that can help you find out \nwhat is going on in a computer program.\n You can stop the execution at any \nprescribed line number, print out variables,\n continue execution, stop again, execute statements one by one,\n and repeat such actions until you have tracked \ndown abnormal behavior and found bugs.",
        "Dictionaries are Python’s implementation of a data \nstructure that is more generally known as an associative array.\n A dictionary consists of a collection of key-value pairs. \nEach key-value pair maps the key to its associated value.",
        "Data types are the classification or categorization of data items.\n It represents the kind of value that tells what \noperations can be performed on a particular data.\n Since everything is an object in Python programming, \ndata types are actually classes and variables are instance (object) of these classes.",
        "Python’s eval() allows you to evaluate arbitrary Python \nexpressions from a string-based or compiled-code-based input.\n This function can be handy when you’re trying to \ndynamically evaluate Python expressions from any input \nthat comes as a string or a compiled code object.",
        "An exception is an event, which occurs during the \nexecution of a program that disrupts the normal flow of the program's instructions.\n In general, when a Python script encounters \na situation that it cannot cope with, it raises an exception.\nAn exception is a Python object that represents an error.",
        "An expression is an instruction that combines values \nand operators and always evaluates down to a single value.",
        "float (floating point real values) − Also called floats,\n they represent real numbers and are written with a decimal point\n dividing the integer and fractional parts. \nFloats may also be in scientific notation, with E or e \nindicating the power of 10 (2.5e2 = 2.5 x 102 = 250).",
        "str.format() is one of the string formatting methods in Python3,\n which allows multiple substitutions and value formatting.\n This method lets us concatenate elements within\n a string through positional formatting.",
        "The for loop in Python is used to iterate over a sequence \n(list, tuple, string) or other iterable objects. \nIterating over a sequence is called traversal.",
        "A function is a block of code which only runs when it is called.\nYou can pass data, known as parameters, into a function.\nA function can return data as a result.",
        "In Python, a variable declared outside of the \nfunction or in global scope is known as a global variable.\n This means that a global variable can be \naccessed inside or outside of the function.",
        "Identity operators are used to compare the objects, not if they are equal,\n but if they are actually the same object,\n with the same memory location.",
        "The if-else statement is used to execute both the \ntrue part and the false part of a given condition. \nIf the condition is true, the if block code is executed and if the condition is false,\n the else block code is executed.",
        "the if statement is how you perform this sort of decision-making.\n It allows for conditional execution of a statement or group\n of statements based on the value of an expression.",
        "an input function which lets you ask a user for some text input.\n You call this function to tell the program to \nstop and wait for the user to key in the data.",
        "The int() function converts the specified value into an integer number.",
        "Jump statements in python are used to alter the flow of a \nloop like you want to skip a part of a loop or terminate a loop",
        "Lists are used to store multiple items in a single variable",
        "Generally, literals are a notation for representing \na fixed value in source code.",
        "A variable created inside a function belongs to the local \nscope of that function, and can only be used inside that function.",
        "Logical operators in Python are used for conditional \nstatements are true or false. \nLogical operators in Python are AND, OR and NOT.",
        "A for loop is used for iterating over a sequence \n(that is either a list, a tuple, a dictionary, a set, or a string)",
        "A Membership Operator in Python can be defined as being\n an operator that is used to validate the membership of a value.",
        "A module allows you to logically organize your Python code.\n Grouping related code into a module makes the code\n easier to understand and use.",
        "In general nested if-else statement is used when \nwe want to check more than one conditions.",
        "A nested loop is a loop inside a loop.\nThe ""inner loop"" will be executed one time for \neach iteration of the ""outer loop"".",
        "A parameter is the variable listed inside \nthe parentheses in the function definition.",
        "The print() function prints the specified message \nto the screen, or other standard output device.",
        "Python is a high-level programming language \ndesigned to be easy to read and simple to implement.",
        "Reserved words (also called keywords) are defined with\n predefined meaning and syntax in the language.",
        "A return statement is used to end the execution of the function call\n and “returns” the result (value of the expression\n following the return keyword) to the caller.",
        "A variable is only available from inside the region it is created.",
        "Sequential statements are set of statements where the execution process \nwill happen in sequence manner. So, these kind of \nstatements are called as sequential statements.",
        "A Set is an unordered collection data type that is iterable,\n mutable and has no duplicate elements.",
        "Software testing is the process of verifying a system wit\n the purpose of identifying any errors, gaps or missing \nrequirement versus the actual requirement.",
        "A tuple is a collection of objects which ordered and immutable. \nTuples are sequences, just like lists.",
        "Variables are containers for storing data values.",
        "variable names in Python can be any length and can consist of \nuppercase and lowercase letters (A-Z, a-z), digits (0-9), \nand the underscore character (_).",
        "A while loop is a control flow statement which allows code to \nbe executed repeatedly, depending on whether a condition is \nsatisfied or not. As long as some condition is true, \n'while' repeats everything inside the loop block."]

    # Example Code / Syntax
    code_dict = [
        "See Also: Simple if, if...else, Nested if..elif..else" ,
        "x = 1\ny = 1\nz = x + y\nprint(z)\n\nOUTPUT:\n2",
        "See Also: Parameters, Functions",
        "x = 1\nprint(x)\n\nOUTPUT:\n1",
        "z = x & y",
        "i = 1\nwhile(i<=6):\n    print(i)\ni+=1\nif i==3\n   break\n\nOUPUT:\n1\n2",
        "See Also: List, Tuple, Sets, Dictionaries",
        "#This is a single line comment\n\n#This is a\n#multi line\n#comment",
        """x = 1\ny = 1\nif x == y\n    print("x is equal to y")\n\nOUTPUT:\nx is equal to y""",
        "x = 2j",
        """x = "Python is "\ny = "awesome"\nz = x + y\nprint(z)\n\nOUTPUT:\nPython is awesome""",
        "i = 1\nwhile(i<=6):\n    print(i)\ni+=1\nif i==3\n   continue\n\nOUPUT:\n1\n2\n4\n5",
        "See Also: Sequential Statement, Alternative, Looping",
        "See Also: Testing, Exception Handling",
        """my_dict = {\n     "Name" : "Entelysa",\n     "Age" : "1",\n}\nprint(my_dict)\n\nOUTPUT:\n{'Name':
        Entelysa', 'Age':'1'}""",
        "See Also: Variable, Int, Float, Complex",
        "See Also: Input Function",
        "try:\n     #code\nexcept:\n     #code",
        "x = 2 + 3\nprint(x)\n\nOUTPUT:\n5",
        "x = 1.50",
        """x = 1\ny = "x is ()"\nprint(y.format(x))\n\nOUTPUT:x is 1""",
        "for counter_variable in range():\n     statements-block",
        """def my_function(x):\n     print("x = " + x)\nmy_function(1)\n\nOUTPUT:\nx = 1""",
        "See Also: Scope, Local Scope",
        "x is y",
        """x = 1\nif x == 1:\n     print("x is 1")\nelse:\n     print("x is not 1")\n\nOUTPUT:\nx is 1""",
        "if <condition>:\n     statements",
        "<variable> = input(<prompt>)",
        "x = 1",
        "See Also: Break, Continue",
        "fruits = ['apple', 'orange', 'grapes']",
        """print("Hello World!")\n\nOUTPUT:\nHello World!""",
        "See Also: Scope, Global Variables",
        "x = 20\nif x > 5 and x > 10\n     print(x)\n\nOUPUT:\n20",
        "See Also: While loop, For loop, Nested loop",
        "x in y",
        "",
        "if <condition-1>:\n     statements-block 1\nelif <condition-2>:\n     statements-block 2\nelse:\n     statements-block n",
        "See Also: While loop, For loop, Looping",
        "See Also: Arguments, Functions",
        "x = 1\nprint(x)\n\nOUTPUT:\n1",
        "",
        "Example of Reserved Words:\nFalse\nclass\nfinally\nis\nreturn\nNone\ncontinut\nfor\nty\nTrue\ndef\nnwhile",
        "See Also: Functions",
        "See Also: Local Scope, Global Variables",
        "See Also: Control Structures, Alternative, Looping",
        "set = {'1', '2', '3'}",
        "See Also: Testing, Debugging, Exception Handling",
        "tuple = ('x','y','z')",
        "x = 5",
        "See Also: Variables, Reserved Words",
        "x=10\nwhile(i<=15):\n     print(i)\n     i = i+1\n\nOUPUT:\n10\n11\n12\n13\n14\n15"]

    # Frame for Background
    mainframe = tk.Label(windowCD,image=bgicd)
    mainframe.place(relwidth=1, relheight=1)

    # Frame for Words
    resultsframe = tk.Frame(windowCD)
    resultsframe.place(x=20,y=150,height=550,width=250)

    # Listbox for Words
    Listbox_words = tk.Listbox(resultsframe,bg="#33266e", fg="#ccffff")
    Listbox_words.place(relheight=1,relwidth=1)
    n=0
    length = len(name_dict)
    for i in range(length):
        Listbox_words.insert(END, name_dict[n])
        n += 1

    scrollbar = tk.Scrollbar(resultsframe)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    Listbox_words.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=Listbox_words.yview)

    # Entry for Definition
    Definition_Entry = tk.Label(windowCD,font=30,bg="#33266e", fg="#ccffff")
    Definition_Entry.place(x=300,y=150,height=350,width=575)

    # Entry for Code Examples
    Example_Entry = tk.Label(windowCD,font=30,bg="#33266e", fg="#ccffff",justify=LEFT)
    Example_Entry.place(x=300,y=540,height=250,width=575)

    # Button to select word
    SelectButton = tk.Button(windowCD,image=selectcdbutton,text="SELECT",command=select)
    SelectButton.place(x=20,y=710,height=90,width=250)

def opencreator():
    windowCreator = Toplevel(root)
    windowCreator.title("THE CREATORS")     
    windowCreator.resizable(width=False,height=False)
    windowCreator.geometry("500x300")
    windowCreator.iconbitmap("stuff\\runiticon.ico")

    framebg = tk.Label(windowCreator,image=creatorspic)
    framebg.place(relwidth=1, relheight=1)

# MAIN MENU ===============================================================================
# Canvas
canvas = tk.Canvas(root, height=700, width=750)
canvas.pack()

#Background--------------------------------------------------------------------------------

background_label = tk.Label(root,image=bgi)
background_label.place(relwidth=1, relheight=1)

#music ====================================================================================
mframe = tk.Frame(root)
mframe.place(x=670,y=665,height=35,width=78)

# Function - Volume For Theme
def volume(x):
    pygame.mixer.music.set_volume(volumeslider.get())

volumeslider = Scale(root,from_=0,to=1,orient=HORIZONTAL,value=0.5,command=volume,length=125 )
volumeslider.place(x=530,y=670)

# Function - Custom Music
def opencm():
    tk.messagebox.showinfo("Custom Music", "Put your custom music\nin the folder RunIT/audio/")
    windowCM = Toplevel(root)
    windowCM.title("Custom Music")     
    windowCM.resizable(width=False,height=False)
    windowCM.geometry("500x350")
    windowCM.iconbitmap("stuff\\runiticon.ico")

    mainframe = tk.Label(windowCM,image=bgi)
    mainframe.place(relwidth=1, relheight=1)

    def volume(x):
        pygame.mixer.music.set_volume(volumeslider.get())

    def  playtime():
        currenttime = pygame.mixer.music.get_pos() / 1000
        convertedcurrenttime = time.strftime('%M:%S',time.gmtime(currenttime))
        statusbar.config(text=convertedcurrenttime)
        statusbar.after(1000,playtime) 

    def addsong():
        song = filedialog.askopenfilename(initialdir='audio/',title="choose a song",filetypes=(("mp3 files","*.mp3"),))
        songlist.insert(END,song)

    def addmanysongs():
        songs = filedialog.askopenfilenames(initialdir='audio/',title="choose a song",filetypes=(("mp3 files","*.mp3"),))   
        
        for song in songs:
            songlist.insert(END,song)


    def play():
        song  = songlist.get(ACTIVE)

        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)

        playtime()

        sliderposition = int(playtime)

    def stop():
        pygame.mixer.music.stop()

  
    def pause(is_paused):
        global paused
        paused = is_paused

        if paused:
            pygame.mixer.music.unpause()
            paused = False
        else:    
            pygame.mixer.music.pause()
            paused = True

    def nextsong():
        nextone = songlist.curselection()
        nextone = nextone[0]+1
        song = songlist.get(nextone)
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)
        songlist.selection_clear(0,END)
        songlist.activate(nextone)
        songlist.selection_set(nextone, last=None)

    def lastsong():
            nextone = songlist.curselection()
            nextone = nextone[0]-1
            song = songlist.get(nextone)
            pygame.mixer.music.load(song)
            pygame.mixer.music.play(loops=0)
            songlist.selection_clear(0,END)
            songlist.activate(nextone)
            songlist.selection_set(nextone, last=None) 

    def deletesong():
        songlist.delete(ANCHOR)
        pygame.mixer.music.stop()        

    def deleteallsongs():
        songlist.delete(0,END)
        pygame.mixer.music.stop() 

    songlist = tk.Listbox(windowCM,bg="#33266e", fg="#ccffff",width=70)
    songlist.pack(pady=20)

    volumeslider = Scale(windowCM,from_=0,to=1,orient=HORIZONTAL,value=1,command=volume,length=110 )
    volumeslider.place(x=370,y=220)

    bbtn = tk.Button(windowCM,text="back",image=lastmusicpic,command=lastsong)
    bbtn.place(x=50,y=200)
    fbtn = tk.Button(windowCM,text="forward",image=nextmusicpic,command=nextsong)
    fbtn.place(x=110,y=200)
    plybtn = tk.Button(windowCM,text="play",image=playmusicpic,command=play)
    plybtn.place(x=170,y=200)
    pbtn = tk.Button(windowCM,text="pause",image=pausemusicpic,command=lambda:pause(paused))
    pbtn.place(x=230,y=200)
    sbtn = tk.Button(windowCM,text="stop",image=stopsmusicpic,command=stop)
    sbtn.place(x=290,y=200)

    menu = tk.Menu(windowCM)
    windowCM.config(menu=menu)

    statusbar = tk.Label(windowCM,text='',bd=1,relief=GROOVE,anchor=E)
    statusbar.pack(fill=X, side=BOTTOM,ipady=2)

    addsongmenu = Menu(menu)
    menu.add_cascade(label="Add Songs",menu=addsongmenu)
    addsongmenu.add_command(label="Add One Song To Playlist",command=addsong)
    addsongmenu.add_command(label="Add Many Songs To Playlist",command=addmanysongs)

    removesongmenu = tk.Menu(menu)
    menu.add_cascade(label="Remove Song From Playlist",menu=removesongmenu,command=deletesong)
    removesongmenu.add_command(label="Remove All Songs From Playlist",command=deleteallsongs)
    
custommusicbutton = tk.Button(root,text="custom music",image=custommusicpic,command=opencm)
custommusicbutton.place(x=5,y=665)

#APPMUSIC----------------------------------------------------------------------------------
moremusic = tk.Button(mframe,text="More",image=moremusicpic,bg="#FFFF00",state=ACTIVE,command=playmore)
moremusic.place(x=1)

moremusic.bind("<Enter>",morehover)
moremusic.bind("<Leave>",moreleave)

stopmusic = tk.Button(mframe,text="stop",image=stopmusicpic,bg="red",command=stop)
stopmusic.place(x=39) 

stopmusic.bind("<Enter>",stophover)
stopmusic.bind("<Leave>",stopleave)

# Main Frame===============================================================================
frame = tk.Label(root,image=bgi2)
frame.place(relwidth=1,relheight=0.22,relx=0.50,rely=0.05, anchor = "n" )

# Run IT logo
logosmol = logopic.subsample(3,3)
logo = tk.Button(frame,image=logosmol,command=opencreator)
logo.place(relx=0.50,rely=0.05,anchor="n")

# CLOCK ===================================================================================
cframe = tk.Frame(root)
cframe.place(x=310,y=0,height=30,width=150)

def clock():  
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    ampm = time.strftime("%p")

    timelabel.config(text=hour + ":" + minute + ":" + second + " " + ampm)
    timelabel.after(1000,clock)
    

timelabel = tk.Label(cframe,text="",font=("Helvetica"),bg="#33266e", fg="#ccffff")
timelabel.place(relheight=1,relwidth=1)

clock()

# Frame for buttons========================================================================

# frame for number converter
nc_frame = tk.Label(root,image=bgi2)
nc_frame.place(x=80, y=250, width=123,height=113,)

#frame for Encryption Decryption
ed_frame = tk.Label(root,image=bgi2)
ed_frame.place(x=200, y=250, width=123,height=113,)

#frame for random number generator
rng_frame = tk.Label(root,image=bgi2)
rng_frame.place(x=320, y=250, width=123,height=113,)

# frame for calculator
cal_frame = tk.Label(root,image=bgi2)
cal_frame.place(x=440, y=250, width=123,height=113,)

#frame for number converter
rpg_frame = tk.Label(root,image=bgi2)
rpg_frame.place(x=560, y=250, width=123,height=113,)

# frame for color scheme
cs_frame = tk.Label(root,image=bgi2)
cs_frame.place(x=80, y=363, width=123,height=113,)

# frame for to do list
tdl_frame = tk.Label(root,image=bgi2)
tdl_frame.place(x=200, y=363, width=123,height=113,)

# frame python colors
cd_frame = tk.Label(root,image=bgi2)
cd_frame.place(x=320, y=363, width=123,height=113,)

# frame number sorter
ns_frame = tk.Label(root,image=bgi2)
ns_frame.place(x=440, y=363, width=123,height=113,)

# frame number sorter
pc_frame = tk.Label(root,image=bgi2)
pc_frame.place(x=560, y=363, width=123,height=113,)

# BUTTONS-----------------------------------------------------------------------------------

# Number Conversion Buttons
buttonnc = tk.Button(nc_frame, image=NCbuttonpic, cursor="heart",command=openNC) #text="NC", fg="#FF8040",activeforeground="#40BFFF",cursor="heart",command=openNC) 
buttonnc.place(x=0, y=0)

# Number Conversion Button Image change - Mouse hover
buttonnc.bind("<Enter>",buttonnchover)
buttonnc.bind("<Leave>",buttonncleave)

# Encryption Decryption Button
buttonED = tk.Button(ed_frame,image=EDbuttonpic, text="ED", fg="#FF8040",activeforeground="#40BFFF",cursor="heart",command=openED) 
buttonED.place(x=0, y=0)

# Encryption Decryption Button Image change - Mouse hover
buttonED.bind("<Enter>",buttonedhover)
buttonED.bind("<Leave>",buttonedleave)

# Random Number Generator Button
buttonRNG = tk.Button(rng_frame,image=RNGbuttonpic, text="RNG", fg="#FF8040",activeforeground="#40BFFF",cursor="heart",command=openRNG) 
buttonRNG.place(x=0, y=0)

buttonRNG.bind("<Enter>",buttonrnghover)
buttonRNG.bind("<Leave>",buttonrngleave)

# Calculator Button
buttonCAL = tk.Button(cal_frame,image=CALbuttonpic, text="CAL", fg="#FF8040",activeforeground="#40BFFF",cursor="heart",command=openCAL) 
buttonCAL.place(x=0, y=0)

buttonCAL.bind("<Enter>",buttoncalhover)
buttonCAL.bind("<Leave>",buttoncalleave)

# Random Password Generator Button
buttonRPG = tk.Button(rpg_frame, image=RPGbuttonpic,text="RPG", fg="#FF8040",activeforeground="#40BFFF",cursor="heart",command=openRPG) 
buttonRPG.place(x=0, y=0)

buttonRPG.bind("<Enter>",buttonrpghover)
buttonRPG.bind("<Leave>",buttonrpgleave)

# Color Button
buttonCS = tk.Button(cs_frame,image=CSbuttonpic, text="CS", fg="#FF8040",activeforeground="#40BFFF",cursor="heart",command=openCS) 
buttonCS.place(x=0, y=0)

buttonCS.bind("<Enter>",buttoncshover)
buttonCS.bind("<Leave>",buttoncsleave)

# Code to do list Button
buttonTDL = tk.Button(tdl_frame, image=TDLbuttonpic,text="CD", fg="#FF8040",activeforeground="#40BFFF",cursor="heart",command=openTDL) 
buttonTDL.place(x=0, y=0)

buttonTDL.bind("<Enter>",buttontdlhover)
buttonTDL.bind("<Leave>",buttontdlleave)

#code dictionary button
buttonCD = tk.Button(cd_frame, image=CDbuttonpic,text="PC", fg="#FF8040",activeforeground="#40BFFF",cursor="heart",command=openCD) 
buttonCD.place(x=0, y=0)

buttonCD.bind("<Enter>",buttoncdhover)
buttonCD.bind("<Leave>",buttoncdleave)

# Number Sorter Button
buttonNS = tk.Button(ns_frame,image=NSbuttonpic, text="NS", fg="#FF8040",activeforeground="#40BFFF",cursor="heart",command=openNS) 
buttonNS.place(x=0, y=0)

buttonNS.bind("<Enter>",buttonnshover)
buttonNS.bind("<Leave>",buttonnsleave)

# python colors Button
buttonPC = tk.Button(pc_frame, image=PCbuttonpic,text="CS", fg="#FF8040",activeforeground="#40BFFF",cursor="heart",command=openPC) 
buttonPC.place(x=0, y=0)

buttonPC.bind("<Enter>",buttonpchover)
buttonPC.bind("<Leave>",buttonpcleave)

root.mainloop()