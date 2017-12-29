# Splits Markform element into pre-tag, post-tag, tag type, and tag inner content.
# Or returns None if line is not a Markform element.

# Remember to trim whitespace around pre-tag and post-tag.

# Also throw an error if input includes newline.



# "parse_element()", "parse_line()", "split_element()", or "split_line()"


# Or, 'get indices of pre, tag, and post'?
def parse_element(line):

    # Validate input.
    # Should be text without "\n"
    
    if type(line) is not str:
        raise ValueError("Markdown element must be a string")
    
    if "\n" in line:
        raise ValueError("Markdown element cannot include newline")
    
    # Components to return.
    tag_type = None
    pre_tag_text = ""
    tag_inner_content = ""
    post_tag_text = ""

    # Initial conditions.
    tag_open = False  # tag_open requires opening bracket followed by opening token.  # Guess I don't need this.
    tag_closed = False  # tag_closed requires closing token followed by closing bracket.  # Or this.
    opening_token = None
    closing_token = None    

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

    
    # Search for opening bracket followed by opening token.
    # If found, get opening token and (based on opening token) closing token.
    while pos + 1 < len(line):
        if line[pos] == "[":
            next_character = line[pos + 1]
            if next_character in simple_tokens:
                opening_token = next_character
                closing_token = opening_token
                break
            elif next_character in inverse_tokens:
                opening_token = next_character
                closing_token = inverse_tokens[opening_token]
                break
        # If not found, keep moving.
        pos += 1

    if opening_token

    # If there is an opening token, search for a tag closing, 
    # which is a closing token followed by a closing bracket.
    if opening_token:
        pos_left = pos
        pos_right = pos
        # Move pos_right to find closing bracket preceded by closing token(s?)
        while pos_right + 1 < len(line):
            if line[pos_right] == closing_token and line[pos_right + 1] == "]":
                # Found tag closing.
                left_bracket_index = pos_left
                right_bracket_index = pos_right + 1
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
        return None


                

def parse_tag(tag_text):
    # Return token type --> tag type, and also inner text.
    
    # Sanity checks
    
    if type(tag_text) is not str:
        raise ValueError("Tag must be a string.")
    
    if tag_text = "":
        raise ValueError("Tag text cannot be empty.")

    # Other validations? Confirm tag format?
    # Should be bracket, opening token, ends with corresponding closing token followed by bracket.
    # Might want to confirm that before proceeding.
    
    # Meanwhile, get the token type.
    
    pos_left = 0
    pos_right = len(tag_text) - 1

    # Move inward, get tag type, and inner content if any.
    
    # If not the right format, or token not on list, return error. (ValueError?) (Tag must be in the right format.)
    
    pos_left += 1
    opening_token = tag_text[pos_left]
    
    if opening_token in simple_tokens:
        closing_token = 
        while tag_text[pos_left] == opening_token:
            # Advance pos_left
            # After opening tokens (and after whitespace?), inner content begins.
            # (I think yes after whitespace. Otherwise [_inner content_] might look like emphasis, underlines, etc.
            pos_left += 1
        # Now, skip whiespace.
        while tag_text[pos_left] == " ":
            pos_left += 1
        # At this point, 
        # pos_left should be at first character of inner content.
        # Or else at closing bracket.
        
        # If pos_left == pos_right, it means pos_left is at closing bracket.
        # If not, then move pos_right leftward to find end of inner content.
        
        # Although, if no closing token, something is wrong -- throw error.

    elif opening_token in inverse_tokens:
        closing_token = inverse_tokens[opening_token]
        # No multiple opening tokens allowed if the tag has inverse tokens.
        # So, just advance one position.
        # Then skip whitespace.
        
    
    
    # In either case,
        # get pos_left to the beginning of inner content,
        # and pos_right to the end of inner content.
        # That is, if there's inner content... which there isn't if pos_left and pos_right are the same.

            # For symmetric tokens, multiple opening/closing tokens are not allowed.
            # Instead, get content between (first) opening token and (first) closing token.
            # For example: `[[[ ]]]`
            # That would become `<textarea>[</textarea>]`
            # Assuming of course that a space is not required after opening token.
            # And assuming we allow pre tag text or post tag text to border tag.
            

            
        # Return tag type, and inner content.
        # Tag type depends on token.
        print("Token: " + token)

        
    else:
        return None
