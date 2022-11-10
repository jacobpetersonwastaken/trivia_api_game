from quiz_interface import Window
from requests import *
import html
answer = None
new_player = True
score = 0
window = Window()
score_label = window.score_label
question_label = window.question_label
backdrop = window.card


def change_color(color):
    if color == 'green':
        backdrop['bg'] = window.GREEN
        question_label['bg'] = window.GREEN
    if color == 'white':
        backdrop['bg'] = 'white'
        question_label['bg'] = 'white'
    if color == 'red':
        backdrop['bg'] = window.RED
        question_label['bg'] = window.RED


def get_data():
    global answer, score
    change_color('white')
    parameters = {
        'amount': 10,
        'type': 'boolean'
    }
    api_link = 'https://opentdb.com/api.php'
    r = get(api_link, params=parameters)
    question = str(r.json()['results'][0]['question'])
    question = html.unescape(question)
    answer = r.json()['results'][0]['correct_answer']
    question_label['text'] = question
    window.correct_button['state'] = 'normal'
    window.wrong_button['state'] = 'normal'
    return answer


def next_question(user_input):
    global answer, score
    window.correct_button['state'] = 'disabled'
    window.wrong_button['state'] = 'disabled'
    if user_input == answer:
        change_color('green')
        score += 1
        score_label['text'] = f'Score: {score}'

    else:
        change_color('red')


def correct():
    next_question('True')


def wrong():
    next_question('False')


def start_game():
    global new_player, score
    if new_player:
        score = 0
        score_label['text'] = f'Score: {score}'
        new_player = False
        get_data()


true_button = window.correct_button['command'] = correct
false_button = window.wrong_button['command'] = wrong
true_label = window.correct_button
false_label = window.wrong_button

start_game()

window.mainloop()
