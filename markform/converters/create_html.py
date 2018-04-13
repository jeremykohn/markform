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
    escaped_label_content = cgi.escape(pre_element_content, quote=True)
    label_html = '<label for="{}">{}</label>'.format(element_id, escaped_label_content)
    return label_html


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
    element_id_segments = ['markform', input_type, 'input', pre_element_content, post_element_content]
    element_id = combine_into_element_id(element_id_segments)
    
    # Generate HTML for label before input.
    if pre_element_content:
        label_before_input = create_label(element_id, pre_element_content)
        output_html_lines.append(label_before_input)
    
    # Generate HTML for input.
    input_tag = '<input id="{}" type="{}">'.format(element_id, input_type)
    output_html_lines.append(input_tag)
    
    # Generate HTML for label after input.
    if post_element_content:
        label_after_input = create_label(element_id, post_element_content)
        output_html_lines.append(label_after_input)

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

    # Generate HTML for label before input.
    if pre_element_content:
        label_before_textarea = create_label(element_id, pre_element_content)
        output_html_lines.append(label_before_textarea)
    
    # Generate HTML for input.
    textarea_tags = '<textarea id="{}"></textarea>'.format(element_id)
    output_html_lines.append(textarea_html)
    
    # Generate HTML for label after input.
    if post_element_content:
        label_after_textarea = create_label(element_id, post_element_content)
        output_html_lines.append(label_after_textarea)

    # Last line is a closing div tag.
    output_html_lines.append('</div>')

    # Output final HTML.
    output_html = "\n".join(output_html_lines)
    
    return output_html
