# Splits Markform element into pre-tag, post-tag, tag type, and tag inner content.
# Or returns None if line is not a Markform element.

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
        return None

    
######


def parse_tag(tag_text):
    # Return opening token (which determines tag type), and also text between tokens (inner content).
    
    # Validate input.
    # TODO: Change this so instead of raising error, it just keeps the text as is and doesn't consider it a tag.
    # Also, write test cases like `[[[ ]]]` to see what should happen.
    # I think `[[ ]]]` would turn into <tag>]
    # And `[[[ ]]` would just be [[[ ]]
    
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
    
    if tag_text[1] not in simple_tokens and tag_text[1] not in inverse_tokens:
        print("Tag text: {}".format(tag_text))
        raise ValueError("The character " + tag_text[1] + " is not a valid Markform token in the current spec.")
    
    if tag_text[1] in simple_tokens and tag_text[-2] != tag_text[1]:
        print("Tag text: {}".format(tag_text))
        raise ValueError("Opening token " + tag_text[1] + " requires the same closing token, not " + tag_text[-2])

    if tag_text[1] in inverse_tokens and tag_text[-2] != inverse_tokens[tag_text[1]]:
        print("Tag text: {}".format(tag_text))
        raise ValueError("Opening token " + tag_text[1] + " requires the inverse closing token, not " + tag_text[-2])
    
    # For inverse tokens, repeated opening tokens or repeated closing tokens are not allowed.
    if tag_text[1] in inverse_tokens and tag_text[-2] == inverse_tokens[tag_text[1]]:
        if tag_text[1] == tag_text[2]:
            print("Tag text: {}".format(tag_text))
            raise ValueError("Opening token " + tag_text[1] + " is an inverse token and cannot be repeated.")            
        if tag_text[-2] == tag_text[-3]:
            print("Tag text: {}".format(tag_text))
            raise ValueError("Closing token " + tag_text[-2] + " is an inverse token and cannot be repeated.")

    # Also disallow newline within tag_text? Though "split into lines" function should take care of that.

    if token in simple_tokens:
        opening_token = token
        closing_token = token
        
        pos_left = 0
        pos_right = len(tag_text) - 1
        
        # Move pos_left forward through continuous opening tokens...
        while pos_left < pos_right:
            if tag_text[pos_left + 1] == opening_token:
                pos_left += 1
            else:
                break
        # ...and then through continuous whitespace.
        while pos_left < pos_right:
            if tag_text[pos_left + 1] == " ":
                pos_left += 1
            else:
                break
        # pos_left is now at rightmost opening token, or rightmost whitespace charactr if there is whitespace.

        # Move pos_right backward through continous closing tokens...
        while pos_right > pos_left:
            if tag_text[pos_right - 1] == closing_token:
                pos_right -= 1
            else:
                break
        # ...and then through continous whitespace.
        while pos_right > pos_left:
            if tag_text[pos_right - 1] == " ":
                pos_right -= 1
            else:
                break
        # pos_right is now at leftmost closing token, or leftmost whitespace character if there is whitespace.
        
        # Then, tag_text[pos_left+1:pos_right] is inner content.
        # Unless pos_left == pos_right, in which case there is no inner content.

        if pos_left == pos_right:
            # No inner content
            return (opening_token, None)
        
        else:
            inner_content = tag_text[pos_left+1:pos_right]
            return (opening_token, inner_content)

    elif token in inverse_tokens:
        opening_token = token
        closing_token = inverse_tokens[token]
        
        # Only one opening token, one closing token.
        # Then check for whitespace.
        # Stop at the end of whitespace, if any.
        
        # Start left-side at opening token.
        pos_left = 1
        # Start right-side at closing token.
        pos_right = len(tag_text) - 2
        
        # Skip whitespace.
        
        while pos_left < pos_right and tag_text[pos_left + 1] == " ":
            pos_left += 1

        while pos_right > pos_left and tag_text[pos_right - 1] == " ":
            pos_right -= 1
                
        if pos_left == pos_right:
            # No inner content
            return (opening_token, None)
        
        else:
            inner_content = tag_text[pos_left+1:pos_right]
            return (opening_token, inner_content)

    # If opening token is on neither list
    else:
        return (None, None)

    

    ###

    # Tag format:
    # Bracket, opening token(s), optionally whitespace, inner content, optionally whitespace, closing token(s), bracket.
    
    # Tag format for simple tokens:
    # Bracket, one or more opening tokens, optionally whitespace, inner content, optionally whitespace, one or more closing tokens, bracket. 
    
    # Tag format for inverse tokens:
    # Bracket, one opening token, optionally whitespace, inner content, optionally whitespace, one closing token, bracket.
    
    ###
    
    # Allow [____ Inner content _]? Or [___ Inner content ___]?
    # Or just allow [_], [___], [_   _], [_ Inner content _] and throw error otherwise?
    
    # I think allow one or more opening tokens, one or more closing tokens, and whitespace optional.

    ###
        
    # Escaped token?
    # Like, [*placeholderincludingasterisk\**]
    
    # No, require a space in between.
    # Like, [*placeholderincludingasterisk* *]
    
    # However, when parsing initially, should allow escaping brackets.
    
    ###
    
    # Special case if [[]], [()], etc? Or require [[ ]], [( )]?
    # I think don't require space.

    # No multiple opening tokens allowed if the tag has inverse tokens.

    # Should be only one opening token, one closing token.
    # And then skip whitespace.

    # What if multiple opening or closing tokens?
    # I think don't create tag in that case.
    # Or, extra tokens become part of inner content.
    # Or just return None, so text isn't converted to tag at all.

    # TODO: Write all these rules into the spec.

    # TODO: Write the validations into the API -- specify input and output formats (and requirements).
