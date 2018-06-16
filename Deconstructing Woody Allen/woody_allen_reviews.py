import re
import urllib.request


def get_plain_text(title):
    try:
        req = urllib.request.Request('https://www.rottentomatoes.com/m/' + title)
        with urllib.request.urlopen(req) as response:
           plain_text = response.read().decode('utf-8')
           return plain_text
    except urllib.error.HTTPError:
        print('Page ' + title + ' does not exist')


def get_review(plain_text):
    regReview = re.compile('                <p class="comment clamp clamp-6">.*?            </div>', re.DOTALL)
    review = regReview.findall(plain_text)
    return review


def review_cleaner(review):
    regTag = re.compile('<.*?>', re.DOTALL)
    regLine = re.compile('\\\\n', re.DOTALL)
    regSlash = re.compile(r'\\', re.DOTALL)
    regList1 = re.compile("\['", re.DOTALL)
    regList2 = re.compile("'\]", re.DOTALL)
    tag_free_review = regTag.sub('', str(review))
    n_free_review = regLine.sub('', tag_free_review)
    review = regSlash.sub('', n_free_review)
    review = regList1.sub('', review)
    clear_review = regList2.sub('', review)
    return clear_review


def file_writer(clear_review, title):
    with open(title + '.txt', 'w', encoding = 'utf-8') as file:
        file.write(clear_review)
        print(title)


def main():
    list_of_titles = ['1032522_alice', 'annie_hall', 'another_woman', 'anything_else',
                      'bananas', 'blue_jasmine', 'broadway_danny_rose', 'bullets_over_broadway',
                      'cafe_society_2016', 'cassandras_dream', '1084868_celebrity', 'crimes_and_misdemeanors',
                      'deconstructing_harry', 'everything_you_always_wanted_to_know_about_sex_but_were_afraid_to_ask', 
                      'everyone_says_i_love_you', 'hannah_and_her_sisters', 'hollywood_ending', '1040798_husbands_and_wives',
                      'interiors', 'irrational_man', 'love_and_death', 'magic_in_the_moonlight', 'manhattan_murder_mystery',
                      'manhattan', 'match_point', 'melinda_and_melinda', 'midnight_in_paris', 'midsummer_nights_sex_comedy',
                      'mighty_aphrodite', 'scoop', 'september_1987', 'small_time_crooks', 'stardust_memories', 'sweet_and_lowdown',
                      'take_the_money_and_run', 'curse_of_the_jade_scorpion', 'to_rome_with_love', 'vicky_cristina_barcelona',
                      'whatever_works', 'wonder_wheel', 'you_will_meet_a_tall_dark_stranger', 'zelig']
    for title in list_of_titles:
        plain_text = get_plain_text(title)
        if plain_text != None:
            review = get_review(plain_text)
            clear_review = review_cleaner(review)
            file_writer(clear_review, title)


if __name__ == "__main__":
    main()
