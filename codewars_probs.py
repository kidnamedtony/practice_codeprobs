"""
7-kyu:
In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

E.g.
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
"""
# Solution I was working on before deciding I could do it in one line:
def filter_list(l):
    returning_lst = []
    for item in l:
        if type(item) == int:
            returning_lst.append(item)
    return returning_lst

# My solution:
def filter_list(l):
    return list(x for x in l if type(x) == int)


# Another user submitted this, and I thought it was a neat use of isinstance:
def filter_list(l):
  'return a new list with the strings filtered out'
  return [i for i in l if not isinstance(i, str)]



"""
7-kyu:
Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.

For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

[10, 343445353, 3453445, 3453545353453] should return 3453455.
"""
# My solution:
def sum_two_smallest_numbers(numbers):
    return sorted(numbers)[0] + sorted(numbers)[1]

# The Internet's solution:
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])


"""
7-kyu:
Implement a method that accepts 3 integer values a, b, c. The method should return true if a triangle can be built with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).
"""

# Solution that Mike helped me get:
def is_triangle(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)

# I was doing this before:
def is_triangle(a, b, c):
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return False
    else:
        return True

"""
6-kyu:
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice
"""

# My solution that satisfies all but 2 edge cases:
def duplicate_count(text):
    text = text.lower()
    char_dict = dict()
    for char in text:
        count = 0
        for _ in text:
            if _ == char:
                count += 1
        char_dict[char] = count
    count_lst = []
    for k,v in char_dict.items():
        if v > 1:
            count_lst.append(v)
    return len(count_lst)

# Super clever answers from the internet:
def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])

def duplicate_count(text):
    return sum(1 for c, n in Counter(text.lower()).iteritems() if n > 1)

# But, these seem to be a pretty good, straightforward answers too:
def duplicate_count(text):
    seen = set()
    dupes = set()
    for char in text:
        char = char.lower()
        if char in seen:
            dupes.add(char)
        seen.add(char)
    return len(dupes)

def duplicate_count(text):
    count = 0
    for c in set(text.lower()):
        if text.lower().count(c) > 1:
            count += 1
    return count



"""
6-kyu:
Polycarpus works as a DJ in the best Berland nightclub, and he often uses dubstep music in his performance. Recently, he has decided to take a couple of old songs and make dubstep remixes from them.

Let's assume that a song consists of some number of words (that don't contain WUB). To make the dubstep remix of this song, Polycarpus inserts a certain number of words "WUB" before the first word of the song (the number may be zero), after the last word (the number may be zero), and between words (at least one between any pair of neighbouring words), and then the boy glues together all the words, including "WUB", in one string and plays the song at the club.

For example, a song with words "I AM X" can transform into a dubstep remix as "WUBWUBIWUBAMWUBWUBX" and cannot transform into "WUBWUBIAMWUBX".

Recently, Jonny has heard Polycarpus's new dubstep track, but since he isn't into modern music, he decided to find out what was the initial song that Polycarpus remixed. Help Jonny restore the original song.

Input
The input consists of a single non-empty string, consisting only of uppercase English letters, the string's length doesn't exceed 200 characters

Output
Return the words of the initial song that Polycarpus used to make a dubsteb remix. Separate the words with a space.

E.g.
song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")
  # =>  WE ARE THE CHAMPIONS MY FRIEND
"""
# My solution:
def song_decoder(song):
    new_song = song
    if "WUB" in song:
        new_song = song.replace("WUB", " ")
    new_song = new_song.split()
    new_song = " ".join(new_song)
    return new_song.strip()

# The Internet's solutions:
def song_decoder(song):
    return " ".join(song.replace('WUB', ' ').split())

# RegEx solution:
def song_decoder(song):
    import re
    return re.sub('(WUB)+', ' ', song).strip()

"""
7-kyu:
The museum of incredible dull things
The museum of incredible dull things wants to get rid of some exhibitions. Miriam, the interior architect, comes up with a plan to remove the most boring exhibitions. She gives them a rating, and then removes the one with the lowest rating.

However, just as she finished rating all exhibitions, she's off to an important fair, so she asks you to write a program that tells her the ratings of the items after one removed the lowest one. Fair enough.

Task
Given an array of integers, remove the smallest value. Do not mutate the original array/list. If there are multiple elements with the same value, remove the one with a lower index. If you get an empty array/list, return an empty array/list.

Don't change the order of the elements that are left.

Examples
remove_smallest([1,2,3,4,5]) = [2,3,4,5]
remove_smallest([5,3,2,1,4]) = [5,3,2,4]
remove_smallest([2,2,1,2,1]) = [2,2,2,1]
"""
# My solution:
def remove_smallest(numbers):
    if numbers == []:
        return numbers
    smallest = sorted(numbers)[0]
    new_numbers = numbers.copy()
    new_numbers.remove(smallest)
    return new_numbers

# The Internet's solution:
def remove_smallest(numbers):
    a = numbers[:]
    if a:
        a.remove(min(a))
    return a

def remove_smallest(n):
    return n[:n.index(min(n))] + n[n.index(min(n)) + 1:] if n != [] else []



"""
6-kyu:
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:
solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']
"""
# My solution:
def solution(s):
    if len(s) % 2 != 0:
        s = s + "_"
    pairs = []
    while (len(s) > 0):
        pairs.append(s[:2])
        s = s[2:]
    return pairs

# The Internet's solutions:
def solution(s):
    result = []
    if len(s) % 2:
        s += '_'
    for i in range(0, len(s), 2):
        result.append(s[i:i+2])
    return result

def solution(s):
    return [(s + "_")[i:i + 2] for i in range(0, len(s), 2)]

# RegEx solution:
import re

def solution(s):
    return re.findall(".{2}", s + "_")



"""
6-kyu:
Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''
"""
# My (very long) solution:
def namelist(names):
    name_str = ""
    # For edge case of only 1 name in the names list:
    if len(names) == 1:
        return names[0]["name"]
    # For the edge case of no names in the names list:
    if len(names) == 0:
        return ""
    # Assuming we've gotten this far, we're going to need to keep track of the last name in the list:
    last_name = names[-1]["name"]
    for n in names:
        for k, v in n.items():
            temp_str = v
            if v == last_name:
                name_str = name_str[:-2]
                name_str += f" & {v}"
                return name_str
            else:
                name_str += f"{v}, "
    return name_str

# The Internet's solutions:
def namelist(names):
    if len(names) > 1:
        return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]),
                                names[-1]['name'])
    elif names:
        return names[0]['name']
    else:
        return ''

def namelist(names):
  return ", ".join([name["name"] for name in names])[::-1].replace(",", "& ",1)[::-1]

def namelist(names):
    if len(names)==0: return ''
    if len(names)==1: return names[0]['name']
    return ', '.join([n['name'] for n in names[:-1]]) + ' & ' + names[-1]['name']



"""
6-kyu:
Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

! Keep in mind that your task is to help Bob solve a `real IQ test`, which means indexes of the elements start from 1 (not 0)

##Examples :

iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even

iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd
"""
# My (very long) solutions:
def iq_test(numbers):
    numbers_lst = list(numbers.split())
    even_count = 0
    odd_count = 0
    for num in numbers_lst:
        # Edge case of 0, which is an even number:
        if int(num) == 0:
            even_count += 1
            even_idx = numbers_lst.index(num)+1
        if int(num) % 2 == 0:
            even_count += 1
            even_idx = numbers_lst.index(num)+1
        else:
            odd_count += 1
            odd_idx = numbers_lst.index(num)+1
    if even_count < odd_count:
        return even_idx
    else:
        return odd_idx

# The Internet's solutions:
def iq_test(numbers):
    e = [int(i) % 2 == 0 for i in numbers.split()]

    return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1

def iq_test(n):
    n = [int(i)%2 for i in n.split()]
    if n.count(0)>1:
        return n.index(1)+1
    else:
        return n.index(0)+1


"""
6-kyu:

Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.

E.g.
test.assert_equals(high('man i need a taxi up to ubud'), 'taxi')
test.assert_equals(high('what time are we climbing up the volcano'), 'volcano')
test.assert_equals(high('take me to semynak'), 'semynak')
"""
# My (very long) solution:
import string
def high(x):
    alpha_score = {v:k+1 for k,v in dict(enumerate(string.ascii_lowercase)).items()}
    x_lst = x.split()
    highest_scoring = (0, "")
    for word in x_lst:
        score = 0
        for lttr in word:
            score += alpha_score[lttr]
            final_word_score = (score, word)
        if final_word_score[0] > highest_scoring[0]:
            highest_scoring = final_word_score
    return highest_scoring[1]

# The Internet's solutions:
def high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))

def high(x):
    words=x.split(' ')
    list = []
    for i in words:
        scores = [sum([ord(char) - 96 for char in i])]
        list.append(scores)
    return words[list.index(max(list))]



"""
6-kyu:
UNIQUE IN ORDER

Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
"""
# My solution:
def unique_in_order(iterable):
    if len(iterable) == 0:
        return []
    itr_lst = list(iterable)
    unique_order = [itr_lst[0]]
    for lttr in itr_lst:
        if lttr != unique_order[-1]:
            unique_order.append(lttr)
    return unique_order

# The Internet's solutions:
def unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result

from itertools import groupby
def unique_in_order(iterable):
    return [k for (k, _) in groupby(iterable)]

def unique_in_order(iterable):
    res = []
    for item in iterable:
        if len(res) == 0 or item != res[-1]:
            res.append(item)
    return res



"""
5-kyu:
DIRECTIONS REDUCTION

Once upon a time, on a way through the old wild west,…
… a man was given directions to go from one point to another. The directions were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too. Going to one direction and coming back the opposite direction is a needless effort. Since this is the wild west, with dreadfull weather and not much water, it's important to save yourself some energy, otherwise you might die of thirst!

How I crossed the desert the smart way.
The directions given to the man are, for example, the following (depending on the language):

["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"].
or

{ "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST" };
or

[North, South, South, East, West, North, West]
You can immediatly see that going "NORTH" and then "SOUTH" is not reasonable, better stay to the same place! So the task is to give to the man a simplified version of the plan. A better plan in this case is simply:

["WEST"]
or

{ "WEST" }
or

[West]
Other examples:
In ["NORTH", "SOUTH", "EAST", "WEST"], the direction "NORTH" + "SOUTH" is going north and coming back right away. What a waste of time! Better to do nothing.

The path becomes ["EAST", "WEST"], now "EAST" and "WEST" annihilate each other, therefore, the final result is [] (nil in Clojure).

In ["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"], "NORTH" and "SOUTH" are not directly opposite but they become directly opposite after the reduction of "EAST" and "WEST" so the whole path is reducible to ["WEST", "WEST"].

Task
Write a function dirReduc which will take an array of strings and returns an array of strings with the needless directions removed (W<->E or S<->N side by side).

The Haskell version takes a list of directions with data Direction = North | East | West | South.
The Clojure version returns nil when the path is reduced to nothing.
The Rust version takes a slice of enum Direction {NORTH, SOUTH, EAST, WEST}.
See more examples in "Sample Tests:"
Notes
Not all paths can be made simpler. The path ["NORTH", "WEST", "SOUTH", "EAST"] is not reducible. "NORTH" and "WEST", "WEST" and "SOUTH", "SOUTH" and "EAST" are not directly opposite of each other and can't become such. Hence the result path is itself : ["NORTH", "WEST", "SOUTH", "EAST"].
if you want to translate, please ask before translating.

"""
# My (very overwrought and ugly) solution:
def dirReduc(arr):
    print(arr)
    if len(arr) == 0:
        return []
    arr_copy = arr.copy()
    location = []
    for _ in range(len(arr_copy)):
        if len(location) == 0:
            if len(arr_copy) == 0:
                return location
            location.append(arr_copy.pop(0))
        elif len(arr_copy) == 0:
            return location
        elif (((arr_copy[0] == "NORTH") and (location[-1] == "SOUTH")) or ((arr_copy[0] == "SOUTH") and (location[-1] == "NORTH"))) or (((arr_copy[0] == "EAST") and (location[-1] == "WEST")) or ((arr_copy[0] == "WEST") and (location[-1] == "EAST"))):
            location.pop(-1)
            arr_copy.pop(0)
            if len(arr_copy) == 0:
                return location
            location.append(arr_copy.pop(0))
            if (len(location) == 2):
                if (((location[0] == "NORTH") and (location[1] == "SOUTH")) or ((location[0] == "SOUTH") and (location[1] == "NORTH"))) or (((location[0] == "EAST") and (location[1] == "WEST")) or ((location[0] == "WEST") and (location[1] == "EAST"))):
                    location.pop()
                    location.pop()
        else:
            location.append(arr_copy.pop(0))

        if len(location) > 2:
            if (((location[-1] == "NORTH") and (location[-2] == "SOUTH")) or ((location[-1] == "SOUTH") and (location[-2] == "NORTH"))) or (((location[-1] == "EAST") and (location[-2] == "WEST")) or ((location[-1] == "WEST") and (location[-2] == "EAST"))):
                location.pop()
                location.pop()
                if len(arr_copy) != 0:
                    location.append(arr_copy.pop(0))
                else:
                    return location
    return location


# The Internet's solutions:
opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}
def dirReduc(plan):
    new_plan = []
    for d in plan:
        if new_plan and new_plan[-1] == opposite[d]:
            new_plan.pop()
        else:
            new_plan.append(d)
    return new_plan

def dirReduc(arr):
    dir = " ".join(arr)
    dir2 = dir.replace("NORTH SOUTH",'').replace("SOUTH NORTH",'').replace("EAST WEST",'').replace("WEST EAST",'')
    dir3 = dir2.split()
    return dirReduc(dir3) if len(dir3) < len(arr) else dir3

def dirReduc(arr):
    opposites = [{'NORTH', 'SOUTH'}, {'EAST', 'WEST'}]
    for i in range(len(arr)-1):
        if set(arr[i:i+2]) in opposites:
            del arr[i:i+2]
            return dirReduc(arr)
    return arr

def dirReduc(arr):
    i = 1
    while i < len(arr) and len(arr) > 1:
        if sorted([arr[i], arr[i-1]]) in [["NORTH", "SOUTH"], ["EAST", "WEST"]]:
            del arr[i-1:i+1]
            i = 1
        else:
            i += 1
    return arr



"""
6-kyu
ROMAN NUMERALS ENCODER:
Create a function taking a positive integer as its parameter and returning a string containing the Roman Numeral representation of that integer.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

Example:

solution(1000) # should return 'M'
Help:

Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000
Remember that there can't be more than 3 identical symbols in a row.
"""
# My (overwrought, hard-coded) solution:
roman_dict = {1: "I", 4: "IV", 5: "V", 6: "VI", 9: "IX", 10: "X", 40: "XL", 50: "L", 60: "LX", 90: "XC", 100: "C",
              400: "CD", 500: "D", 600: "DC", 900: "CM", 1000: "M", 4000: "MV", 5000: "V"}

def solution(n):
    four_thousands = 0
    thousands = 0
    nine_hundreds = 0
    six_hundreds = 0
    five_hundreds = 0
    four_hundreds = 0
    hundreds = 0
    ninties = 0
    sixties = 0
    fifties = 0
    forties = 0
    tens = 0
    nine = 0
    six = 0
    five = 0
    four = 0

    # THOUSANDS:
    if n >= 5000:
        return -1

    if n >= 4000:
        four_thousands = n // 4000
        n = n - 4000

    if n >= 1000 and n <= 4000:
        thousands = n // 1000
        n = n % 1000

    # HUNDREDS:
    if n >= 900:
        nine_hundreds = n // 900
        n = n - 900

    if n >= 600:
        six_hundreds = n // 600
        n = n - 600

    if n >= 500:
        five_hundreds = n // 500
        n = n - 500

    if n >= 400:
        four_hundreds = n // 400
        n = n - 400

    if n >= 100 and n <= 400:
        hundreds = n // 100
        n = n % 100

    # TENS:
    if n >= 90:
        ninties = n // 90
        n = n - 90

    if n >= 60:
        sixties = n // 60
        n = n - 60

    if n >= 50:
        fifties = n // 50
        n = n - 50

    if n >= 40:
        forties = n // 40
        n = n - 40

    if n >= 10 and n <= 40:
        tens = n // 10
        n = n % 10

    # ONES:
    if n == 9:
        nine = n // 9
        n = n - 9

    if n >= 6:
        six = n // 6
        n = n - 6

    if n >= 5:
        five = n // 5
        n = n - 5

    if n >= 4:
        four = n // 4
        n = n - 4

    rn = (four_thousands*roman_dict[4000] + thousands*roman_dict[1000] +
          nine_hundreds*roman_dict[900] + six_hundreds*roman_dict[600] + five_hundreds*roman_dict[500] + four_hundreds*roman_dict[400] + hundreds*roman_dict[100] +
          ninties*roman_dict[90] + sixties*roman_dict[60] + fifties*roman_dict[50] + forties*roman_dict[40] + tens*roman_dict[10] +
          nine*roman_dict[9] + six*roman_dict[6] + five*roman_dict[5] + four*roman_dict[4] + n*roman_dict[1])

    return rn


# The Internet's solutions:
def solution(n):
    roman_numerals = {1000:'M',
                      900: 'CM',
                      500: 'D',
                      400: 'CD',
                      100: 'C',
                      90: 'XC',
                      50: 'L',
                      40: 'XL',
                      10: 'X',
                      9: 'IX',
                      5: 'V',
                      4: 'IV',
                      1: 'I'
    }
    roman_string = ''
    for key in sorted(roman_numerals.keys(),reverse=True):
        while n >= key:
            roman_string += roman_numerals[key]
            n -= key
    return roman_string

units = " I II III IV V VI VII VIII IX".split(" ")
tens = " X XX XXX XL L LX LXX LXXX XC".split(" ")
hundreds = " C CC CCC CD D DC DCC DCCC CM".split(" ")
thousands = " M MM MMM".split(" ")
def solution(n):
    return thousands[n//1000] + hundreds[n%1000//100] + tens[n%100//10] + units[n%10]

vals = zip(('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'),
           (1000, 900, 500,  400, 100,   90,  50,   40,  10,    9,   5,    4,   1))
def solution(n):
    if n == 0: return ""
    return next(c + solution(n-v) for c,v in vals if v <= n)



"""
5-kyu:
EXTRACT THE DOMAIN NAME FROM A URL:
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

domain_name("http://github.com/carbonfive/raygun") == "github"
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
"""
# My answer:
def domain_name(url):
    http_prefixes = ["https://www.", "http://www.", "http://",  "https://", "www."]

    for prefix in http_prefixes:
        if prefix in url:
            new_url = url[len(prefix):]
            print(new_url)
            if "." in new_url:
                newer_url = new_url[:new_url.index(".")]
                return newer_url

    if "." in url:
        new_url = url[:url.index(".")]
        return new_url

# The Internet's Answers:
def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]

import re
def domain_name(url):
    return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')
#
def domain_name(url):
    from re import findall, VERBOSE
    try:
        url = findall("""\A
                        (?: http
                        s?
                        ://)?         # matches http:// or https:// or nothing

                        (?: www.)?    # matches www. or nothing

                        ([- a-z]+)    # matches a sequence of letters and dashes

                        (?: .com|.ru)     # matches either .com or .ru
                        (?: [/ a-z]+)?    # matches a sequence or letters and slashes
                        \Z""", url, VERBOSE)
        return url[0]
    except:
        return "Invalid URL."
#
def domain_name(url):
    return url.split("://")[-1].split(".")[-2]



"""
6-kyu:
DETECT PANGRAM:
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
"""
# My solution:
import string

def is_pangram(s):
    s = set(s.lower().replace(" ", ""))
    alpha = list(string.ascii_lowercase)
    alpha_dict = {}

    for letter in alpha:
        if letter in s:
            alpha_dict[letter] = 1

    is_it_26 = sum(alpha_dict.values())
    return is_it_26 == 26

# The Internet's solutions:
import string
def is_pangram(s):
    return set(string.lowercase) <= set(s.lower())

import string
def is_pangram(s):
    s = s.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s:
            return False
    return True


"""
6-kyu:
HELP THE BOOKSELLER
A bookseller has lots of books classified in 26 categories labeled A, B, ... Z. Each book has a code c of 3, 4, 5 or more capitals letters. The 1st letter of a code is the capital letter of the book category. In the bookseller's stocklist each code c is followed by a space and by a positive integer n (int n >= 0) which indicates the quantity of books of this code in stock.

For example an extract of one of the stocklists could be:

L = {"ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"}.
or

L = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"] or ....
You will be given a stocklist (e.g. : L) and a list of categories in capital letters e.g :

  M = {"A", "B", "C", "W"}
or

  M = ["A", "B", "C", "W"] or ...
and your task is to find all the books of L with codes belonging to each category of M and to sum their quantity according to each category.

For the lists L and M of example you have to return the string (in Haskell/Clojure/Racket a list of pairs):

  (A : 20) - (B : 114) - (C : 50) - (W : 0)
where A, B, C, W are the categories, 20 is the sum of the unique book of category A, 114 the sum corresponding to "BKWRK" and "BTSQZ", 50 corresponding to "CDXEF" and 0 to category 'W' since there are no code beginning with W.

If L or M are empty return string is "" (Clojure and Racket should return an empty array/list instead).

Note:
In the result codes and their values are in the same order as in M.
"""
# My answer:
def stock_list(listOfArt, listOfCat):
    LOA_lst = []
    count_dict = {}
    result = ""
    for lttr in listOfArt:
        LOA_lst.append([lttr.split()[0], int(lttr.split()[-1])])

    for lttr in listOfCat:
        count_dict[lttr] = 0
        current_count = 0
        for element in LOA_lst:
            if lttr == element[0][0]:
                current_count += element[-1]
                count_dict[lttr] = current_count

    empty = 0
    for v in count_dict.values():
        empty += v
    if empty == 0:
        return ""

    for k,v in count_dict.items():
        result += f"({k} : {v}) - "
    result = result[:-3]

    return result

# The Internet's Answers:
from collections import Counter
def stock_list(listOfArt, listOfCat):
    if not listOfArt:
        return ''
    codePos = listOfArt[0].index(' ') + 1
    cnt = Counter()
    for s in listOfArt:
        cnt[s[0]] += int(s[codePos:])
    return ' - '.join('({} : {})'.format(cat, cnt[cat]) for cat in listOfCat)

def stock_list(listOfArt, listOfCat):
    if (len(listOfArt) == 0) or (len(listOfCat) == 0):
        return ""
    result = ""
    for cat in listOfCat:
        total = 0
        for book in listOfArt:
            if (book[0] == cat[0]):
                total += int(book.split(" ")[1])
        if (len(result) != 0):
            result += " - "
        result += "(" + str(cat) + " : " + str(total) + ")"
    return result

def stock_list(a, b):
    a = [(q, sum(int(x.split()[1]) for x in a if x[0] == q)) for q in b]
    return ''.join(['({} : {}) - '.format(x[0], x[1]) for x in a]).strip(' - ') if sum(x[1] for x in a) != 0 else ''


"""
6-kyu:
MULTI-TAP KEYPAD TEXT ENTRY ON AN OLD MOBILE PHONE
Prior to having fancy iPhones, teenagers would wear out their thumbs sending SMS messages on candybar-shaped feature phones with 3x4 numeric keypads.

------- ------- -------
|     | | ABC | | DEF |
|  1  | |  2  | |  3  |
------- ------- -------
------- ------- -------
| GHI | | JKL | | MNO |
|  4  | |  5  | |  6  |
------- ------- -------
------- ------- -------
|PQRS | | TUV | | WXYZ|
|  7  | |  8  | |  9  |
------- ------- -------
------- ------- -------
|     | |space| |     |
|  *  | |  0  | |  #  |
------- ------- -------
Prior to the development of T9 (predictive text entry) systems, the method to type words was called "multi-tap" and involved pressing a button repeatedly to cycle through the possible values.

For example, to type a letter "R" you would press the 7 key three times (as the screen display for the current character cycles through P->Q->R->S->7). A character is "locked in" once the user presses a different key or pauses for a short period of time (thus, no extra button presses are required beyond what is needed for each letter individually). The zero key handles spaces, with one press of the key producing a space and two presses producing a zero.

In order to send the message "WHERE DO U WANT 2 MEET L8R" a teen would have to actually do 47 button presses. No wonder they abbreviated.

For this assignment, write a module that can calculate the amount of button presses required for any phrase. Punctuation can be ignored for this exercise. Likewise, you can assume the phone doesn't distinguish between upper/lowercase characters (but you should allow your module to accept input in either for convenience).

Hint: While it wouldn't take too long to hard code the amount of keypresses for all 26 letters by hand, try to avoid doing so! (Imagine you work at a phone manufacturer who might be testing out different keyboard layouts, and you want to be able to test new ones rapidly.)
"""
# My answer:
keypad_dict = {"1": 1, "ABC2": 2, "DEF3": 3,
               "GHI4": 4, "JKL5": 5, "MNO6": 6,
               "PQRS7": 7, "TUV8": 8, "WXYZ9": 9,
               " 0": 0, "*": "star", "#": "pound"}

def presses(phrase):
    phrase = phrase.upper()
    count = 0
    for lttr in phrase:
        for key in keypad_dict.keys():
            if lttr in key:
                count += (key.index(lttr) + 1)
    return count

# The Internet's answers:
BUTTONS = [ '1',   'abc2',  'def3',
          'ghi4',  'jkl5',  'mno6',
          'pqrs7', 'tuv8', 'wxyz9',
            '*',   ' 0',    '#'   ]
def presses(phrase):
    return sum(1 + button.find(c) for c in phrase.lower() for button in BUTTONS if c in button)

def presses(phrase):
    x = 0
    for letter in phrase:
        if letter.lower() in list('1*#adgjmptw '): x+= 1
        elif letter.lower() in list('0behknqux'): x+= 2
        elif letter.lower() in list('cfilorvy'): x+= 3
        elif letter.lower() in list('234568sz'): x+= 4
        elif letter.lower() in list('79'): x+= 5
    return x



"""
6-kyu:

(Personal note: I've cleaned up the instructions somewhat as it did not make much sense as originally written.)

Enough is enough!
Alice and Bob took many pictures of the places they've been while on holiday, and now they want to show Charlie all of it. However, Charlie doesn't like repeats, so he tells Alice and Bob that he will only sit through the picture viewing session if they show the same photo N times at most. Luckily, Alice and Bob are able to encode this request to prevent showing a repeat more than Charlie can handle. Can you help them to remove numbers such that their list contains each entry only up to N times, without changing the order?

Task
Given a list lst and a number N, create a new list that contains each number of lst at most N times without reordering. For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].

Example
  delete_nth ([1,1,1,1],2) # return [1,1]

  delete_nth ([20,37,20,21],1) # return [20,37,21]
"""
# My answer:
def delete_nth(order, max_e):
    output = []
    for num in order:
        if output.count(num) < max_e:
            output.append(num)
        elif output.count(num) >= max_e:
            continue
        else:
            output.append(num)
    return output

# The Internet's answers:
def delete_nth(order,max_e):
    ans = []
    for o in order:
        if ans.count(o) < max_e: ans.append(o)
    return ans

from collections import defaultdict
def delete_nth(order,max_e):
    c = defaultdict(int)
    def count(x):
        c[x] += 1
        return c[x] <= max_e
    return filter(count, order)

def delete_nth(order, max_e):
    d = {}
    res = []
    for item in order:
      n = d.get(item, 0)
      if n < max_e:
        res.append(item)
        d[item] = n+1
    return res


"""
6-kyu:
MULTIPLICATION TABLE

Create a function that accepts dimensions, of Rows x Columns, as parameters in order to create a multiplication table sized according to the given dimensions. **The return value of the function must be an array, and the numbers must be Fixnums, NOT strings.

Example:

multiplication_table(3,3)

1 2 3
2 4 6
3 6 9

-->[[1,2,3],[2,4,6],[3,6,9]]

Each value on the table should be equal to the value of multiplying the number in its first row times the number in its first column.
"""
# My answer:
import numpy as np
def multiplication_table(row, col):
    row = np.array(range(1, row + 1))
    col = np.array(range(1, col + 1))
    table = [col for r in row]
    new_table = []
    for idx, r in enumerate(table):
        new_table.append(r * (idx + 1))
    return np.array(new_table)

# The Internet's answers:
def multiplication_table(row,col):
    return [[(i+1)*(j+1) for j in range(col)] for i in range(row)]

def multiplication_table(row,col):
    return [[x*y for y in range(1,col+1)] for x in range(1,row+1)]

def multiplication_table(row,col):
    res = []
    for i in range(1, row+1):
        item = []
        for j in range(1, col+1):
            item.append(i*j)
        res.append(item)
    return res



"""
5-kyu:
SUM OF PAIRS
Sum of Pairs
Given a list of integers and a single sum value, return the first two values (parse from the left please) in order of appearance that add up to form the sum.

sum_pairs([11, 3, 7, 5],         10)
#              ^--^      3 + 7 = 10
== [3, 7]

sum_pairs([4, 3, 2, 3, 4],         6)
#          ^-----^         4 + 2 = 6, indices: 0, 2 *
#             ^-----^      3 + 3 = 6, indices: 1, 3
#                ^-----^   2 + 4 = 6, indices: 2, 4
#  * entire pair is earlier, and therefore is the correct answer
== [4, 2]

sum_pairs([0, 0, -2, 3], 2)
#  there are no pairs of values that can be added to produce 2.
== None/nil/undefined (Based on the language)

sum_pairs([10, 5, 2, 3, 7, 5],         10)
#              ^-----------^   5 + 5 = 10, indices: 1, 5
#                    ^--^      3 + 7 = 10, indices: 3, 4 *
#  * entire pair is earlier, and therefore is the correct answer
== [3, 7]
Negative numbers and duplicate numbers can and will appear.

NOTE: There will also be lists tested of lengths upwards of 10,000,000 elements. Be sure your code doesn't time out.
"""
# My answer (thanks to Mike and Andrew):
def sum_pairs(ints, s):
    seen = dict()
    for idx, num in enumerate(ints):
        if num in seen.keys():
            return [ints[seen[num]], num]
        else:
            seen[s - num] = idx
    return None

# The Internet's answers:
def sum_pairs(lst, s):
    cache = set()
    for i in lst:
        if s - i in cache:
            return [s - i, i]
        cache.add(i)

def sum_pairs(nums, sum_value):
    seen = set()
    for num in nums:
        diff = sum_value - num
        if diff in seen:
            return [diff, num]
        seen.add(num)

def sum_pairs(ints, s):
    d = set()
    for n in ints:
        if n in d: return [s - n, n]
        d.add(s - n)



"""
LeetCode Problem #121 (related to the problem just above):
BEST TIME TO BUY AND SELL STOCK:
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""
# My answer:
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_at = None

        for idx, price in enumerate(prices):
            if buy_at == None:
                buy_at = price

            todays_price = price
            if todays_price < buy_at:
                buy_at = todays_price

            running_profit = todays_price - buy_at

            if running_profit > max_profit:
                max_profit = running_profit

        return max_profit


"""
6-kyu:
WRITE NUMBER IN EXPANDED FORM
You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
NOTE: All numbers will be whole numbers greater than 0.
"""
# My answer:
def expanded_form(num):
    num_as_str_split = list(str(num))
    zeros_to_add = 0
    output_lst = []

    # Keeping track of our number's "components" (1s, 10s, 100s, etc.), and adding them to a list
    for element in num_as_str_split[::-1]:
        element = element + ("0" * zeros_to_add)
        # Keeps numbers that start with 0 (e.g. "000") from being appended
        if element[0] != "0":
            output_lst.append(element)
        # As we go up by a power of 10, so do the amount of zeros we want to append to our element (depending on its place)
        zeros_to_add+=1

    # And here, we reverse the list we've created
    output_str = ""
    for thing in output_lst[::-1]:
        output_str+= thing + " + "
    return output_str[:-3]

# The Internet's answers:
def expanded_form(num):
    num = list(str(num))
    return ' + '.join(x + '0' * (len(num) - y - 1) for y,x in enumerate(num) if x != '0')

def expanded_form(n):
    result = []
    for a in range(len(str(n)) - 1, -1, -1):
        current = 10 ** a
        quo, n = divmod(n, current)
        if quo:
            result.append(str(quo * current))
    return ' + '.join(result)

def expanded_form(num):
    num = str(num)
    st = ''
    for j, i in enumerate(num):
        if i != '0':
            st += ' + {}{}'.format(i, (len(num[j+1:])*'0'))
    return st.strip(' +')



"""
5-kyu:
BEST TRAVEL
John and Mary want to travel between a few towns A, B, C ... Mary has on a sheet of paper a list of distances between these towns. ls = [50, 55, 57, 58, 60]. John is tired of driving and he says to Mary that he doesn't want to drive more than t = 174 miles and he will visit only 3 towns.

Which distances, hence which towns, they will choose so that the sum of the distances is the biggest possible to please Mary and John?

Example:

With list ls and 3 towns to visit they can make a choice between: [50,55,57],[50,55,58],[50,55,60],[50,57,58],[50,57,60],[50,58,60],[55,57,58],[55,57,60],[55,58,60],[57,58,60].

The sums of distances are then: 162, 163, 165, 165, 167, 168, 170, 172, 173, 175.

The biggest possible sum taking a limit of 174 into account is then 173 and the distances of the 3 corresponding towns is [55, 58, 60].

The function chooseBestSum (or choose_best_sum or ... depending on the language) will take as parameters t (maximum sum of distances, integer >= 0), k (number of towns to visit, k >= 1) and ls (list of distances, all distances are positive or null integers and this list has at least one element). The function returns the "best" sum ie the biggest possible sum of k distances less than or equal to the given limit t, if that sum exists, or otherwise nil, null, None, Nothing, depending on the language. With C++, C, Rust, Swift, Go, Kotlin return -1.

Examples:

ts = [50, 55, 56, 57, 58] choose_best_sum(163, 3, ts) -> 163

xs = [50] choose_best_sum(163, 3, xs) -> nil (or null or ... or -1 (C++, C, Rust, Swift, Go)

ys = [91, 74, 73, 85, 73, 81, 87] choose_best_sum(230, 3, ys) -> 228
"""
# My solution:


# The Internet's Solution:
