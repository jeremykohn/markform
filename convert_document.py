def convert_document(self, document_text):

    document_output = ""
    lines = document_text.split('\n')
    form_open = False

    for line_number, line in enumerate(lines):

        # Parse line to extract relevant Markform information, if any.
        # Returns None for tag_type if line does not include a Markform tag.
        tag_type, pre_tag_content, inner_content, post_tag_content = parse_line(line)

        if tag_type == "start" and not form_open:
            # Open a Markform block.
            form_open = True
            # Append newline, to separate converted HTML from previous content.
            document_output += '\n'
            # Convert and append Markform start element.
            document_output += convert_tag_to_html(tag_type, pre_tag_content, inner_content, post_tag_content)

        elif tag_type == "end" and form_open:
            # Convert and append Markform end element.
            document_output += convert_tag_to_html(tag_type, pre_tag_content, inner_content, post_tag_content)
            # Append newline, to separate converted HTML from successive content.
            document_output += '\n'
            # Close the Markform block.
            form_open = False

        elif tag_type and form_open:
            # Inside Markform block. Convert and append Markform element.
            document_output += convert_tag_to_html(tag_type, pre_tag_content, inner_content, post_tag_content)

        else:
            # If earlier conditions not met, don't convert line, just append unconverted line.
            document_output += line            
        
        # Done with this line.
        # Append newline to output, unless it's the last line of the document.
        if line_number + 1 < len(lines):
            document_output += '\n'

    return document_output
