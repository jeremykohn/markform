def convert_document(self, document_text):

    document_output = ""
    lines = document_text.split('\n')
    form_open = False

    for line_number, line in enumerate(lines):
        
        # Gets element if the line is valid Markform. Returns None otherwise.
        markform_element = get_markform_element(line)

        if markform_element:
            element_type = markform_element["element_type"]
            element_html_output = convert_element_to_html(markform_element)
        else:
            element_type = None
            element_html = None

        if element_type == "start" and not form_open:
            # Open a Markform block.
            form_open = True
            # Append newline, to separate converted HTML from previous content.
            document_output += '\n'
            
        if element_type and form_open:
            # Append converted Markform element.
            document_output += element_html_output
        
        if element_type == "end" and form_open:
            # Close the Markform block.
            form_open = False            
            # Append newline, to separate converted HTML from successive content.
            document_output += '\n'
        
        else:
            # Don't convert line, just append unconverted line.
            document_output += line            
        
        # Done with this line.
        # Append newline to output, unless it's the last line of the document.
        if line_number + 1 < len(lines):
            document_output += '\n'

    return document_output
