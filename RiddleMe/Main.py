from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window
import random

Window.size = (360, 640)


class RiddleMe(MDApp):
    question = []
    for i in range(0, 36):
        if i not in question:
            question.append(i)
    random.shuffle(question)

    skipped = 0
    correct = 0
    wrong = 0
    index_change = 0
    index = question[index_change]
    answered_questions = 0
    counter = 3
    sound1 = SoundLoader.load("Assets/background_music1.mp3")
    sound2 = SoundLoader.load("Assets/correct.mp3")
    sound3 = SoundLoader.load("Assets/wrong.mp3")
    sound4 = SoundLoader.load("Assets/fail.mp3")
    sound5 = SoundLoader.load("Assets/next.mp3")
    sound6 = SoundLoader.load("Assets/Click.wav")
    sound7 = SoundLoader.load("Assets/VictorySound.mp3")

    riddles = [
        {
            "question": "I speak without a mouth and\n hear without ears. \n I have no body,\n but I come alive with wind. \n What am I?",
            "answer": "echo"},
        {
            "question": "What has keys but can't open locks?",
            "answer": "piano"},
        {'question': "What has to be broken \n before you can use it?", 'answer': "egg"},
        {'question': "What has a head, a tail, \n is brown, \n and has no legs?", 'answer': "penny"},
        {'question': "What can travel around \nthe world while \nstaying in a corner?", 'answer': "stamp"},
        {
            'question': "I'm light as a feather,\n yet the strongest person \ncan't hold me for much longer \nthan a minute. What am I?",
            'answer': "breath"},
        {'question': "I'm not alive, \nbut I can grow. \nI don't have lungs, \nbut I need air. What am I?",
         'answer': "fire"},
        {'question': "The more you take, \nthe more you leave behind. \nWhat am I?", 'answer': "footsteps"},
        {'question': "I can be cracked, \nmade, told, \nand played. \nWhat am I?", 'answer': "joke"},
        {'question': "What goes up but \nnever comes down?", 'answer': "age"},
        {'question': "I'm tall when I'm young, \nand I'm short when I'm old. \nWhat am I?", 'answer': "candle"},
        {'question': "What gets wet \nwhile drying?", 'answer': "towel"},
        {'question': "What has a neck \nbut no head?", 'answer': "bottle"},
        {'question': "What comes once \nin a minute,\n twice in a moment, \nbut never in a thousand years?",
         'answer': "m"},
        {'question': "What belongs to you,\n but other people use \nit more than you?", 'answer': "name"},
        {'question': "What has a face \nand\n two hands but no \narms or legs?", 'answer': "clock"},
        {'question': "What can you hold \nwithout ever touching \nor using your hands?", 'answer': "breath"},
        {'question': "What begins with T,\n ends with T,\n and has T in it?", 'answer': "teapot"},
        {'question': "What runs all around \na backyard, \nyet never moves?", 'answer': "fence"},
        {'question': "What can fill a \nroom but takes \nup no space?", 'answer': "light"},
        {
            'question': "I have keys but no locks. \nI have space but no room. \nYou can enter, \nbut can't go outside. \nWhat am I?",
            'answer': "keyboard"},
        {'question': "What can you \ncatch but not throw?", 'answer': "cold"},
        {'question': "I have a head and a \ntail, but no body. \nWhat am I?", 'answer': "coin"},
        {'question': "What has a bottom\n at the top?", 'answer': "leg"},
        {'question': "I am full of holes,\n but I can still hold water. \nWhat am I?", 'answer': "sponge"},
        {"question": "What has eyes \nbut can't see?", "answer": "potato"},
        {"question": "What is always in \nfront of you but \ncan't be seen?", "answer": "future"},
        {"question": "What has a bed but never sleeps, \nand a mouth but never eats?", "answer": "river"},
        {"question": "What has one eye but can't see?", "answer": "needle"},
        {"question": "What has a mouth but can't eat?", "answer": "river"},
        {"question": "What has a heart \nthat doesn't beat?", "answer": "artichoke"},
        {"question": "What has four eyes \nbut can't see?", "answer": "mississippi"},
        {"question": "What has a thumb and four \nfingers but is not alive?", "answer": "glove"},
        {"question": "What has teeth but cannot bite?", "answer": "comb"},
        {"question": "What can run but never walks,\n has a mouth but never talks?", "answer": "river"},
        {"question": "What begins with an 'e'\n and only contains one letter?", "answer": "envelope"}
    ]

    def build(self):
        global sm
        sm = ScreenManager()
        self.icon = "Assets/Game icon.png"
        sm.add_widget(Builder.load_file("LogoScreen.kv"))
        sm.add_widget(Builder.load_file("HomeScreen.kv"))
        sm.add_widget(Builder.load_file("InstructionScreen.kv"))
        sm.add_widget(Builder.load_file("Question1Screen.kv"))
        sm.add_widget(Builder.load_file("SelectionScreen.kv"))
        sm.add_widget(Builder.load_file("FinalScreen.kv"))
        return sm

    def on_start(self):
        Clock.schedule_once(self.timer1, 5)
        Clock.schedule_interval(self.bg_music, 5)

    def begin_btn(self):
        random.shuffle(self.question)
        self.index = self.question[0]
        sm.get_screen("Question1").ids.riddle1.text = self.riddles[self.index]["question"]
        self.sound5.play()
        self.sound6.play()
        sm.current = "Question1"

    def replay(self):
        random.shuffle(self.question)
        self.index = self.question[0]
        sm.get_screen("Question1").ids.riddle1.text = self.riddles[self.index]["question"]
        self.sound5.play()
        self.sound6.play()
        sm.current = "Question1"
        self.skipped = 0
        self.correct = 0
        self.wrong = 0
        self.index_change = 0


    def bg_music(self, *args):
        self.sound1.play()

    def timer1(self, *args):
        Clock.schedule_once(self.timer2, 3)
        sm.current = "HomeScreen"

    def timer2(self, *args):
        sm.current = "Selection"

    def checker1(self):
        # question 1 checker and Next button
        self.sound6.play()
        if sm.get_screen("Question1").ids.answer1.text.lower() == self.riddles[self.index]["answer"]:
            self.answered_questions += 1
            self.correct += 1
            sm.get_screen("Question1").ids.questions_answered.text = str(self.answered_questions)
            sm.get_screen("Question1").ids.bg1.source = "Assets/Correct.png"
            sm.get_screen("Question1").ids.riddle1.text = self.riddles[self.index]["answer"].upper()
            self.sound2.play()
        elif sm.get_screen("Question1").ids.answer1.text.lower() != self.riddles[self.index]["answer"]:
            self.counter -= 1
            sm.get_screen("Question1").ids.answer1.text = ""
            sm.get_screen("Question1").ids.counter.text = f"{str(self.counter)} : left"
            self.sound3.play()
            if self.counter == 0:
                self.wrong += 1
                sm.get_screen("Question1").ids.riddle1.text = self.riddles[self.index]["answer"].upper()
                sm.get_screen("Question1").ids.bg1.source = "Assets/Wrong.png"
                self.sound4.play()

    def next_btn1(self):
        if self.index_change != 35:
            self.index_change += 1
        elif self.index_change == 35:
            self.final_page()

        self.index = self.question[self.index_change]
        self.counter = 3
        self.sound5.play()
        self.sound6.play()
        sm.get_screen("Question1").ids.answer1.text = ""
        sm.get_screen("Question1").ids.bg1.source = "Assets/QuestonBG.png"
        sm.get_screen("Question1").ids.riddle1.text = self.riddles[self.index]["question"]
        sm.get_screen("Question1").ids.counter.text = f"{str(self.counter)} : left"
        if (sm.get_screen("Question1").ids.bg1.source != "Assets/Correct.png" and
                sm.get_screen("Question1").ids.bg1.source != "Assets/Wrong.png"):
            self.skipped += 1

    def final_page(self):
        sm.get_screen("FinalScreen").ids.correct.text = f"correct: {str(self.correct)}"
        sm.get_screen("FinalScreen").ids.wrong.text = f"wrong: {str(self.wrong)}"
        sm.get_screen("FinalScreen").ids.skipped.text = f"skipped: {str(self.skipped-self.wrong)}"
        sm.current = "FinalScreen"
        self.sound7.play()

    def anim1(self, biscuit):
        anim = Animation(pos_hint={"center_y":  .5})
        anim.start(biscuit)

    def anim2(self, biscuit):
        anim = Animation(pos_hint={"center_y":  .8})
        anim.start(biscuit)

LabelBase.register(name="cartoon", fn_regular="Assets/cartoonist_kooky.ttf")

RiddleMe().run()
