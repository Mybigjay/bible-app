from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import DataBase


class JanuaryCreateWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)

    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"



    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""



    def showjan(self):
        with open("January.txt", "r") as f:
            return (f.read())



class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)


    def loginBtn(self):
        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            sm.current = "main"
        else:
            invalidLogin()

    def createBtn(self):

        sm.current = "create"

    def FebBtn(self):

        sm.current = "Febcreate"

    def MarchBtn(self):

        sm.current = "Marchcreate"

    def AprilBtn(self):

        sm.current = "Aprilcreate"

    def MayBtn(self):

        sm.current = "Maycreate"
    def JuneBtn(self):

        sm.current = "Junecreate"








    def JanBtn(self):
        if dbjan.january1(self.JANUARY, self.WEEK1):
            MainWindow.current = self.JANUARY
            self.reset()
            """smjan.current = "main" """
        else:
            invalidLogin()



    def loginBtn(self):
        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            sm.current = "main"
        else:
            invalidLogin()



    """ def FebBtn(self):
        if db.validate(self.email.text, self.password.text):
            FebWindow.current = self.email.text
            self.reset()
            smFeb.current = "Febcreate"
        else:
            invalidLogin() """




class MainWindow(Screen):
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    JANUARY = ObjectProperty(None)
    current = ""

    def logOut(self):
        sm.current = "login"

    def on_enter(self, *args):
        password, name, created = db.get_user(self.current)
        self.n.text = "Account Name: " + name
        self.email.text = "Email: " + self.current
        self.created.text = "Created On: " + created


class FebWindow(Screen):
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    JANUARY = ObjectProperty(None)
    current = ""

    def logOut(self):
        smFeb.current = "login"

    def on_enter(self, *args):
        password, name, created = db.get_user(self.current)
        self.n.text = "Account Name: " + name
        self.email.text = "Email: " + self.current
        self.created.text = "Created On: " + created

    def showFeb(self):
        with open("abcd.txt", "r") as f:
            return (f.read())

class WindowManager(ScreenManager):
    pass
class WindowManagerFeb(ScreenManager):
    pass


def invalidLogin():
    pop = Popup(title='Invalid Login',
                  content=Label(text='Invalid username or password.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()







def invalidForm():
    pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(400, 400))

    pop.open()


""" FEBRUAY"""


class FebCreateWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                smFeb.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def showfeb(self):
        with open("abcd.txt", "r") as f:
            return (f.read())


""" MARCH"""
class MarchCreateWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def showmarch(self):
        with open("march.txt", "r") as f:
            return (f.read())



""" APRIL"""

class AprilCreateWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def showApril(self):
        with open("April.txt", "r") as f:
            return (f.read())

""" MAY"""
class MayCreateWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""



    def MayWeek1Btn(self):

        sm.current = "Mayweek1"

    def MayWeek2Btn(self):

        sm.current = "Mayweek2"

    def MayWeek3Btn(self):

        sm.current = "Mayweek3"

    def MayWeek4Btn(self):

        sm.current = "Mayweek4"

""" may week1"""

class Mayweek1Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "Maycreate"
            else:
                invalidForm()
        else:
            invalidForm()

    def Maycreate(self):
        self.reset()
        sm.current = "Maycreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"

    def showMayweek1(self):
        with open("mayweek1.txt", "r") as f:
            return (f.read())

""" may week2"""

class Mayweek2Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "Maycreate"
            else:
                invalidForm()
        else:
            invalidForm()

    def Maycreate(self):
        self.reset()
        sm.current = "Maycreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def showMayweek2(self):
        with open("mayweek2.txt", "r") as f:
            return (f.read())


""" MAYWEEK 3"""

class Mayweek3Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "Maycreate"
            else:
                invalidForm()
        else:
            invalidForm()

    def Maycreate(self):
        self.reset()
        sm.current = "Maycreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def showMayweek3(self):
        with open("mayweek3.txt", "r") as f:
            return (f.read())

""" MAYWEEK 4"""

class Mayweek4Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "Maycreate"
            else:
                invalidForm()
        else:
            invalidForm()

    def Maycreate(self):
        self.reset()
        sm.current = "Maycreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def showMayweek4(self):
        with open("mayweek4.txt", "r") as f:
            return (f.read())


""" JUNE """
class JuneCreateWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""



    def JuneWeek1Btn(self):

        sm.current = "Juneweek1"

    def JuneWeek2Btn(self):

        sm.current = "Juneweek2"

    def JuneWeek3Btn(self):

        sm.current = "Juneweek3"

    def JuneWeek4Btn(self):

        sm.current = "Juneweek4"







kv = Builder.load_file("my.kv")

sm = WindowManager()
smFeb = WindowManagerFeb()

db = DataBase("users.txt")
dbjan = DataBase("JAN.txt")

screens = [LoginWindow(name="login"),JanuaryCreateWindow(name="create"),FebCreateWindow(name="Febcreate"),MarchCreateWindow(name="Marchcreate"),AprilCreateWindow(name="Aprilcreate"),MayCreateWindow(name="Maycreate"),Mayweek1Window(name="Mayweek1"),Mayweek2Window(name="Mayweek2"),Mayweek3Window(name="Mayweek3"),Mayweek4Window(name="Mayweek4"),JuneCreateWindow(name="Junecreate"),MainWindow(name="main"),FebWindow(name="main")]
for screen in screens:
    sm.add_widget(screen)


sm.current = "login"


screen1 = [LoginWindow(name="login"),JanuaryCreateWindow(name="create"),FebCreateWindow(name="Febcreate"),MainWindow(name="main"),FebWindow(name="main")]
for screen in screen1:

    smFeb.add_widget(screen)

smFeb.current = "login"


class MyMainApp(App):
    def build(self):
        return sm
        return sma



if __name__ == "__main__":
    MyMainApp().run()
