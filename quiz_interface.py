from tkinter import *

HEIGHT = 800
WIDTH = 400

BACKGROUND_COLOR = "#2E4C6D"


class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()
        self.RED = "#C85C5C"
        self.GREEN = '#34BE82'
        self.config(bg=BACKGROUND_COLOR)
        self.time_keeper = 0
        self.new_player = True
        self.playing = False
        self.choice_selected = False
        self.one_point_per_round = 0
        self.color_change = 'white'
        self.counter = 0
        self.card = Canvas(bg=self.color_change, height=300, width=300)
        self.card.grid(row=2, column=2, columnspan=8, rowspan=8)

        self.exit_button = Button(text="Exit", command=self.click_exit_button)
        self.exit_button.grid(row=0, column=8, pady=10, padx=10)

        self.score_label = Label(text=f"Score: 0", font=('Ariel', 10, 'bold'), bg=BACKGROUND_COLOR,
                                 fg='white')
        self.score_label.grid(row=1, column=4, pady=10)

        self.question_label = Label(text='Question here', font=('Ariel', 11, 'bold'), bg=self.color_change,
                                    wraplength=250, justify='center')
        self.question_label.grid(row=4, column=3, columnspan=4, rowspan=5, sticky='', padx=(35, 0))

        self.correct_button = Button(text='True', width=10, height=5)
        self.correct_button.grid(row=10, column=3, padx=(45, 30))

        self.wrong_button = Button(text='False', width=10, height=5)
        self.wrong_button.grid(row=10, column=4, pady=50, padx=15)

    def click_exit_button(self):
        exit()


