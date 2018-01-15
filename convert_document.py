def convert_document(self, document_text):

    document_output = ""
    lines = document_text.split('\n')
    form_open = False

    for line in lines:

        (markform_tag_type, tag_inner_content, pre_tag_text, post_tag_text) = self.parse_line(line)

        if markform_tag_type == None:
            # append unconverted line to document_output
        elif markform_tag_type == "start":
            form_open = True
            # append additional newline and <form> to document_output
        elif markform_tag_type == "end":
            form_open = False
            # append </form> and additional newline to document_output
        elif markform_tag_type == "text_input" and form_open == True:
            # convert element to HTML --
            # based on (markform_tag_type, tag_inner_content, pre_tag_text, post_tag_text)
            # Then append HTML to document_output

        # Same with other tag types.
        # An elif for each type,
        # which calls a function for each type.



        # Finally, 
        # append \n to document_output.

        # On to the next line.

    # Truncate the last \n we just added, since it's extra.
    
    

    return document_output

