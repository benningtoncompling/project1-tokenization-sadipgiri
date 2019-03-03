#!/usr/bin/env python3
"""
    Python3 program to stemmize using Porter's algorithm with important helper functions
    Author: Sadip Giri (sadipgiri@bennington.edu)
    Date: 03/04/2019
"""

def is_consonant(word, index):
    '''
        normalize word to lowercase
        According to consonant definition: define is consonant function
            A \consonant\ in a word is a letter other than A, E, I, O or U, and other
            than Y preceded by a consonant. (The fact that the term `consonant' is
            defined to some extent in terms of itself does not make it ambiguous.) So in
            TOY the consonants are T and Y, and in SYZYGY they are S, Z and G. If a
            letter is not a consonant it is a \vowel\.
    '''
    word = word.lower()
    if word[index] in 'aeiou':
        return False
    if word[index] == 'y':
        if index == len(word) - 1:
            return True
        elif word[index+1] in 'aeiou':
            return True
        else:
            return False
    return True

def measure_word(word):
    '''
        normalize lowercase word in the form of c's and v's according to definition from the paper as follows:
        count vc's from the represented string -> defined as {m} the measure.
            
            A consonant will be denoted by c, a vowel by v. A list ccc... of length
            greater than 0 will be denoted by C, and a list vvv... of length greater
            than 0 will be denoted by V. Any word, or part of a word, therefore has one
            of the four forms:

                CVCV ... C
                CVCV ... V
                VCVC ... C
                VCVC ... V

            These may all be represented by the single form

                [C]VCVC ... [V]

            where the square brackets denote arbitrary presence of their contents.
            Using (VC){m} to denote VC repeated m times, this may again be written as

                [C](VC){m}[V].

            m will be called the \measure\ of any word or word part when represented in
            this form. The case m = 0 covers the null word. Here are some examples:

                m=0    TR,  EE,  TREE,  Y,  BY.
                m=1    TROUBLE,  OATS,  TREES,  IVY.
                m=2    TROUBLES,  PRIVATE,  OATEN,  ORRERY.
    '''
    word_in_cv = ''
    for i in range(len(word)):
        if is_consonant(word.lower(),i):
            word_in_cv += 'c'
        else:
            word_in_cv += 'v'
    return word_in_cv.count('vc')

if __name__ == '__main__':
    #print(is_consonant('TOYGY'.lower(), 4))
    a1 = ['TR',  'EE',  'TREE',  'Y',  'BY']
    a2 = ['TROUBLE',  'OATS',  'TREES',  'IVY']
    a3 = ['TROUBLES',  'PRIVATE',  'OATEN',  'ORRERY']
    for i in a3:
        print(measure_word(i))
    