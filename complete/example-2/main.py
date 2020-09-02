"""
This module contains methods to count the number words that have other given words as prefix
"""

def countPrefixes(prefix_list,word_list):
    """Counts occurence of prefixes from a list of prefixes in a list of words

    A word w1 is prefix of another w2, if the first letters of w2 make up w1. This method
    Takes a list of prefixes and counts for each one the number of words that have w1 as prefix.
    '' is prefix of any word.

    Args:
        prefix_list (list): list of prefixes to search for in list of words
        word_list (list): list of words to search for prefixes

    Return:
        dict: dictionary containing prefixes as keys and the number of occurences as value

    >>> texto = 'Tinha tanta tia tantã Tinha tanta anta antiga '
    >>> texto += 'Tinha tanta anta que era tia Tinha tanta tia que era anta'
    >>> lista = texto.split()
    >>> countPrefixes(['tant', 't', ''],lista) == {'': 20, 'tant': 5, 't': 8}
    True
    """

    prefix_count_dict = {k:0 for k in prefix_list}

    for prefix in prefix_list:
        if prefix == '':
            prefix_count_dict[prefix] = len(word_list)
        else:
            for word in word_list:
                # if word[:len(prefix)] == prefix:
                if word.startswith(prefix):
                    prefix_count_dict[prefix] += 1

    return prefix_count_dict


if __name__=='__main__':
    import doctest
    doctest.testmod()