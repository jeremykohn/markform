# Validate Markform tag format, in general.
# If not valid, do not create a tag.
def validate_tag(tag_text):

    # For some types of Markform tags, the opening and closing tokens are the same character.
    simple_tokens = ['+', '-', '_', '@', '$', '%', '^', '*']
        
    # For other Markform tags, the closing token is the inverse of the opening token.
    inverse_tokens = {
        "(": ")",
        "[": "]",            
        "{": "}",
        "|": "|"
    }

    # Tag must be at least three characters, since it requires `[`, `]` and at least one token.
    if len(tag_text) < 3:
        return False

    # Validate opening and closing brackets.
    first_char = tag_text[0]
    last_char = tag_text[-1]

    if first_char != "[" or last_char != "]":
        return False

    # Validate opening and closing tokens.
    second_char = tag_text[1]
    second_last_char = tag_text[-2]    

    # If simple token: Tag must have the same opening and closing token.
    if second_char in simple_tokens:
        if second_last_char != second_char:
            return False

    # If inverse tokens: Closing token must be inverse of opening token.
    elif second_char in inverse_tokens:
        if second_last_char != inverse_tokens[second_char]:
            return False

    # If neither simple token or inverse token, then tag is invalid.
    else:
        return False

    # Parse for non-allowed components.
    pos = 0
    while pos < len(tag_text):
        if tag_text[pos] == "\n":
            return False
        pos += 1

    # Also parse for early closing? Like, [+ Inner text content +] More content +]
    # Not here, I think. Just validate the basics. 
    # And provide more flexibility -- spec might change to parse inward, not forward.

    return True


# Test cases.

test_cases_false = [
    # None, 0, 1, 2.3, True, False, 
    "",
    "[+",
    "+]",
    " [+]",
    "[+] ",
    " [+] ",
    "  [+++] ",
    "[+ +]+]",
    "[+-]",
    "[-+]",
    "[+ -]",
    "[- +]",
    "Non-tag text",
    "Pre-text [+]",
    "[+] post-text",
    "Pre- and [+] post-text",
    # Inverse-token tag test cases
    "[(]",
    "[)]",
    "[[)]",
    "[(]]",
    "[[[]]]",
    "[[()]]",
    "[(())]",
    "[[[ ]]]",
    "[(( ))]",
]


test_cases_true = [
    # Simple
    "[+]",
    "[++]",
    "[+++]",
    "[+ +]",
    "[++ +]",
    "[+ ++]",
    "[++ ++]",
    "[+Inner content+]",
    "[+ Inner content+]",
    "[+Inner content +]",
    "[+ Inner content +]",
    "[+  Inner content+]",
    "[+  Inner content +]",
    "[+ Inner content  +]",
    # Inverse
    "[[]]",
    "[()]",
    "[[()]]",
    "[([])]"
]

all_test_cases = test_cases_false + test_cases_true

for test_case in all_test_cases:
    print("Tag: " + test_case)
    print("Validate: {}".format(validate_tag(test_case)))
