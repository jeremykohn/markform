# Splits Markform element into pre-tag, tag, and post-tag.
# Or return None if the line is not a Markform element.

def validate_element(line):
    # Input should be a one-line string.
    
    if type(line) is not str:
        raise ValueError("Element must be a string.")
    if "\n" in line:
        raise ValueError("Element must include only one line, cannot include newline.")
    # Also see if tag is included? 
    
def parse_element(line):

    # Initial conditions.
    opening_token = None
    closing_token = None
    tag_complete = False
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
    
    # Current position. Start at beginning of line.
    pos = 0

    # Search for opening bracket followed by opening token.
    # If found, get opening token and (based on opening token) closing token.
    
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
                
        # If closing token not found, continue parsing.
        pos += 1

    # If there is an opening token, search for a tag closing, 
    # which is a closing token followed by a closing bracket.
    if opening_token:
        pos_left = pos
        pos_right = pos + 1
        # Move pos_right to find closing bracket preceded by closing token.
        while pos_right < len(line):
            if line[pos_right] == "]" and line[pos_right - 1] == closing_token:
                tag_complete = True
                # Found end of tag.
                # Get tag's position.
                left_bracket_index = pos_left
                right_bracket_index = pos_right
                break
       
    if tag_complete:
        # Divide string and return each section.
        pre_tag_text = line[:left_bracket_index]
        tag_text = line[left_bracket_index:right_bracket_index+1]
        post_tag_text = line[right_bracket_index+1:]
        return (pre_tag_text, tag_text, post_tag_text)
    else:
        # No Markform tag in this line.
        return None
    
    # Our work here is done.
    # Other methods will parse tag itself, get token, 
    # trim whitespace around tag, get inner content, 
    # combine label with inner content to create HTML tags, 
    # etc.
