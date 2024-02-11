import tkinter as tk
from tkinter import *
from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def left_state(self):
        pass

    @abstractmethod
    def right_state(self):
        pass

class TestState0(State):
    def __init__(self):
        self.text="Nono mf"
        self.left=""
        self.right=""
        #print(self.text)

    def left_state(self):
        return TestState1()

    def right_state(self):
        return TestState1()

class TestState1(State):
    def __init__(self):
        self.text="Here are two options"
        self.left="Yes"
        self.right="No"
        #print(self.text)

    def left_state(self):
        return TestState2()

    def right_state(self):
        return TestState0()

class TestState2(State):
    def __init__(self):
        self.text="2 more"
        self.left="Yes"
        self.right="No"
        #print(self.text)

    def left_state(self):
        return TestState3()

    def right_state(self):
        return TestState0()

class TestState3(State):
    def __init__(self):
        self.text="Last State"
        self.left=""
        self.right=""
        #print(self.text)

    def left_state(self):
        return TestState1()

    def right_state(self):
        return TestState1()






class State1(State):
    def __init__(self):
        self.text="Are you using Warpstone?"
        self.left="Yes"
        self.right="No"
        #print(self.text)

    def left_state(self):
        return State2()

    def right_state(self):
        return State7()

class State2(State):
    def __init__(self):
        self.text="Double any SL generated from Casting/Channeling Tests, subtracting used spell CN from the stone's total (1 gram of warpstone equals 20CN)."
        self.left=""
        self.right=""
        #print(self.text)

    def left_state(self):
        return State8()

    def right_state(self):
        return State8()

class State3(State):
    def __init__(self):
        self.text="Test Fails"
        self.left=""
        self.right=""
        #print(self.text)

    def left_state(self):
        return State1()

    def right_state(self):
        return State1()

class State4(State):
    def __init__(self):
        self.text="Roll on Minor Miscast Table."
        self.left=""
        self.right=""
        #print(self.text)

    def left_state(self):
        return State6()

    def right_state(self):
        return State6()

class State5(State):
    def __init__(self):
        self.text="Roll on Minor Miscast Table."
        self.left=""
        self.right=""
        #print(self.text)

    def left_state(self):
        return State3()

    def right_state(self):
        return State3()

class State6(State):
    def __init__(self):
        self.text="Add SL equal to Willpower Bonus to Channeling Test"
        self.left=""
        self.right=""
        #print(self.text)

    def left_state(self):
        return State15()

    def right_state(self):
        return State15()

class State7(State):
    def __init__(self):
        self.text="Are you in the vicinity of a corrupting influence?"
        self.left="Yes"
        self.right="No"
        #print(self.text)

    def left_state(self):
        return State8()

    def right_state(self):
        return State11()

class State8(State):
    def __init__(self):
        self.text="Any failed Casting/Channeling Test results in a Minor Miscast. Any future rolls which result in a Minor Miscast, is upgraded to a Major Miscast."
        self.left=""
        self.right=""
        #print(self.text)

    def left_state(self):
        return State11()

    def right_state(self):
        return State11()

class State9(State):
    def __init__(self):
        self.text="Did the roll result in a Fumble? (rolling doubles: 66, 55, 44)"
        self.left="Yes"
        self.right="No"
        #print(self.text)

    def left_state(self):
        return State5()

    def right_state(self):
        return State3()

class State10(State):
    def __init__(self):
        self.text="Does the caster posses Aethyric Attunement Talent?"
        self.left="Yes"
        self.right="No"
        #print(self.text)

    def left_state(self):
        return State6()

    def right_state(self):
        return State4()

class State11(State):
    def __init__(self):
        self.text="Do you wish to Channel a specific wind of magic?"
        self.left="Yes"
        self.right="No"
        #print(self.text)

    def left_state(self):
        return State12()

    def right_state(self):
        return State16()

class State12(State):
    def __init__(self):
        self.text="Use an Action to perform an Extended Channeling Test for a Wind of Magic."
        self.left=""
        self.right=""
        #print(self.text)

    def left_state(self):
        return State13()

    def right_state(self):
        return State13()

class State13(State):
    def __init__(self):
        self.text="Did the caster Pass the Channeling Test?"
        self.left="Yes"
        self.right="No"
        #print(self.text)

    def left_state(self):
        return State14()

    def right_state(self):
        return State9()

class State14(State):
    def __init__(self):
        self.text="Did the roll result in a Critical? (rolling doubles: 66, 55, 44)"
        self.left="Yes"
        self.right="No"
        #print(self.text)

    def left_state(self):
        return State10()

    def right_state(self):
        return State15()

class State15(State):
    def __init__(self):
        self.text="Record number of SL generated from Channeling Test"
        self.left=""
        self.right=""
        #print(self.text)

    def left_state(self):
        return State18()

    def right_state(self):
        return State18()

class State16(State):
    def __init__(self):
        self.text="Select a Spell to Cast"
        self.left=""
        self.right=""
        #print(self.text)

    def left_state(self):
        return State19()

    def right_state(self):
        return State19()

class State17(State):
    def __init__(self):
        self.text="Does the caster want to channel, cast, or stop channeling? Stop Channeling uses an Action to safely vent gathered power"
        self.left="Cast"
        self.right="Continue Channeling"
        #print(self.text)

    def left_state(self):
        return State16()

    def right_state(self):
        return State12()

class State18(State):
    def __init__(self):
        self.text="Did the spell caster get interrupted (by damage, surprise, or choice)?"
        self.left="Yes"
        self.right="No"
        #print(self.text)

    def left_state(self):
        return State21()

    def right_state(self):
        return State17()

class State19(State):
    def __init__(self):
        self.text="Is the Spell Memorized?"
        self.left="Yes"
        self.right="No"
        #print(self.text)

    def left_state(self):
        return State24()

    def right_state(self):
        return State23()

class State20(State):
    def __init__(self):
        self.text="Use an Action to safely vent gathered power"
        self.left=""
        self.right=""
        #print(self.text)

    def left_state(self):
        return State1()

    def right_state(self):
        return State1()

class State21(State):
    def __init__(self):
        self.text="Perform a Hard (-20) Cool Test."
        self.left="Pass"
        self.right="Fail"
        #print(self.text)

    def left_state(self):
        return State17()

    def right_state(self):
        return State22()

class State22(State):
    def __init__(self):
        self.text="Lose any generated SL, and roll on Minor Miscast Table."
        self.left=""
        self.right=""
        #print(self.text)

    def left_state(self):
        return State1()

    def right_state(self):
        return State1()

class State23(State):
    def __init__(self):
        self.text="Double the original CN of the spell"
        self.left=""
        self.right=""
        #print(self.text)

    def left_state(self):
        return State24()

    def right_state(self):
        return State24()

class State24(State):
    def __init__(self):
        self.text="Did you Channel?"
        self.left="Yes"
        self.right="No"
        #print(self.text)

    def left_state(self):
        return State27()

    def right_state(self):
        return State29()

class State25(State):
    def __init__(self):
        self.text="Roll on Minor Miscast Table."
        self.left=""
        self.right=""
        #print(self.text)

    def left_state(self):
        return State26()

    def right_state(self):
        return State26()

class State26(State):
    def __init__(self):
        self.text="Select a Critical Casting Effect: \n\n Critical Cast: if the spell causes Damage, it also inflicts a Critical Wound \n\n Total Power: The spell is cast even if the spellcaster did not adchieve enough SLs for the Casting Number. The spell can be dispelled as normal. \n\n Unstoppable Force: The Spell is cast if the spellcaster adchieved enough SLs and it cannot be dispelled."
        self.left=""
        self.right=""
        #print(self.text)

    def left_state(self):
        return State32()

    def right_state(self):
        return State32()

class State27(State):
    def __init__(self):
        self.text="Apply any gathered SL to reduce the CN of the spell to a minimum of 0 CN."
        self.left=""
        self.right=""
        #print(self.text)

    def left_state(self):
        return State29()

    def right_state(self):
        return State29()

class State28(State):
    def __init__(self):
        self.text="Does the caster posses Instinctive Diction Talent?"
        self.left="Yes"
        self.right="No"
        #print(self.text)

    def left_state(self):
        return State26()

    def right_state(self):
        return State25()

class State29(State):
    def __init__(self):
        self.text="Use an Action to perform an Language (Magick) Test to Cast"
        self.left=""
        self.right=""
        #print(self.text)

    def left_state(self):
        return State30()

    def right_state(self):
        return State30()

class State30(State):
    def __init__(self):
        self.text="Did the caster pass the Language (Magick) Test?"
        self.left="Yes"
        self.right="No"
        #print(self.text)

    def left_state(self):
        return State31()

    def right_state(self):
        return State34()

class State31(State):
    def __init__(self):
        self.text="Did the roll result in a Critical? (rolling doubles: 66, 55, 44)"
        self.left="Yes"
        self.right="No"
        #print(self.text)

    def left_state(self):
        return State28()

    def right_state(self):
        return State32()

class State32(State):
    def __init__(self):
        self.text="Is the SL greater than or equal to the CN of spell?"
        self.left="Yes"
        self.right="No"
        #print(self.text)

    def left_state(self):
        return State33()

    def right_state(self):
        return State35()

class State33(State):
    def __init__(self):
        self.text="Is there any excess SL beyond those required to cast?"
        self.left="Yes"
        self.right="No"
        #print(self.text)

    def left_state(self):
        return State36()

    def right_state(self):
        return State38()

class State34(State):
    def __init__(self):
        self.text="Did the roll result in a Fumble? (rolling doubles: 66, 55, 44)"
        self.left="Yes"
        self.right="No"
        #print(self.text)

    def left_state(self):
        return State37()

    def right_state(self):
        return State35()

class State35(State):
    def __init__(self):
        self.text="Spell Fails. If Channeling Test was used to lower CN, Roll on Minor Miscast Table"
        self.left=""
        self.right=""
        #print(self.text)

    def left_state(self):
        return State1()

    def right_state(self):
        return State1()

class State36(State):
    def __init__(self):
        self.text="Apply an effect from the Overccast Table"
        self.left=""
        self.right=""
        #print(self.text)

    def left_state(self):
        return State38()

    def right_state(self):
        return State38()

class State37(State):
    def __init__(self):
        self.text="Roll on Minor Miscast Table"
        self.left=""
        self.right=""
        #print(self.text)

    def left_state(self):
        return State35()

    def right_state(self):
        return State35()

class State38(State):
    def __init__(self):
        self.text="Spell is cast successfully"
        self.left=""
        self.right=""
        #print(self.text)

    def left_state(self):
        return State1()

    def right_state(self):
        return State1()




if __name__ == "__main__":
#    app = MainWindow()
#    app.mainloop()




    global right_button
    global left_button
    global currentState
    currentState = State1()




    # Create the main application window
    window = tk.Tk()
    window.geometry("300x250")

#    def handle_click(event):
    # As far as I know mouse klicks are handled after buttons
    # Bind the mouse click event to the handle_click function
#    window.bind("<Button-1>", handle_click)

    # Create a label widget
    mainText = tk.Label(window, text=currentState.text, wraplength=300)
    mainText.pack(anchor=tk.N)

    def reset_state():
        global currentState
        currentState = State1()
        left_button.config(text=currentState.left, command=lambda:update_and_set_state("left"))
        right_button.config(text=currentState.right, command=lambda:update_and_set_state("right"))
        mainText.config(text=currentState.text)

    def update_and_set_state(buttonSide):
        global currentState
        if (buttonSide == "left"):
            #print(currentState.left)
            currentState = currentState.left_state()
        if (buttonSide == "right"):
            #print(currentState.right)
            currentState = currentState.right_state()
        mainText.config(text=currentState.text)

        if (currentState.left != ""):
            left_button.config(text=currentState.left, command=lambda:update_and_set_state("left"))
        else:
            left_button.config(text="continue", command=lambda:update_and_set_state("left"))
        if (currentState.right != ""):
            right_button.config(text=currentState.right, command=lambda:update_and_set_state("right"))
        else:
            right_button.config(text="continue", command=lambda:update_and_set_state("right"))


    if (currentState.left != ""):
        left_button = tk.Button(window, text=currentState.left, command=lambda:update_and_set_state("left"))
        left_button.pack(ipadx=20, side=LEFT ,anchor=tk.E, expand=FALSE)


    if (currentState.right != ""):
        right_button = tk.Button(window, text=currentState.right, command=lambda:update_and_set_state("right"))
        right_button.pack(ipadx=20, side=RIGHT, anchor=tk.W, expand=FALSE)


    reset_button = tk.Button(window, text="Reset", command=lambda:reset_state())
    reset_button.pack(ipadx=20, side=BOTTOM, expand=False)



    # Run the Tkinter event loop
    window.mainloop()
