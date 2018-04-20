from helpers import create_html
from helpers.parse_line import parse_line


def convert_text(markform_text):

    input_lines = markform_text.split("\n")
    output_segments = []

    # Convert document line by line.
    
    for line in input_lines:
        
        # Call function to split line into components.
        parsed_line = parse_line(line)
        
        # Get individual components of line.
        pre = parsed_line["pre_element_content"]
        post = parsed_line["post_element_content"]
        inner = parsed_line["inner_content"]
        identifier = parsed_line["opening_identifier"]
        
        # Use different functions to convert an element based on its opening identifier.
        
        # Form start.
        if identifier == "+":
            output = create_html.form_start(pre_element_content=pre, post_element_content=post, inner_content=inner)
        # Form end.
        elif identifier == "-":
            output = create_html.form_end(pre_element_content=pre, post_element_content=post, inner_content=inner)
        # Various types of <input> elements.
        # Text input.
        elif identifier == "_":
            output = create_html.input_element(input_type="text", pre_element_content=pre, post_element_content=post, inner_content=inner)
        # Email input.
        elif identifier == "@":
            output = create_html.input_element(input_type="email", pre_element_content=pre, post_element_content=post, inner_content=inner)
        # Password input.
        elif identifier == "*":
            output = create_html.input_element(input_type="password", pre_element_content=pre, post_element_content=post, inner_content=inner)
        # Number input.
        elif identifier == "$":
            output = create_html.input_element(input_type="number", pre_element_content=pre, post_element_content=post, inner_content=inner)
        # Range input.
        elif identifier == "%":
            output = create_html.input_element(input_type="range", pre_element_content=pre, post_element_content=post, inner_content=inner)
        # File input.
        elif identifier == "^":
            output = create_html.input_element(input_type="file", pre_element_content=pre, post_element_content=post, inner_content=inner)
        # Textarea.
        elif identifier == "[":
            output = create_html.textarea_element(pre_element_content=pre, post_element_content=post, inner_content=inner)
        # Submit button.
        elif identifier == "(":
            output = create_html.submit_button_element(pre_element_content=pre, post_element_content=post, inner_content=inner)
        # Element group.
        elif identifier == "{":
            # Parse the inner content first, to get components and determine valid type of element group. If any.
            parsed_element_group = parse_element_group(inner)
            group_type = parsed_element_group["group_type"]
            inner_element_list = parsed_element_group["inner_element_list"]  # Each inner element includes a [ ], [x], ( ), (o), or >, but not | characters
            # Checkbox group.
            if group_type == "checkbox":
                output = create_html.checkbox_group(pre_element_content=pre, post_element_content=post, inner_element_list=inner_element_list)
            # Radio button group.
            elif group_type == "radio":
                output = create_html.radio_group(pre_element_content=pre, post_element_content=post, inner_element_list=inner_element_list)
            # Select / dropdown menu.
            elif group_type == "dropdown":
                output = create_html.dropdown_menu(pre_element_content=pre, post_element_content=post, inner_element_list=inner_element_list)
            else:
                # Don't convert element group, just append to output.
                output = line
    
        # No identifier returned by parser. Not a Markform element.
        else:
            # Don't convert line, just append to output.
            output = line
        
        # Add output from this element
        output_segments.append(output)
    
    # Finally, combine output segments.
    complete_output = "\n".join(output_segments)
    
    return complete_output
