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


def element_group(pre_element_content, post_element_content, inner_content):
    # Turn inner content into array of inner elements
        # Divide using pipe characters `|`
        # Detect type of the first inner element
        # Detect type of the other inner elements; 
            # parse as 'same type' if they're of the same type,
            # or parse as just strings if they aren't of the same type
    
    # Provide input to the respective function
    # checkbox_group()
    # radio_button_group()
    # dropdown_menu()
    # And within each of those, have functions to parse inner elements into pre-identifier content, post-identifier content, and identifier
