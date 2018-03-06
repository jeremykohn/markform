# Parse one line.

# First, validate input: A one-line string. No newlines.
def validate_single_line(line):
    if type(line) is not str:
        raise ValueError("Element must be a string.")
    if "\n" in line:
        raise ValueError("Element must include only one line, cannot include newline.")

# Parse line to get tag type, tag text, pre-tag text, and post-tag text.
def parse_line(line):
    # First, search for opening bracket followed by opening identifier.
    # If found, get opening identifier and deduce closing identifier.
    # Then search for closing identifer followed by closing bracket.
    
    # Initial conditions.
    tag_open = False
    tag_complete = False

    # Types of Markform identifiers.
    tag_type_identifiers = {
        "+": "start",
        "-": "end",
        "_": "text_input",
        "@": "email_input",
        "$": "number_input",
        "%": "range_input",
        "^": "file_input",
        "(": "submit_button",
        "[": "textarea",
        "{": "multiple_choice"
    }
    
    # For some tag types, the opening identifier and closing identifier are inverses of each other.
    inverses_of_identifiers = {
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
            if next_character in tag_type_identifiers:
                # Found tag opening.
                tag_open = True
                opening_identifier = next_character

        if tag_open:
            # In some types of tags, the opening and closing identifiers are the same.
            if opening_identifier not in inverse_identifiers:
                closing_identifier = opening_identifier        
            # In other types of tags, the opening and closing identifiers are inverses of each other.
            else:
                closing_identifier = inverse_identifiers[opening_identifier]

            # Search for tag closing.

            # Start at current position, where the tag opens.
            pos_left = pos

            # Search for closing bracket preceded by closing identifier.
            pos_right = pos_left + 1                
            while pos_right + 1 < len(line):
                if line[pos_right] == closing_identifier and line[pos_right + 1] == "]":
                    # Found end of tag.
                    tag_complete = True
                    # Get tag's starting and ending positions.
                    left_bracket_index = pos_left
                    right_bracket_index = pos_right
                    # Stop looking for end of tag. 
                    break
                else:
                    # Keep looking for end of tag.
                    pos_right += 1

        if tag_complete:   
            # Get tag type based on opening identifier.
            tag_type = tag_type_identifiers[opening_identifier]
            # Divide line into sections.
            tag_text = line[left_bracket_index : right_bracket_index + 1]
            # inner_content: Need to parse tag.
            # Also, validate_tag: Need to parse tag.
                # If not valid tag, don't convert line -- "convert to HTML" just returns original line.
            if left_bracket_index > 0:
                pre_tag_text = line[:left_bracket_index]
            if right_bracket_index < len(line) - 1:
                post_tag_text = line[right_bracket_index + 1 :]
            # Return tag type and content of each section.
            return (tag_type, tag_text, pre_tag_text, post_tag_text)

        # If tag not open and not complete, continue parsing.
        pos += 1
    
    # Parser has reached the end of this line. 
    # No Markform tag found, so return None for tag type, and return empty strings in place of text sections.
    return None, "", "", ""


test_cases = [
    # None, 0, 1, 2.3, True, False, 
    "",
    "No tag here"
    "[+]",
    " [+] ",
    "  [+++] ",
    "Form [+] start",
    "No tag",
    "Not a [+ tag",
    "Yes [+   +] a tag",
    "Yes [+  +]+] a tag",
    "Yes [+++ + all sorts of text in here++++] a tag",
    "Tag and pre-tag text [+   +]",
    "[+    +] tag and post-tag text"
    "No tag [[ on this line",
    "No tag [[] on this line",
    "Textarea [[]] tag",
    "Yes [[+   +]] tag",
    "No [[+   +] ] tag",
    "Not a valid tag [[[ though that will be taken care of later]]]",
    "Yes valid tag [[{[ with all sorts of text in here  }]}]] and text afterwards"
]


for line in test_cases:
    validate_element(line)
    print(parse_element(line))

    
for line in inverse_test_cases:
    validate_element(line)
    print(parse_element(line))
