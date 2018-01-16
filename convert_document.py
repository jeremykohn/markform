def convert_document(self, document_text):

    document_output = ""
    lines = document_text.split('\n')
    form_open = False

    for line in lines:

        (markform_tag_type, tag_inner_content, pre_tag_text, post_tag_text) = self.parse_line(line)

        if markform_tag_type == None:
            # If line is not a Markform element, append unconverted line to document_output
            document_output += line
        elif markform_tag_type == "start":
            # Open a Markform block
            form_open = True
            # Append additional newline and form opening tag to document_output
            document_output += '\n'
            document_output += convert_element(markform_tag_type, tag_inner_content, pre_tag_text, post_tag_text)
        elif markform_tag_type == "end":
            # Append form closing tag and additional newline to document_output
            document_output += convert_element(markform_tag_type, tag_inner_content, pre_tag_text, post_tag_text)
            document_output += '\n'
            # Close the Markform block
            form_open = False
        else:
            if form_open == True:
                # Convert Markform element to HTML, append to document_output                
                document_output += convert_element(markform_tag_type, tag_inner_content, pre_tag_text, post_tag_text)
            else:
                # If not within Markform block, append unconverted line to document_output
                document_output += line                

        # Finally, append \n to document_output.
        document_output += '\n'

        # On to the next line.

    # Might truncate the last \n we just added, since it's extra.
    
    

    return document_output

