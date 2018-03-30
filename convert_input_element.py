def convert_input_element(input_type, pre_element_content, inner_content, post_element_content):
    
    html_lines = []
    
    # Start.
    html_lines.append('<div>')
    
    # Trim whitespace around pre- and post-element content.
    pre_element_content = pre_element_content.strip()
    post_element_content = post_element_content.strip()
    
    # Combine input type with pre-element and post-element content 
    # to create an ID for the HTML input element.
    element_id = 'markform-' + input_type + '-input'
    if pre_element_content:
        element_id += '-' += kebab_case(pre_element_content)
    if post_element_content:
        element_id += '-' += kebab_case(post_element_content)

    # Generate HTML for label before input, if applicable.
    if pre_element_content:
        label_before_input = '<label for="{}">{}</label>'.format(element_id, html_escape(pre_element_content))
        html_lines.append(label_before_input)
    
    # Generate HTML for input.
    input_element = '<input id="{}" type="{}">'.format(element_id, input_type)
    html_lines.append(input_element)
    
    # Generate HTML for label after input, if applicable.
    if post_element_content:
        label_after_input = '<label for="{}">{}</label>'.format(element_id, html_escape(post_element_content))
        html_lines.append(label_after_input)

    # Finish.
    html_lines.append('</div>')

    # Output final HTML.
    html_output = "\n".join(html_lines)
    
    return html_output
