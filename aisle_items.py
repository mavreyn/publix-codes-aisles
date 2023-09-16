'''
Script to parse the PbxAisles.txt document into a dictionary
It will quiz me on the items

Maverick Reynolds
07.28.2023
'''

import re
import random


def rand_from_dict(d, p=1):
    entries = list(d.items())
    amount = round(len(entries) * p)
    return dict(entries[:amount])


def parse_txt_file():
    with open('PbxAisles.txt', 'r') as f:
        txt = f.read()
    
    store_sections = txt.split('\n\n')
    aisle_items = dict()

    for section in store_sections:
        match = re.search(r'(.+?)\n(.+)', section, flags=re.DOTALL)
        aisle, items_str = match.groups()
        items = items_str.split('\n')

        for item in items:
            aisle_items[item] = aisle

    return aisle_items


def shuffle_dict(d):
    lst = list(d.items())
    random.shuffle(lst)
    return dict(lst)


# Present the terms and return a list of terms to review (incorrectly answered)
def present_terms(d):
    print(f'\n{len(d)}\n')

    review_dict = dict()

    for key, value in d.items():
        # Prompt for code
        while value != (inp := input(f'{key} > ')):
            # Append to review list
            review_dict[key] = value
            if inp == '':
                # Show the code if unknown
                print(value)
    
    print(f'\n{len(review_dict)}/{len(d)}\n')
    return review_dict


def main():
    # Get info
    aisle_items = shuffle_dict(parse_txt_file())

    frac_to_test = float(input('Frac >'))
    aisle_items = rand_from_dict(aisle_items, frac_to_test)

    num = len(aisle_items)
    perfect = True

    print()
    # Keep testing until all terms done perfectly at least once
    while (terms_to_review := present_terms(aisle_items)):
        perfect = False
        aisle_items = shuffle_dict(terms_to_review)

    # End program
    print()
    input(f'Finished {num} terms' + (' perfectly!' if perfect else ''))


if __name__ == '__main__':
    main()

