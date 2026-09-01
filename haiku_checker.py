
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
    "create":2,
    "the":1
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
    "idea": 3,
    "an": 1,
"old": 1,
"silent": 2,
"pond": 1,
"frog": 1,
"jumps": 1,
"into": 2,
"splash": 1,
"silence": 2,
"again": 2,
}

def input_poetry(poem=''):

    if len(poem) == 0:
        lines = []

        for i in range(3):
            poem_line = input(f"Enter {i+1} Line Of The Poem: ")

            if len(poem_line) == 0:
                poem_line = input(f"Please Enter {i+1} Line Of The Poem, Do not leave it empty: ")

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

    for line in poem:
        for word in line.split():
            word = word.strip('.,!?;;:')
            words_list.append(word)
        words_list.append(f'END')
        
    return words_list

def estimate_word_syllables(word):
    word = word.lower()
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

def estimate_syllables(word_list):
    line_syllables = []
    syllables = 0

    for word in word_list:

         if word == "END":
              line_syllables.append(syllables)
              syllables = 0
              continue
         syllables += estimate_word_syllables(word)
    return line_syllables

def is_haiku(structure):
     if structure == [5,7,5]:
        return True
     else:
          return False


def main():
    print("Haiku Checker - CLI")

    poem = input_poetry()

    words_list = word_splitter(poem)

    result = estimate_syllables(words_list)

    if is_haiku(result):
        print("This poem follows the 5,7,5 structure!")
    else:
        print(f"This does not follow the 5,7,5 structure.\n Expected 5 got {result[0]} \n Expected 7 got {result[1]}\n Expected 5 got {result[2]}" )
if __name__ == "__main__":
    main()