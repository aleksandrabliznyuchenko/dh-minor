import os

folder = input('Введите название папки с файлами, в которых вы хотите посчитать частотные слова: ')
freq = {}

with open('en.txt', 'r', encoding = 'utf-8') as f1:
    data = f1.read()
    stopwords = data.split()

        
for file in os.listdir(folder):
    line = '--- ' + file[:-4] + ' ---'
    punct = '.,:;?!-_()[]{}«»""\''
    with open(os.path.join(folder, file), 'r', encoding = 'utf-8') as f2:
        text = f2.read()
        words = text.split()
        words = [word.strip(punct) for word in words if word != ' ']
        print(line)
        for word in words:
            if word not in stopwords:
                if word in freq.keys():
                    freq[word] += 1
                else:
                    freq[word] = 1

                
    for key in sorted(freq.keys()):
        print(key, freq[key])
    freq.clear()
