
LIST_OF_VOWELS = [
    "a", "e", "i", "o", "u", 
]

LIST_OF_CONSONANTS = [
    "b", "c", "d", "f", "g", "h", "j", "k", "l", "m",
    "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"
]

SPECIAL_CASES = {
    "quiet": 2,
    "idea": 3,
    "rhythm": 2,
    "create":2
}

ONE_SYLLABLE_GROUPS = [
    "ai",
    "au",
    "aw",
    "ay",
    "ea",
    "ee",
    "ei",
    "eu",
    "ew",
    "oa",
    "oe",
    "oi",
    "oo",
    "ou",
    "ow",
    "oy"
]

TWO_SYLLABLE_GROUPS = [
    "ia",
    "ie",
    "io",
    "iu",
    "ua",
    "ue",
    "ui",
    "uo",
    "eo",
    "eu",
    "ea",
    "oe",
    "oa"
]

ONE_SYLLABLE_THREE_VOWEL_GROUPS = [
    "eau",
    "ieu",
    "iou",
    "uai",
    "uei",
    "uie"
]


ENDING_WITH_E = [
    "e"
]

ENDING_WITH_ED = [
    "ed"
]

ENDING_WITH_ES = [
    "es"
]

ENDING_WITH_LE = [
    "le"
]

ENDING_WITH_LES = [
    "les"
]

ED_ADDS_SYLLABLE = [
    "wanted",
    "needed",
    "wasted",
    "painted",
    "printed",
    "started",
    "ended",
    "waited",
    "decided",
    "created",
    "visited",
    "accepted"
]

ED_NO_EXTRA_SYLLABLE = [
    "walked",
    "talked",
    "jumped",
    "helped",
    "washed",
    "kissed",
    "played",
    "stayed",
    "called",
    "opened",
    "closed",
    "loved"
]

Y_AS_VOWEL = [
    "my",
    "cry",
    "fly",
    "sky",
    "happy",
    "pretty",
    "funny",
    "family",
    "rhythm",
    "mystery"
]

Y_AS_CONSONANT = [
    "yes",
    "you",
    "yellow",
    "yard",
    "young",
    "year",
    "yesterday"
]

LE_NO_EXTRA_SYLLABLE = [
    "file",
    "while",
    "mile",
    "smile",
    "style",
    "whole",
    "role"
]

SYLLABLE_TEST_WORDS = {
    "cat": 1,
    "dog": 1,
    "book": 1,
    "beautiful": 3,
    "computer": 3,
    "banana": 3,
    "my": 1,
    "happy": 2,
    "rhythm": 2,
    "make": 1,
    "alone": 2,
    "little": 2,
    "walked": 1,
    "wanted": 2,
    "played": 1,
    "quiet": 2,
    "cloud": 1,
    "piano": 3,
    "lion": 2,
    "create": 2,
    "idea": 3
}

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


def scan_vowels(word):
    groups = []
    current = ""

    for letter in word:
        if letter in LIST_OF_VOWELS:
            current += letter
        else:
            if current != "":
                groups.append(current)
                current = ""

    if current != "":
        groups.append(current)

    return groups

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

def estimate_word_syllables(word):

    if word in SPECIAL_CASES:
        return SPECIAL_CASES[word]

    vowel_groups = scan_vowels(word)

    syllables = 0

    for group in vowel_groups:

        if group in ONE_SYLLABLE_GROUPS:
            syllables += 1

        elif group in TWO_SYLLABLE_GROUPS:
            syllables += 2

        elif group in ONE_SYLLABLE_THREE_VOWEL_GROUPS:
            syllables += 1

        else:
            syllables += 1

    if word.endswith('le'):
        is_con = False
        for c in LIST_OF_CONSONANTS:
              m=''
              m += c + 'le'

              if word.endswith(m):
                   is_con = True
                   syllables+=1
                   break
              else:
                   continue
        if is_con:
            syllables-=1
    elif word.endswith("ed") and word not in ED_ADDS_SYLLABLE:
        syllables -= 1

    elif word.endswith("e") and len(word) > 2:
        syllables -= 1
    elif word in Y_AS_VOWEL:
         syllables+=1
    elif word in Y_AS_CONSONANT:
         syllables-=1

    return syllables        

# def estimate_word_syllables_old(word):
    syllable_count = 0
    group = []
    str_group =''
    prev_group = ''
    i = 0
    for letter in word:
        

        if letter in LIST_OF_VOWELS:
            str_group += letter
        else:
            if str_group != "":
                group.append(str_group)
                str_group = ""

        prev_group = str_group
        temp_group = prev_group + word[i]
        print(prev_group+" "+temp_group)

                

        if temp_group in ONE_SYLLABLE_GROUPS:
            prev_group = temp_group
            if i+1 < len(word):

                temp_group = prev_group + word[i+1]

            if temp_group in ONE_SYLLABLE_THREE_VOWEL_GROUPS:
                if word[i] in LIST_OF_CONSONANTS:
                    group.append(prev_group)
                                    
                    str_group = ""
                                    
                

            if i+1 < len(word):
                if word[i] in LIST_OF_CONSONANTS:
                    group.append(prev_group)
                
                    str_group = ""
                    
        elif prev_group in ONE_SYLLABLE_THREE_VOWEL_GROUPS:
            if i+1 < len(word):
                
                if word[i] in LIST_OF_CONSONANTS:
                    group.append(str_group)
        elif prev_group in TWO_SYLLABLE_GROUPS:
            print("multi")
            if i+1 < len(word):
                print(str_group)
                print(temp_group)
                print(prev_group)

                if word[i] in LIST_OF_CONSONANTS:
                        group.append(str_group)
                        str_group = ""
                    


        print(group)
            

            
            
        if letter in LIST_OF_VOWELS:
            i+=1
            syllable_count+=1
            str_group +=  str_group.join(letter)
            
            
        else:
             i+=1
    if str_group in LIST_OF_VOWELS:
         group.append(str_group)
    syllable_count = len(group)
    if 'y' in word:
         if word in Y_AS_VOWEL:
              syllable_count+=0
         if word in Y_AS_CONSONANT:
              syllable_count-=1


    if word.endswith('ed'):
         if word in ED_ADDS_SYLLABLE:
              syllable_count+=0
         if word in ED_NO_EXTRA_SYLLABLE:
            syllable_count-=1   
    if word.endswith('le'):
        if word in LE_NO_EXTRA_SYLLABLE:
             syllable_count-=1
        is_con_end = False
        for c in LIST_OF_CONSONANTS:
                ending = c + 'le'
                print(ending)
                
                if word.endswith(ending):
                    print("y")
                    syllable_count+=1
                    is_con_end = True
                    break
                else:
                    continue
        if is_con_end == False:
                syllable_count-=1
                
        

        syllable_count-=1
    if word.endswith('e') and len(word)>2:
        syllable_count-=1
    print(f"{word} - {syllable_count}")
    print(group)
    

# def estimate_syllables(word_list):
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

        if word.endswith('oo'):
            syllable_count-=1
        if 'uie' in word:
                syllable_count-=2
        if 'eau' in word:
                syllable_count-=2
        if word.endswith('y'):
                syllable_count+=1
        if 'ei' in word:
                syllable_count-=1
        if 'ou' in word:
             syllable_count-=1
        if word.endswith('ed'):
            syllable_count-=1
        if word.endswith('le'):
            is_con_end = False
            for c in LIST_OF_CONSONANTS:
                 ending = c.join('le')
                 if word.endswith(ending):
                      syllable_count+=1
                      is_con_end = True
                      break
                 else:
                    continue
            if is_con_end == False:
                 syllable_count-=1
                 
            

            syllable_count-=1
        if word.endswith('e') and len(word)>2:
            syllable_count-=1

    print(syllable_count_list)


def main():
    print("Haiku Checker - CLI")

    # poem = input_poetry("You and me alone,Madness of world locked away,Peace and quiet reigns")

    # words_list = word_splitter(poem)

    # estimate_syllables(words_list)
    
    # estimate_word_syllables('piano')
    for word, expected in SYLLABLE_TEST_WORDS.items():
        result = estimate_word_syllables(word)
        print(f"{word}: expected={expected}, got={result}")
if __name__ == "__main__":
    main()