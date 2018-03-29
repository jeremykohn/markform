# Validate Markform element format, in general.
def validate_element(element_text):

    # For some types of Markform elements, the opening and closing tokens are the same character.
    simple_tokens = ['+', '-', '_', '@', '$', '%', '^', '*']
        
    # For other Markform elements, the closing token is the inverse of the opening token.
    inverse_tokens = {
        "(": ")",
        "[": "]",            
        "{": "}",
        "|": "|"
    }

    # Element must be at least three characters, since it requires `[`, `]` and at least one token.
    if len(element_text) < 3:
        return False

    # Validate opening and closing brackets.
    first_char = element_text[0]
    last_char = element_text[-1]

    if first_char != "[" or last_char != "]":
        return False

    # Validate opening and closing tokens.
    second_char = element_text[1]
    second_last_char = element_text[-2]    

    # If simple token: Element must have the same opening and closing token.
    if second_char in simple_tokens:
        if second_last_char != second_char:
            return False

    # If inverse tokens: Closing token must be inverse of opening token.
    elif second_char in inverse_tokens:
        if second_last_char != inverse_tokens[second_char]:
            return False

    # If neither simple token or inverse token, then element is invalid.
    else:
        return False

    # Parse for non-allowed components.
    pos = 0
    while pos < len(element_text):
        if element_text[pos] == "\n":
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
    "Non-element text",
    "Pre-text [+]",
    "[+] post-text",
    "Pre- and [+] post-text",
    # Inverse-token element test cases
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
    print("Element: " + test_case)
    print("Validate: {}".format(validate_element(test_case)))
