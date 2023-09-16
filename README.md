# Publix Produce Codes

This project was made to help me memorize and practice the produce codes at Publix. I also made another script to help with aisle locations of certain products.

## Use

Simply run either the `aisle_items.py` or the `produce_codes.py` functions and the program will begin immediately.

## Implementation

Both of these files use the same underlying method `present_terms()`. This is actually quite an abstract way to present a dictionary to a user for review. It mixes the key value pairs and prints them to the user. If the user enters `enter`, the result will be provided in case they don't know. The same term will continue to be displayed until it is correctly entered. Every incorrect guess adds the term to the list to be reviewed, which is returned at the end of the function. This means that terms answered incorrectly more are going to be more frequent in the returned list. The process repeats until all terms are exhausted and the review is complete.

To create the dictionaries, parsers were written foe each text file. However, these are dependent on the nature of the format of the text file, and not the primary focus.

## Opportunities

Since the function uses key-value pairs, any series of terms and definitions can be used by this algorithm repeatedly to simulate a review system for the user. This is great for studying and memorizing important definitions or matching values.