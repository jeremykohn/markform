# Splits Markform element into pre-tag, post-tag, tag type, and tag inner content.
# Or returns None if line is not a Markform element.

def validate_element(line):
    # Input should be a one-line string.
    
    if type(line) is not str:
        raise ValueError("Element must be a string.")
    if "\n" in line:
        raise ValueError("Element must include only one line, cannot include newline.")


def parse_element(line):

    # Components to return.
    tag_type = None
    pre_tag_text = ""
    tag_inner_content = ""
    post_tag_text = ""

    # Initial conditions.
    opening_token = None
    closing_token = None
    left_bracket_index = None
    right_bracket_index = None

    # Types of Markform tokens.
    # Move these to class variable?
    
    # For some types of Markform tags, the opening and closing tokens are the same character.
    simple_tokens = ['+', '-', '_', '@', '$', '%', '^', '*']
        
    # For other Markform tags, the closing token is the inverse of the opening token.
    inverse_tokens = {
        "(": ")",
        "[": "]",            
        "{": "}",
        "|": "|"
    }
    
    # Ready.
    
    # Current position. Start at beginning of line.
    pos = 0
    
    # If line begins with four or more spaces, or a tab, not a Markform element.
    # If line begins with fewer than four spaces, ignore initial spaces.
    initial_spaces = 0
    while pos < len(line):
        if pos == " ":
            initial_spaces += 1
        elif pos == "\t":
            # Line is not a Markform element if it has a tab before content.
            return None
        else:
            break
        # Step forward.
        pos += 1
            
            
    # Get content after initial spaces, before opening bracket.
    # Allow any number of spaces, including zero spaces, before opening bracket.
    # Trim whitespace afterwards?
    
    # Search for opening bracket followed by opening token.
    # If found, get opening token and (based on opening token) closing token.
    
    # Remember to replace "simple_tokens" with "same_tokens"?
    # Or "symmetric_tokens"?
    
    while pos < len(line):
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
        # Check for an unescaped opening bracket followed by a Markform token.
        if current_character == "[" and previous_character != "\\":
            # Simple opening tokens (for same-token tags)
            if next_character in simple_tokens:
                opening_token = next_character
                closing_token = opening_token
                break
            # Inverse opening token (for inverse-token tags)
            elif next_character in inverse_tokens:
                opening_token = next_character
                closing_token = inverse_tokens[opening_token]
                break
        # If not found, continue parsing.
        pos += 1

    # Initialize variables.    
    
    # If there is an opening token, search for a tag closing, 
    # which is a closing token followed by a closing bracket.
    if opening_token:
        pos_left = pos
        pos_right = pos + 1
        # Move pos_right to find closing bracket preceded by closing token.
        while pos_right < len(line):
            if line[pos_right] == "]" and line[pos_right - 1] == closing_token:
                # Found end of tag.
                # Get tag's position.
                left_bracket_index = pos_left
                right_bracket_index = pos_right
                break
       
    if left_bracket_index and right_bracket_index:
        # Divide string and return each.
        # Or, return indices and let other function divide string.
        pre_tag_text = line[:left_bracket_index]
        tag_text = line[left_bracket_index:right_bracket_index+1]
        post_tag_text = line[right_bracket_index+1:]
        return (pre_tag_text, tag_text, post_tag_text)
            # Our work here is done.
            # Other methods will parse tag itself, get token, get inner content, 
            # combine label with inner content to create HTMl tags, etc.
    else:
        # No Markform tag.
        # Thus, no pre-tag, tag, or post-tag text.
        return (pre_tag_text, tag_text, post_tag_text)
