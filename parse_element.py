def parse_element(line):
    # To be a Markform element, line must start with zero to three spaces before opening bracket.
    while i < 4 and i < len(line):
        # A bracket opens a Markform element.
        if line[i] == '{'
            tag_open = True
            i += 1
            break
        # If a space before a bracket, keep going.
        elif line[i] == ' ':
            i += 1
        else
            # If other characters precede the opening bracket and/or spaces, not a Markform element.
            tag_open = False
            break
    
    if tag_open:
        # Get the next character, right after opening bracket.
        i += 1
        # Make sure to avoid index errors.
        if i < len(line):
            # This is the token that determines the type of Markform element.
            token = line[i]
        else:
            token = None
    
    if token:
        # Find the first closing bracket immediately preceded by the relevant token.
        # That'll be end of the Markform tag.
        
        # When only one token is required.
        single_tokens = ['+', '-', '_', '@', '$', '%', '^', '*']
        
        # When two tokens are required.
        # Maps opening token to the corresponding closing token.
        symmetric_tokens: {
            "(": ")",
            "[": "]",            
            "{": "}",
            "|": "|"
        }

        # See if token is on one of the relevant lists.    

        if token is in single_tokens:
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

        elif token is in symmetric_tokens:
            
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
        
        # if inner_content,
        # return that too.
        
    else:
        return None