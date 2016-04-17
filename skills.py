"""Skills-dictionaries.

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""


def without_duplicates(words):
    """Given a list of words, return list with duplicates removed.

    For example::

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different::

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

        An empty list should return an empty list::

        >>> sorted(without_duplicates(
        ...     []))
        []

    The function should work for a list containing integers::

        >>> sorted(without_duplicates([111111, 2, 33333, 2]))
        [2, 33333, 111111]
    """
    # Sets do not contain duplicates
    return set(words)


def find_unique_common_items(items1, items2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items
    shared between the lists.

    **IMPORTANT**: you may not use `'if ___ in ___``
    or the method `list.index()`.

    This should find [1, 2]::

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists,
    don't show more than 1 or 2 once::

        >>> sorted(find_unique_common_items([3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    The elements should not be treated as duplicates if they are
    different data types::

        >>> sorted(find_unique_common_items(["2", "1", 2], [2, 1]))
        [2]
    """
    # Union of 2 sets returns commonality
    # Sets do not contain duplicates
    return set(items1) & set(items2)


def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """
    # Split string by spaces
    split_phrase = phrase.split(" ")

    # Create an empty dictionary
    word_dictionary = {}

    # Iterate over every word in the split_phrase list
    for word in split_phrase:
    # If the dictionary contains the word, increment the value count by 1
        if word in word_dictionary:
            word_dictionary[word] += 1
    # If the dictionary doesn't contain the word, add the word as a key
    # and set the value to 1
        else:
            word_dictionary[word] = 1
    
    return word_dictionary


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    boy         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """

    # Created separate lists of English and Pirate words
    # Added "man" and "matey" for English-to-Pirate translation for doctest to pass
    English = ["sir", "hotel", "student", "boy", "professor", "restaurant",
                "your", "excuse", "students", "are", "restroom", "my", "is",
                "man"]

    Pirate = ["matey", "fleabag inn", "swabbie", "matey", "foul blaggart", 
                "galley", "yer", "arr", "swabbies", "be", "head", "me", "be",
                "matey"]

    # Created a list of tuples (for key-value pairings) by zipping the 
    # English and Pirate lists 
    pirate_lookup = zip(English, Pirate)

    # Turned the list of tuples into a dictionary
    pirate_lookup = dict(pirate_lookup)

    # Separated the string by spaces
    split_phrase = phrase.split(" ")

    # Created an empty list to contain all of my translated words
    translated_words = []

    # Iterated over every word.  If word was in the dictionary, translate to the
    # value in the dictionary.  If word was not in the dictionary, word
    # remains unchanged.  
    for word in split_phrase:

        if word in pirate_lookup:
            new_word = pirate_lookup[word]
        else:
            new_word = word
        
        # Add every word to a list
        translated_words.append(new_word)
    
    # Join all the words from the list into a new string
    new_phrase = " ".join(translated_words)

    return new_phrase


def sort_by_word_length(words):
    """Given list of words, return list of ascending (len, [words]).

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- the length
    of the words for that word-length, and the list of words of
    that word length.

    For example::

        >>> sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]
    """

    # Initialize an empty dictionary
    word_dictionary = {}

    # Iterate over words list
    # If the key is in the dictionary, return the value and append the word
    # If the key is not in the dictionary, insert the key and set the value
    # to the default (word)
    for word in words:
        word_dictionary.setdefault(len(word), []).append(word)
    
    # Sort by dictionary's keys in ascending order
    sorted(word_dictionary)

    # items() returns a dictionary's list of key-values as tuple pairs
    word_tuple = word_dictionary.items()

    return word_tuple


def get_sum_zero_pairs(numbers):
    """Given list of numbers, return list of pair summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.

    For example::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself)::

        >>> sort_pairs( get_sum_zero_pairs([1, 3, -1, 1, 1, 0]) )
        [[-1, 1], [0, 0]]
    """
    
    # Created an empty set (no duplicates)
    numbers_set = set()

    # Created 2 for loops to establish placeholder for first number in pair
    # and second number in pair to sum
    for number in numbers:
        for number2 in numbers:
            # if the pair of numbers sum to 0, add to the first number to the set
            # using absolute value first to remove the scenario of a -1 and 1
            # both getting added to the set for example.
            if number + number2 == 0:
                numbers_set.add(abs(number))
    
    # Create an empty list to enable sorting
    pairs_list = []

    # For every number in the set, append his matching pair in a unique list
    for number in numbers_set:
        pairs_list.append([number, -number])
    
    # Sort in ascending order
    sorted(pairs_list)

    return pairs_list


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """
    
    word_dictionary = {}

    for name in names:
        word_dictionary.setdefault(name, [])

    for name in word_dictionary:
        for name2 in word_dictionary:
            if name2.startswith(name[-1]):
                word_dictionary[name].append(name2)
    
    # print word_dictionary

    # current_word = names[0]

    # new_string = current_word + " "

    # for name in word_dictionary:
    #     for i in word_dictionary[name]:
    #         if word_dictionary[name][i] in new_string:
    #             pass
    #         else:
    #             current_word = word_dictionary[name][i]
    #             new_string += current_word + " "

    # while True:
    #     if word_dictionary[name][0] in new_string:
    #         if word_dictionary[name][1] in new_string:
    #             break
    #         else:
    #             current_word = word_dictionary[name][1]
    #             new_string += current_word + " "
    #     else:
    #         current_word = word_dictionary[name][0]
    #         new_string += current_word + " "
    # return new_string

    stringing = True

    ordered_names = [names[0]]
    names.remove(names[0])

    while stringing == True:
        for name in names:
            if name.startswith(ordered_names[-1][-1]):
                ordered_names.append(name)
                names.remove(name)
                break
            elif name == names[-1]:
                stringing = False

    print ordered_names
    
#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
