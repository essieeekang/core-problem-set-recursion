# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
# this implementation changes the list provided
def search(array, query):
    if not array:
        return False

    if array.pop() == query:
        return True

    return search(array, query)


def search_preserve_array(array, query):
    if not array:
        return False

    if array[0] == query:
        return True

    return search_preserve_array(array[1:], query)


# is_palindrome
def is_palindrome(text):
    if not text:
        return True

    if text[0] != text[-1]:
        return False

    return is_palindrome(text[1:-1])


# challenge attempt
def is_palindrome_challenge(text):
    return is_palindrome_challenge_helper(text, 0, -1)


def is_palindrome_challenge_helper(text, s, e):
    if s > len(text)/2:
        return True

    if text[s] != text[e]:
        return False

    return is_palindrome_challenge_helper(text, s+1, e-1)


# digit_match
def digit_match(int1, int2):
    return digit_match_helper(int1, int2, 0)


def digit_match_helper(int1, int2, count):
    if int1 % 10 == int2 % 10:
        count += 1

    if not int1 // 10 or not int2 // 10:
        return count

    return digit_match_helper(int1//10, int2//10, count)
