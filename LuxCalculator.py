import tkinter
from tkinter import *
from tkinter import ttk
global AnswerBox
global result
result = 0 
AnswerBox = None
def MainWindowDaemon():
    global AnswerBox
    MainWindowDaemon = Tk()
    MainWindowDaemon.title("Lux Calculator")
    frm = ttk.Frame(MainWindowDaemon, padding=10)
    frm.grid()
    ttk.Label(frm, text="Bucko").grid(column=0, row=0)
    UserInput = ""
    MainEntryBox = Entry(MainWindowDaemon, textvariable = UserInput)
    MainEntryBox.grid(column= 1, row= 0)
    CalculatorRunner = Button(MainWindowDaemon, text="Run Calculation", command=lambda: CalculatorFunctionDaemon(MainEntryBox))
    CalculatorRunner.grid(column=0, row=1)
    QuitButton = Button(MainWindowDaemon, text="Quit Application", command=MainWindowDaemon.destroy).grid(row= 1, column= 1) 
    AnswerBox = ttk.Label(MainWindowDaemon, text="Result:" + str(result))
    AnswerBox.grid(row =2, column = 0)

    MainWindowDaemon.mainloop()

def CalculatorFunctionDaemon(MainEntryBox):
    global AnswerBox
    global result
    UserInput = MainEntryBox.get()
    WorkingValues = UserInput
    SplitValues = WorkingValues.split()
    try:
       result =  eval(UserInput)
    except SyntaxError:
        print("Oh No! Invalid Syntax")
        return None
    except KeyboardInterrupt:
        print("Keyboard Interrupt")
        return None
    except MemoryError:
        print("Something went horribly wrong and you should never see this")
        return None
    except OverflowError:
        print("Overflow error!")
        return None
    except ZeroDivisionError:
        print("Zero Division Error! Don't Do that!")
    finally:
        print(result)
        if AnswerBox:
            AnswerBox.config(text="Result: " + str(result))
MainWindowDaemon()
