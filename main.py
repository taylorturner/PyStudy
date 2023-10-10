import urllib.request
import random
import tkinter as tk
from pygame import mixer


words = ['apple', 'orange', 'banana']

for word in words:
    url = 'https://ssl.gstatic.com/dictionary/static/sounds/oxford/{}--_gb_1.mp3'.format(word)
    urllib.request.urlretrieve(url, './{}.mp3'.format(word))

window = tk.Tk()
# window.geometry('600x200')
window.title('PyStudy')

random.shuffle(words)
words_idx = 0
words_len = len(words)

mixer.init()


def show_spelling():
    w_idx = globals()['words_idx']
    w_len = globals()['words_len']
    if w_idx < w_len:
        guess = sp_text.get(1.0, tk.END).rstrip()
        print('"' + guess + '" ' + '"' + words[w_idx] + '"')
        sp_text.delete(1.0, tk.END)
        sp_text.insert(1.0, words[w_idx] + ' ({}/{})'.format(w_idx + 1, w_len))
        if guess == words[w_idx]:
            sp_text.insert(1.0, 'CORRECT! \n')
        else:
            sp_text.insert(1.0, f'SORRY! You spelled "{guess}"...\n')
        globals()['words_idx'] += 1


def speak_word():
    w_idx = globals()['words_idx']
    w_len = globals()['words_len']
    if w_idx < w_len:
        f_name = words[w_idx] + '.mp3'
        mixer.music.load(f_name)
        mixer.music.play()


def clear_word():
    sp_text.delete(1.0, tk.END)


def reset_count():
    globals()['words_idx'] = 0
    random.shuffle(words)


sk_button = tk.Button(window, text='Say the word', command=speak_word)
sk_button.grid(row=0, column=4, columnspan=2)

sp_text = tk.Text(window, height=3, width=30, font=('Helvetica', 24))
sp_text.grid(row=0, column=0, rowspan=4, columnspan=3)

sp_button = tk.Button(window, text='Show correct spelling', command=show_spelling)
sp_button.grid(row=1, column=4, columnspan=2)

cl_button = tk.Button(window, text='Clear', command=clear_word)
cl_button.grid(row=2, column=4)

reset_button = tk.Button(window, text='Reset', command=reset_count)
reset_button.grid(row=2, column=5)

window.mainloop()
