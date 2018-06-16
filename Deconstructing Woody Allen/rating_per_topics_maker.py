import json
import os


def topic_definer(folder, topics, list_of_topics):
    freq = {}
    for file in os.listdir(folder):
        title = file[:-9]
        with open(os.path.join(folder, file), 'r', encoding = 'utf-8') as f:
            text = f.read()
            words = text.split()
            for word in words:
                for topic in list_of_topics:
                    if word in topics[topic]:
                        line = title + ' : ' + topic + ' --> ' + word + ' '
                        with open('topics_words.txt', 'a', encoding = 'utf-8') as f3:
                            f3.write(line)
                        if title in freq.keys():
                            if topic in freq.keys():
                                freq[title][topic] += 1
                            else:
                                freq[title][topic] = 1
                        else:
                            freq = {title : {topic : 1}}
                            
            
            with open('json_topics_words.json', 'a', encoding = 'utf-8') as f2:
                json.dump(freq, f2, ensure_ascii = False)
                    
            

def main():
    folder = 'mallet'
    list_of_topics = ['god_work_love', 'writing_action', 'friends', 'affair', 'lifestyle']
    topics = {
        'god_work_love' :
        {
            'good', 'make', 'love', 'time', 'great', 'back', 'life', 'god', 'thing', 'lot',
            'thought', 'work', 'hey', 'give', 'wanna', 'call', 'told', 'book', 'man', 'put'
            },
        'writing_action' :
        {
            'wait', 'rain', 'mind', 'writing', 'pretty', 'care', 'marry', 'script', 'kind', 'london', 'telling',
            'love', 'itwas', 'bank', 'carol', 'finally', 'fella', 'napoleon', 'played', 'beautiful'
            },
        'friends' :
        {
            'opera', 'place', "l'll", "l'm", 'part', 'face', 'future', 'friends', 'mine', 'honour', 'dia',
            'c.w', 'guitar', 'anymore', 'willie', 'idea', 'foundation', 'figure', 'wheat', 'killer'
            },
        'affair' :
        {
            'darling', 'understand', 'lunch', 'wine', 'doctor', 'man', 'melody', 'famous', 'past', 'affair',
            'house', 'played', 'park', 'making', 'yeager', 'milos', 'blind', 'mom', 'boyfriend'
            },
        'lifestyle' :
        {
            'feel', 'chinese', 'day', 'matter', 'story', 'picture', 'open', 'card', 'white', 'doctor',
            'ago', 'wanna', 'good', 'hell', 'dough', 'prison', 'dub', 'restaurant', 'fantastic', 'paper'
            }
        }
    topic_definer(folder, topics, list_of_topics)


if __name__ == "__main__":
    main()
