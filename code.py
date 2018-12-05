from tkinter import *
import webbrowser
import time
import os
global w1
global w2

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.master.title("Grid Manager")

        for r in range(6):
            self.master.rowconfigure(r, weight=1)    
        for c in range(15):
            self.master.columnconfigure(c, weight=1)
            #Button(master, text="Button {0}".format(c)).grid(row=6,column=c,sticky=E+W)

        Frame1 = Frame(master, bg="peach puff")
        Frame1.grid(row = 0, column = 0, rowspan = 6, columnspan = 2, sticky = W+E+N+S)
        Frame2 = Frame(master, bg="black")
        Frame2.grid(row = 0, column = 2, rowspan = 6, columnspan = 11, sticky = W+E+N+S)
        Frame3 = Frame(master, bg="mediumpurple1")
        Frame3.grid(row = 0, column = 13, rowspan = 6, columnspan = 2, sticky = W+E+N+S)
        Frame4 = Frame(master,bg="grey")
        Frame4.grid(row=0,column = 13,rowspan=1,columnspan=2,sticky=W+E+N+S)
        m = PanedWindow(Frame3)
        m.pack( expand=1)
        def callback(event):
                 webbrowser.open_new(r"http://www.facebook.com")
        link = Label(Frame4, bg="grey",width=20,text="""FACEBOOK
        """, fg="peach puff", cursor="hand2", font='Helvetica 12 bold')
        link.pack()
        link.bind("<Button-1>", callback)
        img = PhotoImage(file = "logo.gif")
        def callback(event):
                 webbrowser.open_new(r"http://www.gmail.com")
        link = Label(Frame4, bg="grey",width=20,text="""GMAIL
        """, fg="peach puff", cursor="hand2", font='Helvetica 12 bold')
        link.pack()
        link.bind("<Button-1>", callback)
        img = PhotoImage(file = "logo.gif")

        w1 = Label(Frame2,text='NEWSYAP',width=30, font='Helvetica 30 bold',bg="black",foreground="peach puff").pack(side="top")
        
        def add_image():
            for widget in Frame2.winfo_children():
                  widget.destroy()
            logo = PhotoImage(file="D:\PYTHON\project\i1.gif")
            w1 = Label(Frame2, image=img,width=200,bg="black",foreground="peach puff").pack(side="top")
            explanation = """           BJP did exceptionally well in
            the 2nd phase of panchayat
            elections in Maharashtra."""
            w2 = Label(Frame2,bg="black",foreground="peach puff",
            justify=LEFT,
            width=70,
            padx = 10, 
            text=explanation).pack(side="top")
            def callback(event):
                 webbrowser.open_new(r"http://www.google.com")
            link = Label(Frame2, bg="black",width=70,text="""Maharashtra Gram Panchayat Elections:
            BJP leave Cong, Sena, NCP in the dust;
            win 1311 seats out of 3692
            """, fg="blue", cursor="hand2")
            link.pack()
            link.bind("<Button-1>", callback)

            
            w1 = Label(Frame2,foreground="peach puff",width=100,bg="black", image=img2).pack(side="top")
            explanation = """           However, the announcement failed to
            placate the workers and helpers, who have been on strike
            for nearly a month— agitating near Chief
            Sunday, 23 July 2017 - 8:00am"""
            w2 = Label(Frame2,bg="black",
            width=70,foreground="peach puff",
            justify=LEFT,
            padx = 10, 
            text=explanation).pack(side="top")
            def callback(event):
                 webbrowser.open_new(r"http://www.dnaindia.com/delhi/report-govt-to-hike-allowances-of-anganwadi-workers-2511016")
            link = Label(Frame2,bg="black", width=70,text="""Govt to hike allowances of anganwadi workers""", fg="blue", cursor="hand2")
            link.pack()
            link.bind("<Button-1>", callback)

            w1 = Label(Frame2,bg="black",width=100, image=img3).pack(side="top")
            explanation = """         Homegrown app adds wallet,
            UPI payment features in a bid to cash in
            on the growing digital transactions in India
            """
            w2 = Label(Frame2,foreground="peach puff",bg="black",
            width=70,
            justify=LEFT,
            padx = 10, 
            text=explanation).pack(side="top")
            
            def callback(event):
                 webbrowser.open_new(r"http://www.dnaindia.com/business/report-messaging-unicorn-hike-moves-into-payments-2478817")
            link = Label(Frame2,bg="black", width=70,text="""Messaging Unicorn Hike moves into payments""", fg="blue", cursor="hand2")
            link.pack()
            link.bind("<Button-1>", callback)
        def  business():
            for widget in Frame2.winfo_children():
                  widget.destroy()
            logo = PhotoImage(file="D:\PYTHON\project\i4.gif")
            w1 = Label(Frame2, bg="black",image=img4,width=100).pack(side="top")
            
            def callback(event):
                 webbrowser.open_new(r"http://www.dnaindia.com/personal-finance/report-with-ppf-nsc-out-of-bounds-here-are-smart-options-for-nris-to-invest-2558119")
            link = Label(Frame2,bg="black", width=70,text="""   Take gold exposure only
            hrough sovereign gold bond


  
            """, fg="blue", cursor="hand2")
            link.pack()
            link.bind("<Button-1>", callback)

            
            w1 = Label(Frame2,bg="black",width=100, image=img5).pack(side="top")
            explanation="""         The central bank advises it has not given
            any licence/authorisation to any entity/company to operate
            such schemes """
            w2 = Label(Frame2,bg="black",
            width=70,foreground="peach puff",
            justify=LEFT,
            padx = 10, 
            text=explanation).pack(side="top")
            def callback(event):
                 webbrowser.open_new(r"http://www.dnaindia.com/personal-finance/report-stay-away-from-bitcoins-few-people-understand-it-2558668")
            link = Label(Frame2,bg="black", width=70,text="""	 Stay away from bitcoins. Few people understand it


 """, fg="blue", cursor="hand2")
            link.pack()
            link.bind("<Button-1>", callback)

            w1 = Label(Frame2,bg="black",foreground="peach puff",width=100, image=img6).pack(side="top")
            explanation = """          Insurers have to implement
            the rules without awaiting further instructions
            """
            w2 = Label(Frame2,bg="black",foreground="peach puff",
            width=70,
            justify=LEFT,
            padx = 10, 
            text=explanation).pack(side="top")
         
            def callback(event):
                 webbrowser.open_new(r"http://www.dnaindia.com/personal-finance/report-aadhaar-linkage-to-insurance-covers-to-improve-customer-experience-lower-frauds-2558972")
            link = Label(Frame2,bg="black", width=70,text="""    Aadhaar linkage to insurance covers to
improve customer experience, lower frauds""", fg="blue", cursor="hand2")
            link.pack()
            link.bind("<Button-1>", callback)
        def  technology():
            for widget in Frame2.winfo_children():
                  widget.destroy()
            logo = PhotoImage(file="D:\PYTHON\project\i4.gif")
            w1 = Label(Frame2, bg="black",image=s1,width=100).pack(side="top")
            explanation="""         Professor Stephen Hawking has stated
            that Artificial Intelligence will soon replace humans as the
            dominant being on """
            w2 = Label(Frame2,
            width=70,bg="black",foreground="peach puff",
            justify=LEFT,
            padx = 10, 
            text=explanation).pack(side="top")
            def callback(event):
                 webbrowser.open_new(r"http://www.dnaindia.com/science/report-stephen-hawking-says-ai-will-replace-humans-as-dominant-being-on-earth-2558060")
            link = Label(Frame2,bg="black", width=70,text="""   	
            Stephen Hawking says AI will replace humans as dominant being on Earth!


  
            """, fg="blue", cursor="hand2")
            link.pack()
            link.bind("<Button-1>", callback)

            
            w1 = Label(Frame2,bg="black",width=100, image=s2).pack(side="top")
            explanation="""         China, which is building its own navigation system
            to rival United States GPS, has launched two BeiDou-3 satellites """
            w2 = Label(Frame2,bg="black",foreground="peach puff",
            width=70,
            justify=LEFT,
            padx = 10, 
            text=explanation).pack(side="top")
            def callback(event):
                 webbrowser.open_new(r"http://www.dnaindia.com/science/report-china-launches-2-navigation-satellites-2558022")
            link = Label(Frame2,bg="black", width=70,text="""	 	
China launches 2 navigation satellites


 """, fg="blue", cursor="hand2")
            link.pack()
            link.bind("<Button-1>", callback)

            w1 = Label(Frame2,bg="black",width=100, image=s3).pack(side="top")
            explanation = """          Insurers have to implement
            the rules without awaiting further instructions
            """
            w2 = Label(Frame2,bg="black",
            width=70,
            justify=LEFT,foreground="peach puff",
            padx = 10, 
            text=explanation).pack(side="top")
         
            def callback(event):
                 webbrowser.open_new(r"http://www.dnaindia.com/personal-finance/report-aadhaar-linkage-to-insurance-covers-to-improve-customer-experience-lower-frauds-2558972")
            link = Label(Frame2,bg="black", width=70,text="""    Aadhaar linkage to insurance covers to
improve customer experience, lower frauds""", fg="blue", cursor="hand2")
            link.pack()
            link.bind("<Button-1>", callback)

        def  sports():
            for widget in Frame2.winfo_children():
                  widget.destroy()
            logo = PhotoImage(file="D:\PYTHON\project\i4.gif")
            w1 = Label(Frame2,bg="black", image=img4,width=100).pack(side="top")
            
            def callback(event):
                 webbrowser.open_new(r"http://www.dnaindia.com/personal-finance/report-with-ppf-nsc-out-of-bounds-here-are-smart-options-for-nris-to-invest-2558119")
            link = Label(Frame2,bg="black", width=70,text="""   Take gold exposure only
            hrough sovereign gold bond


  
            """, fg="blue", cursor="hand2")
            link.pack()
            link.bind("<Button-1>", callback)

            
            w1 = Label(Frame2,width=100, bg="black",image=img5).pack(side="top")
            explanation="""         The central bank advises it has not given
            any licence/authorisation to any entity/company to operate
            such schemes """
            w2 = Label(Frame2,bg="black",foreground="peach puff",
            width=70,
            justify=LEFT,
            padx = 10, 
            text=explanation).pack(side="top")
            def callback(event):
                 webbrowser.open_new(r"http://www.dnaindia.com/personal-finance/report-stay-away-from-bitcoins-few-people-understand-it-2558668")
            link = Label(Frame2,bg="black", width=70,text="""	 Stay away from bitcoins. Few people understand it


 """, fg="blue", cursor="hand2")
            link.pack()
            link.bind("<Button-1>", callback)

            w1 = Label(Frame2,bg="black",width=100, image=img6).pack(side="top")
            explanation = """          Insurers have to implement
            the rules without awaiting further instructions
            """
            w2 = Label(Frame2,bg="black",foreground="peach puff",
            width=70,
            justify=LEFT,
            padx = 10, 
            text=explanation).pack(side="top")
         
            def callback(event):
                 webbrowser.open_new(r"http://www.dnaindia.com/personal-finance/report-aadhaar-linkage-to-insurance-covers-to-improve-customer-experience-lower-frauds-2558972")
            link = Label(Frame2,bg="black", width=70,text="""    Aadhaar linkage to insurance covers to
improve customer experience, lower frauds""", fg="blue", cursor="hand2")
            link.pack()
            link.bind("<Button-1>", callback)







        def  cricket():
            for widget in Frame2.winfo_children():
                  widget.destroy()
            logo = PhotoImage(file="D:\PYTHON\project\i4.gif")
            w1 = Label(Frame2,bg="black", image=img4,width=70).pack(side="top")
            
            def callback(event):
                 webbrowser.open_new(r"http://www.dnaindia.com/personal-finance/report-with-ppf-nsc-out-of-bounds-here-are-smart-options-for-nris-to-invest-2558119")
            link = Label(Frame2,bg="black", width=70,text="""   Take gold exposure only
            hrough sovereign gold bond


  
            """, fg="blue", cursor="hand2")
            link.pack()
            link.bind("<Button-1>", callback)

            
            w1 = Label(Frame2,width=100, bg="black",image=img5).pack(side="top")
            explanation="""         The central bank advises it has not given
            any licence/authorisation to any entity/company to operate
            such schemes """
            w2 = Label(Frame2,bg="black",
            width=70,foreground="peach puff",
            justify=LEFT,
            padx = 10, 
            text=explanation).pack(side="top")
            def callback(event):
                 webbrowser.open_new(r"http://www.dnaindia.com/personal-finance/report-stay-away-from-bitcoins-few-people-understand-it-2558668")
            link = Label(Frame2,bg="black", width=70,text="""	 Stay away from bitcoins. Few people understand it


 """, fg="blue", cursor="hand2")
            link.pack()
            link.bind("<Button-1>", callback)

            w1 = Label(Frame2,bg="black",width=100, image=img6).pack(side="top")
            explanation = """          Insurers have to implement
            the rules without awaiting further instructions
            """
            w2 = Label(Frame2,bg="black",foreground="peach puff",
            width=70,
            justify=LEFT,
            padx = 10, 
            text=explanation).pack(side="top")
         
            def callback(event):
                 webbrowser.open_new(r"http://www.dnaindia.com/personal-finance/report-aadhaar-linkage-to-insurance-covers-to-improve-customer-experience-lower-frauds-2558972")
            link = Label(Frame2,bg="black", width=70,text="""    Aadhaar linkage to insurance covers to
improve customer experience, lower frauds""", fg="blue", cursor="hand2")
            link.pack()
            link.bind("<Button-1>", callback)







        def  entertainment():
            for widget in Frame2.winfo_children():
                  widget.destroy()
            logo = PhotoImage(file="D:\PYTHON\project\i4.gif")
            w1 = Label(Frame2,bg="black", image=img4,width=100).pack(side="top")
            
            def callback(event):
                 webbrowser.open_new(r"http://www.dnaindia.com/personal-finance/report-with-ppf-nsc-out-of-bounds-here-are-smart-options-for-nris-to-invest-2558119")
            link = Label(Frame2,bg="black", width=70,text="""   Take gold exposure only
            hrough sovereign gold bond


  
            """, fg="blue", cursor="hand2")
            link.pack()
            link.bind("<Button-1>", callback)

            
            w1 = Label(Frame2,bg="black",width=70, image=img5).pack(side="top")
            explanation="""         The central bank advises it has not given
            any licence/authorisation to any entity/company to operate
            such schemes """
            w2 = Label(Frame2,bg="black",foreground="peach puff",
            width=70,
            justify=LEFT,
            padx = 10, 
            text=explanation).pack(side="top")
            def callback(event):
                 webbrowser.open_new(r"http://www.dnaindia.com/personal-finance/report-stay-away-from-bitcoins-few-people-understand-it-2558668")
            link = Label(Frame2,bg="black", width=70,text="""	 Stay away from bitcoins. Few people understand it


 """, fg="blue", cursor="hand2")
            link.pack()
            link.bind("<Button-1>", callback)

            w1 = Label(Frame2,width=100,bg="black", image=img6).pack(side="top")
            explanation = """          Insurers have to implement
            the rules without awaiting further instructions
            """
            w2 = Label(Frame2,bg="black",foreground="peach puff",
            width=70,
            justify=LEFT,
            padx = 10, 
            text=explanation).pack(side="top")
         
            def callback(event):
                 webbrowser.open_new(r"http://www.dnaindia.com/personal-finance/report-aadhaar-linkage-to-insurance-covers-to-improve-customer-experience-lower-frauds-2558972")
            link = Label(Frame2, bg="black",width=70,text="""    Aadhaar linkage to insurance covers to
improve customer experience, lower frauds""", fg="blue", cursor="hand2")
            link.pack()
            link.bind("<Button-1>", callback)







        def  lifestyle():
            for widget in Frame2.winfo_children():
                  widget.destroy()
            logo = PhotoImage(file="D:\PYTHON\project\i4.gif")
            w1 = Label(Frame2,bg="black", image=img4,width=100).pack(side="top")
            
            def callback(event):
                 webbrowser.open_new(r"http://www.dnaindia.com/personal-finance/report-with-ppf-nsc-out-of-bounds-here-are-smart-options-for-nris-to-invest-2558119")
            link = Label(Frame2, bg="black",width=70,text="""   Take gold exposure only
            hrough sovereign gold bond


  
            """, fg="blue", cursor="hand2")
            link.pack()
            link.bind("<Button-1>", callback)

            
            w1 = Label(Frame2,bg="black",width=100, image=img5).pack(side="top")
            explanation="""         The central bank advises it has not given
            any licence/authorisation to any entity/company to operate
            such schemes """
            w2 = Label(Frame2,bg="black",foreground="peach puff",
            width=70,
            justify=LEFT,
            padx = 10, 
            text=explanation).pack(side="top")
            def callback(event):
                 webbrowser.open_new(r"http://www.dnaindia.com/personal-finance/report-stay-away-from-bitcoins-few-people-understand-it-2558668")
            link = Label(Frame2, width=70,bg="black",text="""	 Stay away from bitcoins. Few people understand it


 """, fg="blue", cursor="hand2")
            link.pack()
            link.bind("<Button-1>", callback)

            w1 = Label(Frame2,width=100, bg="black",image=img6).pack(side="top")
            explanation = """          Insurers have to implement
            the rules without awaiting further instructions
            """
            w2 = Label(Frame2,bg="black",
            width=70,foreground="peach puff",
            justify=LEFT,
            padx = 10, 
            text=explanation).pack(side="top")
         
            def callback(event):
                 webbrowser.open_new(r"http://www.dnaindia.com/personal-finance/report-aadhaar-linkage-to-insurance-covers-to-improve-customer-experience-lower-frauds-2558972")
            link = Label(Frame2, bg="black",width=100,text="""    Aadhaar linkage to insurance covers to
improve customer experience, lower frauds""", fg="blue", cursor="hand2")
            link.pack()
            link.bind("<Button-1>", callback)






        def  education():
            for widget in Frame2.winfo_children():
                  widget.destroy()
            logo = PhotoImage(file="D:\PYTHON\project\i4.gif")
            w1 = Label(Frame2,bg="black", image=img4,width=100).pack(side="top")
            
            def callback(event):
                 webbrowser.open_new(r"http://www.dnaindia.com/personal-finance/report-with-ppf-nsc-out-of-bounds-here-are-smart-options-for-nris-to-invest-2558119")
            link = Label(Frame2, bg="black",width=70,text="""   Take gold exposure only
            hrough sovereign gold bond


  
            """, fg="blue", cursor="hand2")
            link.pack()
            link.bind("<Button-1>", callback)

            
            w1 = Label(Frame2,width=100,bg="black", image=img5).pack(side="top")
            explanation="""         The central bank advises it has not given
            any licence/authorisation to any entity/company to operate
            such schemes """
            w2 = Label(Frame2,bg="black",foreground="peach puff",
            width=70,
            justify=LEFT,
            padx = 10, 
            text=explanation).pack(side="top")
            def callback(event):
                 webbrowser.open_new(r"http://www.dnaindia.com/personal-finance/report-stay-away-from-bitcoins-few-people-understand-it-2558668")
            link = Label(Frame2,bg="black", width=70,text="""	 Stay away from bitcoins. Few people understand it


 """, fg="blue", cursor="hand2")
            link.pack()
            link.bind("<Button-1>", callback)

            w1 = Label(Frame2,bg="black",width=100, image=img6).pack(side="top")
            explanation = """          Insurers have to implement
            the rules without awaiting further instructions
            """
            w2 = Label(Frame2,bg="black",foreground="peach puff",
            width=70,
            justify=LEFT,
            padx = 10, 
            text=explanation).pack(side="top")
         
            def callback(event):
                 webbrowser.open_new(r"http://www.dnaindia.com/personal-finance/report-aadhaar-linkage-to-insurance-covers-to-improve-customer-experience-lower-frauds-2558972")
            link = Label(Frame2,bg="black", width=70,text="""    Aadhaar linkage to insurance covers to
improve customer experience, lower frauds""", fg="blue", cursor="hand2")
            link.pack()
            link.bind("<Button-1>", callback)
        b = Button(Frame1, text="INDIA",width=30,command = add_image,foreground="black",border="10",background="grey80").pack(pady=30)
        img = PhotoImage(file = "i1.gif")
        img2 = PhotoImage(file = "i2.gif")
        img3=PhotoImage(file = "i3.gif")
        img4=PhotoImage(file = "i4.gif")
        img5=PhotoImage(file = "i5.gif")
        img6=PhotoImage(file = "i6.gif")
        s1=PhotoImage(file = "s1.gif")
        s2=PhotoImage(file = "s2.gif")
        s3=PhotoImage(file = "s3.gif")
        b = Button(Frame1, text="Business",width=30,command = business,foreground="black",border="10",background="grey80").pack(pady=30)
        b = Button(Frame1, text="Technology",width=30,command=technology,foreground="black",border="10",background="grey80").pack(pady=30)
        b = Button(Frame1, text="Sports",width=30,command=sports,foreground="black",border="10",background="grey80").pack(pady=30)
        b = Button(Frame1, text="Cricket",width=30,command=cricket,foreground="black",border="10",background="grey80").pack(pady=30)
        b = Button(Frame1, text="Entertainment",width=30,command=entertainment,foreground="black",border="10",background="grey80").pack(pady=30)
        b = Button(Frame1, text="Lifestyle",width=30,command=lifestyle,foreground="black",border="10",background="grey80").pack(pady=30)
        b = Button(Frame1, text="Education",width=30,command=education,foreground="black",border="10",background="grey80").pack(pady=30)

        input_user = StringVar()
        input_field = Entry(Frame3, text=input_user,bd=5,width=50)
        input_field.pack(side=BOTTOM)
        def Enter_pressed(event):
               
               """Took the current string in the Entry field."""
               input_get = input_field.get()
               w1 = Label(Frame3,bd=5,width=50, background="peach puff",text=input_get+"""
                          """).pack(side="top")
               input_field.delete(0, "end")
               explanation = input_get
               localtime = time.asctime( time.localtime(time.time()) )
               t=Label(Frame3,width=51,text=localtime).pack(side="top")
               
               l=Label(Frame3,width=51,text="-----------------------------------------------------------------------").pack()
        input_field.bind("<Return>", Enter_pressed)
root = Tk()
app = Application(master=root)
app.mainloop()























