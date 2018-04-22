import re
import cgi

# Helpers.

# Create element ID by assembling specified text segments.
def combine_into_element_id(id_segments):
    # Remove empty segments.
    id_segments = [segment for segment in id_segments if segment]
    # Join with '-', replace nonword characters with '-', and convert all to lowercase.
    combined_text = ('-').join(id_segments)
    combined_text = re.sub(r'\W+', '-', combined_text)
    combined_text = combined_text.lower()
    return combined_text

def create_label(element_id, label_content):
    escaped_label_content = cgi.escape(label_content, quote=True)
    label_html = '<label for="{}">{}</label>'.format(element_id, escaped_label_content)
    return label_html

def create_button_text(content):
    button_text = content.strip()
    button_text = cgi.escape(button_text)
    return button_text


# Later, might add more features.
# Like, convert `Name of form: [+]` into <form><fieldset><legend>Name of form:</legend>...<fieldset></form>
# Or, convert `[+ method="post" action="action.php" +]` into <form method="post" action="action.php">

def form_start(pre_element_content, post_element_content, inner_content):
    return "<form>"


def form_end(pre_element_content, post_element_content, inner_content):
    return "</form>"


def input_element(input_type, pre_element_content, post_element_content, inner_content):

    output_html_lines = []
    
    # Output is surrounded by div tags.
    # First line is an opening div tag.
    output_html_lines.append('<div>')

    # Trim whitespace around pre- and post-element content.
    pre_element_content = pre_element_content.strip()
    post_element_content = post_element_content.strip()
    
    # Create HTML element ID by joining element type with pre/post element content.
    element_id = combine_into_element_id(['markform', input_type, 'input', pre_element_content, post_element_content])
    
    # Generate HTML for label before element.
    if pre_element_content:
        pre_element_label = create_label(element_id, pre_element_content)
        output_html_lines.append(pre_element_label)
    
    # Generate HTML for input.
    input_tag = '<input id="{}" type="{}">'.format(element_id, input_type)
    output_html_lines.append(input_tag)
    
    # Generate HTML for label after element.
    if post_element_content:
        post_element_label = create_label(element_id, post_element_content)
        output_html_lines.append(post_element_label)

    # Last line is a closing div tag.
    output_html_lines.append('</div>')

    # Output final HTML.
    output_html = "\n".join(output_html_lines)
    
    return output_html


# Later, might convert textarea with [[ Inner Text ]] either to placeholder or to pre-filled text.

def textarea_element(pre_element_content, post_element_content, inner_content):

    output_html_lines = []
    
    # Output is surrounded by div tags.
    # First line is an opening div tag.
    output_html_lines.append('<div>')

    # Trim whitespace around pre- and post-element content.
    pre_element_content = pre_element_content.strip()
    post_element_content = post_element_content.strip()
    
    # Create HTML element ID by joining element type with pre/post element content.
    element_id = combine_into_element_id(['markform', 'textarea', pre_element_content, post_element_content])

    # Generate HTML for label before element.
    if pre_element_content:
        pre_element_label = create_label(element_id, pre_element_content)
        output_html_lines.append(pre_element_label)
    
    # Generate HTML for textarea.
    textarea_tags = '<textarea id="{}"></textarea>'.format(element_id)
    output_html_lines.append(textarea_tags)
    
    # Generate HTML for label after element.
    if post_element_content:
        post_element_label = create_label(element_id, post_element_content)
        output_html_lines.append(post_element_label)

    # Last line is a closing div tag.
    output_html_lines.append('</div>')

    # Output final HTML.
    output_html = "\n".join(output_html_lines)
    
    return output_html


def submit_button_element(pre_element_content, post_element_content, inner_content):
    output_html_lines = []
    
    # Output is surrounded by div tags.
    # First line is an opening div tag.
    output_html_lines.append('<div>')

    # Trim whitespace around pre- and post-element content.
    pre_element_content = pre_element_content.strip()
    post_element_content = post_element_content.strip()
    
    # Create HTML element ID by joining element type with inner content and pre/post element content.
    element_id = combine_into_element_id(['markform', 'submit-button', pre_element_content, inner_content, post_element_content])
    
    # Generate HTML for label before element.
    if pre_element_content:
        pre_element_label = create_label(element_id, pre_element_content)
        output_html_lines.append(pre_element_label)

    # Generate button text from inner content.
    button_text = create_button_text(inner_content)

    # Generate HTML for submit button.
    submit_button_tags = '<button id="{}" type="submit">{}</button>'.format(element_id, button_text)
    output_html_lines.append(submit_button_tags)

    # Generate HTML for label after element.
    if post_element_content:
        post_element_label = create_label(element_id, post_element_content)
        output_html_lines.append(post_element_label)

    # Last line is a closing div tag.
    output_html_lines.append('</div>')

    # Output final HTML.
    output_html = "\n".join(output_html_lines)
    
    return output_html

"""

def parse_element_group

def checkbox_group( ... )

def radio_button_group( ... )

def dropdown_menu( ... )




def element_group(pre_element_content, post_element_content, inner_content):
    # Turn inner content into array of inner elements
        # Divide using pipe characters `|`
        # Detect type of the first inner element
        # Detect type of the other inner elements; 
            # parse as 'same type' if they're of the same type,
            # or parse as just strings if they aren't of the same type
    
    # Parse inner content of element group.
    parsed_inner_elements = []
    # That will include element type, prechecked/preselected, pre-identifier label/content, post-identifier label/content

    inner_element_list = []
    # Just a list of separate inner elements.

    pos = 0
    current_character = None
    previous_character = None
    next_character = None

    current_inner_element_start = 0
    # current_inner_element_end = None


    # Parse inner content, divide into elements.
    while pos < len(inner_content):
        current_character = inner_content[pos]
        if pos > 0:
            previous_character = inner_content[pos - 1]
        if pos < len(inner_content) - 1:
            next_character = inner_content[pos + 1]
        
        # Check for unescaped pipe character. This character divides inner elements from each other.
        if current_character == '|' and previous_character != '\\':
            # End of inner element, beginning of next element.
            # Add current inner element to list.
            current_inner_element = inner_content[current_inner_element_start:pos]
            inner_element_list.append(current_inner_element)
            # Update the start position of next inner element.
            current_inner_element_start = pos + 1

        # Next character.
        pos += 1

    # Remember to remove empty/blank inner elements from inner_element_list? Or treat them as empty labels?
    

    # Process each inner element.
    # Return pre inner identifier content, post inner identifier content, element type, and checked/unchecked or selected/unselected.

    # Then, provide that as input to the respective function --
    # checkbox_group()
    # radio_button_group()
    # dropdown_menu()
    # (And within each of those, have functions to parse inner elements into pre-identifier content, post-identifier content, and identifier?)






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

"""
