# Get type of Markform tag, and the tag's inner content.

# First, validate Markform tag format.
# If not valid, do not create a tag.
def validate_tag(tag_text):

    # For some types of Markform tags, the opening and closing tokens are the same character.
    simple_tokens = ['+', '-', '_', '@', '$', '%', '^', '*']
        
    # For other Markform tags, the closing token is the inverse of the opening token.
    inverse_tokens = {
        "(": ")",
        "[": "]",            
        "{": "}",
        "|": "|"
    }

    # Tag must be at least three characters, since it requires `[`, `]` and at least one token.
    if len(tag_text) < 3:
        return False

    # Validate opening and closing brackets.
    first_char = tag_text[0]
    last_char = tag_text[-1]

    if first_char != "[" or last_char != "]":
        return False

    # Validate opening and closing tokens.
    second_char = tag_text[1]
    second_last_char = tag_text[-2]    

    # If simple token: Tag must have the same opening and closing token.
    if second_char in simple_tokens:
        if second_last_char != opening_token:
            return False

    # If inverse tokens: Closing token must be inverse of opening token.
    elif second_char in inverse_tokens:
        if second_last_char != inverse_tokens(second_char):
            return False

    # If neither simple token or inverse token, then tag is invalid.
    else:
        return False

    # Parse for non-allowed components.
    pos = 0
    while pos < len(tag_text):
        if tag_text[pos] == "\n":
            return False

    # Also parse for early closing? Like, [+ Inner text content +] More content +]
    # Not here, I think. Just validate the basics. 
    # And provide more flexibility -- spec might change to parse inward, not forward.

    return True




def parse_tag(tag_text):
    # Return opening token (which determines tag type), and also text between tokens (inner content).
    
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


    opening_token = tag_text[1]

    if opening_token in simple_tokens:
        closing_token = token 
    elif token in inverse_tokens:
        closing_token = inverse_tokens[opening_token]

    if opening_token in simple_tokens:
        pos_left = 0
        pos_right = len(tag_text) - 1
        
        # Move pos_left forward through continuous opening tokens.
        while pos_left < pos_right:
            if tag_text[pos_left + 1] == opening_token:
                pos_left += 1
            else:
                break
        # Now pos_left is at rightmost opening token.

        # Move pos_right backward through continous closing tokens.
        while pos_right > pos_left:
            if tag_text[pos_right - 1] == closing_token:
                pos_right -= 1
            else:
                break
        # Now pos_right is at leftmost closing token, 
        # or at pos_right if the "opening" and "closing" tokens intersect.
        
        # Then, tag_text[pos_left+1:pos_right] is inner content.
        # Unless pos_left == pos_right, in which case there is no inner content.

        if pos_left == pos_right:
            # No inner content
            return (opening_token, None)
        else:
            inner_content = tag_text[pos_left+1:pos_right]
            return (opening_token, inner_content)

    elif opening_token in inverse_tokens:
        
        # Only one opening token, one closing token.

        # Start left-side at opening token.
        pos_left = 1
        # Start right-side at closing token.
        pos_right = len(tag_text) - 2
                
        if pos_left == pos_right:
            # No inner content.
            return (opening_token, None)
        else:
            # Return inner content.
            inner_content = tag_text[pos_left+1:pos_right]
            return (opening_token, inner_content)

    # If opening token is on neither list:
    else:
        opening_token = None
        inner_content = None

    # Return opening token and inner content, if any.
    # Though there should be opening token. Validation should take care of that.

    return (opening_token, inner_content)
