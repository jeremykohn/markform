# Convert document containing Markform elements to document containing HTML form elements.
def convert_markform_document_to_html(markform_document):
    input_lines = markform_document.split("\n")
    output_lines = []

    for line in input_lines:
        markform_element_type = detect_element_type(line)
        if markform_element_type:
            # Convert and append.
            converted_line = convert_markform_line(line, markform_element_type)
            output_lines.append(converted_line)
        else:
            # Don't convert, just append.
            output_lines.append(line)
    
    return "\n".join(output_lines)
