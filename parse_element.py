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
    # Return token type --> tag type, and also text between tokens --> inner content.
    
    # Initial values.
    token_type = None
    inner_content = None
    
    # Validations.
    
    # Also disallow newline? Though earlier function should take care of that.
    
    if type(tag_text) is not str:
        print("Tag text: {}".format(tag_text))
        raise ValueError("Tag must be a string.")
    
    if tag_text = "":
        raise ValueError("Tag text cannot be empty.")

    if len(tag_text) < 3:
        print("Tag text: {}".format(tag_text))
        raise ValueError("Tag text must be at least three characters.")
    
    if tag_text[0] != "[" or tag_text[-1] != "]":
        print("Tag text: {}".format(tag_text))
        raise ValueError("Tag text must begin with '[' and end with ']'.")
    

    # Allow [____ Inner content _]? Or [___ Inner content ___]?
    # Or just allow [_], [___], [_   _], [_ Inner content _] and throw error otherwise?
    
    # Character immediately following the opening bracket is the opening token.
    opening_token = tag_text[1]

    if opening_token in simple_tokens:
        # Opening and closing tokens are the same.
        closing_token = opening_token
 
    elif opening_token in inverse_tokens:
        # Opening and closing tokens are inverses. ( ), { }, etc.
        closing_token = inverse_tokens[opening_token]
    
    else:
        print("Tag text: {}".format(tag_text))
        raise ValueError("The character " + opening_token + " is not a valid Markform token in the current spec.")
    
    # Validate.

    if tag_text[-2] != closing_token:
        print("Tag text: {}".format(tag_text))
        raise ValueError("Tag must include both opening token and closing token.")
        
        
    # Continue parsing.
    # Again, it depends on simple_tokens vs inverse_tokens.
   
    if opening_token in simple_tokens:
        # Special cases: [_], [@], [__], [@@], etc.
        if len(tag_text) == 3 or len(tag_text) == 4:
            return (opening_token, None)
        else:
            pos_left = 1  # Opening token
            pos_right = len(tag_text) - 2  # Closing token
            
            while tag_text[pos_left] == opening_token:
                # Advance pos_left
                # After opening tokens (and after whitespace?), inner content begins.
                # (I think yes after whitespace. Otherwise [_inner content_] might look like emphasis, underlines, etc.
                pos_left += 1

            if pos_left >= pos_right:
                # Done. pos_left got to closing token or to closing bracket. No inner content.
                return (opening_token, None)
            
            elif tag_text[pos_left] != " ":
                # Should be whitespace. If not, invalid.
                print("Tag text: {}".format(tag_text))
                raise ValueError("There must be at least one space separating opening tokens from inner content.")

            # Else, skip whitespace.
            while tag_text[pos_left] == " ":
                pos_left += 1
            # At this point, 
            # pos_left should be at first character of inner content.
            # Or else at (one of the) closing token(s), in which case we're done.
            # Though what if [+++ +o+]?


            # Move pos_right leftward to find end of inner content.
            while tag_text[pos_right] == closing_token:
                pos_right -= 1

            if pos_left >= pos_right:
                # Done. pos_left got to closing token or to closing bracket. No inner content.
                return (opening_token, None)
            
            # If there is inner content, there must be whitespace after it, before closing token(s0.
            elif tag_text[pos_right] != " ":
                # Should be whitespace. If not, invalid.
                print("Tag text: {}".format(tag_text))
                raise ValueError("There must be at least one space separating opening tokens from inner content.")

            # Now, skip whitespace while moving leftward.
            while tag_text[pos_right] == " ":
                pos_right -= 1
            # At this point, 
            # pos_right should be at first character of inner content.
            # Or else at opening token.

            if pos_left >= pos_right:
                # They are either at the same position, or they crossed over.
                # In either case, it means there's no inner content.
                return (opening_token, None)
            else:
                inner_content = line[pos_left:pos_right+1]


    elif opening_token in inverse_tokens:

        # Special case if [[]], [()], etc? Or require [[ ]], [( )]?
        
        # Validate whitespace next to opening, closing tokens
        if tag_text[2] != " " or tag_text[-3] != " ":
            print("Tag text: {}".format(tag_text))
            raise ValueError("Tag must include space between the opening token and the corresponding closing token.")  # Really? or allow things like [[]]?   
        
        # No multiple opening tokens allowed if the tag has inverse tokens.
        
        # Should be only one opening token, one closing token.
        # And then at least one " " in each direction.
        # Skip whitespace.
        
        # Move pos_left rightward.
        # Likewise, move pos_right leftward.
        # Skip whitespace.
        # Though whitespace is required if there's inner content.
        
        # Then, line[pos_left:pos_right+1] is inner content.
        
    
    
    # In either case,
        # get pos_left to the beginning of inner content,
        # and pos_right to the end of inner content.
        # That is, if there's inner content... which there isn't if pos_left and pos_right are the same.
        # Of if there's just whitespace.

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

    
# Instead of skip whitespace, just trim whitespace later?    
