def input_poetry(poem=''):

    if len(poem) == 0:
        lines = []

        for i in range(3):
            poem_line = input(f"Enter {i+1} Line Of The Poem: ")

            lines.append(poem_line)




        return lines
    else:
        lines = poem.split(",")
        return lines

def word_splitter(poem):
    words_list = []
    line_count = 0
    for line in poem:
        line_count+=1
        for word in line.split(' '):
            words_list.append(word)
        words_list.append(f'END')
        
    print(words_list)
    return words_list

def estimate_syllables(word_list):
    syllable_count_list = []
    syllable_count=0 
    
    for word in word_list:
        if word == "END":
            syllable_count_list.append(syllable_count)
            syllable_count=0 
            continue
        for letter in word:
            if letter in ['a','e','u','i','o']:
                syllable_count+=1
        if word.endswith('ou'):
            syllable_count-=1
        if 'uie' in word:
                syllable_count-=2
        if 'ei' in word:
                syllable_count-=1
        if word.endswith('ed'):
            syllable_count-=1
        if word.endswith('e') and len(word)>2:
            syllable_count-=1

    print(syllable_count_list)


def main():
    print("Haiku Checker - CLI")

    poem = input_poetry("You and me alone,Madness of world locked away,Peace and quiet reigns")

    words_list = word_splitter(poem)

    estimate_syllables(words_list)


if __name__ == "__main__":
    main()