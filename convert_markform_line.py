def convert_markform_line(line, element_type):

    # Form start.
    if element_type == "form_start":
        return convert_form_start_element(line)
    
    # Form end.
    elif element_type == "form_end":
        return convert_form_end_element(line)
    
    # Different types of input elements.
    if element_type in ["text_input", "email_input", "number_input", "range_input", "file_input"]:
        return convert_input_element(line, element_type)

    # Textarea.
    elif element_type == "textarea":
        return convert_textarea_element(line)

    # Submit button.
    elif element_type == "submit":
        return convert_submit_element(line)
    
    # Element groups -- later
    elif element_type == "element_group":
        return convert_element_group(line)
        # Remember this might return an unconverted line if the element is not well formed.
