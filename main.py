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

    for line in poem:
        for word in line.split(' '):
            words_list.append(word)
        
    print(words_list)
    return words_list

def main():
    print("Haiku Checker - CLI")

    poem = input_poetry("You and me alone, Madness of world locked away,Peace and quiet reigns")

    words_list = word_splitter(poem)


if __name__ == "__main__":
    main()