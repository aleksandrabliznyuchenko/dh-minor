import os

def get_words(folder, freq):
    punct = '.,:;?!-_()[]{}«»""\''
    for file in os.listdir(folder):
        with open(os.path.join(folder, file), 'r', encoding = 'utf-8') as f:
            text = f.read()
            words = text.split()
            words = [word.strip(punct) for word in words if word != ' ']
            freq = make_dict(words, freq)
            for key in sorted(freq.keys()):
                if freq[key] >= 10:
                    print(key, freq[key])


def make_dict(words, freq):
    for word in words:
        if word.istitle() == True:
            if word in freq.keys():
                freq[word] += 1
            else:
                freq[word] = 1
    return freq


def main():
    folder = input('Введите название папки: ')
    freq = {}
    get_words(folder, freq)
    
 
if __name__ == "__main__":
    main()
