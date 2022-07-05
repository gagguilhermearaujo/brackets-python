#!/bin/python3

# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING brackets as parameter.
brackets_pairs = {
    "(": ")",
    "[": "]",
    "{": "}",
}


def isBalanced(brackets):
    if brackets[0] not in brackets_pairs.keys():
        return "NO"
    is_balanced = True
    last_open_bracket = []
    for bracket in brackets:
        if bracket in brackets_pairs.keys():
            last_open_bracket.append(bracket)
        else:
            pair = brackets_pairs[last_open_bracket[-1]]
            if bracket != pair:
                is_balanced = False
            else:
                last_open_bracket.pop(-1)
    if is_balanced:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":

    t = int(input().strip())

    results = []
    for t_itr in range(t):
        brackets = input()

        results.append(isBalanced(brackets))

    print(*results, sep="\n")
