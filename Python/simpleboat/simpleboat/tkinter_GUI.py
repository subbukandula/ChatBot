# -*- coding: utf-8 -*-
import tkinter as tk
import aiml
try:
    import ttk as ttk
    import ScrolledText
except ImportError:
    import tkinter.ttk as ttk
    import tkinter.scrolledtext as ScrolledText
import time


class TkinterGUI(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        """
        Create & set window variables.
        """
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("TMCLPORT Chatbot")
        
        self.bot = aiml.Kernel();
        self.bot.setBotPredicate('name', 'Allo')
        self.bot.setBotPredicate('master', 'Venkat')
        self.bot.learn("basic.aiml");
        self.bot.learn("apps.aiml");
        self.bot.learn("devurl.aiml");
        self.bot.learn("apps.aiml");

        self.initialize()

    def initialize(self):
        """
        Set window layout.
        """
        self.grid()

        self.respond = ttk.Button(self, text='Get Response', command=self.get_response)
        self.respond.grid(column=1, row=2, sticky='nesw', padx=3, pady=3)

        self.usr_input = ttk.Entry(self, state='normal')
        self.usr_input.grid(column=0, row=2, sticky='nesw', padx=3, pady=3)
        self.usr_input.bind('<Return>',self.get_response_enter)

        self.conversation_lbl = ttk.Label(self, anchor=tk.E, text='Conversation')
        self.conversation_lbl.grid(column=0, row=0, sticky='nesw', padx=3, pady=3)

        self.conversation = ScrolledText.ScrolledText(self, state='disabled')
        self.conversation.grid(column=0, row=1, columnspan=2, sticky='nesw', padx=3, pady=3)

        s = ttk.Style()
        s.configure('TButton', font=('Verdana', 11), foreground='maroon')

        s = ttk.Style()
        s.configure('TLabel', font=('Courier', 12))
        

    def get_response(self):
        """
        Get a response from the chatbot and display it.
        """
        user_input = self.usr_input.get()
        if user_input:
            self.usr_input.delete(0, tk.END)
            response = self.bot.respond(user_input)
            requester = 'You:'
            endUser = 'ChatBot:'
            self.conversation['state'] = 'normal'
            self.conversation.tag_config("green",foreground='green',font=('Courier', 10, 'bold'))
            self.conversation.tag_config("font",font=('Verdana', 10, 'normal'))
            self.conversation.insert(
                tk.END, "\n"+ requester +"\n" ,"green"
            )
            self.conversation.insert(
                tk.END, user_input + "\n" , "font" 
            )
            self.conversation.insert(
                tk.END, endUser +"\n" , "green"
            )
            self.conversation.insert(
                tk.END, str(response) + "\n" , "font"
            )
            self.conversation.see(tk.END)
            self.conversation['state'] = 'disabled'

            time.sleep(0.5)
            
    def get_response_enter(self,event):
        """
        Get a response from the chatbot and display it.
        """
        user_input = self.usr_input.get()
        if user_input:
            self.usr_input.delete(0, tk.END)
            response = self.bot.respond(user_input)
            requester = 'You:'
            endUser = 'ChatBot:'
            self.conversation['state'] = 'normal'
            self.conversation.tag_config("green",foreground='green',font=('Courier', 10, 'bold'))
            self.conversation.tag_config("font",font=('Verdana', 10, 'normal'))
            self.conversation.insert(
                tk.END, "\n"+ requester +"\n" ,"green"
            )
            self.conversation.insert(
                tk.END, user_input + "\n" , "font" 
            )
            self.conversation.insert(
                tk.END, endUser +"\n" , "green"
            )
            self.conversation.insert(
                tk.END, str(response) + "\n" , "font"
            )
            self.conversation.see(tk.END)
            self.conversation['state'] = 'disabled'

            time.sleep(0.5)

gui_example = TkinterGUI()
gui_example.mainloop()
