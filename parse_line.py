# Parse one line from a Markform document.
# If line includes a Markform element, return an object with these components: 
# 1. Pre-element content
# 2. Opening identifier
# 3. Inner content
# 4. Closing identifier
# 5. Post-element content
# If line does not include a Markform element, return an object containing 'None' values.

"""
# First, validate input: A one-line string. No newlines.
def validate_single_line(line):
    if type(line) is not str:
        raise ValueError("Line must be a string.")
    if "\n" in line:
        raise ValueError("Line must include only one line, cannot include newline.")
"""

def get_inner_content(element_text, opening_identifier, closing_identifier):
    # Validate.
    element_length = len(element_text)
    if element_length < 3 or element_text[0] != "[" or element_text[element_length - 1] != "]":
        raise ValueError("Invalid element: {}".format(element_text))

    # Start looking for inner content just inside the opening/closing brackets.
    inner_pos_left = 1
    inner_pos_right = len(element_text) - 2
    
    current_character_left = element_text[inner_pos_left]
    current_character_right = element_text[inner_pos_right]

    # Validate.
    if current_character_left != opening_identifier or current_character_right != closing_identifier:
        raise ValueError("Invalid input: {} does not start with {} and end with {}".format(element_text, "[" + opening_identifier, closing_identifier + "]"))

    # For simple identifiers, there can be one or more repeated identifiers on each side.
    if opening_identifier == closing_identifier:
        # Skip continuous repeated identifiers on the left.
        while current_character_left == opening_identifier:
            inner_pos_left += 1
            current_character_left = element_text[inner_pos_left]
        # And skip continuous repeated identifiers on the right.
        while current_character_right == closing_identifier:
            inner_pos_right -= 1
            current_character_right = element_text[inner_pos_right]
    # For paired/inverse identifiers, there should only be one on the left and one on the right. No repeats.
    elif opening_identifier != closing_identifier:
        inner_pos_left += 1
        inner_pos_right -= 1

    # Now, have inner content.
    # Anything between the opening and closing identifiers.
    inner_content = element_text[inner_pos_left : inner_pos_right + 1]
    return inner_content


# Parse line to get element type, element text, pre-element text, and post-element text.
# Rename "parse_line_into_components"?

def parse_line(line):

    # Default values.
    opening_identifier = None
    closing_identifier = None
    pre_element_text = None
    element_text = None
    post_element_text = None
    inner_content = None

    # element_type = None

    # First, search for opening bracket followed by opening identifier.
    # If found, get opening identifier and deduce closing identifier.
    # Then search for closing identifer followed by closing bracket.
    
    # Initial conditions.
    
    element_open = False
    element_complete = False

    # Types of Markform identifiers.
    element_type_identifiers = {
        "+": "start",
        "-": "end",
        "_": "text_input",
        "@": "email_input",
        "*": "password_input",
        "$": "number_input",
        "%": "range_input",
        "^": "file_input",
        "(": "submit_button",
        "[": "textarea",
        "{": "element_group"
    }
    
    # For some element types, the opening identifier and closing identifier are inverses of each other.
    inverse_identifiers = {
        "(": ")",
        "[": "]",            
        "{": "}"
    }

    # Current position. Start at beginning of line.
    pos = 0
    
    # Search for opening bracket followed by opening identifier.
    while pos < len(line):

        # print(pos)

        # Current character.
        current_character = line[pos]
        
        # Previous character, if it exists.
        if pos - 1 >= 0:
            previous_character = line[pos - 1]
        else:
            previous_character = None
            
        # Next character, if it exists.
        if pos + 1 < len(line):
            next_character = line[pos + 1]
        else:
            next_character = None
            
        # Check for an unescaped opening bracket followed by an opening identifier.
        if current_character == "[" and previous_character != "\\":
            if next_character in element_type_identifiers:
                # Found element opening.
                element_open = True
                opening_identifier = next_character
                
                # print("Element is now open. Opening identifier is " + opening_identifier + ".")
                

        if element_open:
            # In some types of elements, the opening and closing identifiers are the same.
            if opening_identifier not in inverse_identifiers:
                closing_identifier = opening_identifier        
            # In other types of elements, the opening and closing identifiers are inverses of each other.
            else:
                closing_identifier = inverse_identifiers[opening_identifier]

            # Starting at element opening, search for element closing.
            # Closing bracket preceded by closing identifier.

            # Start at current position, at the opening bracket.
            pos_left = pos

            # Start pos_right one step past the opening identifier, that is, two steps past the opening bracket.
            pos_right = pos_left + 2
            
            # Advance pos_right to search for end of element.
            while pos_right < len(line):
                # Look for a closing bracket preceded by the closing identifier.
                if line[pos_right] == "]" and line[pos_right - 1] == closing_identifier:
                    # Found end of element.
                    element_complete = True
                    # Get element's starting and ending positions.
                    left_bracket_index = pos_left
                    right_bracket_index = pos_right
                    # Stop looking for end of element. 
                    break
                else:
                    # Keep looking for end of element.
                    pos_right += 1

        if element_complete:
            # print("Element is complete.")
            
            # Get element type based on opening identifier.
            # element_type = element_type_identifiers[opening_identifier]

            # Divide line into sections.
            
            # Text of element itself.
            element_text = line[left_bracket_index : right_bracket_index + 1]
            # print("Element text: " + element_text)

            # Text preceding element.
            if left_bracket_index > 0:
                pre_element_text = line[:left_bracket_index]
            else:
                pre_element_text = ""
            
            # Text following element.
            if right_bracket_index < len(line) - 1:
                post_element_text = line[right_bracket_index + 1 :]
            else:
                post_element_text = ""
            
            # Inner content: anything between the element's opening and closing identifiers.
            inner_content = get_inner_content(element_text, opening_identifier, closing_identifier)
            
            # Also validate_element? (If not valid element, don't convert line -- "convert to HTML" just returns original line.)
            
            # The element is complete. Finished parsing this line.
            break
        
        
        
        # If element not open and not complete, continue parsing.
        else:
          pos += 1
    
    # End of line reached.
    # If no element was found, make sure to return None values.
    if element_text == None:
        opening_identifier = None
        closing_identifier = None
    

    # Return this object, which contains the line's compoments.
    parsed_line = {
        "opening_identifier": opening_identifier,
        "closing_identifier": closing_identifier,
        "element_text": element_text,
        "pre_element_content": pre_element_text,
        "post_element_content": post_element_text,
        "inner_content": inner_content
    }
    
    return parsed_line



positive_test_cases = [
    "[+]",
    " [+] ",
    "  [+++] ",
    "Form [+] start",
    "Yes [+   +] an element",
    "Yes [+  +]+] an element",
    "Yes [[+   +]] element",
    "Yes [+++ + all sorts of text in here++++] an element",
    "Element and pre-element text [+   +]",
    "[+    +] element and post-element text"
    "Textarea [[]] element",
    "Yes valid element [[{[ with all sorts of text in here  }]}]] and text afterwards"
]

negative_test_cases = [
    # None, 0, 1, 2.3, True, False, 
    "",
    "No element here",
    "No element",
    "Not a [+ element",
    "No element [[ on this line",
    "No element [[] on this line",

]

unsure_test_cases = [
    "Might be a form start element [[+   +] ] certainly not a textarea",
    "Might be a textarea [[[ the validation might be taken care of later]]]"
]

for line in positive_test_cases:
    parsed_line = parse_line(line)
    if parsed_line["opening_identifier"] != None:
        print("Line with Markform element: {}".format(line))
        print(parse_line(line))
    else:
        print("Uh oh, this line is supposed to have a Markform element in it: {}".format(line))
        print("Instead, the parsed line is: {}".format(parse_line(line)))
    
for line in negative_test_cases:
    parsed_line = parse_line(line)
    if parsed_line["element_text"] == None:
        print("Line without Markform element: {}".format(line))
        print(parse_line(line))
    else:
        print("Uh oh, this line isn't supposed to have a Markform element in it: {}".format(line))
        print("Instead, the parsed line is: {}".format(parse_line(line)))
