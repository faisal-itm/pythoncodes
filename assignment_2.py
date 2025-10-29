'''Define a function reverse()that computes the reversal of a string. For example, reverse("I am
testing")should return the string "gnitset ma I".'''

def reverse(x):

    z = len(x)

    str1 = ""

    for i in range(len(x)):

        y = z-i-1

        b = (x[y])

        str1 = str1 + b

    return (str1)

aAA = reverse ('khan is here')
print(aAA)


'''Define a function is_palindrome()that recognizes palindromes (i.e. words that look the same written
backwards). For example, is_palindrome("radar")should return True.'''


def is_plindrome(x):

    y = str.lower(x)


    z = reverse(y)

    if y == z:
        print (True)
    else:
        print (False)

aka = is_plindrome('radar')


''' Define a function sum()and a function multiply()that sums and multiplies (respectively) all the
numbers in a list of numbers. For example, sum([1, 2, 3, 4])should return 10, and multiply([1,
2, 3, 4])should return 24. '''


def sum(x):

    y = list(x)

    z = 0
    for i in range(len(y)):

        z = z+ y[i]

    return z


sum1 = sum([1,2,3,4,5,6,7,8,9,10])

print(sum1)

def multiply(x):

    y = list(x)

    z = 1
    for i in range(len(y)):

        z = z * y[i]

    return z

mul1=multiply([1,2,3,4])

print(mul1)


'''Write a function translate()that will translate a text into "rövarspråket" (Swedish for "robber's
language"). That is, double every consonant and place an occurrence of "o"in between. For example,
translate("this is fun")should return the string "tothohisos isos fofunon".'''

def translate(x):

    x = x.lower()
    vowle = 'aeiou '
    str1=''
    for i in x:
        if i in vowle:
            str1 = str1+i
        else:
            y=i+"o"+i
            str1 = str1+y

    return str1


amg=translate('this is khan')

print(amg)

