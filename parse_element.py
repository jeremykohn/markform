# Splits Markform element into pre-tag, post-tag, tag type, and tag inner content.
# Or returns None if line is not a Markform element.

# Remember to trim whitespace around pre-tag and post-tag.

# Also throw an error if input includes newline.



# "parse_element()", "parse_line()", "split_element()", or "split_line()"

def parse_element(line):
    
    # Initialize values.
    tag_open = False
    token = None
    tag_closed = False
    
    pre_tag_text = ""
    tag_type = None
    tag_inner_content = ""
    post_tag_text = ""
    
    # Or, instead of tag_text return tag_type and inner_content
    
    # Thus, this function would
    # "split Markform element into four values, or return None if not a Markform element"
    # Thus the function does one thing. No "And".
    
    # Current position in line. Start at beginning of line.
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
            
            
    # Parse content after initial spaces, before tag.
    
    content_before_tag = ""
    
    # Find opening bracket if any.
    while pos < len(line): 
        if line[pos] == "[":
            tag_open = True
        else:
            content_before_tag += line[pos]
        # Step forward.
        pos += 1

    # If there is an opening bracket, get the next character, if any.
    # That character is a "token" that determines the type of Markform tag.
    if tag_open:
        pos += 1
        if pos < len(line):
            token = line[pos]
    else:
        token = None
    
    
    # If there is an opening token, search for a tag closing, 
    # which is a closing token followed by a closing bracket.
    if token:

        # For some types of Markform tags, the opening and closing tokens are the same character.
        single_tokens = ['+', '-', '_', '@', '$', '%', '^', '*']
        
        # For other Markform tags, the closing token is the inverse of the opening token.
        
        # This dictionary maps each opening token to the corresponding closing token.
        symmetric_tokens = {
            "(": ")",
            "[": "]",            
            "{": "}",
            "|": "|"
        }
        # Change to "paired_tokens"?

        
        # See if token is on one of the relevant lists.    

                
        if token in single_tokens:
            # Search forward for closing bracket.
            j = i
            while j < len(line):
                j += 1
                if line[j] == ']' and line[j-1] == token:
                    # Found end of tag.
                    tag_closed = True
                    break
            
            # Get content in between continous opening token(s) and continuous closing token(s).
            # Work forwards, and backwards.
            
            if tag_closed:
                i += 1
                j -= 1
                while line[i] == token and i < j:
                    i += 1
                    # At this point, line[i] should be the first post-token character, if any.
                while line[j] == token and i < j:
                    j -= 1
                    # At this point, line[j] should be the last pre-token character, if any.
                if i <= j:
                    # There is inner content.
                    # One or more characters.
                    inner_content = line[i:j+1]
                else:
                    inner_content = None

                # Make sure to test this! Avoid off-by-one errors.

        elif token in symmetric_tokens:
            
            # Get the opening token and the corresponding closing token.
            opening_token = token            
            closing_token = symmetric_tokens[opening_token]
            
            # Now, parse for closing token.
            # If found, get tag type (based on opening token) and inner content.
            # and set tag_closed = True
            
            j = i
            while j < len(line):
                j += 1
                if line[j] == ']' and line[j-1] == closing_token:
                    # Found end of tag.
                    tag_closed = True
                    break            

            # Now, get inner content between tokens.
            
            # For symmetric tokens, multiple opening/closing tokens are not allowed.
            # Instead, get content between (first) opening token and (last) closing token.
            # For example: [[[ ]]]
            # That would become <textarea>[ ]</textarea>
            
            if tag_closed:
                i += 1  # First post-opening-token character
                j -= 2  # Last pre-closing-token character
                if i >= j:
                    # Inner content is everything between opening token and closing token
                    inner_content = line[i:j+1]

        else:
            # Token not on list. Can't close tag.
            tag_closed = False

    if tag_open and token and tag_closed:
        # Return tag type, and inner content.
        # Tag type depends on token.
        print("Tag opened and closed. Token: " + token)

        # if inner_content,
        # return that too.
        
    else:
        return None
