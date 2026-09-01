# Haiku Checker

A small Python CLI program that checks whether a poem follows the traditional 5-7-5 syllable structure of a haiku.

I made this as a small exercise in Python and basic rule-based NLP. Instead of using an existing NLP library to count syllables, the program tries to estimate syllables using vowel groups and a collection of rules for common English spelling patterns and exceptions.

## What it does

The program:

* Takes a three-line poem as input
* Splits each line into words
* Estimates the number of syllables in each word
* Adds the syllables together for each line
* Checks whether the final structure is `5-7-5`
* Tells you the syllable count if the poem doesn't match

For example:

```text
An old silent pond
A frog jumps into the pond
Splash! Silence again
```

The program calculates:

```text
[5, 7, 5]
```

and reports that the poem follows the 5-7-5 structure.

## How syllable counting works

The main part of the project is the syllable estimator.

It starts by looking for groups of consecutive vowels in a word. These groups are then compared against lists of common vowel combinations.

For example, the program has rules for combinations such as:

```text
ai, au, aw, ay
ea, ee, ei, eu, ew
oa, oe, oi, oo, ou, ow, oy
```

There are also rules for combinations that can represent two syllables, as well as some three-vowel combinations.

After the initial vowel-group count, the program applies some additional rules.

### Special cases

Some words don't behave particularly well with simple vowel counting, so they are explicitly defined:

```python
SPECIAL_CASES = {
    "quiet": 2,
    "idea": 3,
    "rhythm": 2,
    "create": 2,
    "the": 1
}
```

### Silent `e`

The program handles words ending in `e` by removing a syllable in cases where the final `e` is likely silent.

For example:

```text
make → 1
alone → 2
```

### `-ed` endings

Words ending in `-ed` are another problem because the ending doesn't always add a syllable.

The program therefore has lists for words where `-ed` adds an extra syllable and words where it doesn't.

For example:

```text
wanted → 2
walked → 1
```

### `-le` endings

The program also has some handling for words ending in `-le`, since words such as `little` can otherwise be incorrectly counted.

### The letter `y`

The letter `y` can act as either a vowel or a consonant depending on the word.

The program has separate lists for some common examples:

```text
my
happy
funny
rhythm
```

and:

```text
yes
you
yellow
young
```

## Program structure

The program is split into several functions, each handling a different part of the process.

```text
input_poetry()
       |
       v
word_splitter()
       |
       v
estimate_word_syllables()
       |
       v
estimate_syllables()
       |
       v
is_haiku()
```

### `input_poetry()`

Gets the three lines of the poem from the user.

It also checks for empty input and asks the user to enter the line again.

### `word_splitter()`

Splits the poem into individual words and removes some common punctuation.

An `END` marker is added after every line so that the program knows where one line finishes.

### `scan_vowels()`

Finds consecutive vowel groups inside a word.

These groups are later used by the syllable estimation function.

### `estimate_word_syllables()`

Estimates the number of syllables in a single word.

This is where most of the rules for special cases, vowel groups, `-ed`, `-le`, silent `e`, and `y` are applied.

### `estimate_syllables()`

Runs the syllable estimator over the entire poem and keeps track of the syllables belonging to each line.

For example:

```python
[5, 7, 5]
```

### `is_haiku()`

Checks whether the calculated structure is exactly:

```python
[5, 7, 5]
```

If it is, the poem passes the check.

## Running it

You only need Python 3.

Run the program with:

```bash
python haiku_checker.py
```

You'll then be asked to enter the three lines:

```text
Haiku Checker - CLI

Enter 1 Line Of The Poem:
Enter 2 Line Of The Poem:
Enter 3 Line Of The Poem:
```

If the poem matches the structure:

```text
This poem follows the 5,7,5 structure!
```

Otherwise, the program shows the expected and calculated syllable counts.

## Testing

I also included a collection of words with known syllable counts:

```python
SYLLABLE_TEST_WORDS = {
    "cat": 1,
    "dog": 1,
    "book": 1,
    "beautiful": 3,
    "computer": 3,
    "banana": 3,
    "happy": 2,
    "rhythm": 2,
    "alone": 2,
    "little": 2,
    "wanted": 2,
    "quiet": 2,
    "piano": 3,
    "lion": 2,
    "create": 2,
    "idea": 3,
}
```

These were useful for checking whether the syllable estimation rules were behaving as expected.

## Limitations

This isn't a perfect English syllable counter.

The main reason is that English pronunciation doesn't always follow consistent spelling rules. Counting vowel groups works for many words, but there are plenty of exceptions.

I've handled some of these exceptions manually with special-case lists and additional rules, but there will still be words that the program counts incorrectly.

Because of this, the result should be treated as an estimate rather than a guaranteed pronunciation-based syllable count.

The program also only checks the 5-7-5 structure. It doesn't try to determine whether a poem follows other conventions or interpretations of haiku.

## Possible improvements

Some things I could add in the future:

* More special-case words
* Proper unit tests
* Better punctuation handling
* Reading poems from files
* A more complete pronunciation dictionary
* Showing the syllable count for every individual word
* A better command-line interface
* Support for checking multiple poems at once

For example, instead of only showing:

```text
[5, 7, 5]
```

the program could eventually show:

```text
An      → 1
old     → 1
silent  → 2
pond    → 1

Total: 5
```

## What I learned

The main thing I wanted to explore with this project was how difficult seemingly simple language-processing problems can become.

At first, counting syllables seems like it should just involve counting vowels. Once I started adding actual English words, though, things like silent letters, vowel combinations, `-ed`, `-le`, and `y` made it considerably more complicated.

The project ended up being a useful introduction to basic rule-based NLP and showed me why more sophisticated NLP systems often rely on dictionaries, linguistic rules, or trained models instead of simply looking at the spelling of a word.
