import customtkinter as ctk
import pyperclip as pc
import random

class PasswordGenerator:
    def __init__(self):
        self.uppercaseLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.lowercaseLetters = self.uppercaseLetters.lower()
        self.digits = '0123456789'
        self.symbols = '!@#$%^&*_-+=~'
        self.space = ' '

        self.combination = ''
        self.password = ''

    def generate(self, upper: bool, lower: bool, numbers: bool, symbols: bool, spaces: bool, length: int):
        if upper:
            self.combination += self.uppercaseLetters
        if lower:
            self.combination += self.lowercaseLetters
        if spaces:
            for x in range(int(length / 2)):
                self.combination += self.space
        if numbers:
            self.combination += self.digits
        if symbols:
            self.combination += self.symbols

        self.password = ''.join(random.sample(self.combination, length))
        return self.password

class Interface:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title('Secure Password Generator')

        WIDTH, HEIGHT = self.window.winfo_screenwidth(), self.window.winfo_screenheight()
        RESULTWIDTH, RESULTHEIGHT = ((WIDTH / 2) - (800 / 2) + 20), ((HEIGHT / 2) - (800 / 2) - 20)
        self.window.geometry(f'{800}x{800}+{int(RESULTWIDTH)}+{int(RESULTHEIGHT)}')
        print(WIDTH, HEIGHT)

        self.regFont = ctk.CTkFont('Gothic', 20)

        self.welcomeLabel = ctk.CTkLabel(self.window, text='Welcome to the Secure\nPassword Generator!!!', font=('Gothic', 50))

        self.string = ctk.StringVar(self.window, value='')
        self.passLabel = ctk.CTkLabel(self.window, text='Generated Password:', font=self.regFont)
        self.passwordEntry = ctk.CTkEntry(self.window, textvariable=self.string, font=self.regFont, state=ctk.DISABLED)
        self.copyButton = ctk.CTkButton(self.window, font=self.regFont, text='Copy', fg_color='green', hover_color='black', width=200, height=10, command=self.copy)

        self.checkLabel = ctk.CTkLabel(self.window, text='Choose desired password length:', font=self.regFont)

        self.passwordLength = ctk.CTkSlider(self.window, button_color='green', button_hover_color='white', from_=0, to=20, command=self.slide, width=300)
        self.passwordLength.set(0)

        self.passLengthLabel = ctk.CTkLabel(self.window, font=self.regFont, text='0')

        self.optVar1 = ctk.StringVar(self.window, value='off')
        self.option1 = ctk.CTkCheckBox(self.window, fg_color='green', hover_color='white', font=self.regFont, text='Include UPPERCASE letters', variable=self.optVar1, onvalue='on', offvalue='off')

        self.optVar2 = ctk.StringVar(self.window, value='off')
        self.option2 = ctk.CTkCheckBox(self.window, fg_color='green', hover_color='white', font=self.regFont, text='Include lowercase letters', variable=self.optVar2, onvalue='on', offvalue='off')

        self.optVar3 = ctk.StringVar(self.window, value='off')
        self.option3 = ctk.CTkCheckBox(self.window, fg_color='green', hover_color='white', font=self.regFont, text='Include numbers', variable=self.optVar3, onvalue='on', offvalue='off')

        self.optVar4 = ctk.StringVar(self.window, value='off')
        self.option4 = ctk.CTkCheckBox(self.window, fg_color='green', hover_color='white', font=self.regFont, text='Include symbols', variable=self.optVar4, onvalue='on', offvalue='off')

        self.optVar5 = ctk.StringVar(self.window, value='off')
        self.option5 = ctk.CTkCheckBox(self.window, fg_color='green', hover_color='white', font=self.regFont, text='Include spaces', variable=self.optVar5, onvalue='on', offvalue='off')

        self.generateButton = ctk.CTkButton(self.window, fg_color='green', hover_color='black', font=self.regFont, text='Generate', width=200, height=30, command=self.generate)

        # PACKING
        self.welcomeLabel.pack(pady=40)
        self.passLabel.pack()
        self.passwordEntry.pack(pady=10, ipadx=250, ipady=30)
        self.copyButton.pack()
        self.checkLabel.pack(pady=30)
        self.passwordLength.pack()
        self.passLengthLabel.pack(pady=20)
        self.option1.pack(pady=5)
        self.option2.pack(pady=5)
        self.option3.pack(pady=5)
        self.option4.pack(pady=5)
        self.option5.pack(pady=5)
        self.generateButton.pack(pady=40)

    def slide(self, value):
        self.passLengthLabel.configure(text=int(value))

    def generate(self):
        v1, v2, v3, v4, v5 = False, False, False, False, False

        if self.optVar1.get() == 'on':
            v1 = True
        if self.optVar2.get() == 'on':
            v2 = True
        if self.optVar3.get() == 'on':
            v3 = True
        if self.optVar4.get() == 'on':
            v4 = True
        if self.optVar5.get() == 'on':
            v5 = True

        PW = PasswordGenerator()
        password = PW.generate(v1, v2, v3, v4, v5, int(self.passwordLength.get()))

        self.string.set(password)

    def copy(self):
        password = self.string.get()
        pc.copy(password)

    def start(self):
        self.window.mainloop()

def main() -> None:
    application = Interface()
    application.start()

if __name__ == "__main__":
    main()
