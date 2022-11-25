import email
from re import X
import tkinter as tk
import pyrebase
from tkinter.ttk import *
from tkinter import messagebox
import firebase_admin
from newsapi import NewsApiClient
from tkinter import *
from tkinter import messagebox 
import requests 
import json 

def anaSayfaEkrani():

    #Anasayfa Ekranı
    anasayfa = tk.Tk()
    anasayfa.geometry('1650x900+150+60')
    anasayfa.title("eHaber Uygulaması")

    btnHaberler = []
    trhaberler = ["genel", "eğlence","finans", "spor", "teknoloji", "sağlık"] 
    arkaPlanRenk = "#c60000"
    FontRengi = "#b0e0e6"
    title = Label(anasayfa, text="eHaber", font=("times new roman", 30, "bold"),  
    pady=2, relief=GROOVE, bg=arkaPlanRenk, fg=FontRengi).pack(fill=X) 



    #Api gelen bilgilerinin ekrana yazılması 
    def eHaber(a):
        tur = a.widget.cget('text').lower() 
        if tur == "GENEL" : 
            tur = "GENERAL"
        elif tur == "EĞLENCE" : 
            tur = "ENTERTAINMENT"
        elif tur == "SPOR":
            tur = "BUSINESS"
        elif tur == "TEKNOLOJİ":
            tur = "TECHNOLOGY"
        else : 
            tur = "HEALTH"





        apiurl = f'http://newsapi.org/v2/top-headlines?country=tr&category={tur}&apiKey=0e26e464830941f7b9c7f82f37151c2e'
        txtVeriler.insert(END, f"\n eHaber Uygulamasına Hoş Geldiniz..\n") 
        txtVeriler.insert(END, "--------------------------------------------------------------------\n") 
        txtVeriler.delete("1.0", END) 
        try: 
            cevap = (requests.get(apiurl).json())['articles'] 
            if(cevap != 0): 
                for i in range(len(cevap)): 
                    txtVeriler.insert(END, f"{cevap[i]['title']}\n") 
                    txtVeriler.insert(END, f"{cevap[i]['description']}\n\n") 
                    txtVeriler.insert(END, f"{cevap[i]['content']}\n\n") 
                    txtVeriler.insert(END, f"Okumaya Devam et...{cevap[i]['url']}\n") 
                    txtVeriler.insert(END, "--------------------------------------------------------------------\n") 
                    txtVeriler.insert(END, "--------------------------------------------------------------------\n") 
            else: 
                    txtVeriler.insert(END, "Üzgünüz, haber yok") 
        except Exception as e: 
                    messagebox.showerror('Hata', "Maalesef internete bağlanamıyorum veya haber uygulamasıyla ilgili bazı sorunlar var !!") 

    #Kategorilerinin menusu

    F1 = tk.LabelFrame(anasayfa, text="Kategoriler", font=("times new roman", 20, "bold"), bg= "gray") 
    F1.place(x=0, y=70, relwidth=1, height=100)
    for i in range(len(trhaberler)): 
            

            b = tk.Button(F1, text=trhaberler[i].upper(), width=20, font="arial 15 bold") 
            b.grid(row=0, column=i, padx=10, pady=15) 
            b.bind('<Button-1>', eHaber) 
            btnHaberler.append(b) 
            



    

    F2 = tk.Frame(anasayfa, relief=tk.GROOVE , bg="red")
    F2.place(x=70 , y=210 ,relwidth=0.9, relheight=0.7)
    haberBasligi = tk.Label(F2, text="Haberler", font=("arial", 20, "bold"),bg="red")
    haberBasligi.place(x=500 , y=0)
    dikeyScrol = tk.Scrollbar(F2, orient=tk.VERTICAL,width=14 , bg= "white") 
    txtVeriler = tk.Text(F2, yscrollcommand=dikeyScrol.set, font=("times new roman", 15, "bold"), bg="white", fg="#1c0f45" , height=100 , width=150) 
    dikeyScrol.pack(side=tk.RIGHT, fill=tk.Y) 
    dikeyScrol.config(command=txtVeriler.yview) 
    txtVeriler.insert(tk.END,"Lütfen Yukarıdan İlgili Kategoriyi Seçiniz ") 
    txtVeriler.pack() 


    
    anasayfa.mainloop()


#Giriş ekranı baslangıc
girisEKrani = tk.Tk()
#Ekranın boyutları 
girisEKrani.geometry("700x400")
girisEKrani.maxsize(700,400)
girisEKrani.minsize(700,400)
#Ekranın Baslıgı
girisEKrani.title("Uygulama Başlığı")

txtbaslik = tk.Label(text="Giriş Ekranı" , font="Verdana 15 italic" , fg="black")
txtbaslik.place(x=290,y=10)

#EPosta sifre 
txtEposta = tk.Label(text="E posta : " , font="Verdana 14")
txtEposta.place(x=100 , y=100)
txtSifre = tk.Label(text="Şifre : " , font="Verdana 14")
txtSifre.place(x=125 , y=170)

veriEposta = tk.Entry(width=20)
veriEposta.place(x=200 , y=100)
veriSifre = tk.Entry(width=20)
veriSifre.place(x=200, y=170)

#
#Kayit EKrani --------

def kayitEkrani():
    kayitEkrani = tk.Toplevel(girisEKrani)
     #Boyutları
    kayitEkrani.geometry("700x400+800+80")
    kayitEkrani.maxsize(700,400)
    kayitEkrani.minsize(700,400)
    #Title
    kayitEkrani.title("Kayıt Ol")

    #Kullanıcıdan bilgi almak
    txtEposta = tk.Label(kayitEkrani,text="E posta : " , font="Verdana 20")
    txtEposta.place(x=150 , y=100)
    txtSifre = tk.Label(kayitEkrani,text="Şifre : " , font="Verdana 20")
    txtSifre.place(x=185 , y=170)

    veriEposta =tk.Entry(kayitEkrani,width=20)
    veriEposta.place(x=300 , y=108)
    veriSifre = tk.Entry(kayitEkrani,width=20)
    veriSifre.place(x=300, y=180)

    #Firebase bağlaması

    firebaseconfig = {
        "apiKey": "AIzaSyA4mdhX9i0ew7w1_XJ8EZG4SYw7oULj-sE",
        "authDomain": "new-kayit.firebaseapp.com",
        "projectId": "new-kayit",
        "databaseURL": "xxxxxx",
        "storageBucket": "new-kayit.appspot.com",
        "messagingSenderId": "984392839671",
        "appId": "1:984392839671:web:70fe5e52b11f0439e83ef2",
        "measurementId": "G-JYSMTQFHFL"
    }
    firebase = pyrebase.initialize_app(firebaseconfig)
    auth = firebase.auth()

    #KAyıt tamamalama fonksiyonu 

    def kayit(): 
        a = veriEposta.get()
        b = veriSifre.get()
        #Hatayı önleme
        try : 
            user = auth.create_user_with_email_and_password(a,b)
            messagebox.showinfo("Başarılı" , "Kaydınız Başarılı Şekilde Oluştu.") 
            
        except:
           messagebox.showerror("Hata" , "Şifre 6 hane ve üstü olmalıdır.")
  #Kayıt tamamlama butonu 
    btnOnayla = tk.Button(kayitEkrani,text='Kayıt Ol' , font='Verdana 13' ,command=kayit)
    btnOnayla.place(x=250 , y=270)
 
    
    kayitEkrani.mainloop()   


def giris() : 

    firebaseconfig = {
        "apiKey": "AIzaSyA4mdhX9i0ew7w1_XJ8EZG4SYw7oULj-sE",
        "authDomain": "new-kayit.firebaseapp.com",
        "projectId": "new-kayit",
        "databaseURL": "xxxxxx",
        "storageBucket": "new-kayit.appspot.com",
        "messagingSenderId": "984392839671",
        "appId": "1:984392839671:web:70fe5e52b11f0439e83ef2",
        "measurementId": "G-JYSMTQFHFL"
    }
#Giriş Ekranı Giriş Yapma
    firebase = pyrebase.initialize_app(firebaseconfig)
    auth= firebase.auth()
    try:
        login = auth.sign_in_with_email_and_password(veriEposta.get(),veriSifre.get())
        girisEKrani.destroy()
        anaSayfaEkrani()
            
    except: 
        messagebox.showerror("Hata" , "Hatalı Kullanıcı adı ve sifre")
    


#Giriş yap ve kayıt ol butonları 

btnGiris = tk.Button(text="Giriş" ,font="Verdana 16" , command=giris)
btnKayit = tk.Button(text="Kayit" ,font="Verdana 16" , command=kayitEkrani)
btnGiris.place(x=150 , y=240)
btnKayit.place(x=300 , y=240)

#Giriş ekranı bitiş
girisEKrani.mainloop()


