import random

PARTS = ['юж', 'ра', 'мэ', 'ке', 'бэ', 'же']

def generate_phrase(n_words, type=None):
    words=[]
    for n in range(n_words):
        word=''
        for p in range(random.randrange(1, 10)):
            if type=='creepy':
                word+=chr(random.randint(97, 120))
                words.append(word)
            else:
                word+=random.choice(PARTS)
                words.append(word)

    return ' '.join(words)


print(generate_phrase(10, 'creepy'))