
LIST_OF_VOWELS = [
    "a", "e", "i", "o", "u", "y"
]

LIST_OF_CONSONANTS = [
    "b", "c", "d", "f", "g", "h", "j", "k", "l", "m",
    "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"
]

SINGLE_SOUND_GROUPS = [
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

MULTIPLE_SOUND_GROUPS = [
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

THREE_VOWEL_GROUPS = [
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
    syllable_count = 0
    group = ''
    prev_group = ''
    i = 0

    is_single_sound = False
    is_multiple_sound = False
    is_three_vowel_sound = False
    for letter in word:
        if len(group) >= 1:
             #check which group it can be possible within
             prev_group = group

             temp_group = prev_group + word[i]


             if i+1 < len(word):
               if word[i] in LIST_OF_CONSONANTS:
                    group = ""
                    

             if temp_group in SINGLE_SOUND_GROUPS:
                  prev_group = temp_group
                  if i+1 < len(word):
                    if word[i] in LIST_OF_CONSONANTS:
                         group = ""
                        
                    else:
                        temp_group = prev_group + word[i+1]
                        is_single_sound = True
                        if temp_group in THREE_VOWEL_GROUPS:
                         is_three_vowel_sound = True
                         is_single_sound = False
             elif temp_group in THREE_VOWEL_GROUPS:
                  is_three_vowel_sound = True
             elif temp_group in MULTIPLE_SOUND_GROUPS:
                  is_single_sound = False

                  
                  
        if letter in LIST_OF_VOWELS:
            i+=1
            syllable_count+=1
            group += group.join(letter)
            
        else:
             i+=1
             continue
    if is_single_sound:
         syllable_count-=1
    elif is_three_vowel_sound:
         syllable_count-=2
    elif is_multiple_sound:
         syllable_count-=1


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
    print(f"{word} - {syllable_count}")
    

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
    
    # estimate_word_syllables('computer')
    for word in SYLLABLE_TEST_WORDS:
         estimate_word_syllables(word)
if __name__ == "__main__":
    main()