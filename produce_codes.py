'''
To help me learn the produce codesfor my job at Publix
More than just produce (water/ice as well)

Reads from text file (split by ' ') and then randomly test

Maverick Reynolds
05.11.2023

'''

import random
import re


def main():
    # Get info
    with open('codes.txt') as f:
        lines = [ln.strip('\n') for ln in f.readlines() if ln != '\n']

    num = len(lines)
    perfect = True

    # Keep testing until all terms done perfectly at least once
    while (terms_to_review := present_terms(lines)):
        perfect = False
        lines = terms_to_review

    # End program
    print()
    input(f'Finished {num} terms' + (' perfectly!' if perfect else ''))


# Present the terms and return a list of terms to review (incorrectly answered)
def present_terms(lst):
    review = []

    random.shuffle(lst)
    for line in lst:
        # Get the groups
        rgx_match = re.match('^(.+) (\d+)$', line)
        name, code = rgx_match.groups()

        # Prompt for code
        while code != (inp := input(f'{name} > ')):
            # Append to review list
            review.append(line)
            if inp == '':
                # Show the code if unknown
                print(code)
    
    print()
    return review


if __name__ == '__main__':
    main()

